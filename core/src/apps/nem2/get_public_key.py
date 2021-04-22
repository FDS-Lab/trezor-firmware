from ubinascii import hexlify

from trezor.messages.NEM2GetPublicKey import NEM2GetPublicKey
from trezor.messages.NEM2PublicKey import NEM2PublicKey
from trezor.ui.layouts import show_pubkey

from apps.common import paths
from apps.common.keychain import Keychain, auto_keychain


@auto_keychain(__name__)
async def get_public_key(ctx, msg: NEM2GetPublicKey, keychain: Keychain):
    await paths.validate_path(ctx, keychain, msg.address_n)
    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()

    if msg.show_display:
        await show_pubkey(ctx, hexlify(pubkey).decode())

    return NEM2PublicKey(public_key=pubkey)
