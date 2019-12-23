# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2AccountRestrictionFlags = Literal[1, 2, 4, 16385, 16388, 32769, 32770, 32772, 49153, 49156]
    except ImportError:
        pass


class NEM2AccountMosaicRestrictionTransaction(p.MessageType):

    def __init__(
        self,
        restriction_type: EnumTypeNEM2AccountRestrictionFlags = None,
        restriction_additions: List[str] = None,
        restriction_deletions: List[str] = None,
    ) -> None:
        self.restriction_type = restriction_type
        self.restriction_additions = restriction_additions if restriction_additions is not None else []
        self.restriction_deletions = restriction_deletions if restriction_deletions is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('restriction_type', p.EnumType("NEM2AccountRestrictionFlags", (1, 2, 4, 16385, 16388, 32769, 32770, 32772, 49153, 49156)), 0),
            2: ('restriction_additions', p.UnicodeType, p.FLAG_REPEATED),
            3: ('restriction_deletions', p.UnicodeType, p.FLAG_REPEATED),
        }
