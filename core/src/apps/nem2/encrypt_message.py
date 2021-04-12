from ubinascii import hexlify, unhexlify

from trezor import ui, wire
from trezor.crypto import aes, random
from trezor.messages import ButtonRequestType, MessageType
from trezor.messages.NEM2EncryptedMessage import NEM2EncryptedMessage
from trezor.messages.NEM2EncryptMessage import NEM2EncryptMessage
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
from apps.nem2.validators import validate_encrypt_message


async def encrypt_message(
    ctx, msg: NEM2EncryptMessage, keychain
) -> NEM2EncryptedMessage:
    validate_encrypt_message(msg)

    await validate_path(
        ctx,
        validate_nem2_path,
        keychain,
        msg.address_n,
        CURVE,
    )

    properties = []

    t = Text("Encrypt Message", ui.ICON_SEND, new_lines=False)
    t.bold("For Public Key:")
    t.mono(*split_address(msg.recipient_public_key.upper()))
    properties.append(t)

    t = Text("Encrypt Message", ui.ICON_SEND, new_lines=False)
    t.bold("Message:")
    t.br()
    t.normal(msg.payload)
    properties.append(t)

    paginated = Paginated(properties)
    await require_hold_to_confirm(ctx, paginated, ButtonRequestType.ConfirmOutput)

    node = keychain.derive(msg.address_n, CURVE)

    iv = random.bytes(AES_BLOCK_SIZE)

    # 1. generate a shared key between sender private key and recipient public key
    shared_key = derive_shared_key(
        node.private_key(), unhexlify(msg.recipient_public_key)
    )

    # 2. encrypt the message payload using AES
    ctx = aes(aes.CBC, shared_key, iv)

    # get the number of bytes to pad
    padding = max(0, AES_BLOCK_SIZE - len(msg.payload) % AES_BLOCK_SIZE)
    # use the number of padding bytes required as the padding character
    enc = ctx.encrypt(bytes(msg.payload, "ascii") + bytes([padding] * padding))

    encrypted_payload = iv + enc

    return NEM2EncryptedMessage(payload=encrypted_payload)
