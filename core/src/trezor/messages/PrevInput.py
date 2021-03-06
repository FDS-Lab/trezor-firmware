# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class PrevInput(p.MessageType):

    def __init__(
        self,
        *,
        prev_hash: bytes,
        prev_index: int,
        script_sig: bytes,
        sequence: int,
        decred_tree: Optional[int] = None,
    ) -> None:
        self.prev_hash = prev_hash
        self.prev_index = prev_index
        self.script_sig = script_sig
        self.sequence = sequence
        self.decred_tree = decred_tree

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('prev_hash', p.BytesType, p.FLAG_REQUIRED),
            3: ('prev_index', p.UVarintType, p.FLAG_REQUIRED),
            4: ('script_sig', p.BytesType, p.FLAG_REQUIRED),
            5: ('sequence', p.UVarintType, p.FLAG_REQUIRED),
            9: ('decred_tree', p.UVarintType, None),
        }
