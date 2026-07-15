import re

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>预备党员转正大会</h4><p>支部书记宋丹主持，讨论张晓航同志预备党员转正事宜', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/8275.htm" target="_blank"><h4>预备党员转正大会</h4></a><p>支部书记宋丹主持，讨论张晓航同志预备党员转正事宜', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>2025年度组织生活会暨民主评议党员大会</h4><p>支部书记宋丹作党建工作述职报告', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7945.htm" target="_blank"><h4>2025年度组织生活会暨民主评议党员大会</h4></a><p>支部书记宋丹作党建工作述职报告', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>接收预备党员大会</h4><p>支部书记宋丹主持，讨论接收刘佳杰同志', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7725.htm" target="_blank"><h4>接收预备党员大会</h4></a><p>支部书记宋丹主持，讨论接收刘佳杰同志', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><h4>11月主题党日活动：传承红色廉脉，筑牢廉洁初心</h4><p>组织全体党员前往株洲博物馆', 
                r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7635.htm" target="_blank"><h4>11月主题党日活动：传承红色廉脉，筑牢廉洁初心</h4></a><p>组织全体党员前往株洲博物馆', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-graduation-cap"></i></div><div class="content"><h4>第53期入党积极分子培训开班典礼</h4><p>党总支书记曾昭山', 
                r'<li><div class="icon"><i class="fas fa-graduation-cap"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7605.htm" target="_blank"><h4>第53期入党积极分子培训开班典礼</h4></a><p>党总支书记曾昭山', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-book"></i></div><div class="content"><h4>学习《习近平谈治国理政》第五卷座谈会</h4><p>领导班子成员', 
                r'<li><div class="icon"><i class="fas fa-book"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7485.htm" target="_blank"><h4>学习《习近平谈治国理政》第五卷座谈会</h4></a><p>领导班子成员', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-film"></i></div><div class="content"><h4>观看纪念中国人民抗日战争', 
                r'<li><div class="icon"><i class="fas fa-film"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7385.htm" target="_blank"><h4>观看纪念中国人民抗日战争', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>预备党员转正大会</h4><p>讨论预备党员转正事宜，严格按照组织程序', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7255.htm" target="_blank"><h4>预备党员转正大会</h4></a><p>讨论预备党员转正事宜，严格按照组织程序', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>接收预备党员大会</h4><p>接收新党员，注入新鲜血液', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7265.htm" target="_blank"><h4>接收预备党员大会</h4></a><p>接收新党员，注入新鲜血液', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>2024年度组织生活会</h4><p>学生党员开展批评与自我批评', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7035.htm" target="_blank"><h4>2024年度组织生活会</h4></a><p>学生党员开展批评与自我批评', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>2024年度组织生活会暨民主评议党员大会</h4><p>党总支召开年度组织生活会', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/7025.htm" target="_blank"><h4>2024年度组织生活会暨民主评议党员大会</h4></a><p>党总支召开年度组织生活会', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><h4>3月份主题党日活动</h4><p>开展主题党日活动', 
                r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6995.htm" target="_blank"><h4>3月份主题党日活动</h4></a><p>开展主题党日活动', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><h4>学习两会精神与师德师风建设专题会议</h4><p>传达学习两会精神', 
                r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6985.htm" target="_blank"><h4>学习两会精神与师德师风建设专题会议</h4></a><p>传达学习两会精神', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><h4>赴茶陵县工农兵政府旧址', 
                r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6485.htm" target="_blank"><h4>赴茶陵县工农兵政府旧址', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><h4>"党谊织梦·智趣童行"志愿服务主题党日活动</h4><p>学生党支部', 
                r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6455.htm" target="_blank"><h4>"党谊织梦·智趣童行"志愿服务主题党日活动</h4></a><p>学生党支部', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><h4>"城市守望者"公交站志愿服务活动</h4><p>学生党员', 
                r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6385.htm" target="_blank"><h4>"城市守望者"公交站志愿服务活动</h4></a><p>学生党员', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><h4>"乐得"关爱为国作出特殊贡献老人慰问活动</h4><p>关爱特殊贡献老人', 
                r'<li><div class="icon"><i class="fas fa-heart"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6355.htm" target="_blank"><h4>"乐得"关爱为国作出特殊贡献老人慰问活动</h4></a><p>关爱特殊贡献老人', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><h4>赴醴陵廉洁教育主题活动</h4><p>赴醴陵开展廉洁教育', 
                r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6185.htm" target="_blank"><h4>赴醴陵廉洁教育主题活动</h4></a><p>赴醴陵开展廉洁教育', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><h4>赴株洲烈士纪念园主题党日活动</h4><p>赴株洲烈士纪念园', 
                r'<li><div class="icon"><i class="fas fa-map-marker-alt"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6055.htm" target="_blank"><h4>赴株洲烈士纪念园主题党日活动</h4></a><p>赴株洲烈士纪念园', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><h4>党总支部委员会换届选举大会</h4><p>召开换届选举大会', 
                r'<li><div class="icon"><i class="fas fa-users"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/5985.htm" target="_blank"><h4>党总支部委员会换届选举大会</h4></a><p>召开换届选举大会', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><h4>"一月一课一片一实践"活动</h4><p>深入开展', 
                r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/5965.htm" target="_blank"><h4>"一月一课一片一实践"活动</h4></a><p>深入开展', content)

content = re.sub(r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><h4>师德师风专题法纪教育活动</h4><p>开展师德师风', 
                r'<li><div class="icon"><i class="fas fa-book-open"></i></div><div class="content"><a href="https://swmy.hnae.edu.cn/info/1181/6035.htm" target="_blank"><h4>师德师风专题法纪教育活动</h4></a><p>开展师德师风', content)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/activity.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("activity.html all links updated successfully!")