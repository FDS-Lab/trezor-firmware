from micropython import ure
from trezor.messages.NEM2SignTx import (
    NEM2SignTx,
    NEM2TransactionCommon,
    NEM2TransferTransaction,
)
from trezor.wire import ProcessError

from ..helpers import (
    NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT,
    NEM2_NAMESPACE_REGISTRATION_TYPE_SUB
)

def _validate_namespace_registration(namespace_registration: NEM2NamespaceRegistrationTransaction, version: int):
    if(
        namespace_registration.registration_type != NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT and
        namespace_registration.registration_type != NEM2_NAMESPACE_REGISTRATION_TYPE_SUB
    ):
        raise ProcessError("Invalid namespace registration type")
    if(namespace_registration.registration_type == NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT):
        if(namespace_registration.duration < 1 or namespace_registration.duration > 2102400):
            raise ProcessError("Invalid namespace registration duration")
    if(namespace_registration.registration_type == NEM2_NAMESPACE_REGISTRATION_TYPE_SUB):
        if(namespace_registration.parent_id is None):
            raise ProcessError("Parent Id is required for subnamespace registration")
    namespace_name_decoded = bytes(namespace_registration.namespace_name).decode()
    #TODO: figure out how to get regex in here, valid characters are a,b,c,…,z,0,1,2,…,9,_ ,-
    if(len(bytes(namespace_registration.namespace_name).decode() > 64)):
        raise ProcessError("Maximum namespace name is 64 characters")
    if(namespace_registration.id is None):
        raise ProcessError("Id is required")



