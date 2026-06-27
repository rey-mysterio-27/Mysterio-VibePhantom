import socket
import requests
from datetime import datetime

def run(domain):
    print("\033[38;5;141m🔮 [MYSTERIO-VIBEPHANTOM] ─── 🔍 AGENT ACTIVE\033[0m")
    print("\033[38;5;141m🔮 [VIBE-CHECK] ─── 🌐 NETWORK & PERFORMANCE DETECTIONS\033[0m")
    try:
        ip = socket.gethostbyname(domain)
        print(f"  [+] Target IP       : {ip}")
    except Exception:
        print("  [-] Error: Unable to resolve IP.")
        return

    try:
        start_time = datetime.now()
        res = requests.get(f"https://{domain}", timeout=5, allow_redirects=True)
        load_time = (datetime.now() - start_time).total_seconds()
        
        print(f"  [+] HTTP Status     : {res.status_code} ({load_time:.2f}s load time)")
        print(f"  [+] Page Weight     : {len(res.content)/1024:.2f} KB")
        
        # Cookies
        print(f"  [+] Cookies Found   : {len(res.cookies)}")
        for cookie in res.cookies:
            print(f"    - {cookie.name} (Secure={cookie.secure})")
    except Exception as e:
        print(f"  [-] HTTP Connection : Failed ({e})")

    try:
        geo = requests.get(f"https://ipapi.co/{ip}/json/", timeout=4).json()
        print(f"  [+] ISP / Org       : {geo.get('org')} ({geo.get('asn')})")
        print(f"  [+] Server Location : {geo.get('city')}, {geo.get('country_name')}")
    except Exception:
        pass

    print("  [+] Scanning Common Ports...")
    for port in [22, 80, 443, 8080]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.8)
        if s.connect_ex((ip, port)) == 0:
            print(f"    - Port {port} : OPEN")
        s.close()