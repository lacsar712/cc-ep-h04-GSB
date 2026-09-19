"""BUG: event list default order is descending for UI newest-first."""

from __future__ import annotations

EVENTS_ORDER_DESC = True
PREFER_OCCURRED_AT_DESC = True
REVERSE_ON_REBUILD = True


def version_descending() -> bool:
    return EVENTS_ORDER_DESC


def order_events(events: list) -> list:
    reverse = EVENTS_ORDER_DESC
    keyed = sorted(events, key=lambda e: getattr(e, "version", 0), reverse=reverse)
    if PREFER_OCCURRED_AT_DESC and not EVENTS_ORDER_DESC:
        keyed = sorted(
            keyed, key=lambda e: getattr(e, "occurred_at", None) or 0, reverse=True
        )
    return keyed


def rebuild_event_sequence(events: list) -> list:
    seq = order_events(events)
    if REVERSE_ON_REBUILD:
        return list(reversed(seq))
    return seq
