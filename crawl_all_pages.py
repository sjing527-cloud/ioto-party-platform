import urllib.request
import re
import json
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

base_url = "https://swmy.hnae.edu.cn/dj/djdt"
all_news = {}

for page in range(1, 11):
    if page == 1:
        url = f"{base_url}.htm"
    else:
        url = f"{base_url}/{page}.htm"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=ssl_context, timeout=15)
        html = response.read().decode('utf-8')
        
        pattern = r'<a[^>]*href="(/info/1181/\d+\.htm)"[^>]*>([^<]+)</a>'
        matches = re.findall(pattern, html)
        
        date_pattern = r'<span class="date">(.*?)</span>'
        dates = re.findall(date_pattern, html)
        
        for i, (href, title) in enumerate(matches):
            title = title.strip()
            if len(title) > 10 and '/info/1181/' in href:
                full_url = f"https://swmy.hnae.edu.cn{href}"
                try:
                    req_check = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
                    resp_check = urllib.request.urlopen(req_check, context=ssl_context, timeout=10)
                    if resp_check.getcode() == 200:
                        date = dates[i] if i < len(dates) else ""
                        all_news[title] = {"url": full_url, "date": date}
                        print(f"✓ Page {page}: [{date}] {title[:30]}...")
                except:
                    print(f"✗ Page {page}: {full_url} -> 404")
        
        print(f"--- Page {page} completed ---")
    except Exception as e:
        print(f"Page {page} failed: {e}")

print(f"\nTotal valid links: {len(all_news)}")

with open('news_links_full.json', 'w', encoding='utf-8') as f:
    json.dump({"news_links": list(all_news.values())}, f, ensure_ascii=False, indent=2)

print("\nSaved to news_links_full.json")
