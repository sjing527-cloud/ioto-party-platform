import re

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/learning.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<li><span class="date">(\d{4}-\d{2}-\d{2})</span><div class="content"><a href="(.*?)" target="_blank"><h4>(.*?)</h4></a><p>(.*?)</p><div class="source"><i class="fas fa-external-link-alt"></i> 查看详情</div></div></li>'

def replace_match(match):
    date = match.group(1)
    url = match.group(2)
    title = match.group(3)
    desc = match.group(4)
    return f'<li><span class="date">{date}</span><a href="{url}" target="_blank" class="news-link"><div class="content"><h4>{title}</h4><p>{desc}</p><div class="source"><i class="fas fa-external-link-alt"></i> 查看详情</div></div></a></li>'

content = re.sub(pattern, replace_match, content)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/learning.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("learning.html updated with clickable news items!")