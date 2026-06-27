import whois
import requests

def run(domain):
    print("\033[38;5;141m🔮 [MYSTERIO-VIBEPHANTOM] ─── 🔍 AGENT ACTIVE\033[0m")
    print("\033[38;5;141m🔮 [VIBE-CHECK] ─── 🗂️ META & HISTORICAL DATA\033[0m")
    try:
        w = whois.whois(domain)
        print(f"  [+] Registrar       : {w.registrar}")
        print(f"  [+] Creation Date   : {w.creation_date}")
    except Exception:
        print("  [-] WHOIS Data      : Private or Fetch Failed")

    try:
        res = requests.get(f"http://archive.org/wayback/available?url={domain}", timeout=4).json()
        snapshots = res.get("archived_snapshots", {})
        if snapshots:
            print(f"  [+] Wayback Snapshot: Found available snapshot at {snapshots['closest']['timestamp']}")
        else:
            print("  [-] Wayback Snapshot: No snapshots found.")
    except Exception:
        pass