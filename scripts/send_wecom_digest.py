#!/usr/bin/env python3
"""将每日情报概要中的精简区块发送到企业微信群机器人。"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DIGEST_ROOT = PROJECT_ROOT / "每日概要"
LOG_ROOT = DIGEST_ROOT / "推送日志"
DEFAULT_WEBHOOK_FILE = Path.home() / ".config" / "xkw-intelligence" / "wecom-webhook-url"
DEFAULT_KEYCHAIN_SERVICE = "xkw-intelligence-wecom-webhook"
GROUPS = {
    "原群": DEFAULT_KEYCHAIN_SERVICE,
    "产品群": "xkw-intelligence-wecom-webhook-product",
    "解决方案群": "xkw-intelligence-wecom-webhook-solution",
}
MAX_CONTENT_BYTES = 3500


def parse_args():
    parser = argparse.ArgumentParser(description="发送学科网情报系统每日概要到企业微信群")
    parser.add_argument("--date", default=date.today().isoformat(), help="概要日期，格式 YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="只校验并打印消息，不发送")
    parser.add_argument("--force", action="store_true", help="忽略相同内容已发送记录")
    parser.add_argument(
        "--group",
        action="append",
        choices=GROUPS.keys(),
        help="只发送到指定群，可重复使用；默认发送到全部群",
    )
    return parser.parse_args()


def digest_path(report_date: str) -> Path:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", report_date):
        raise ValueError("日期格式必须为 YYYY-MM-DD")
    return DIGEST_ROOT / f"{report_date}-每日情报概要.md"


def extract_message(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    match = re.search(r"<!-- WECOM_START -->\s*(.*?)\s*<!-- WECOM_END -->", content, re.S)
    if not match:
        raise ValueError(f"{path.name} 缺少 WECOM_START/WECOM_END 标记")
    message = match.group(1).strip()
    if "学科网情报系统" not in message:
        raise ValueError("企微消息必须包含“学科网情报系统”")
    size = len(message.encode("utf-8"))
    if size > MAX_CONTENT_BYTES:
        raise ValueError(f"企微精简内容为 {size} 字节，超过安全上限 {MAX_CONTENT_BYTES} 字节")
    return message


def content_hash(message: str) -> str:
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def log_path(report_date: str) -> Path:
    return LOG_ROOT / f"{report_date}.json"


def read_previous_log(report_date: str):
    path = log_path(report_date)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def write_log(report_date: str, status: str, digest_hash: str, groups: dict):
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        "date": report_date,
        "status": status,
        "content_sha256": digest_hash,
        "updated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    payload["groups"] = groups
    log_path(report_date).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def validate_webhook(webhook: str) -> str:
    parsed = urlparse(webhook)
    query = parse_qs(parsed.query)
    if not (
        parsed.scheme == "https"
        and parsed.hostname == "qyapi.weixin.qq.com"
        and parsed.path == "/cgi-bin/webhook/send"
        and query.get("key")
        and query["key"][0]
    ):
        raise ValueError("Webhook 地址不是合法的企业微信群机器人地址")
    return webhook


def load_webhook(group_name: str, keychain_service: str):
    webhook = ""
    if group_name == "原群":
        webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook:
        keychain = subprocess.run(
            ["security", "find-generic-password", "-s", keychain_service, "-w"],
            capture_output=True,
            text=True,
            check=False,
        )
        if keychain.returncode == 0:
            webhook = keychain.stdout.strip()
    if not webhook and group_name == "原群":
        path = Path(os.getenv("WECOM_WEBHOOK_FILE", DEFAULT_WEBHOOK_FILE)).expanduser()
        if path.exists():
            webhook = path.read_text(encoding="utf-8").strip()
    if not webhook:
        return None
    return validate_webhook(webhook)


def previous_group_status(previous, group_name: str, digest_hash: str):
    if not previous or previous.get("content_sha256") != digest_hash:
        return None
    groups = previous.get("groups")
    if isinstance(groups, dict):
        return groups.get(group_name)
    # 兼容升级前的单群日志：旧的 sent 只代表原群已发送。
    if group_name == "原群" and previous.get("status") == "sent":
        return {"status": "sent", "migrated_from_legacy_log": True}
    return None


def send_message(webhook: str, message: str):
    payload = json.dumps({"msgtype": "markdown", "markdown": {"content": message}}, ensure_ascii=False).encode("utf-8")
    request = Request(webhook, data=payload, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    try:
        with urlopen(request, timeout=15) as response:
            body = response.read().decode("utf-8")
    except HTTPError as exc:
        raise RuntimeError(f"企微接口 HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"企微接口连接失败：{exc.reason}") from exc
    result = json.loads(body)
    if result.get("errcode") != 0:
        raise RuntimeError(f"企微接口返回失败：errcode={result.get('errcode')} errmsg={result.get('errmsg')}")
    return {"errcode": result.get("errcode"), "errmsg": result.get("errmsg", "ok")}


def main():
    args = parse_args()
    path = digest_path(args.date)
    if not path.exists():
        print(f"未找到每日概要：{path}", file=sys.stderr)
        return 2

    message = extract_message(path)
    digest_hash = content_hash(message)
    previous = read_previous_log(args.date)

    if args.dry_run:
        print(message)
        print(f"\n[校验通过] {len(message.encode('utf-8'))} bytes | sha256={digest_hash[:12]}")
        return 0

    selected_groups = args.group or list(GROUPS)
    group_results = {}
    if previous and previous.get("content_sha256") == digest_hash:
        if isinstance(previous.get("groups"), dict):
            group_results.update(previous["groups"])
        elif previous.get("status") == "sent":
            group_results["原群"] = {"status": "sent", "migrated_from_legacy_log": True}

    failed = False
    for group_name in selected_groups:
        prior = previous_group_status(previous, group_name, digest_hash)
        if not args.force and prior and prior.get("status") == "sent":
            group_results[group_name] = prior
            print(f"{group_name}：相同内容已发送，跳过。")
            continue

        try:
            webhook = load_webhook(group_name, GROUPS[group_name])
            if not webhook:
                group_results[group_name] = {"status": "skipped_no_webhook"}
                print(f"{group_name}：未配置 Webhook，已跳过。")
                continue
            result = send_message(webhook, message)
            group_results[group_name] = {"status": "sent", "detail": result}
            print(f"{group_name}：{args.date} 每日概要已发送。")
        except Exception as exc:
            failed = True
            group_results[group_name] = {"status": "failed", "detail": str(exc)}
            print(f"{group_name}：{exc}", file=sys.stderr)

    statuses = [item.get("status") for item in group_results.values()]
    if failed:
        overall_status = "partial_failed" if "sent" in statuses else "failed"
    elif "sent" in statuses:
        overall_status = "sent"
    else:
        overall_status = "skipped_no_webhook"
    write_log(args.date, overall_status, digest_hash, group_results)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
