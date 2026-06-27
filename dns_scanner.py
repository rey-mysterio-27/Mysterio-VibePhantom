import dns.resolver

def run(domain):
    print("\033[38;5;141m🔮 [MYSTERIO-VIBEPHANTOM] ─── 🔍 AGENT ACTIVE\033[0m")
    print("\033[38;5;141m🔮 [VIBE-CHECK] ─── 🧬 DNS & MAIL CONFIGURATION\033[0m")
    for r_type in ['A', 'MX', 'TXT', 'NS']:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            print(f"  [+] {r_type} Records :")
            for rdata in answers:
                print(f"    - {rdata}")
                if r_type == 'TXT' and 'v=spf1' in str(rdata):
                    print("      [✔] Security: SPF Mail Protection Active.")
        except Exception:
            print(f"  [-] No {r_type} records found.")