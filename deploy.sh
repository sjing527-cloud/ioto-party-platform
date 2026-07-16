#!/bin/bash
set -e

# ============================================
# POWER智慧党建平台 - 一键部署脚本
# 用途：将本地文件推送到 GitHub Pages 自动发布
# 用法：
#   ./deploy.sh                  # 部署所有更改
#   ./deploy.sh conclusion.html  # 仅部署指定文件
#   ./deploy.sh "" "修复了某bug"  # 部署所有，自定义提交信息
# ============================================

SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_URL="git@github.com:sjing527-cloud/ioto-party-platform.git"
DEPLOY_URL="https://sjing527-cloud.github.io/ioto-party-platform/"

cd "$SITE_DIR"

echo "=========================================="
echo "  POWER智慧党建平台 · 部署工具"
echo "=========================================="
echo "📁 站点目录: $SITE_DIR"
echo "🌐 目标仓库: $REPO_URL"
echo ""

# 检查是否在Git仓库中
if [ ! -d .git ]; then
    echo "❌ 当前目录不是Git仓库，请先执行 git init 并关联远程仓库"
    exit 1
fi

# 检查是否有未提交的更改
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ 没有需要提交的更改，工作区干净"
    echo "🔥 直接推送确认..."
    git push origin main
    echo ""
    echo "🎉 推送成功!"
    echo "🌐 访问地址: $DEPLOY_URL"
    exit 0
fi

# 显示待提交的文件列表
echo "📋 待提交的文件:"
git status --short
echo ""

# 添加文件
if [ -n "$1" ]; then
    echo "📤 添加指定文件: $1"
    git add "$1"
else
    echo "📤 添加所有更改的文件"
    git add -A
fi

# 提交信息
if [ -n "$2" ]; then
    MESSAGE="$2"
elif [ -n "$1" ]; then
    MESSAGE="更新 $1"
else
    MESSAGE="更新网站文件 ($(date '+%Y-%m-%d %H:%M'))"
fi

echo "💾 提交信息: $MESSAGE"
git commit -m "$MESSAGE"

echo "🔄 推送到远程仓库 main 分支..."
git push origin main

echo ""
echo "=========================================="
echo "  🎉 部署成功！"
echo "=========================================="
echo "  🌐 访问地址: $DEPLOY_URL"
echo "  ⏳ GitHub Pages 正在构建，请等待 1-5 分钟"
echo "  📊 可在仓库 Settings > Pages 查看构建状态"
echo "=========================================="
