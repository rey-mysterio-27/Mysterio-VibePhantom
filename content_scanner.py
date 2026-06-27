import requests
from bs4 import BeautifulSoup

def run(domain):
    print("\033[38;5;141m🔮 [MYSTERIO-VIBEPHANTOM] ─── 🔍 AGENT ACTIVE\033[0m")
    print("\033[38;5;141m🔮 [VIBE-CHECK] ─── 📝 CONTENT & SEO AUDIT\033[0m")
    try:
        res = requests.get(f"https://{domain}", timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        title = soup.title.string if soup.title else "No Title"
        print(f"  [+] Page Title      : {title.strip()}")
        print(f"  [+] Meta Description: {'✔ Present' if soup.find('meta', attrs={'name': 'description'}) else '❌ Missing'}")
        print(f"  [+] Total Links     : {len(soup.find_all('a'))} links found.")
    except Exception:
        print("  [-] HTML Parsing    : Failed.")

    try:
        rb = requests.get(f"https://{domain}/robots.txt", timeout=3)
        print(f"  [+] robots.txt      : {'✔ Active' if rb.status_code == 200 else '❌ Not Found'}")
    except Exception:
        pass