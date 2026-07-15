#!/bin/bash
set -e

SITE_DIR="/Users/songdan/Library/Mobile Documents/com~apple~CloudDocs/宋丹个人/2024年党支部书记双带头人申报/IOTO智慧党建平台网站"
REPO_URL="git@github.com:sjing527-cloud/ioto-party-platform.git"
DEPLOY_URL="https://sjing527-cloud.github.io/ioto-party-platform/"

cd "$SITE_DIR"

echo "📁 当前目录: $(pwd)"

if [ -n "$1" ]; then
    echo "📤 准备上传文件: $1"
    git add "$1"
    MESSAGE="更新 $1"
else
    echo "📤 准备上传所有文件"
    git add -A
    MESSAGE="更新网站文件"
fi

echo "✅ 添加文件到暂存区"
git commit -m "$MESSAGE"

echo "🔄 推送到远程仓库..."
git push origin main

echo ""
echo "🎉 部署成功!"
echo "🌐 访问地址: $DEPLOY_URL"
echo ""
echo "⏳ 等待1-5分钟后刷新页面即可看到更新"