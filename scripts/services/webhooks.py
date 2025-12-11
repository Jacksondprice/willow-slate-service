"""Webhooks helpers for attendance tracking service for campus front offices."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def webhooks_step_0(records: list[dict], limit: int = 56) -> list[dict]:
    """Apply webhooks rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_1(records: list[dict], limit: int = 168) -> list[dict]:
    """Apply webhooks rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_2(records: list[dict], limit: int = 233) -> list[dict]:
    """Apply webhooks rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_3(records: list[dict], limit: int = 60) -> list[dict]:
    """Apply webhooks rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_4(records: list[dict], limit: int = 326) -> list[dict]:
    """Apply webhooks rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_5(records: list[dict], limit: int = 336) -> list[dict]:
    """Apply webhooks rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_6(records: list[dict], limit: int = 284) -> list[dict]:
    """Apply webhooks rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_7(records: list[dict], limit: int = 264) -> list[dict]:
    """Apply webhooks rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_8(records: list[dict], limit: int = 333) -> list[dict]:
    """Apply webhooks rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
