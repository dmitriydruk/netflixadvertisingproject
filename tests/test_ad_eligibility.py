from datetime import datetime

from src.ad_eligibility import Campaign, is_eligible


def make_campaign(*, enabled: bool = True) -> Campaign:
    return Campaign(
        campaign_id="campaign-demo-7",
        starts_at=datetime.fromisoformat("2026-10-01T09:00:00"),
        ends_at=datetime.fromisoformat("2026-10-01T10:00:00"),
        enabled=enabled,
    )


def test_campaign_is_eligible_before_end_time() -> None:
    campaign = make_campaign()
    request_time = datetime.fromisoformat("2026-10-01T09:59:59")

    assert is_eligible(campaign, request_time) is True


def test_campaign_is_eligible_exactly_at_end_time() -> None:
    campaign = make_campaign()
    request_time = datetime.fromisoformat("2026-10-01T10:00:00")

    assert is_eligible(campaign, request_time) is True


def test_campaign_is_ineligible_after_end_time() -> None:
    campaign = make_campaign()
    request_time = datetime.fromisoformat("2026-10-01T10:00:01")

    assert is_eligible(campaign, request_time) is False


def test_disabled_campaign_is_ineligible() -> None:
    campaign = make_campaign(enabled=False)
    request_time = datetime.fromisoformat("2026-10-01T09:30:00")

    assert is_eligible(campaign, request_time) is False


# The exact-end-time regression test is intentionally added during the demo.