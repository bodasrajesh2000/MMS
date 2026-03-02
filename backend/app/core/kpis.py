from __future__ import annotations

from datetime import date, datetime


def is_due_today(next_due_date: date | None, completed: bool, today: date) -> bool:
    return bool(next_due_date == today and not completed)


def is_completed_today(completed_at: datetime | None, today: date) -> bool:
    return bool(completed_at and completed_at.date() == today)


def is_scheduled_today(scheduled_for: date | None, today: date) -> bool:
    return bool(scheduled_for == today)
