from trezor import wire
from trezor.messages import MessageType

from apps.common.paths import PATTERN_BIP44

CURVE = "ed25519"
SLIP44_ID = 4343
PATTERN = PATTERN_BIP44


def boot() -> None:
    wire.add(MessageType.SymbolGetAddress, __name__, "get_address")
    # wire.add(MessageType.SymbolGetPublicKey, __name__, "get_public_key")
    # wire.add(MessageType.SymbolSignTx, __name__, "sign_tx")
