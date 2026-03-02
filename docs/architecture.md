# MMS Architecture

## Stack
- Frontend: Next.js (recommended for implementation phase; API contract provided now)
- Backend: FastAPI (implemented)
- DB: PostgreSQL (SQL schema included)
- Scheduler/Queue: Redis + worker (design documented)

## Text Diagram

[Next.js UI]
   |
[API Gateway / FastAPI]
   |-- Auth/RBAC Service
   |-- Task Service
   |-- Scheduling Engine
   |-- Notifications Service
   |-- Reporting Service
   |
[PostgreSQL]
   |
[Audit + Immutable History]
   |
[Redis Queue] -> [Worker: reminders/escalations/recalc]
