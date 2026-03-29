# 🛡️ S.T.I.A.R.S (Security Tool for Intelligent Alerting & Real-time Status)

**S.T.I.A.R.S** is a lightweight, Python-driven security monitoring suite designed for Site Reliability Engineers (SRE) and Security Analysts. It provides real-time "Heartbeat" monitoring of web assets and instant incident notification via Telegram.

---

## 🚀 Core Capabilities
* **Real-Time Uptime Monitoring:** Constant status-code verification for mission-critical web endpoints.
* **Instant Incident Alerting:** Seamless integration with the Telegram Bot API to push "Critical Failure" alerts directly to your mobile device.
* **Forensic Event Logging:** Maintains a local `security_log.txt` with millisecond-accurate ISO timestamps for post-incident audits.
* **Defensive Connectivity:** Built-in handling for SSL/TLS handshake errors and network timeouts to ensure the monitor stays online during instability.
* **Secure Credential Management:** Utilizes environment variables (`.env`) to isolate sensitive API tokens from the source code.

---

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Networking:** `requests`, `urllib3`
* **Security:** `python-dotenv` (Credential Isolation), SSL verification handling.
* **Automation:** `time`, `os`

---

## 📋 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Kashy10g/S.T.I.A.R.S.git](https://github.com/Kashy10g/S.T.I.A.R.S.git)
   cd S.T.I.A.R.S