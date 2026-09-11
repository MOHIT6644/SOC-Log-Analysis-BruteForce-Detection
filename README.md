# SOC Log Analysis & Brute Force Detection

## Overview

This project analyzes Windows authentication logs and identifies brute force attacks.

## Features

- Failed Login Analysis
- IOC Extraction
- Severity Classification
- Alert Generation
- MITRE ATT&CK Mapping
- Attack Timeline
- Source Country Analysis
- Investigation Reporting

## Tools

- Python
- Pandas
- Windows Logs
- MITRE ATT&CK Framework

## Outcome

Successfully identified malicious login attempts, generated alerts, mapped activity to MITRE ATT&CK T1110, and documented incident response actions.

## PROJECT STRUCTURE

├── Alerts<br>
│   └── alerts.txt

├── Logs<br>
│   └── windows_logs.csv

├── Reports<br>
│   ├── investigation_report.txt<br>
│   ├── case_report.txt<br>
│   ├── executive_summary.txt<br>
│   ├── recommendations.txt<br>
│   ├── mitre_mapping.txt<br>
│   └── ioc_report.txt<br>

├── Src<br>
│   └── log_detector.py<br>
<br>
└── README.md

## Detection Logic

### Brute Force Detection
Trigger:<br>
- 5 or more failed logins from same IP<br>
<br>
Severity:<br>
- HIGH = 10+<br>
- MEDIUM = 5-9<br>
- LOW = < 5 <br>

### Password Spraying Detection
Trigger:<br>
- One source targets multiple accounts<br>

### Account Lockout Risk 
Trigger:<br>
- User receives 5+ failed logins<br>

## MITRE Mapping Table
<br>
| Technique ID | Technique |<br>
|--------------|-----------|<br>
| T1110 | Brute Force |<br>

## Future Improvements
<br>
- Splunk Integration<br>
- Real-time Log Monitoring<br>
- Email Alerting<br>
- Dashboard Visualizations<br>
- Threat Intelligence Feed Integration<br>