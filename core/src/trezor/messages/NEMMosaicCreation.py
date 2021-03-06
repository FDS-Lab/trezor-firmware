# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEMMosaicDefinition import NEMMosaicDefinition

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMMosaicCreation(p.MessageType):

    def __init__(
        self,
        *,
        definition: Optional[NEMMosaicDefinition] = None,
        sink: Optional[str] = None,
        fee: Optional[int] = None,
    ) -> None:
        self.definition = definition
        self.sink = sink
        self.fee = fee

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('definition', NEMMosaicDefinition, None),
            2: ('sink', p.UnicodeType, None),
            3: ('fee', p.UVarintType, None),
        }
