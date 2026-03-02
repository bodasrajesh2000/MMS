# Data Integrity & Reconciliation Report

## Unified KPI Definitions
- Due Today: tasks where `next_due_date = today` and current state is not completed.
- Completed Today: history rows where `completed_at` date equals today.
- Scheduled Today: generated schedule instances whose `scheduled_for = today`.
- Overdue: due date < today and not completed.
- Due Soon: due date in `(today, today+7]` and not completed.

## Common Mismatch Causes
1. Tasks page uses Due Today but Calendar shows Completed Today (history rows).
2. Calendar can show multiple completion entries; task list deduplicates by task id.
3. Date truncation/timezone conversion mismatch between UTC timestamps and local-date comparison.
4. Status divergence caused by evaluating completion state on different tables.

## Resolution Implemented
- Canonical KPI functions are centralized in `app/core/kpis.py`.
- Reconciliation utility `app/services/reconciliation.py` checks count differences and explains causes.
- Tests verify parity logic and mismatch detection.
