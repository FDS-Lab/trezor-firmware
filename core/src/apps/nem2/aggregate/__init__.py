from trezor.messages.NEM2AggregateTransaction import NEM2AggregateTransaction
from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon

from .layout import ask_aggregate
from .serialize import serialize_aggregate_transaction


async def aggregate(
    ctx, common: NEM2TransactionCommon, aggregate: NEM2AggregateTransaction
) -> bytearray:
    await ask_aggregate(ctx, common, aggregate)
    return serialize_aggregate_transaction(common, aggregate)
