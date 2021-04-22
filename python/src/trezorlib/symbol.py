# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from . import messages
from .protobuf import dict_to_proto
from .tools import expect, session


@expect(messages.SymbolAddress, field="address")
def get_address(client, address_n, show_display=False):
    return client.call(
        messages.SymbolGetAddress(address_n=address_n, show_display=show_display)
    )


# @expect(messages.SymbolPublicKey, field="public_key")
# def get_public_key(client, address_n, show_display=False):
#     return client.call(
#         messages.SymbolGetPublicKey(address_n=address_n, show_display=show_display)
#     )


# @session
# def sign_tx(client, address_n, tx_json):
#     msg = tx_json["msgs"][0]
#     envelope = dict_to_proto(messages.SymbolSignTx, tx_json)
#     envelope.msg_count = 1
#     envelope.address_n = address_n

#     response = client.call(envelope)

#     if not isinstance(response, messages.SymbolTxRequest):
#         raise RuntimeError(
#             "Invalid response, expected SymbolTxRequest, received "
#             + type(response).__name__
#         )

#     if "refid" in msg:
#         msg = dict_to_proto(messages.SymbolCancelMsg, msg)
#     elif "inputs" in msg:
#         msg = dict_to_proto(messages.SymbolTransferMsg, msg)
#     elif "ordertype" in msg:
#         msg = dict_to_proto(messages.SymbolOrderMsg, msg)
#     else:
#         raise ValueError("can not determine msg type")

#     response = client.call(msg)

#     if not isinstance(response, messages.SymbolSignedTx):
#         raise RuntimeError(
#             "Invalid response, expected SymbolSignedTx, received "
#             + type(response).__name__
#         )

#     return response
