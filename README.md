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
| Technique ID | Technique | Tactics |<br>
|--------------|-----------|---------|<br>
| T1110 | Brute Force | Credential Access <br>

## Future Improvements
<br>
- Splunk Integration<br>
- Real-time Log Monitoring<br>
- Dashboard Visualizations<br>

## Project Screenshots

### Detection Engine<br>
Detection dashboard for a SOC log analysis tool, showing a dark terminal interface with a timeline of suspicious activity, failed login counts, IOC summaries, and source country analysis. The display uses green and cyan text on a black background and emphasizes an active brute force investigation. Text visible includes Attack Timeline, IOC Summary, and Source Countries, with a serious, alert-driven tone.[(Screenshots/detection_engine.png)]

### IOC & Timeline Analysis<br>
IOC and timeline analysis screen showing a chronological attack sequence, flagged malicious IP addresses, and a summary of suspicious activity across multiple countries. The interface is a dark security dashboard with technical text and numerical counts, highlighting a brute force campaign and an investigative workflow. Text visible includes malicious IPs found and source countries, with a tense, high-alert tone.[(Screenshots/ioc_timeline.png)]


### Account Abuse Detection <br>
Account abuse detection report displaying repeated failed authentication attempts and account lockout indicators in a dark SOC monitoring interface. The screen highlights suspicious activity targeting a user account, with technical event details and warning-style information. The environment is a security operations dashboard with a serious, urgent tone and visible alerts about account abuse. [(Screenshots/account_lockout.png)]


## Investigation Workflow

1. Collect Windows Authentication Logs<br>
2. Parse Log Data<br>
3. Detect Failed Logins<br>
4. Identify Brute Force Patterns<br>
5. Extract IOCs<br>
6. Map Technique to MITRE ATT&CK<br>
7. Generate Alerts<br>
8. Produce Investigation Report<br>

## Indicators of Compromise

| IOC Type | Value |<br>
|----------|-------|<br>
| Source IP | 192.168.1.50 |<br>
| Username | Administrator |<br>
| Event ID | 4625 |<br>
| Technique | T1110 |<br>

## Windows Event IDs Used

| Event ID | Description |<br>
|-----------|-------------|<br>
| 4624 | Successful Login |<br>
| 4625 | Failed Login |<br>
| 4740 | Account Locked |<br>

## Detection Rules

### Brute Force

Condition:<br>
- Same IP<br>
- 5+ failed logins<br>
- Within short period<br>
<br>
Severity:<br>
- High: 10+<br>
- Medium: 5-9<br>
- Low: < 5<br>


## [HIGH] Brute Force Attack Detected
<br>
Source IP: 192.168.1.50<br>
Failed Attempts: 15<br>
Target User: Administrator<br >

MITRE Technique:<br>
T1110 - Brute Force<br>

## Skills Demonstrated

- Log Analysis<br>
- Incident Investigation<br>
- IOC Identification<br>
- MITRE ATT&CK Mapping<br>
- Threat Detection<br>
- Python Automation<br>
- Windows Security Monitoring<br>
- Alert Generation<br>


## Incident Summary

Detected 15 failed login attempts from a single source IP against the Administrator account.<br>

Classification: High Severity<br>

MITRE Technique:<br>
T1110 - Brute Force<br>

Recommended Actions:<br>
- Block Source IP<br>
- Reset Credentials<br>
- Review Authentication Logs<br>