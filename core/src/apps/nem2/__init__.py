from trezor import wire
from trezor.messages import MessageType

from apps.common.paths import PATTERN_SEP5

CURVE = "ed25519"
SLIP44_ID = 4343
PATTERNS = (
    PATTERN_SEP5,
    "m/44'/coin_type'/0'/account'",  # Ledger compatibility
)


def boot() -> None:
    wire.add(MessageType.NEM2GetPublicKey, __name__, "get_public_key")
    wire.add(MessageType.NEM2SignTx, __name__, "sign_tx")
    wire.add(MessageType.NEM2EncryptMessage, __name__, "encrypt_message")
    wire.add(MessageType.NEM2DecryptMessage, __name__, "decrypt_message")
