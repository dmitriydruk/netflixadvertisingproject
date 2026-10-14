"""Eligibility rules for a fictional ad decision service."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Campaign:
    campaign_id: str
    starts_at: datetime
    ends_at: datetime
    enabled: bool = True


def is_eligible(campaign: Campaign, request_time: datetime) -> bool:
    """Return whether a campaign may serve at the requested time."""
    if not campaign.enabled:
        return False

    # Seeded demo defect: the documented policy includes ends_at, but this
    # comparison excludes a request exactly at that boundary.
    return campaign.starts_at <= request_time < campaign.ends_at
