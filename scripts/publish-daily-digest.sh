#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_ROOT="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$WEBSITE_ROOT")"
REPORT_DATE="${1:-$(date '+%Y-%m-%d')}"
DIGEST_FILE="$PROJECT_ROOT/每日概要/$REPORT_DATE-每日情报概要.md"
PUBLIC_URL="https://wzrong.github.io/competitor-analysis/daily/$REPORT_DATE/"

if [ ! -f "$DIGEST_FILE" ]; then
    echo "未找到每日概要：$DIGEST_FILE" >&2
    exit 2
fi

cd "$WEBSITE_ROOT"
./scripts/sync.sh "发布每日情报概要 $REPORT_DATE"

echo "等待 GitHub Pages 更新：$PUBLIC_URL"
PAGE_READY=0
for _ in {1..12}; do
    if curl -fsSL "$PUBLIC_URL" | grep -q "$REPORT_DATE"; then
        PAGE_READY=1
        break
    fi
    sleep 10
done

if [ "$PAGE_READY" -ne 1 ]; then
    echo "GitHub Pages 在 120 秒内未更新，暂不发送企微，避免群内链接指向旧内容。" >&2
    exit 1
fi

./venv/bin/python scripts/send_wecom_digest.py --date "$REPORT_DATE"
