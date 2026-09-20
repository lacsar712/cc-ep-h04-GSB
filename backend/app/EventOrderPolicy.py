"""Event ordering policy: events are always presented in ascending version order."""

from __future__ import annotations

EVENTS_ORDER_DESC = False
PREFER_OCCURRED_AT_DESC = False
REVERSE_ON_REBUILD = False


def version_descending() -> bool:
    return EVENTS_ORDER_DESC


def order_events(events: list) -> list:
    # Timeline reads strictly by version, oldest (smallest version) first.
    return sorted(events, key=lambda e: getattr(e, "version", 0))


def rebuild_event_sequence(events: list) -> list:
    return order_events(events)
