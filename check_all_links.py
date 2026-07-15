import re
import urllib.request
import urllib.error
import os
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

skip_domains = [
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'cdnjs.cloudflare.com',
    'cdn.jsdelivr.net'
]

skip_protocols = ['tel:', 'mailto:', 'data:', 'javascript:', '#']

html_files = [
    'index.html', 'modules.html', 'learning.html', 'activity.html',
    'service.html', 'service_detail.html', 'news.html', 'analysis.html', 
    'management.html', 'vote.html', 'honor.html', 'dashboard.html', 
    'methods.html', 'conclusion.html'
]

broken_links = []
total_links = 0
valid_links = 0
skipped_links = 0

for html_file in html_files:
    if not os.path.exists(html_file):
        print(f"❌ 文件不存在: {html_file}")
        continue
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    script_pattern = r'<script[\s\S]*?</script>'
    clean_content = re.sub(script_pattern, '', html_content)
    
    pattern = r'href="([^"]+)"'
    links = re.findall(pattern, clean_content)
    
    for href in links:
        total_links += 1
        
        if href.startswith('#') or href == '':
            valid_links += 1
            continue
        
        skip = False
        for protocol in skip_protocols:
            if href.startswith(protocol):
                skipped_links += 1
                skip = True
                break
        if skip:
            continue
        
        for domain in skip_domains:
            if domain in href:
                skipped_links += 1
                skip = True
                break
        if skip:
            continue
        
        if href.startswith('http://') or href.startswith('https://'):
            url = href
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, context=ssl_context, timeout=15)
                status = response.getcode()
                if status == 200:
                    valid_links += 1
                else:
                    broken_links.append((html_file, url, f"HTTP {status}"))
            except urllib.error.HTTPError as e:
                broken_links.append((html_file, url, f"HTTP {e.code}"))
            except Exception as e:
                broken_links.append((html_file, url, str(e)))
        else:
            href_clean = href.split('#')[0]
            if os.path.exists(href_clean):
                valid_links += 1
            else:
                full_path = os.path.join(os.path.dirname(html_file) or '.', href_clean)
                if os.path.exists(full_path):
                    valid_links += 1
                else:
                    broken_links.append((html_file, href, "文件不存在"))

print(f"\n=== 链接检查结果 ===")
print(f"总链接数: {total_links}")
print(f"有效链接: {valid_links}")
print(f"失效链接: {len(broken_links)}")
print(f"跳过的CDN资源和特殊协议: {skipped_links}")

if broken_links:
    print(f"\n❌ 失效链接列表:")
    for file, url, reason in broken_links:
        print(f"  • [{file}] {url} -> {reason}")
else:
    print(f"\n✅ 所有链接均有效！")
