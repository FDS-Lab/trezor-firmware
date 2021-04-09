# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2NamespaceRegistrationType = Literal[0, 1]
    except ImportError:
        pass


class NEM2NamespaceRegistrationTransaction(p.MessageType):

    def __init__(
        self,
        *,
        duration: Optional[str] = None,
        parent_id: Optional[str] = None,
        id: Optional[str] = None,
        registration_type: EnumTypeNEM2NamespaceRegistrationType = 0,
        name_size: Optional[int] = None,
        namespace_name: Optional[str] = None,
    ) -> None:
        self.duration = duration
        self.parent_id = parent_id
        self.id = id
        self.registration_type = registration_type
        self.name_size = name_size
        self.namespace_name = namespace_name

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('duration', p.UnicodeType, None),
            2: ('parent_id', p.UnicodeType, None),
            3: ('id', p.UnicodeType, None),
            4: ('registration_type', p.EnumType("NEM2NamespaceRegistrationType", (0, 1)), 0),  # default=ROOT
            5: ('name_size', p.UVarintType, None),
            6: ('namespace_name', p.UnicodeType, None),
        }
