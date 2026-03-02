# MMS (Maintenance Management System)

Production-oriented MMS foundation with Excel-logic parity utilities.

## Implemented Deliverables
- FastAPI backend with task/kpi/calendar endpoints.
- Frequency and due-date rule engine.
- Excel parser for formulas, named ranges, conditional formatting, data validation.
- Reconciliation utilities for Due Today vs Completed Today vs Scheduled Today mismatches.
- SQL schema and standardized seed data T-001..T-025.
- Tests for logic parity and KPI reconciliation.
- Architecture, business logic spec, and reconciliation report docs.

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .[test]
uvicorn app.main:app --reload
pytest
```

## Roadmap
- Phase 1: Core tasking + parity engine + immutable history (current).
- Phase 2: Next.js enterprise UI with RBAC, reports, and calendar workflows.
- Phase 3: Redis worker for notifications/escalations, IaC deployment on AWS/GCP, observability.
