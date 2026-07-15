import json
import re

with open('news_links.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    news_links = data['news_links']

with open('learning.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

news_items = []
for news in news_links:
    title = news['title']
    url = news['url']
    date = news['date']
    news_items.append(f'      <li><span class="date">{date}</span><a href="{url}" target="_blank" class="news-link"><div class="content"><h4>{title}</h4><p>点击查看详情</p><div class="source"><i class="fas fa-external-link-alt"></i> 查看详情</div></div></a></li>')

news_list_html = '\n'.join(news_items)

pattern = r'<ul class="news-list">[\s\S]*?</ul>'
replacement = f'<ul class="news-list">\n{news_list_html}\n    </ul>'
new_html = re.sub(pattern, replacement, html_content)

with open('learning.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Successfully updated learning.html with {len(news_links)} valid news links")
