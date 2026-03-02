from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
import calendar


@dataclass(frozen=True)
class FrequencyRule:
    code: str
    label: str


FREQUENCY_MAP = {
    "daily": FrequencyRule("daily", "Daily"),
    "weekly": FrequencyRule("weekly", "Weekly"),
    "bi_weekly": FrequencyRule("bi_weekly", "Bi-Weekly"),
    "monthly": FrequencyRule("monthly", "Monthly"),
    "six_weeks": FrequencyRule("six_weeks", "Every 6 Weeks"),
    "quarterly": FrequencyRule("quarterly", "Quarterly"),
    "bi_annual": FrequencyRule("bi_annual", "Bi-Annual"),
    "annual": FrequencyRule("annual", "Annual"),
    "on_demand": FrequencyRule("on_demand", "On-Demand"),
}


def _add_months(d: date, months: int) -> date:
    year = d.year + (d.month - 1 + months) // 12
    month = (d.month - 1 + months) % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def calculate_next_due_date(last_completion: date, frequency_code: str) -> date | None:
    if frequency_code == "on_demand":
        return None

    match frequency_code:
        case "daily":
            return last_completion + timedelta(days=1)
        case "weekly":
            return last_completion + timedelta(weeks=1)
        case "bi_weekly":
            return last_completion + timedelta(weeks=2)
        case "monthly":
            return _add_months(last_completion, 1)
        case "six_weeks":
            return last_completion + timedelta(weeks=6)
        case "quarterly":
            return _add_months(last_completion, 3)
        case "bi_annual":
            return _add_months(last_completion, 6)
        case "annual":
            return _add_months(last_completion, 12)
        case _:
            raise ValueError(f"Unsupported frequency code: {frequency_code}")


def due_status(next_due_date: date | None, today: date) -> str:
    if next_due_date is None:
        return "on_demand"
    if next_due_date < today:
        return "overdue"
    if next_due_date == today:
        return "due_today"
    if (next_due_date - today).days <= 7:
        return "due_soon"
    return "upcoming"
