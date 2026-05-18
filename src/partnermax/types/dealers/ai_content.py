# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AIContent"]


class AIContent(BaseModel):
    """AI-generated editorial content for a single vehicle.

    Produced asynchronously by the ``usato_ai_content_worker`` in
    ``azurenet-engine`` within ~60 seconds of vehicle creation. While the
    worker is still pending, every field is ``null``; once the worker
    completes the row this object carries the full editorial set the
    cross-network AI consumers (MCP, ChatGPT Custom GPT, NLWeb) display.

    Layered descriptions:

    * ``tagline``       — 8–12 word headline. Use on listing cards / push notifications.
    * ``short``         — 1–2 sentence summary (≤ 220 chars). Use as the meta description fallback.
    * ``medium``        — paragraph (~400 chars). Use on vehicle-detail SEO blurbs.
    * ``long``          — full marketing description (1500–3000 chars). Use on detail pages.
    * ``highlights``    — array of 3–7 selling points. Render as a bullet list above the description.
    * ``faq``           — array of ``{question, answer}`` objects. Render as accordion / JSON-LD ``FAQPage``.
    * ``seo_title``     — ≤ 60 chars, ``<title>``-ready.
    * ``seo_description`` — ≤ 160 chars, meta description-ready.
    * ``slug``          — URL-safe slug used in the canonical URL on the dealer site.

    The Italian language is canonical (``lang='it'``). Multi-language is
    on the roadmap; until then the partner gets exactly what the
    consumer AI surfaces get.
    """

    faq: Optional[List[Dict[str, str]]] = None
    """Array of `{question, answer}` objects.

    Each entry has two string keys; render with the partner's own FAQ UI or feed
    into a `FAQPage` JSON-LD block.
    """

    generated_at: Optional[datetime] = None
    """UTC timestamp of the most recent AI generation.

    `null` until the worker first processes the vehicle (≤ 60 seconds after vehicle
    creation).
    """

    highlights: Optional[List[str]] = None

    long: Optional[str] = None

    medium: Optional[str] = None

    seo_description: Optional[str] = None

    seo_title: Optional[str] = None

    short: Optional[str] = None

    slug: Optional[str] = None

    tagline: Optional[str] = None
