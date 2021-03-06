# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoAddressParametersType import CardanoAddressParametersType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoGetAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 307

    def __init__(
        self,
        *,
        protocol_magic: int,
        network_id: int,
        address_parameters: CardanoAddressParametersType,
        show_display: bool = False,
    ) -> None:
        self.protocol_magic = protocol_magic
        self.network_id = network_id
        self.address_parameters = address_parameters
        self.show_display = show_display

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('show_display', p.BoolType, False),  # default=false
            3: ('protocol_magic', p.UVarintType, p.FLAG_REQUIRED),
            4: ('network_id', p.UVarintType, p.FLAG_REQUIRED),
            5: ('address_parameters', CardanoAddressParametersType, p.FLAG_REQUIRED),
        }
