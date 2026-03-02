-- PostgreSQL schema (core)
create table roles (
  id serial primary key,
  name varchar(100) not null unique
);
create table role_permissions (
  id serial primary key,
  role_id int not null references roles(id),
  permission varchar(120) not null
);
create table users (
  id serial primary key,
  email varchar(255) not null unique,
  full_name varchar(255) not null,
  role_id int not null references roles(id),
  created_at timestamptz not null default now()
);
create table sites (
  id serial primary key,
  name varchar(120) not null
);
create table assets (
  id serial primary key,
  site_id int not null references sites(id),
  name varchar(120) not null
);
create table tasks (
  id serial primary key,
  task_code varchar(20) not null unique,
  title varchar(255) not null,
  category varchar(80) not null,
  priority varchar(20) not null,
  frequency_code varchar(20) not null,
  next_due_date date,
  is_enabled boolean not null default true
);
create table task_assignments (
  id serial primary key,
  task_id int not null references tasks(id),
  user_id int not null references users(id)
);
create table task_completions (
  id bigserial primary key,
  task_id int not null references tasks(id),
  completed_by int not null references users(id),
  completed_at timestamptz not null,
  notes text not null default ''
);
create table notifications (
  id bigserial primary key,
  task_id int not null references tasks(id),
  channel varchar(20) not null,
  sent_at timestamptz not null default now(),
  status varchar(20) not null
);
create table audit_logs (
  id bigserial primary key,
  actor_user_id int not null references users(id),
  action varchar(120) not null,
  entity_type varchar(80) not null,
  entity_id int not null,
  at_utc timestamptz not null default now()
);
create table sla_policies (
  id serial primary key,
  name varchar(120) not null,
  days_until_breach int not null
);
create table escalation_rules (
  id serial primary key,
  name varchar(120) not null,
  overdue_days_trigger int not null,
  escalate_to_role_id int not null references roles(id)
);
