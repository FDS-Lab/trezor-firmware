# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosAsset(p.MessageType):

    def __init__(
        self,
        *,
        amount: Optional[int] = None,
        symbol: Optional[int] = None,
    ) -> None:
        self.amount = amount
        self.symbol = symbol

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('amount', p.SVarintType, None),
            2: ('symbol', p.UVarintType, None),
        }
