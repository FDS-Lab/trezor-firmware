# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroLiveRefreshStepRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 554

    def __init__(
        self,
        *,
        out_key: Optional[bytes] = None,
        recv_deriv: Optional[bytes] = None,
        real_out_idx: Optional[int] = None,
        sub_addr_major: Optional[int] = None,
        sub_addr_minor: Optional[int] = None,
    ) -> None:
        self.out_key = out_key
        self.recv_deriv = recv_deriv
        self.real_out_idx = real_out_idx
        self.sub_addr_major = sub_addr_major
        self.sub_addr_minor = sub_addr_minor

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('out_key', p.BytesType, None),
            2: ('recv_deriv', p.BytesType, None),
            3: ('real_out_idx', p.UVarintType, None),
            4: ('sub_addr_major', p.UVarintType, None),
            5: ('sub_addr_minor', p.UVarintType, None),
        }
