# Business Logic Spec (Excel → Backend)

This repository includes a parser (`app/services/excel_logic_parser.py`) that extracts:
- sheet structures
- formulas
- named ranges
- data validations
- conditional formatting

## Formula-to-Backend Mapping
- `next_due_date = last_completion + frequency interval` → `calculate_next_due_date()` in `app/core/frequency.py`.
- Due status derivation (`overdue`, `due_today`, `due_soon`, `upcoming`) → `due_status()`.
- KPI definitions:
  - Due Today: `next_due_date == today AND not completed`
  - Completed Today: `completion.completed_at::date == today`
  - Scheduled Today: `scheduled_for == today`

## Notes
- Any extracted Excel formula should be represented as explicit deterministic Python service logic.
- No hidden behavior is allowed: helper columns become auditable service methods.
