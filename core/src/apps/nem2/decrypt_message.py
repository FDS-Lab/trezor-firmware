from ubinascii import hexlify, unhexlify

from trezor import ui, wire
from trezor.crypto import aes, random
from trezor.messages import ButtonRequestType, MessageType
from trezor.messages.NEM2DecryptedMessage import NEM2DecryptedMessage
from trezor.messages.NEM2DecryptMessage import NEM2DecryptMessage
from trezor.ui.scroll import Paginated
from trezor.ui.text import Text

from apps.common import HARDENED
from apps.common.confirm import require_hold_to_confirm
from apps.common.layout import split_address
from apps.common.paths import validate_path
from apps.nem2 import CURVE
from apps.nem2.crypto import derive_shared_key
from apps.nem2.helpers import (
    AES_BLOCK_SIZE,
    NEM2_HASH_ALG,
    NEM2_SALT_SIZE,
    validate_nem2_path,
)
from apps.nem2.validators import validate_decrypt_message


async def decrypt_message(
    ctx, msg: NEM2DecryptMessage, keychain
) -> NEM2DecryptedMessage:
    validate_decrypt_message(msg)

    await validate_path(
        ctx,
        validate_nem2_path,
        keychain,
        msg.address_n,
        CURVE,
    )

    properties = []

    t = Text("Decrypt Message", ui.ICON_SEND, new_lines=False)
    t.bold("From Public Key:")
    t.mono(*split_address(msg.sender_public_key.upper()))
    properties.append(t)

    t = Text("Decrypt Message", ui.ICON_SEND, new_lines=False)
    t.bold("Encrypted Message:")
    t.mono(*split_address(msg.payload[:20] + "..." + msg.payload[-20:]))
    properties.append(t)

    paginated = Paginated(properties)
    await require_hold_to_confirm(ctx, paginated, ButtonRequestType.ConfirmOutput)

    node = keychain.derive(msg.address_n, CURVE)

    payload_bytes = unhexlify(msg.payload)

    iv = payload_bytes[:16]
    message = payload_bytes[16:]

    # 1. generate a shared key between sender public key and recipient private key
    shared_key = derive_shared_key(node.private_key(), unhexlify(msg.sender_public_key))

    # 2. decrypt the message payload using AES
    ctx = aes(aes.CBC, shared_key, iv)
    decrypted_payload = ctx.decrypt(message)

    # payloads are padded with a number representing the number of spaces to pad
    last_char = bytes(decrypted_payload)[len(decrypted_payload) - 1]
    if last_char > 0 and last_char <= 16:
        # remove the padding from the message
        decrypted_payload = decrypted_payload[:-last_char]

    return NEM2DecryptedMessage(payload=decrypted_payload)
