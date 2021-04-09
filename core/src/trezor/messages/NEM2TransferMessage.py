# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2TransferMessage(p.MessageType):

    def __init__(
        self,
        *,
        payload: Optional[str] = None,
        type: Optional[int] = None,
    ) -> None:
        self.payload = payload
        self.type = type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payload', p.UnicodeType, None),
            2: ('type', p.UVarintType, None),
        }
