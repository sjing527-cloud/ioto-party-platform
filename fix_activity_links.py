import re

broken_to_fixed = {
    "7255.htm": "https://swmy.hnae.edu.cn/info/1181/2855.htm",
    "7265.htm": "https://swmy.hnae.edu.cn/info/1181/2815.htm",
    "7035.htm": "https://swmy.hnae.edu.cn/info/1181/2915.htm",
    "7025.htm": "https://swmy.hnae.edu.cn/info/1181/2455.htm",
    "6995.htm": "https://swmy.hnae.edu.cn/info/1181/2795.htm",
    "6985.htm": "https://swmy.hnae.edu.cn/info/1181/2785.htm",
    "6485.htm": "https://swmy.hnae.edu.cn/info/1181/3055.htm",
    "6455.htm": "https://swmy.hnae.edu.cn/info/1181/3025.htm",
    "6385.htm": "https://swmy.hnae.edu.cn/info/1181/3015.htm",
    "6355.htm": "https://swmy.hnae.edu.cn/info/1181/2995.htm",
    "6185.htm": "https://swmy.hnae.edu.cn/info/1181/2975.htm",
    "6055.htm": "https://swmy.hnae.edu.cn/info/1181/2955.htm",
    "5985.htm": "https://swmy.hnae.edu.cn/info/1181/2935.htm",
    "5965.htm": "https://swmy.hnae.edu.cn/info/1181/2925.htm",
    "6035.htm": "https://swmy.hnae.edu.cn/info/1181/3035.htm"
}

with open('activity.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

updated_count = 0
for broken, fixed in broken_to_fixed.items():
    pattern = r'https://swmy\.hnae\.edu\.cn/info/1181/' + re.escape(broken) + r'"'
    new_content, count = re.subn(pattern, fixed + '"', html_content)
    if count > 0:
        html_content = new_content
        updated_count += count
        print(f"✓ {broken} -> {fixed.split('/')[-1]}")

with open('activity.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\nTotal links updated: {updated_count}")
