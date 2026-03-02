from __future__ import annotations

from datetime import date
from fastapi import FastAPI
from app.core.frequency import due_status

app = FastAPI(title="MMS API", version="0.1.0")

SEED_TASKS = [
    {"task_code": f"T-{i:03d}", "title": f"Maintenance Task {i}", "next_due_date": date(2026, 1, (i % 28) + 1), "completed": False}
    for i in range(1, 26)
]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/tasks")
def tasks(today: date = date(2026, 1, 15)) -> list[dict]:
    return [{**t, "status": due_status(t["next_due_date"], today)} for t in SEED_TASKS]


@app.get("/dashboard/kpis")
def dashboard_kpis(today: date = date(2026, 1, 15)) -> dict:
    due_today = [t for t in SEED_TASKS if t["next_due_date"] == today and not t["completed"]]
    return {
        "due_today": len(due_today),
        "completed_today": 0,
        "scheduled_today": len(due_today),
    }


@app.get("/calendar/2026")
def calendar_2026() -> dict:
    months = {month: [] for month in range(1, 13)}
    for t in SEED_TASKS:
        months[t["next_due_date"].month].append(t["task_code"])
    return {"year": 2026, "months": months}
