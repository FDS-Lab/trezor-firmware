# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEM2Address import NEM2Address
from .NEM2Mosaic import NEM2Mosaic
from .NEM2TransferMessage import NEM2TransferMessage

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2TransferTransaction(p.MessageType):

    def __init__(
        self,
        *,
        mosaics: Optional[List[NEM2Mosaic]] = None,
        recipient_address: Optional[NEM2Address] = None,
        message: Optional[NEM2TransferMessage] = None,
    ) -> None:
        self.mosaics = mosaics if mosaics is not None else []
        self.recipient_address = recipient_address
        self.message = message

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_address', NEM2Address, None),
            2: ('message', NEM2TransferMessage, None),
            3: ('mosaics', NEM2Mosaic, p.FLAG_REPEATED),
        }
