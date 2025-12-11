"""Billing helpers for attendance tracking service for campus front offices."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def billing_step_0(records: list[dict], limit: int = 443) -> list[dict]:
    """Apply billing rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def billing_step_1(records: list[dict], limit: int = 55) -> list[dict]:
    """Apply billing rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def billing_step_2(records: list[dict], limit: int = 100) -> list[dict]:
    """Apply billing rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def billing_step_3(records: list[dict], limit: int = 267) -> list[dict]:
    """Apply billing rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def billing_step_4(records: list[dict], limit: int = 306) -> list[dict]:
    """Apply billing rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def billing_step_5(records: list[dict], limit: int = 435) -> list[dict]:
    """Apply billing rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("billing step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
