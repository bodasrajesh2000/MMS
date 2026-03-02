insert into roles(name) values ('operator'), ('supervisor'), ('admin');
insert into users(email, full_name, role_id) values
('op1@example.com','Operator 1',1),
('op2@example.com','Operator 2',1),
('sup1@example.com','Supervisor 1',2),
('admin@example.com','Admin',3);

insert into tasks(task_code,title,category,priority,frequency_code,next_due_date,is_enabled) values
('T-001','Inspect UPS battery health','Electrical','High','weekly','2026-01-06',true),
('T-002','Network switch firmware check','Network','Medium','monthly','2026-01-10',true),
('T-003','Emergency exit light test','Safety','High','bi_weekly','2026-01-05',true),
('T-004','Printer roller cleaning','Devices','Low','quarterly','2026-01-21',true),
('T-005','Server room temperature log','Hardware','High','daily','2026-01-02',true),
('T-006','HVAC filter inspection','Facilities','Medium','six_weeks','2026-01-15',true),
('T-007','Patch management audit','IT','High','monthly','2026-01-12',true),
('T-008','Backup generator run test','Electrical','High','monthly','2026-01-18',true),
('T-009','Core router redundancy failover','Network','High','quarterly','2026-01-25',true),
('T-010','Fire suppression panel check','Safety','High','weekly','2026-01-07',true),
('T-011','Barcode scanner calibration','Devices','Medium','bi_annual','2026-01-30',true),
('T-012','Rack cable re-tie','Hardware','Low','annual','2026-02-01',true),
('T-013','Floor safety markings audit','Facilities','Medium','monthly','2026-01-14',true),
('T-014','Endpoint antivirus verification','IT','High','weekly','2026-01-08',true),
('T-015','Grounding continuity test','Electrical','High','quarterly','2026-01-20',true),
('T-016','Wi-Fi AP channel optimization','Network','Medium','six_weeks','2026-01-16',true),
('T-017','First aid kit replenishment','Safety','Medium','monthly','2026-01-11',true),
('T-018','Tablet OS update check','Devices','Low','bi_weekly','2026-01-09',true),
('T-019','Storage array SMART review','Hardware','High','weekly','2026-01-04',true),
('T-020','Dock door lubrication','Facilities','Low','monthly','2026-01-22',true),
('T-021','Identity provider sync check','IT','Medium','weekly','2026-01-03',true),
('T-022','Panel thermal scan','Electrical','High','bi_annual','2026-01-27',true),
('T-023','WAN latency baseline test','Network','Medium','monthly','2026-01-17',true),
('T-024','PPE stock take','Safety','Medium','weekly','2026-01-13',true),
('T-025','Kiosk touch panel cleaning','Devices','Low','daily','2026-01-02',true);

insert into task_completions(task_id, completed_by, completed_at, notes)
select id, 1, '2026-01-01T08:00:00Z', 'Completed seed execution'
from tasks where task_code in ('T-001','T-003','T-005','T-010','T-014','T-019','T-021','T-024','T-025');
