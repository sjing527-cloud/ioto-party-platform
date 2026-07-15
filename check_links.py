import re
import urllib.request

with open('learning.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

pattern = r'href="(https://swmy.hnae.edu.cn/info/1181/\d+\.htm)"'
links = re.findall(pattern, html_content)

print(f"Total links found: {len(links)}")
print("=" * 60)

broken_links = []

for url in links:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        status = response.getcode()
        if status != 200:
            print(f"❌ [{status}] {url}")
            broken_links.append(url)
        else:
            print(f"✅ [{status}] {url}")
    except Exception as e:
        print(f"❌ [ERROR] {url} - {e}")
        broken_links.append(url)

print("=" * 60)
print(f"Broken links: {len(broken_links)}")
if broken_links:
    print("\nList of broken links:")
    for link in broken_links:
        print(f"  - {link}")
