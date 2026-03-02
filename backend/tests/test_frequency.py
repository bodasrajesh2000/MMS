from datetime import date, datetime
from app.core.frequency import calculate_next_due_date
from app.core.kpis import is_due_today, is_completed_today, is_scheduled_today
from app.services.reconciliation import reconcile_kpis


def test_frequency_parity():
    start = date(2026, 1, 1)
    assert calculate_next_due_date(start, "daily") == date(2026, 1, 2)
    assert calculate_next_due_date(start, "weekly") == date(2026, 1, 8)
    assert calculate_next_due_date(start, "bi_weekly") == date(2026, 1, 15)
    assert calculate_next_due_date(start, "monthly") == date(2026, 2, 1)
    assert calculate_next_due_date(start, "six_weeks") == date(2026, 2, 12)
    assert calculate_next_due_date(start, "quarterly") == date(2026, 4, 1)
    assert calculate_next_due_date(start, "bi_annual") == date(2026, 7, 1)
    assert calculate_next_due_date(start, "annual") == date(2027, 1, 1)
    assert calculate_next_due_date(start, "on_demand") is None


def test_kpi_definitions():
    today = date(2026, 1, 15)
    assert is_due_today(today, False, today)
    assert not is_due_today(today, True, today)
    assert is_completed_today(datetime(2026, 1, 15, 9, 0, 0), today)
    assert is_scheduled_today(today, today)


def test_reconciliation_mismatch_detection():
    today = date(2026, 1, 15)
    task_rows = [
        {"next_due_date": today, "is_completed": False},
        {"next_due_date": date(2026, 1, 16), "is_completed": False},
    ]
    calendar_rows = [
        {"scheduled_for": today, "completed_at": datetime(2026, 1, 15, 8, 0, 0)},
        {"scheduled_for": today, "completed_at": None},
    ]
    report = reconcile_kpis(task_rows, calendar_rows, today)
    assert report["due_today_count"] == 1
    assert report["scheduled_today_count"] == 2
    assert report["mismatch_causes"]
