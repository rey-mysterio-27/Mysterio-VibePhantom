import socket
import ssl
import requests

def run(domain):
    print("\033[38;5;141m🔮 [MYSTERIO-VIBEPHANTOM] ─── 🔍 AGENT ACTIVE\033[0m")
    print("\033[38;5;141m🔮 [VIBE-CHECK] ─── 🛡️ SECURITY, SSL & WAF\033[0m")
    
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, 443), timeout=4) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert['issuer'])
                print(f"  [+] SSL Issuer      : {issuer.get('organizationName', 'Unknown')}")
                print(f"  [+] SSL Expiry      : {cert.get('notAfter')}")
    except Exception:
        print("  [-] SSL Context     : Connection Failed.")

    try:
        res = requests.head(f"https://{domain}", timeout=4)
        headers = res.headers
        for sh in ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']:
            status = "✔ FOUND" if sh in headers else "❌ MISSING"
            print(f"    - {sh}: {status}")
    except Exception:
        pass

    try:
        sec_txt = requests.get(f"https://{domain}/.well-known/security.txt", timeout=3)
        print(f"  [+] security.txt    : {'✔ Found' if sec_txt.status_code == 200 else '❌ Missing'}")
    except Exception:
        pass