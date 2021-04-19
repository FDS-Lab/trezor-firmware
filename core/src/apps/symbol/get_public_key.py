from ubinascii import hexlify

from trezor.messages.SymbolGetPublicKey import SymbolGetPublicKey
from trezor.messages.SymbolPublicKey import SymbolPublicKey
from trezor.ui.layouts import show_pubkey

from apps.common import paths
from apps.common.keychain import Keychain, auto_keychain


@auto_keychain(__name__)
async def get_public_key(ctx, msg: SymbolGetPublicKey, keychain: Keychain):
    await paths.validate_path(ctx, keychain, msg.address_n)
    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()

    if msg.show_display:
        await show_pubkey(ctx, hexlify(pubkey).decode())

    return SymbolPublicKey(public_key=pubkey)
