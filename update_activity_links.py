import re

activity_links = {
    "专题党课：树立和践行正确政绩观": "https://swmy.hnae.edu.cn/info/1181/8515.htm",
    "预备党员转正大会": "https://swmy.hnae.edu.cn/info/1181/8275.htm",
    "专题党课：深学细悟两会精神 勇担教育育人使命": "https://swmy.hnae.edu.cn/info/1181/8065.htm",
    "2025年度组织生活会暨民主评议党员大会": "https://swmy.hnae.edu.cn/info/1181/7945.htm",
    "专题宣讲：党的二十届四中全会精神": "https://swmy.hnae.edu.cn/info/1181/8015.htm",
    "接收预备党员大会": "https://swmy.hnae.edu.cn/info/1181/7725.htm",
    "11月主题党日活动：传承红色廉脉，筑牢廉洁初心": "https://swmy.hnae.edu.cn/info/1181/7635.htm",
    "第53期入党积极分子培训开班典礼": "https://swmy.hnae.edu.cn/info/1181/7605.htm",
    "学习《习近平谈治国理政》第五卷座谈会": "https://swmy.hnae.edu.cn/info/1181/7485.htm",
    "观看纪念中国人民抗日战争暨世界反法西斯战争胜利80周年大会": "https://swmy.hnae.edu.cn/info/1181/7385.htm",
    "2024年度组织生活会": "https://swmy.hnae.edu.cn/info/1181/7035.htm",
    "2024年度组织生活会暨民主评议党员大会": "https://swmy.hnae.edu.cn/info/1181/7025.htm",
    "3月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6995.htm",
    "学习两会精神与师德师风建设专题会议": "https://swmy.hnae.edu.cn/info/1181/6985.htm",
    "赴茶陵县工农兵政府旧址、湾里红湘赣革命根据地主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6485.htm",
    "\"党谊织梦·智趣童行\"志愿服务主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6455.htm",
    "\"城市守望者\"公交站志愿服务活动": "https://swmy.hnae.edu.cn/info/1181/6385.htm",
    "\"乐得\"关爱为国作出特殊贡献老人慰问活动": "https://swmy.hnae.edu.cn/info/1181/6355.htm",
    "赴醴陵廉洁教育主题活动": "https://swmy.hnae.edu.cn/info/1181/6185.htm",
    "赴株洲烈士纪念园主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6055.htm",
    "党总支部委员会换届选举大会": "https://swmy.hnae.edu.cn/info/1181/5985.htm",
    "\"一月一课一片一实践\"活动": "https://swmy.hnae.edu.cn/info/1181/5965.htm",
    "师德师风专题法纪教育活动": "https://swmy.hnae.edu.cn/info/1181/6035.htm",
}

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<li><div class="icon"><i class="fas fa-(\w+)-(\w+)"></i></div><div class="content"><h4>(.*?)</h4><p>(.*?)</p><div class="meta">'

def replace_match(match):
    icon1 = match.group(1)
    icon2 = match.group(2)
    title = match.group(3)
    desc = match.group(4)
    url = activity_links.get(title, "#")
    return f'<li><div class="icon"><i class="fas fa-{icon1}-{icon2}"></i></div><div class="content"><a href="{url}" target="_blank"><h4>{title}</h4></a><p>{desc}</p><div class="source"><i class="fas fa-external-link-alt"></i> 点击跳转至官网查看详情</div><div class="meta">'

content = re.sub(pattern, replace_match, content)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("activity.html updated successfully!")