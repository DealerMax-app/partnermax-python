# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VehicleRetrieveParams"]


class VehicleRetrieveParams(TypedDict, total=False):
    dealer_id: Required[str]

    include_deleted: bool
    """If true, the detail of a soft-deleted vehicle is returned.

    Default false — soft-deleted rows return 404 to keep behaviour consistent with
    the list endpoint.
    """
