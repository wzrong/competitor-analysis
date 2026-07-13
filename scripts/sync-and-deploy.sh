#!/bin/bash
# 本地自动同步脚本
# 用法：在 Obsidian 文件变更后手动执行，或配合 fswatch 自动触发

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="$(dirname "$SCRIPT_DIR")"
echo "=========================================="
echo "学科网情报系统 → 网站同步部署"
echo "=========================================="

cd "$WEBSITE_DIR"

# 1. 激活虚拟环境
source venv/bin/activate

# 2. 运行构建脚本
echo "[1/3] 构建 docs/ 目录..."
python3 scripts/build.py

# 3. 提交变更
echo "[2/3] 提交变更..."
git add -A
if git diff --cached --quiet; then
    echo "没有变更需要提交"
    exit 0
fi

git commit -m "sync: $(date '+%Y-%m-%d %H:%M:%S')"

# 4. 推送到 GitHub（触发 GitHub Actions 部署）
echo "[3/3] 推送到 GitHub..."
git push origin main

echo ""
echo "✅ 同步完成！GitHub Actions 将自动部署到 Pages。"
echo "   部署状态可在 GitHub 仓库的 Actions 标签页查看。"
