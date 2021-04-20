from trezor import wire
from trezor.messages import MessageType

from apps.common.paths import PATTERN_SEP5

CURVE = "ed25519"
SLIP44_ID = 4343

PATTERNS = (
    PATTERN_SEP5,
    "m/44'/coin_type'/account'/0'/0'",  # NanoWallet compatibility
)


def boot() -> None:
    wire.add(MessageType.NEM2GetPublicKey, __name__, "get_public_key")