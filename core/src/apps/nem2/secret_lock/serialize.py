from ubinascii import unhexlify

from trezor.crypto import base32
from trezor.messages.NEM2EmbeddedTransactionCommon import NEM2EmbeddedTransactionCommon
from trezor.messages.NEM2SecretLockTransaction import NEM2SecretLockTransaction
from trezor.messages.NEM2SecretProofTransaction import NEM2SecretProofTransaction
from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon

from apps.common.writers import (
    write_bytes,
    write_uint8,
    write_uint16_le,
    write_uint32_le,
    write_uint64_le,
)

from ..writers import (
    get_common_message_size,
    get_embedded_common_message_size,
    serialize_embedded_tx_common,
    serialize_tx_common,
)


def serialize_secret_lock(
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    secret_lock: NEM2SecretLockTransaction,
    embedded=False,
) -> bytearray:
    tx = bytearray()

    # Total size is the size of the common transaction properties
    # + the secret lock transaction specific properties
    size = (
        get_common_message_size()
        if not embedded
        else get_embedded_common_message_size()
    )
    size += get_secret_lock_body_size()

    # Write size
    write_uint32_le(tx, size)
    # Write the common properties
    serialize_tx_common(tx, common) if not embedded else serialize_embedded_tx_common(
        tx, common
    )

    # Write the secret lock transaction body
    write_bytes(tx, unhexlify(secret_lock.secret))  # secret
    serialize_mosaic(tx, secret_lock.mosaic.id, secret_lock.mosaic.amount)  # mosaic
    write_uint64_le(tx, int(secret_lock.duration))  # duration
    write_uint8(tx, secret_lock.hash_algorithm)  # hash algorithm
    # recipient_address (catbuffer UnresolvedAddress - 25 bits) base 32 encoded
    write_bytes(tx, base32.decode(secret_lock.recipient_address.address))

    return tx


def serialize_secret_proof(
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    secret_proof: NEM2SecretProofTransaction,
    embedded=False,
) -> bytearray:
    tx = bytearray()

    # Total size is the size of the common transaction properties
    # + the secret lock transaction specific properties
    size = (
        get_common_message_size()
        if not embedded
        else get_embedded_common_message_size()
    )
    size += get_secret_proof_body_size(secret_proof.proof)

    # # Write size
    write_uint32_le(tx, size)
    # # Write the common properties
    serialize_tx_common(tx, common) if not embedded else serialize_embedded_tx_common(
        tx, common
    )

    # Write the secret lock transaction body
    write_bytes(tx, unhexlify(secret_proof.secret))  # secret
    write_uint16_le(tx, len(unhexlify(secret_proof.proof)))  # proof length
    write_uint8(tx, secret_proof.hash_algorithm)  # hash algorithm
    # recipient_address (catbuffer UnresolvedAddress - 25 bits) base 32 encoded
    write_bytes(tx, base32.decode(secret_proof.recipient_address.address))
    write_bytes(tx, unhexlify(secret_proof.proof))  # proof

    return tx


def get_secret_lock_body_size():
    # Add up the secret lock specific message attribute sizes
    size = 8  # mosaic ID is 8 bytes
    size += 8  # mosaic amount is 8 bytes
    size += 8  # duration is 8 bytes
    size += 1  # algorithm is 1 bytes
    size += 25  # recipient is 25 bytes
    size += 32  # secret is 32 bytes
    return size


def get_secret_proof_body_size(proof):
    # Add up the secret proof specific message attribute sizes
    size = 32  # secret is 32 bytes
    size += 2  # proof size is 2 bytes
    size += 1  # algorithm is 1 bytes
    size += 25  # recipient is 25 bytes
    size += len(unhexlify(proof))
    return size


def serialize_mosaic(w: bytearray, mosaic_id: str, amount: int):
    write_uint64_le(w, int(mosaic_id, 16))
    write_uint64_le(w, int(amount))
