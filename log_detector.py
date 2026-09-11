import pandas as pd
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parents[1]
    input_path = project_root / "Src" / "windows_logs.csv"
    alert_path = project_root / "Alerts" / "alerts.txt"

    df = pd.read_csv(input_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    failed_logins = df[df["status"] == "Failed Login"]
    ip_counts = failed_logins["source_ip"].value_counts()

    print("\n===== TARGETED USERS =====\n")
    user_counts = failed_logins["username"].value_counts()
    for user, count in user_counts.items():
        print(f"User: {user}")
        print(f"Failed Attempts: {count}")
        print("---------------------")

    alerts = []
    print("\n===== SUSPICIOUS IPS =====\n")
    for ip, count in ip_counts.items():
        if count < 5:
            continue

        severity = "HIGH" if count >= 10 else "MEDIUM"
        alert = (
            "ALERT: Possible Brute Force Attack\n"
            f"IP Address: {ip}\n"
            f"Attempts: {count}\n"
            f"Severity: {severity}\n"
            "--------------------------\n"
        )
        print(alert)
        alerts.append(alert)

    alert_path.parent.mkdir(parents=True, exist_ok=True)
    alert_path.write_text("".join(alerts), encoding="utf-8")
    print("Alerts saved successfully.")

    print("\n===== ATTACK TIMELINE =====\n")
    if failed_logins.empty:
        print("No failed logins found.")
    else:
        attack_start = failed_logins["timestamp"].min()
        attack_end = failed_logins["timestamp"].max()
        print(f"Attack Start : {attack_start}")
        print(f"Attack End   : {attack_end}")
        print(f"Duration     : {attack_end - attack_start}")

    print("\n===== IOC SUMMARY =====\n")
    suspicious_ips = [ip for ip, count in ip_counts.items() if count >= 5]
    print("Malicious IPs Found:")
    for ip in suspicious_ips:
        print(ip)

    print("\n===== SOURCE COUNTRIES =====\n")
    print(df["country"].value_counts())

    print("\n===== PASSWORD SPRAYING CHECK =====\n")
    unique_users = failed_logins["username"].nunique()
    if unique_users >= 5:
        print("Possible Password Spraying Detected")
        print(f"Targeted Accounts: {unique_users}")
    else:
        print("No Password Spraying Detected")

    print("\n===== ACCOUNT LOCKOUT DETECTION =====\n")
    for user, count in user_counts.items():
        if count >= 5:
            print(f"LOCKOUT RISK: {user}")
            print(f"Failed Attempts: {count}")
            print("-------------------")


if __name__ == "__main__":
    main()