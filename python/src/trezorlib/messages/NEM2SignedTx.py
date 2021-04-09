# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2SignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 807

    def __init__(
        self,
        *,
        payload: Optional[bytes] = None,
        hash: Optional[bytes] = None,
        signature: Optional[bytes] = None,
    ) -> None:
        self.payload = payload
        self.hash = hash
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payload', p.BytesType, None),
            2: ('hash', p.BytesType, None),
            3: ('signature', p.BytesType, None),
        }
