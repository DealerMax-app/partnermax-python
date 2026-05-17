# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AuthLoginResponse"]


class AuthLoginResponse(BaseModel):
    partner_id: str

    session_expires_at: datetime
