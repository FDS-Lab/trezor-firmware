# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2DecryptMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 811

    def __init__(
        self,
        *,
        address_n: Optional[List[int]] = None,
        sender_public_key: Optional[str] = None,
        payload: Optional[str] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.sender_public_key = sender_public_key
        self.payload = payload

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('sender_public_key', p.UnicodeType, None),
            3: ('payload', p.UnicodeType, None),
        }
