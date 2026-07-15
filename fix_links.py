import json
import re

with open('news_links.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    news_links = data['news_links']

with open('learning.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

updated_count = 0

for title, correct_url in news_links.items():
    pattern = r'<a href="[^"]+" target="_blank" class="news-link"><div class="content"><h4>' + re.escape(title) + r'</h4>'
    replacement = '<a href="' + correct_url + '" target="_blank" class="news-link"><div class="content"><h4>' + title + '</h4>'
    new_content, count = re.subn(pattern, replacement, html_content)
    if count > 0:
        html_content = new_content
        updated_count += count
        print(f"Updated: {title[:50]}... -> {correct_url}")

with open('learning.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\nTotal links updated: {updated_count}")
