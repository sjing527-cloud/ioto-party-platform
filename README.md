# IOTO智慧党建平台 - 部署指南

## 📁 项目结构

```
IOTO智慧党建平台网站/
├── index.html              # 首页
├── conclusion.html         # 结项材料窗口（主展示页面）
├── common.css              # 统一公共样式文件
├── data/                   # JSON数据目录（可自由更新）
│   ├── members.json        # 团队成员信息
│   ├── papers.json         # 论文成果清单
│   ├── projects.json       # 课题研究成果
│   ├── competitions.json   # 竞赛获奖记录
│   └── ip.json             # 知识产权成果
├── dashboard.html          # 数据驾驶舱
├── honor.html              # 荣誉展示
├── news.html               # 宣传资讯
├── learning.html           # 学习教育
├── activity.html           # 组织活动
├── service.html            # 服务师生
├── analysis.html           # 数据分析
├── management.html         # 综合管理
├── modules.html            # 平台架构
├── vote.html               # 投票问卷
├── service_detail.html     # 服务详情页
└── README.md               # 本文件
```

## 🚀 部署方式

### 方式一：GitHub Pages（推荐）

**优点**：完全免费、速度快、支持自定义域名

**步骤**：

1. **创建GitHub仓库**
   - 登录 https://github.com
   - 创建新仓库，命名为：`ioto-party-platform`（或其他名称）

2. **上传文件**
   - 将整个 `IOTO智慧党建平台网站` 目录下的文件上传到GitHub仓库

3. **开启GitHub Pages**
   - 进入仓库 → Settings → Pages
   - Source选择：`Deploy from a branch`
   - Branch选择：`main`，目录选择：`/(root)`
   - 点击Save，等待几分钟后会生成访问地址

4. **访问网站**
   - 地址格式：`https://你的用户名.github.io/ioto-party-platform/`

### 方式二：Vercel

**优点**：自动部署、速度更快、界面更现代

**步骤**：

1. **登录Vercel**
   - 访问 https://vercel.com ，用GitHub账号登录

2. **导入项目**
   - 点击 `New Project` → 选择你的GitHub仓库

3. **配置部署**
   - Framework Preset：选择 `Other`
   - Build Command：留空（纯静态文件无需构建）
   - Output Directory：留空
   - 点击 `Deploy`

4. **访问网站**
   - Vercel会自动生成访问地址

### 方式三：Cloudflare Pages

**优点**：全球CDN加速、免费SSL证书

**步骤**：

1. **登录Cloudflare**
   - 访问 https://dash.cloudflare.com

2. **创建Pages项目**
   - 点击 `Pages` → `Create a project`
   - 连接GitHub仓库

3. **配置构建**
   - Build command：留空
   - Build output directory：留空
   - 点击 `Deploy`

## ✏️ 如何更新数据

### 更新团队成员信息
编辑 `data/members.json` 文件：

```json
{
  "team": [
    {
      "name": "成员姓名",
      "title": "职务（如：组织委员）",
      "position": "职称（如：讲师）",
      "achievements": ["成果1", "成果2"],
      "role": "党员"
    }
  ]
}
```

### 更新论文/课题/竞赛/知识产权
分别编辑 `data/papers.json`、`data/projects.json`、`data/competitions.json`、`data/ip.json`

### 更新后部署
更新JSON文件后，只需将文件重新上传到GitHub仓库，GitHub Pages会自动重新部署。

## 📱 移动端适配

平台已支持响应式布局，在手机、平板上均可正常浏览。

## ⚠️ 注意事项

1. **JSON格式要求**：编辑JSON文件时，请确保语法正确（逗号、引号等），否则数据无法加载
2. **图片路径**：如果需要添加图片，请将图片放入项目目录，并使用相对路径引用
3. **本地预览**：本地打开HTML文件时，由于浏览器安全限制，`fetch()` 可能无法加载本地JSON文件。建议使用本地服务器：
   ```bash
   # 方法1：使用Python（推荐）
   python3 -m http.server 8000
   
   # 方法2：使用Node.js
   npx serve
   ```
   然后访问 http://localhost:8000

4. **部署后路径**：部署后访问结项材料页面的地址是 `/conclusion.html`

## 📧 技术支持

如有问题，请联系：宋丹工作室

---

**宋丹"双带头人"工作室** · 2024-2026学年