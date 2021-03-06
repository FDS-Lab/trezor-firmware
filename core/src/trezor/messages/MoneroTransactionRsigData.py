# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionRsigData(p.MessageType):

    def __init__(
        self,
        *,
        grouping: Optional[List[int]] = None,
        rsig_parts: Optional[List[bytes]] = None,
        rsig_type: Optional[int] = None,
        offload_type: Optional[int] = None,
        mask: Optional[bytes] = None,
        rsig: Optional[bytes] = None,
        bp_version: Optional[int] = None,
    ) -> None:
        self.grouping = grouping if grouping is not None else []
        self.rsig_parts = rsig_parts if rsig_parts is not None else []
        self.rsig_type = rsig_type
        self.offload_type = offload_type
        self.mask = mask
        self.rsig = rsig
        self.bp_version = bp_version

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('rsig_type', p.UVarintType, None),
            2: ('offload_type', p.UVarintType, None),
            3: ('grouping', p.UVarintType, p.FLAG_REPEATED),
            4: ('mask', p.BytesType, None),
            5: ('rsig', p.BytesType, None),
            6: ('rsig_parts', p.BytesType, p.FLAG_REPEATED),
            7: ('bp_version', p.UVarintType, None),
        }
