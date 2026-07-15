import re

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<li><div class="icon"><i class="fas fa-(\w+)-(\w+)"></i></div><div class="content"><a href="(.*?)" target="_blank"><h4>(.*?)</h4></a><p>(.*?)</p><div class="source"><i class="fas fa-external-link-alt"></i> 查看详情</div><div class="meta">(.*?)</div></div><span class="status done">已完成</span></li>'

def replace_match(match):
    icon1 = match.group(1)
    icon2 = match.group(2)
    url = match.group(3)
    title = match.group(4)
    desc = match.group(5)
    meta = match.group(6)
    return f'<li><div class="icon"><i class="fas fa-{icon1}-{icon2}"></i></div><a href="{url}" target="_blank" class="activity-link"><div class="content"><h4>{title}</h4><p>{desc}</p><div class="source"><i class="fas fa-external-link-alt"></i> 查看详情</div><div class="meta">{meta}</div></div></a><span class="status done">已完成</span></li>'

content = re.sub(pattern, replace_match, content)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("activity.html updated with clickable activity items!")