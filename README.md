# 🔮 Mysterio-Vibephantom (v2.0)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-purple.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20Windows-blue.svg" alt="Platforms">
  <img src="https://img.shields.io/badge/Vibe-Phantom%20Stealth-darkgreen.svg" alt="Vibe">
</p>

**Mysterio-Vibephantom** is a pro-grade, color-infused modular reconnaissance and intelligence-gathering suite. Built entirely in Python, it allows cybersecurity researchers and ethical hackers to run deep target profiling across networks, DNS architecture, security configurations, and historical web footprints—all while maintaining a sleek cyber-punk terminal vibe.

---

## ✨ Features Across 5 Intelligent Modules

* 🌐 **Network & Performance:** Resolves target IP, tracks real-time HTTP load latency, page weight, cookie security flags, and geolocation mapping. Includes a built-in fast port-scanner.
* 🧬 **DNS & Mail Audit:** Enumerates A, MX, TXT, and NS records with automatic SPF mail spoofing protection layout tracking.
* 🛡️ **Security & WAF Auditor:** Extracts SSL/TLS certificate details (issuer, expiry) and evaluates critical missing defense headers (CSP, HSTS, X-Frame-Options).
* 📝 **Content & SEO Crawler:** Parses HTML structure, extracts active URLs, audits site titles, meta descriptions, and maps exposed `robots.txt` paths.
* 🗂️ **Meta & Wayback History:** Performs WHOIS data scraping and directly queries the Internet Archive (Wayback Machine) to trace deep historical snapshots.

---

## 🛠️ Installation & Setup

Choose your battleground and copy the commands below to deploy the phantom engine.

### 🐧 Option A: Kali Linux / Ubuntu
Open your terminal and execute the following line-by-line commands:

```bash
# Update system packages
sudo apt update && sudo apt install git python3 python3-pip -y

# Clone the repository
git clone [https://github.com/YOUR-USERNAME/spy-recon-pro.git](https://github.com/YOUR-USERNAME/spy-recon-pro.git)
cd spy-recon-pro

# Install essential dependencies
pip3 install -r requirements.txt

# Fire up the engine!
python3 Mysterio-vibephantom.py



