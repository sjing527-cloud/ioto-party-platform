import urllib.request
import re
import json

base_url = "https://swmy.hnae.edu.cn/dj/djdt"
all_news = []

for page in range(1, 11):
    if page == 1:
        url = f"{base_url}.htm"
    else:
        url = f"{base_url}/{page}.htm"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8')
        
        pattern = r'<a[^>]*href="(/info/1181/\d+\.htm)"[^>]*>([^<]+)</a>'
        matches = re.findall(pattern, html)
        
        for href, title in matches:
            title = title.strip()
            if len(title) > 10:
                full_url = f"https://swmy.hnae.edu.cn{href}"
                all_news.append({"title": title, "url": full_url})
        print(f"Page {page}: {len(matches)} links found")
    except Exception as e:
        print(f"Page {page} failed: {e}")

all_news.sort(key=lambda x: x['url'], reverse=True)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/news_links.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)

print(f"\nTotal news: {len(all_news)}")
print("Saved to news_links.json")