# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroRingCtSig import MoneroRingCtSig

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionAllOutSetAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 514

    def __init__(
        self,
        *,
        extra: Optional[bytes] = None,
        tx_prefix_hash: Optional[bytes] = None,
        rv: Optional[MoneroRingCtSig] = None,
        full_message_hash: Optional[bytes] = None,
    ) -> None:
        self.extra = extra
        self.tx_prefix_hash = tx_prefix_hash
        self.rv = rv
        self.full_message_hash = full_message_hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('extra', p.BytesType, None),
            2: ('tx_prefix_hash', p.BytesType, None),
            4: ('rv', MoneroRingCtSig, None),
            5: ('full_message_hash', p.BytesType, None),
        }
