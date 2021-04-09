# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2MosaicDefinitionTransaction(p.MessageType):

    def __init__(
        self,
        *,
        nonce: Optional[int] = None,
        mosaic_id: Optional[str] = None,
        flags: Optional[int] = None,
        divisibility: Optional[int] = None,
        duration: Optional[int] = None,
    ) -> None:
        self.nonce = nonce
        self.mosaic_id = mosaic_id
        self.flags = flags
        self.divisibility = divisibility
        self.duration = duration

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('nonce', p.UVarintType, None),
            2: ('mosaic_id', p.UnicodeType, None),
            3: ('flags', p.UVarintType, None),
            4: ('divisibility', p.UVarintType, None),
            5: ('duration', p.UVarintType, None),
        }
