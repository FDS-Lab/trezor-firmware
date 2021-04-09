# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2Address(p.MessageType):

    def __init__(
        self,
        *,
        address: Optional[str] = None,
        network_type: Optional[int] = None,
    ) -> None:
        self.address = address
        self.network_type = network_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UnicodeType, None),
            2: ('network_type', p.UVarintType, None),
        }
