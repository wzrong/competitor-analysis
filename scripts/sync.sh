#!/bin/bash
set -e

# 竞品分析工作台 — 一键构建+推送脚本
# 用法: ./scripts/sync.sh [提交信息]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "=================================================="
echo "  竞品分析工作台 → 构建 & 推送"
echo "=================================================="
echo ""

# ── 步骤 1: 从 Obsidian 构建到 docs/ ──
echo "[1/4] 从 Obsidian 构建 MkDocs 源文件..."
python3 scripts/build.py

# ── 步骤 2: 生成静态站点 ──
echo ""
echo "[2/4] 生成静态 HTML 站点..."
set +e
BUILD_OUTPUT=$(./venv/bin/mkdocs build --quiet 2>&1)
BUILD_STATUS=$?
set -e
printf "%s\n" "$BUILD_OUTPUT" | awk '
  /Warning from the Material for MkDocs team/ { skip = 1; next }
  skip && /https:\/\/squidfunk.github.io\/mkdocs-material\/blog\/2026\/02\/18\/mkdocs-2.0\// { skip = 0; next }
  !skip { print }
'
if [ "$BUILD_STATUS" -ne 0 ]; then
    exit "$BUILD_STATUS"
fi

# ── 步骤 3: Git 提交 ──
echo ""
echo "[3/4] Git 提交..."
git add -A

# 检查是否有变更
if git diff --cached --quiet; then
    echo ""
    echo "⚠️  没有可提交的变更（内容可能未更新）"
    exit 0
fi

# 提交信息：支持自定义，默认用时间戳
COMMIT_MSG="${1:-更新站点内容 $(date '+%Y-%m-%d %H:%M:%S')}"
git commit -m "$COMMIT_MSG"

# ── 步骤 4: 推送到 GitHub ──
echo ""
echo "[4/4] 推送到 GitHub..."

# 检测代理是否可用
PROXY=$(git config --global --get https.proxy 2>/dev/null || true)
if [ -n "$PROXY" ]; then
    echo "      检测到 Git 代理: $PROXY"
    # 尝试带代理推送
    if git push origin main 2>&1; then
        PUSH_OK=1
    else
        echo "      代理推送失败，尝试绕过代理..."
        if git -c http.proxy= -c https.proxy= push origin main 2>&1; then
            PUSH_OK=1
        fi
    fi
else
    if git push origin main 2>&1; then
        PUSH_OK=1
    fi
fi

# ── 完成 ──
echo ""
echo "=================================================="
if [ "$PUSH_OK" = "1" ]; then
    echo "✅ 推送成功！"
    echo ""
    echo "   GitHub Pages 将在 1-2 分钟后自动部署"
    echo "   访问地址: https://wzrong.github.io/competitor-analysis"
else
    echo "❌ 推送失败"
    echo ""
    echo "   可能原因:"
    echo "   1. 网络代理未开启（你配置了 $PROXY）"
    echo "   2. GitHub 认证过期"
    echo ""
    echo "   你可以稍后手动推送:"
    echo "   cd $(pwd) && git push origin main"
fi
echo "=================================================="
