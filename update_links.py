import re

news_links = {
    "深学细悟正确政绩观 坚守育人实干初心——商务贸易学院全体党员参加专题党课学习": "https://swmy.hnae.edu.cn/info/1181/8515.htm",
    "商务贸易学院教工党支部召开预备党员转正大会": "https://swmy.hnae.edu.cn/info/1181/8275.htm",
    "深学细悟两会精神 勇担教育育人使命——党委委员、副校长周金宗为三院党员讲授专题党课": "https://swmy.hnae.edu.cn/info/1181/8065.htm",
    "商务贸易学院教工党支部召开2025年度组织生活会暨民主评议党员大会": "https://swmy.hnae.edu.cn/info/1181/7945.htm",
    "深入学习贯彻党的二十届四中全会精神——校党委委员、副校长周金宗为商务贸易学院全体教师作专题宣讲": "https://swmy.hnae.edu.cn/info/1181/8015.htm",
    "商务贸易学院教工党支部召开接收预备党员大会": "https://swmy.hnae.edu.cn/info/1181/7725.htm",
    "商务贸易学院党总支开展11月主题党日活动": "https://swmy.hnae.edu.cn/info/1181/7635.htm",
    "商务贸易学院党总支部举行2025下期分党校入党积极分子培训开班典礼": "https://swmy.hnae.edu.cn/info/1181/7605.htm",
    "学深悟透 笃信笃行——商贸学院开展学习《习近平谈治国理政》第五卷座谈会": "https://swmy.hnae.edu.cn/info/1181/7485.htm",
    "商务贸易学院组织师生收看纪念中国人民抗日战争暨世界反法西斯战争胜利80周年大会": "https://swmy.hnae.edu.cn/info/1181/7385.htm",
    "商务贸易学院教工党支部召开预备党员转正党员大会": "https://swmy.hnae.edu.cn/info/1181/7255.htm",
    "商务贸易学院教工党支部召开接收预备党员大会": "https://swmy.hnae.edu.cn/info/1181/7265.htm",
    "商务贸易学院学生党支部召开2024年度组织生活会": "https://swmy.hnae.edu.cn/info/1181/7035.htm",
    "商务贸易学院召开2024年度组织生活会暨民主评议党员大会": "https://swmy.hnae.edu.cn/info/1181/7025.htm",
    "商务贸易学院组织召开3月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6995.htm",
    "商务贸易学院召开全体教师会议深入学习两会精神与师德师风建设": "https://swmy.hnae.edu.cn/info/1181/6985.htm",
    "商贸学院学工线组织开展学习党的二十届三中全会精神主题班会活动": "https://swmy.hnae.edu.cn/info/1181/6945.htm",
    "商务贸易学院教工党支部召开预备党员转正党员大会": "https://swmy.hnae.edu.cn/info/1181/6585.htm",
    "商务贸易学院召开第51期入党积极分子思想导师见面会": "https://swmy.hnae.edu.cn/info/1181/6525.htm",
    "商务贸易学院党总支赴茶陵县工农兵政府旧址、湾里红湘赣革命根据地红色文化园开展主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6485.htm",
    "商贸学院学生党支部组织开展\"党谊织梦·智趣童行\"主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6455.htm",
    "商务贸易学院第五十一期入党积极分子党校实践活动召开": "https://swmy.hnae.edu.cn/info/1181/6445.htm",
    "商务贸易学院学生党支部第四期\"书香汇 师生共读\"读书分享会举行": "https://swmy.hnae.edu.cn/info/1181/6435.htm",
    "商务贸易学院学生党支部第三期\"书香汇·师生共读\"分享会举行": "https://swmy.hnae.edu.cn/info/1181/6415.htm",
    "商贸学子积极参加株洲\"城市守望者\"公交站志愿活动": "https://swmy.hnae.edu.cn/info/1181/6385.htm",
    "商务贸易学院积极参加株洲晚报志愿者联合会发起的\"'乐得'关爱为国作出特殊贡献老人\"慰问活动": "https://swmy.hnae.edu.cn/info/1181/6355.htm",
    "激发青春活力 引领时代新风——商贸务贸易学院第51期入党积极分子推优大会召开": "https://swmy.hnae.edu.cn/info/1181/6345.htm",
    "下真功 求真知 见真效—商务贸易学院学生党支部召开全体党员大会": "https://swmy.hnae.edu.cn/info/1181/6325.htm",
    "商务贸易学院2024级新生入党启蒙教育专题讲座顺利召开": "https://swmy.hnae.edu.cn/info/1181/6315.htm",
    "商务贸易学院党总支组织学院全体党员教师深入学习党的二十届三中全会精神": "https://swmy.hnae.edu.cn/info/1181/6305.htm",
    "商务贸易学院教工党支部补选大会顺利召开": "https://swmy.hnae.edu.cn/info/1181/6295.htm",
    "商务贸易学院组织学院教师党员赴醴陵开展廉洁教育主题活动": "https://swmy.hnae.edu.cn/info/1181/6185.htm",
    "商务贸易学院党员大会顺利召开": "https://swmy.hnae.edu.cn/info/1181/6125.htm",
    "2024年上半年商贸学院教工党支部接收预备党员大会召开": "https://swmy.hnae.edu.cn/info/1181/6085.htm",
    "商贸务贸易学院部分师生前往株洲烈士纪念园开展5月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/6055.htm",
    "商务贸易学院组织开展师德师风专题法纪教育活动": "https://swmy.hnae.edu.cn/info/1181/6035.htm",
    "商务贸易学院召开党总支部委员会换届选举大会": "https://swmy.hnae.edu.cn/info/1181/5985.htm",
    "商贸学院党总支部深入开展\"一月一课一片一实践\"活动": "https://swmy.hnae.edu.cn/info/1181/5965.htm",
    "商务贸易学院党总支部召开党员大会": "https://swmy.hnae.edu.cn/info/1181/5915.htm",
    "商贸学院开展3月份微党课学习活动": "https://swmy.hnae.edu.cn/info/1181/5905.htm",
    "商贸学院党总支部组织开展走进图书馆阅读图书教育实践活动": "https://swmy.hnae.edu.cn/info/1181/5895.htm",
    "《大美中国·春天系列》春天的湖南：让商贸党员师生感悟美丽湖南建设成就": "https://swmy.hnae.edu.cn/info/1181/5845.htm",
    "商贸学院开展2月份微党课学习活动": "https://swmy.hnae.edu.cn/info/1181/5835.htm",
    "商贸学院开展1月份微党课学习活动": "https://swmy.hnae.edu.cn/info/1181/5805.htm",
    "正风不止步 肃纪不停歇——商贸学院党总支组织观看《正风肃纪》警示教育片": "https://swmy.hnae.edu.cn/info/1181/5775.htm",
    "商务贸易学院党支部开展\"寻初心豪情 学使命担当\"主题党日活动": "https://swmy.hnae.edu.cn/info/1181/5725.htm",
    "2023年下半年商贸学院教工党支部接收预备党员大会召开": "https://swmy.hnae.edu.cn/info/1181/5695.htm",
    "商务贸易学院教工党支部举行2023年预备党员转正大会": "https://swmy.hnae.edu.cn/info/1181/5685.htm",
    "商贸学院党支部开展《志愿军：雄兵出击》党性锤炼观影活动": "https://swmy.hnae.edu.cn/info/1181/5655.htm",
    "商贸学院党总支十一月党课开课": "https://swmy.hnae.edu.cn/info/1181/5635.htm",
    "商贸学院组织党员师生收看第三届\"一带一路\"国际合作高峰论坛直播": "https://swmy.hnae.edu.cn/info/1181/5595.htm",
    "商贸学院党总支召开学习贯彻习近平新时代中国特色社会主义思想主题教育专题组织生活会": "https://swmy.hnae.edu.cn/info/1181/5565.htm",
    "商务贸易学院八月份主题党日活动举行": "https://swmy.hnae.edu.cn/info/1181/5505.htm",
    "商贸学院开展\"党建引领推动垃圾分类成为低碳生活新时尚\"主题党日活动": "https://swmy.hnae.edu.cn/info/1181/5475.htm",
    "商贸学院组织全体党员在线观看系列专题影片《七七事变》": "https://swmy.hnae.edu.cn/info/1181/5455.htm",
    "商务贸易学院六月份主题党日活动举行": "https://swmy.hnae.edu.cn/info/1181/5405.htm",
    "党委委员、副院长周金宗为商贸党员师生讲授主题教育专题党课": "https://swmy.hnae.edu.cn/info/1181/5375.htm",
    "商务贸易学院五月份主题党日活动举行": "https://swmy.hnae.edu.cn/info/1181/5345.htm",
    "商务贸易学院党总支部开展四月份专题党课学习——学习株洲市优秀共产党员严亮同志的优秀事迹": "https://swmy.hnae.edu.cn/info/1181/5305.htm",
    "商务贸易学院四月份主题党日活动举行": "https://swmy.hnae.edu.cn/info/1181/5295.htm",
    "党建引领铸师魂，课堂示范展风采——商务贸易学院三月份主题党日活动举行": "https://swmy.hnae.edu.cn/info/1181/5255.htm",
    "商务贸易学院教工党支部开展2022年度组织生活会和民主评议党员活动": "https://swmy.hnae.edu.cn/info/1181/5245.htm",
    "奋进新征程 建功新时代——商务贸易学院党总支部开展二月份专题党课学习主题党日活动": "https://swmy.hnae.edu.cn/info/1181/5215.htm",
    "商贸学院召开学院第四届教职工代表大会暨工会会员大会代表选举会议": "https://swmy.hnae.edu.cn/info/1181/5195.htm",
    "奋斗正当时，再上新征程——商务贸易学院党总支二0二三年一月份主题党日活动顺利召开": "https://swmy.hnae.edu.cn/info/1181/5165.htm",
    "2022年下半年商贸学院教工党支部预备党员转正大会召开": "https://swmy.hnae.edu.cn/info/1181/4565.htm",
    "商务贸易学院党总支十二月份主题党日活动顺利召开": "https://swmy.hnae.edu.cn/info/1181/4545.htm",
    "2022年下半年商贸学院教工党支部接收预备党员大会召开": "https://swmy.hnae.edu.cn/info/1181/4525.htm",
    "\"疫\"线主题党日，让党旗在疫情防控一线高高飘扬——商务贸易学院党总支十一月主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/4485.htm",
    "学习二十大 凝聚青年心——商务贸易学院组织学习二十大原文活动": "https://swmy.hnae.edu.cn/info/1181/4475.htm",
    "踔厉奋发担使命，勇毅前行向未来——商务贸易学院党总支十月份主题党日活动顺利召开": "https://swmy.hnae.edu.cn/info/1181/2755.htm",
    "无愧今天的使命担当，不负明天的伟大梦想": "https://swmy.hnae.edu.cn/info/1181/3085.htm",
    "商务贸易学院2022级新生入党启蒙教育顺利开展": "https://swmy.hnae.edu.cn/info/1181/3075.htm",
    "商务贸易学院党总支部召开总支委员补选大会": "https://swmy.hnae.edu.cn/info/1181/3445.htm",
    "传承红色基因 凝聚奋进力量——商务贸易学院党总支九月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3055.htm",
    "商务贸易学院党总支（筹）组织全院师生收看《为时代育新人》第二集 《远方——在复兴的赛道上》": "https://swmy.hnae.edu.cn/info/1181/3435.htm",
    "商务贸易学院（筹）党总支召开出席学校第二次党代会代表选举大会": "https://swmy.hnae.edu.cn/info/1181/3365.htm",
    "商务贸易学院（筹）党总支七月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3415.htm",
    "商务贸易学院党总支六月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3355.htm",
    "突破自我，再创奇迹": "https://swmy.hnae.edu.cn/info/1181/3315.htm",
    "商务贸易学院党总支开展关于深化整治领导干部违规收送红包礼金专题组织生活会": "https://swmy.hnae.edu.cn/info/1181/3305.htm",
    "商务贸易学院党总支五月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3285.htm",
    "2022年上半年商贸学院教工党支部预备党员转正大会召开": "https://swmy.hnae.edu.cn/info/1181/3275.htm",
    "商务贸易学院党总支四月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3265.htm",
    "商务贸易学院党总支三月份主题党日活动召开": "https://swmy.hnae.edu.cn/info/1181/3245.htm",
    "商务贸易学院教工支部2021年度组织生活会暨民主评议党员大会顺利召开": "https://swmy.hnae.edu.cn/info/1181/3235.htm",
    "商务贸易学院（筹）党总支召开1月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/3215.htm",
    "商贸学院教工党支部召开新党员发展大会": "https://swmy.hnae.edu.cn/info/1181/3195.htm",
    "商务贸易学院（筹）党总支召开十二月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/3185.htm",
    "总结过去，展望未来": "https://swmy.hnae.edu.cn/info/1181/3175.htm",
    "商务贸易学院党总支组织11月份主题党日活动": "https://swmy.hnae.edu.cn/info/1181/3155.htm",
    "商务贸易学院（筹）党总支十月份主题党日活动顺利开展": "https://swmy.hnae.edu.cn/info/1181/3135.htm",
    "商务贸易学院开展 2021 级新生入党启蒙教育": "https://swmy.hnae.edu.cn/info/1181/3115.htm",
    "商务贸易学院（筹）党总支部召开党员大会暨总支委员选举大会": "https://swmy.hnae.edu.cn/info/1181/3095.htm",
}

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/learning.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<li><span class="date">(\d{4}-\d{2}-\d{2})</span><div class="content"><h4>(.*?)</h4><p>(.*?)</p></div></li>'

def replace_match(match):
    date = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    url = news_links.get(title, "#")
    return f'<li><span class="date">{date}</span><div class="content"><a href="{url}" target="_blank"><h4>{title}</h4></a><p>{desc}</p><div class="source"><i class="fas fa-external-link-alt"></i> 点击跳转至官网查看详情</div></div></li>'

content = re.sub(pattern, replace_match, content)

with open('/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站/learning.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("learning.html updated successfully!")