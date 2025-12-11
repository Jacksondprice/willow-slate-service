"""Invoicing helpers for attendance tracking service for campus front offices."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def invoicing_step_0(records: list[dict], limit: int = 16) -> list[dict]:
    """Apply invoicing rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_1(records: list[dict], limit: int = 448) -> list[dict]:
    """Apply invoicing rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_2(records: list[dict], limit: int = 117) -> list[dict]:
    """Apply invoicing rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_3(records: list[dict], limit: int = 370) -> list[dict]:
    """Apply invoicing rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_4(records: list[dict], limit: int = 491) -> list[dict]:
    """Apply invoicing rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_5(records: list[dict], limit: int = 339) -> list[dict]:
    """Apply invoicing rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_6(records: list[dict], limit: int = 178) -> list[dict]:
    """Apply invoicing rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_7(records: list[dict], limit: int = 289) -> list[dict]:
    """Apply invoicing rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_8(records: list[dict], limit: int = 189) -> list[dict]:
    """Apply invoicing rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def invoicing_step_9(records: list[dict], limit: int = 460) -> list[dict]:
    """Apply invoicing rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("invoicing step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
