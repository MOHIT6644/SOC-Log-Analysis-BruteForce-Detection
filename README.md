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

PROJECT STRUCTURE

├── Alerts
│   └── alerts.txt

├── Logs
│   └── windows_logs.csv

├── Reports
│   ├── investigation_report.txt
│   ├── case_report.txt
│   ├── executive_summary.txt
│   ├── recommendations.txt
│   ├── mitre_mapping.txt
│   └── ioc_report.txt

├── Src
│   └── log_detector.py

└── README.md