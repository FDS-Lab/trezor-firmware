from ubinascii import unhexlify

from trezor.messages.NEM2EmbeddedTransactionCommon import NEM2EmbeddedTransactionCommon
from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon

from apps.common.writers import write_bytes, write_uint8, write_uint32_le

from ..writers import (
    get_common_message_size,
    get_embedded_common_message_size,
    serialize_embedded_tx_common,
    serialize_tx_common,
)


def serialize_account_link(
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    account_link: NEM2AccountLinkTransaction,
    embedded=False,
) -> bytearray:
    tx = bytearray()
    entity_type = common.type

    # Total size is the size of the common transaction properties
    # + the account link properties
    size = (
        get_common_message_size()
        if not embedded
        else get_embedded_common_message_size()
    )
    size += 32  # remote public key
    size += 1  # link action

    # Write size
    write_uint32_le(tx, size)
    # Write the common properties
    serialize_tx_common(tx, common) if not embedded else serialize_embedded_tx_common(
        tx, common
    )

    # Write Remote Public Key
    write_bytes(tx, unhexlify(account_link.remote_public_key))
    # Write Action Link Type
    write_uint8(tx, account_link.link_action)

    return tx
