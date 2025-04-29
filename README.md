# 🔍 Vulnerability Scanner

A lightweight Python-based vulnerability scanner designed for educational and ethical hacking purposes. This tool helps identify open ports, fetch HTTP headers, grab banners, and perform basic Nmap scans on a target host.

---

## 📌 Features

- 🔓 **Port Scanning** (1–100) using Python's `socket`
- 🌐 **HTTP Header Retrieval** via the `requests` module
- 🧾 **Service Banner Grabbing** for ports 21, 22, 80, and 443
- 🛰️ **Integrated Nmap Scan** using `python-nmap`

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure your environment has the following installed:

- Python 3.x
- `nmap` installed and in your PATH
- Bash (for running `.sh` script, if using)
- Recommended: Kali Linux or any pentest-friendly distro

---

### 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CoderNandhu/vuln_scanner.git
   cd vuln_scanner
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

### 🧪 Usage

To start scanning:
```bash
python3 scanner.py
```

Follow the prompt to enter a domain or IP (e.g., `scanme.nmap.org` or `192.168.1.1`).

---

## 🧰 Modules Used

- `socket` – For low-level network port scanning and banner grabbing
- `requests` – For HTTP header retrieval
- `nmap` – For full-featured port scanning (via Python wrapper)

---

## 📂 Sample Output

```text
[+] Scanning ports 1 to 100...
[OPEN] Port 22
[OPEN] Port 80

[+] Fetching HTTP headers...
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html

[+] Banner on port 22: SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5

[+] Running Nmap scan (1-100)...
Host: 192.168.1.1 (up)
Protocol: tcp
Port: 22     State: open
Port: 80     State: open
```

---

## ⚠️ Disclaimer

> **This tool is strictly for educational purposes.**  
> Do **NOT** use this to scan targets you do not own or have permission to test. Unauthorized scanning is **illegal** and **unethical**.

---

## 👨‍💻 Author

Made with ❤️ by **Neo (CoderNandhu)**  
GitHub: [@CoderNandhu](https://github.com/CoderNandhu)

---
