from __future__ import annotations

from datetime import date


def reconcile_kpis(task_rows: list[dict], calendar_rows: list[dict], today: date) -> dict:
    due_today = [r for r in task_rows if r.get("next_due_date") == today and not r.get("is_completed")]
    completed_today = [r for r in calendar_rows if r.get("completed_at") and r["completed_at"].date() == today]
    scheduled_today = [r for r in calendar_rows if r.get("scheduled_for") == today]

    mismatch_causes = []
    if len(due_today) != len(scheduled_today):
        mismatch_causes.append("Tasks view uses due-date KPI while calendar uses scheduled instances KPI")
    if len(completed_today) > len(due_today):
        mismatch_causes.append("Calendar includes completion history records not equivalent to due tasks")

    return {
        "due_today_count": len(due_today),
        "completed_today_count": len(completed_today),
        "scheduled_today_count": len(scheduled_today),
        "mismatch_causes": mismatch_causes,
    }
