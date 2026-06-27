import os  # System commands chalane ke liye import kiya
import sys
from datetime import datetime

# Importing custom modules
import network_scanner
import dns_scanner
import security_scanner
import content_scanner
import meta_scanner

# ANSI Neon Color Palette
NEON_PURPLE = "\033[38;5;141m"
CYAN        = "\033[36m"
GREEN       = "\033[32m"
YELLOW      = "\033[33m"
RED         = "\033[31m"
RESET       = "\033[0m"
BOLD        = "\033[1m"

def clear_terminal():
    # Windows ke liye 'cls' aur Linux/Termux ke liye 'clear' automatically chalega
    os.system('cls' if os.name == 'nt' else 'clear')

def mysterio_banner():
    # Large Cyber-punk style ASCII for MYSTERIO-VIBEPHANTOM
    banner_text = rf"""{NEON_PURPLE}{BOLD}
    __  ___           _            _                 _    _ ____  
   /  |/  /_  _______| |_ ___  ___(_)___       _  __(_)__| | __ ) 
  / /|_/ / / / / ___/ __/ _ \/ __/ / __ \_____| |/ / / _  |  _ \ 
 / /  / / /_/ (__  ) /_/  __/ / / / /_/ /_____|   / / (_| | |_) |
/_/  /_/\__, /____/\__/\___/_/ /_/\____/      |_/_/_\__,_|____/  
       /____/                                                    
                                                            {RESET}"""
    print(banner_text)
    print(f"{CYAN}=" * 68 + f"{RESET}")
    print(f"{NEON_PURPLE}{BOLD} 🔮  MYSTERIO-VIBEPHANTOM v2.0 : ADVANCED INTELLIGENCE SUITE  🔮{RESET}")
    print(f"{CYAN}=" * 68 + f"{RESET}")
    print(f" 🛠️  {BOLD}Developed By{RESET} : {GREEN}rey-mysterio-27{RESET} (GitHub)")
    print(f" 📸  {BOLD}Instagram{RESET}    : {YELLOW}@rey.mysterio.27/{RESET}")
    print(f" 🌐  {BOLD}Website{RESET}      : {CYAN}mysterio-27.vercel.app{RESET}")
    print(f" 📧  {BOLD}Mail{RESET}         : {RED}rey_mysterio_27@wearehackerone.com{RESET}")
    print(f"{CYAN}=" * 68 + f"{RESET}")
    print(f" 🕒  {BOLD}Time Started{RESET} : {YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"{CYAN}=" * 68 + f"{RESET}")

def menu():
    clear_terminal()  # Banner print hone se theek pehle terminal saaf!
    mysterio_banner()
    target = input(f"\n{BOLD}Enter Target Domain (e.g., example.com): {RESET}").strip()
    target = target.replace("https://", "").replace("http://", "").split('/')[0]
    
    if not target:
        print(f"{RED}[-] Domain cannot be empty!{RESET}")
        return

    while True:
        print(f"\n{NEON_PURPLE}--- SELECT RECON MODULE ---{RESET}")
        print(f"{CYAN}1.{RESET} Network & Performance (IP, Status, GeoIP, Ports, Load Time)")
        print(f"{CYAN}2.{RESET} DNS & Mail Config (A, MX, TXT, SPF Check)")
        print(f"{CYAN}3.{RESET} Security & WAF (SSL, Headers, security.txt)")
        print(f"{CYAN}4.{RESET} Content & SEO Audit (Title, Links, robots.txt)")
        print(f"{CYAN}5.{RESET} Meta & History (WHOIS, Wayback Archive)")
        print(f"{CYAN}6.{RESET} {BOLD}Run Full Phantom-Check (All Modules){RESET}")
        print(f"{RED}7. Exit{RESET}")
        
        choice = input(f"\n{BOLD}Enter your choice (1-7): {RESET}").strip()
        
        print("\n" + f"{CYAN}*" * 68 + f"{RESET}")
        if choice == '1':
            network_scanner.run(target)
        elif choice == '2':
            dns_scanner.run(target)
        elif choice == '3':
            security_scanner.run(target)
        elif choice == '4':
            content_scanner.run(target)
        elif choice == '5':
            meta_scanner.run(target)
        elif choice == '6':
            print(f"{YELLOW}[*] Deploying Vibephantom Stealth Engines...{RESET}\n")
            network_scanner.run(target)
            dns_scanner.run(target)
            security_scanner.run(target)
            content_scanner.run(target)
            meta_scanner.run(target)
        elif choice == '7':
            print(f"{GREEN}[+] Terminating Mysterio-Vibephantom session. Stay Safe!{RESET}")
            sys.exit()
        else:
            print(f"{RED}[-] Invalid Option! Please choose between 1-7.{RESET}")
        print(f"{CYAN}*" * 68 + f"{RESET}")

if __name__ == "__main__":
    menu()
