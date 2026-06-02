#!/usr/bin/env python3
"""将 Obsidian 战略情报系统转换为 MkDocs 网站源文件。"""

import csv
import hashlib
import html
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path("/Users/wzrong/Documents/Claude/Projects/竞品分析工作台")
WEBSITE_ROOT = Path(__file__).parent.parent
DOCS_ROOT = WEBSITE_ROOT / "docs"

SITE_NAME = "学科网战略情报系统"
SITE_DESCRIPTION = "行业分析、竞争分析、政策分析、市场监测与应对建议门户"

SLUG_MAP = {
    "21世纪教育网": "21cnjy",
    "菁优网": "jyeoo",
    "橡皮网": "xiangpi",
    "教习网": "51jiaoxi",
    "正确云": "zhengqueyun",
    "希沃": "seewo",
    "好未来-九章爱学": "tal-jiuzhang",
    "猿辅导-飞象老师": "yuanfudao-feixiang",
    "智学网": "zhixue",
    "作业帮教师版": "zuoyebang-teacher",
    "金太阳·中课云": "jintaiyang-zhongkeyun",
    "猿题库": "yuantiku",
    "百度文库教育专区": "baidu-wenku-edu",
    "国家中小学智慧教育平台": "smartedu",
    "dokie": "dokie",
    "小盒科技": "xiaohe",
    "一起教育科技": "17zuoye",
    "翼鸥ClassIn": "classin",
    "洋葱学园": "yangcong",
    "鸿合科技": "hitevision",
    "高考网": "gaokao",
    "豆神教育": "doushen",
    "纳米盒": "namibox",
    "广州中金育能科技": "guangzhou-zhongjin-yuneng",
    "安徽智慧皆成数字技术": "anhui-zhihui-jiecheng",
    "成都爱易佰网络科技": "chengdu-aiyibai",
    "同方知网数字科技": "tongfang-cnki-digital",
    "北京简单科技": "beijing-jiandan",
    "山东浩学信息科技": "shandong-haoxue",
    "北京三海教育科技": "beijing-sanhai",
    "化育学川（江西）数字科技": "huayuxuechuan",
    "河北习知软件科技": "hebei-xizhi",
    "福建天启智汇科技": "fujian-tianqi-zhihui",
    "北京世纪超星": "beijing-shiji-chaoxing",
}

ACTION_DIRS = {
    "决策层简报": "executive-briefs",
    "Battlecard": "battlecards",
    "销售话术卡": "sales-cards",
    "教研参考卡": "teaching-cards",
    "运营参考卡": "operation-cards",
}

ACTION_DESCRIPTIONS = {
    "决策层简报": "面向管理层，回答威胁等级、关键变化与战略选项。",
    "Battlecard": "面向产品线，沉淀功能对比、核心差异和数据弹药。",
    "销售话术卡": "面向市场线，提供客户对比场景下的反制话术。",
    "教研参考卡": "面向教研线，提炼竞品教学理念、课标依据和可借鉴动作。",
    "运营参考卡": "面向运营线，分析竞品增长、内容、变现和渠道策略。",
}


def slugify(name: str) -> str:
    if name in SLUG_MAP:
        return SLUG_MAP[name]
    ascii_slug = re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-")
    if ascii_slug:
        return ascii_slug
    digest = hashlib.md5(name.encode("utf-8")).hexdigest()[:8]
    return f"item-{digest}"


def clean_docs():
    old_docs = None
    if DOCS_ROOT.exists():
        old_docs = WEBSITE_ROOT / f".docs-old-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        DOCS_ROOT.rename(old_docs)
    for path in [
        DOCS_ROOT,
        DOCS_ROOT / "assets" / "screenshots",
        DOCS_ROOT / "assets" / "images",
        DOCS_ROOT / "assets" / "downloads",
        DOCS_ROOT / "stylesheets",
        DOCS_ROOT / "javascripts",
    ]:
        path.mkdir(parents=True, exist_ok=True)
    if old_docs is not None:
        shutil.rmtree(old_docs, ignore_errors=True)


def has_front_matter(content: str) -> bool:
    return content.startswith("---")


def inject_front_matter(content: str, **fields) -> str:
    if has_front_matter(content):
        return content
    lines = ["---"]
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    lines.extend(["---", ""])
    return "\n".join(lines) + content


def rewrite_image_refs(content: str) -> str:
    def repl(match):
        alt_text = match.group(1)
        old_path = match.group(2)
        parts = old_path.split("/")
        if len(parts) >= 4 and parts[0] == "竞品库" and parts[2] == "screenshots":
            slug = slugify(parts[1])
            rest = "/".join(parts[3:])
            return f"![{alt_text}](/assets/screenshots/{slug}/{rest})"
        return match.group(0)

    return re.sub(r"!\[(.*?)\]\((竞品库/[^)]+)\)", repl, content)


def site_relative(dst: Path, target: str) -> str:
    target_path = DOCS_ROOT / target
    return Path(os.path.relpath(target_path, dst.parent)).as_posix()


def rewrite_obsidian_link(target: str, dst: Path) -> str:
    decoded = target.replace("%20", " ")
    anchor = ""
    if "#" in decoded:
        decoded, anchor = decoded.split("#", 1)
        anchor = f"#{anchor}"

    if decoded in ("系统状态看板.md", "./系统状态看板.md"):
        return f"index.md{anchor}"
    if decoded in ("INDEX.md", "./INDEX.md"):
        return f"index.md{anchor}"
    if decoded == "../INDEX.md":
        return f"{site_relative(dst, 'index.md')}{anchor}"
    if decoded == "./CLAUDE.md":
        return target
    if decoded in ("行业分析 · 实施方案.md", "./行业分析 · 实施方案.md"):
        return target
    if decoded in ("市场监测 · 实施方案-v0.1.md", "./市场监测 · 实施方案-v0.1.md"):
        return f"{site_relative(dst, 'market/市场监测 · 实施方案-v0.1.md')}{anchor}"
    if decoded.startswith("../销售话术卡/"):
        return f"../sales-cards/{decoded.split('/', 2)[2]}{anchor}"
    if decoded.startswith("../Battlecard/"):
        return f"../battlecards/{decoded.split('/', 2)[2]}{anchor}"
    if decoded.startswith("../监测日志/") or decoded.startswith("../../监测日志/"):
        filename = decoded.rsplit("/", 1)[1]
        return f"{site_relative(dst, f'monitor/{filename}')}{anchor}"
    if decoded.startswith("../政策分析/"):
        return f"{site_relative(dst, 'policy/index.md')}{anchor}"
    if decoded.startswith("../竞品库/INDEX.md"):
        return f"{site_relative(dst, 'competitors/index.md')}{anchor}"
    if decoded.startswith("../竞品库/") or decoded.startswith("../../竞品库/"):
        parts = decoded.split("/")
        if "竞品库" in parts:
            idx = parts.index("竞品库")
            if len(parts) > idx + 1:
                name = parts[idx + 1]
                slug = slugify(name)
                if len(parts) > idx + 2 and parts[idx + 2] == "profile.md":
                    return f"{site_relative(dst, f'competitors/{slug}/index.md')}{anchor}"
                if len(parts) > idx + 3 and parts[idx + 2] == "analyses":
                    filename = parts[idx + 3]
                    return f"{site_relative(dst, f'competitors/{slug}/analyses/{filename}')}{anchor}"
                if len(parts) > idx + 3 and parts[idx + 2] == "发版追踪":
                    filename = parts[idx + 3]
                    return f"{site_relative(dst, f'competitors/{slug}/releases/{filename}')}{anchor}"
    if decoded.startswith("../系统状态/") or decoded.startswith("../../系统状态/"):
        filename = decoded.rsplit("/", 1)[1]
        target = f"status/{filename}"
        target_path = DOCS_ROOT / target
        if not target_path.exists():
            return target
        return f"{site_relative(dst, target)}{anchor}"
    if decoded.startswith("Projects/竞品分析工作台/竞品库/") and "/screenshots/" in decoded:
        parts = decoded.split("/")
        idx = parts.index("竞品库")
        slug = slugify(parts[idx + 1])
        filename = parts[-1]
        return f"{site_relative(dst, f'assets/screenshots/{slug}/{filename}')}{anchor}"
    return target


def normalize_links(content: str, dst: Path) -> str:
    def repl(match):
        label = match.group(1)
        target = match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#", "/assets/")):
            return match.group(0)
        return f"[{label}]({rewrite_obsidian_link(target, dst)})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, content)


def write_markdown(src: Path, dst: Path, **front_matter):
    content = src.read_text(encoding="utf-8")
    content = rewrite_image_refs(content)
    if dst == DOCS_ROOT / "industry" / "index.md":
        content = re.sub(r"\n> .*?(CLAUDE\.md|实施方案).*", "", content)
    if dst == DOCS_ROOT / "market" / "index.md":
        content = re.sub(r"\n> .*?(实施方案|CLAUDE\.md).*", "", content)
        content = "\n".join(
            line for line in content.splitlines()
            if not any(skip in line for skip in ["运行手册.md", "字段口径.md", "采集记录/", "周报模板.md"])
        )
        content = re.sub(r"\((招投标数据/[^)]+)\.csv\)", r"(\1.md)", content)
    if dst == DOCS_ROOT / "status" / "index.md":
        content = re.sub(r"\n\d+\. 已新增 \[发版追踪记录模板\]\([^)]*\).*", "", content)
    content = normalize_links(content, dst)
    content = inject_front_matter(content, **front_matter)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content, encoding="utf-8")


def parse_competitor_index() -> dict:
    index_src = VAULT_ROOT / "竞品库" / "INDEX.md"
    text = index_src.read_text(encoding="utf-8")
    tiers = {"Tier 1": [], "Tier 2": [], "Tier 3": []}
    current_tier = None
    for line in text.splitlines():
        heading = re.match(r"##\s+(Tier\s+[123])", line)
        if heading:
            current_tier = heading.group(1)
            continue
        if not current_tier or not line.startswith("|"):
            continue
        cols = [col.strip() for col in line.strip("|").split("|")]
        if len(cols) < 7 or cols[0] in ("竞品名", "---") or set(cols[0]) <= {"-", " "}:
            continue
        name = cols[0]
        tiers[current_tier].append({
            "name": name,
            "slug": slugify(name),
            "relation": cols[1],
            "track": cols[2],
            "company": cols[3],
            "url": cols[4],
            "latest": cols[5],
            "updated": cols[6],
        })
    return tiers


def copy_extra_assets():
    assets = [
        (WEBSITE_ROOT / "overrides" / "extra.css", DOCS_ROOT / "stylesheets" / "extra.css", "/* Custom styles */\n"),
        (WEBSITE_ROOT / "overrides" / "extra.js", DOCS_ROOT / "javascripts" / "extra.js", "// Custom scripts\n"),
        (WEBSITE_ROOT / "overrides" / "images" / "weixin.png", DOCS_ROOT / "assets" / "images" / "weixin.png", None),
    ]
    for src, dst, fallback in assets:
        if src.exists():
            shutil.copyfile(src, dst)
        elif fallback is not None:
            dst.write_text(fallback, encoding="utf-8")


def copy_system_status():
    src_dir = VAULT_ROOT / "系统状态"
    dst_dir = DOCS_ROOT / "status"
    files = sorted(src_dir.glob("*.md"))
    for src in files:
        dst_name = "index.md" if src.name == "系统状态看板.md" else src.name
        write_markdown(src, dst_dir / dst_name, page_type="system_status", tags=["系统状态"])
    return [f.stem for f in files]


def copy_framework():
    dst = DOCS_ROOT / "framework" / "index.md"
    src = VAULT_ROOT / "战略情报系统落地方案.md"
    write_markdown(src, dst, page_type="framework", tags=["战略框架", "9层分析框架"])


def copy_industry_analysis():
    dst_dir = DOCS_ROOT / "industry"
    write_markdown(VAULT_ROOT / "行业分析" / "INDEX.md", dst_dir / "index.md", page_type="industry_index", tags=["行业分析"])
    nav_files = []
    for subdir in ["日情报", "素材池"]:
        src_subdir = VAULT_ROOT / "行业分析" / subdir
        if not src_subdir.exists():
            continue
        for src in sorted(src_subdir.glob("*.md"), reverse=True):
            dst = dst_dir / subdir / src.name
            write_markdown(src, dst, page_type="industry_report", tags=["行业分析", subdir])
            nav_files.append((subdir, src.stem, f"industry/{subdir}/{src.name}"))
    return nav_files


def copy_policy_analysis():
    dst_dir = DOCS_ROOT / "policy"
    write_markdown(VAULT_ROOT / "政策分析" / "policy_timeline.md", dst_dir / "index.md", page_type="policy_timeline", tags=["政策分析"])
    nav_files = []
    src_interpretations = VAULT_ROOT / "政策分析" / "解读"
    if src_interpretations.exists():
        for src in sorted(src_interpretations.glob("*.md"), reverse=True):
            write_markdown(src, dst_dir / "解读" / src.name, page_type="policy_interpretation", tags=["政策解读"])
            nav_files.append((src.stem, f"policy/解读/{src.name}"))
    return nav_files


def csv_to_table_page(src: Path, dst: Path):
    rows = []
    with src.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    title = src.stem
    lines = [
        "---",
        "page_type: market_bid_data",
        "tags:",
        "  - 市场监测",
        "  - 招投标数据",
        "---",
        f"# {title}",
        "",
        f"> 原始 CSV：[下载 {src.name}]({src.name})",
        "",
    ]
    if rows:
        headers = rows[0]
        lines.append('<div class="table-scroll">')
        lines.append("<table>")
        lines.append("<thead><tr>" + "".join(f"<th>{html.escape(cell)}</th>" for cell in headers) + "</tr></thead>")
        lines.append("<tbody>")
        for row in rows[1:]:
            padded = row + [""] * max(0, len(headers) - len(row))
            lines.append("<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in padded[:len(headers)]) + "</tr>")
        lines.append("</tbody>")
        lines.append("</table>")
        lines.append("</div>")
    else:
        lines.append("> CSV 当前为空。")

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(lines) + "\n", encoding="utf-8")


def copy_market_monitoring():
    dst_dir = DOCS_ROOT / "market"
    write_markdown(VAULT_ROOT / "市场监测" / "INDEX.md", dst_dir / "index.md", page_type="market_index", tags=["市场监测"])
    nav_files = []

    weekly_src = VAULT_ROOT / "市场监测" / "周报"
    if weekly_src.exists():
        for src in sorted(weekly_src.glob("*.md"), reverse=True):
            if src.name in {"README.md", "周报模板.md"}:
                continue
            dst = dst_dir / "周报" / src.name
            write_markdown(src, dst, page_type="market_weekly", tags=["市场监测", "周报"])
            nav_files.append(("周报", dst.stem, f"market/周报/{src.name}"))

    object_list = VAULT_ROOT / "市场监测" / "监测对象清单.md"
    if object_list.exists():
        dst = dst_dir / object_list.name
        write_markdown(object_list, dst, page_type="market_watchlist", tags=["市场监测", "招投标数据"])
        nav_files.append(("招投标数据", "监测对象清单", f"market/{object_list.name}"))

    data_src = VAULT_ROOT / "市场监测" / "招投标数据"
    data_dst = dst_dir / "招投标数据"
    if data_src.exists():
        data_dst.mkdir(parents=True, exist_ok=True)
        for src in sorted(data_src.iterdir()):
            if not src.is_file():
                continue
            if src.suffix.lower() == ".csv":
                shutil.copyfile(src, data_dst / src.name)
                table_dst = data_dst / f"{src.stem}.md"
                csv_to_table_page(src, table_dst)
                nav_files.append(("招投标数据", src.stem, f"market/招投标数据/{src.stem}.md"))
            elif src.suffix.lower() == ".md":
                continue

    nav_files.sort(key=lambda x: (x[0], x[1]))
    return nav_files


def sort_markdown_by_date(files):
    def key(path: Path):
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.stem)
        return (match.group(1) if match else "0000-00-00", path.stem)
    return sorted(files, key=key, reverse=True)


def copy_monitor_logs():
    monitor_src = VAULT_ROOT / "监测日志"
    monitor_dst = DOCS_ROOT / "monitor"
    monitor_dst.mkdir(parents=True, exist_ok=True)
    dated_logs = [src for src in monitor_src.glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}-", src.stem)]
    other_logs = [src for src in monitor_src.glob("*.md") if src not in dated_logs]
    log_files = sort_markdown_by_date(dated_logs) + sorted(other_logs, reverse=True)
    for src in log_files:
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})-", src.stem)
        write_markdown(src, monitor_dst / src.name, page_type="monitor_log", date=date_match.group(1) if date_match else src.stem, tags=["竞争监测"])
    if dated_logs:
        latest_file = sort_markdown_by_date(dated_logs)[0]
        latest_content = (monitor_dst / latest_file.name).read_text(encoding="utf-8")
        (monitor_dst / "index.md").write_text(latest_content, encoding="utf-8")
    elif log_files:
        latest_content = (monitor_dst / log_files[0].name).read_text(encoding="utf-8")
        (monitor_dst / "index.md").write_text(latest_content, encoding="utf-8")
    else:
        (monitor_dst / "index.md").write_text("# 竞争监测日志\n\n> 暂无监测简报。\n", encoding="utf-8")
    return [f.stem for f in log_files]


def build_competitor_index(tiers: dict, analysis_map: dict) -> str:
    lines = [
        "# 竞争分析 · 竞品库",
        "",
        "> 按新版战略情报系统分层展示。Tier 1 执行完整9层分析，Tier 2 执行 L1-L5，Tier 3 进入观察池。",
        "",
    ]
    for tier, items in tiers.items():
        if not items:
            continue
        lines.extend([f"## {tier}", "", "| 竞品名 | 竞争关系 | 赛道 | 所属公司 | URL | 最新分析 | 最后更新 |", "|---|---|---|---|---|---|---|"])
        for item in items:
            name_link = f"[{item['name']}](./{item['slug']}/index.md)"
            url = item["url"]
            url_link = "—" if url == "—" else f"[{url}]({url})"
            latest = item["latest"]
            if item["name"] in analysis_map and analysis_map[item["name"]]:
                latest_file = analysis_map[item["name"]][-1]
                latest = f"[{latest}](./{item['slug']}/analyses/{latest_file})"
            lines.append(f"| {name_link} | {item['relation']} | {item['track']} | {item['company']} | {url_link} | {latest} | {item['updated']} |")
        lines.append("")
    lines.extend([
        "---",
        "",
        "## 观察池",
        "",
        "完整观察池见源文件 `竞品库/观察池/INDEX.md`。",
    ])
    return "\n".join(lines) + "\n"


def copy_competitors(tiers: dict):
    lib_root = VAULT_ROOT / "竞品库"
    competitors_dir = DOCS_ROOT / "competitors"
    competitors_dir.mkdir(parents=True, exist_ok=True)
    analysis_map = {}
    for item in sorted(lib_root.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            analyses_src = item / "analyses"
            analysis_map[item.name] = [f.name for f in sorted(analyses_src.glob("*.md"))] if analyses_src.exists() else []

    index_content = build_competitor_index(tiers, analysis_map)
    index_content = inject_front_matter(index_content, page_type="competitor_index", tags=["竞争分析", "竞品库"])
    (competitors_dir / "index.md").write_text(index_content, encoding="utf-8")

    tier_by_name = {item["name"]: tier for tier, items in tiers.items() for item in items}
    for item in sorted(lib_root.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue
        cn_name = item.name
        slug = slugify(cn_name)
        comp_dir = competitors_dir / slug
        comp_dir.mkdir(parents=True, exist_ok=True)
        tier = tier_by_name.get(cn_name, "未分层")
        profile_src = item / "profile.md"
        if profile_src.exists():
            content = profile_src.read_text(encoding="utf-8")
            dst = comp_dir / "index.md"
            content = normalize_links(rewrite_image_refs(content), dst)
            sections = []
            if analysis_map.get(cn_name):
                sections.append("## 深度分析\n")
                for fname in analysis_map[cn_name]:
                    sections.append(f"- [{Path(fname).stem}](analyses/{fname})")
            releases_src = item / "发版追踪"
            release_files = sorted(releases_src.glob("*.md")) if releases_src.exists() else []
            if release_files:
                sections.append("\n## 发版追踪\n")
                for fname in release_files:
                    sections.append(f"- [{fname.stem}](releases/{fname.name})")
            if sections:
                content += "\n\n---\n\n" + "\n".join(sections) + "\n"
            content = inject_front_matter(content, page_type="competitor_profile", competitor_name=cn_name, tier=tier, tags=["竞品档案", tier])
            dst.write_text(content, encoding="utf-8")

        analyses_src = item / "analyses"
        if analyses_src.exists():
            for src in sorted(analyses_src.glob("*.md")):
                content = src.read_text(encoding="utf-8")
                dst = comp_dir / "analyses" / src.name
                content = normalize_links(rewrite_image_refs(content), dst)
                back_link = f"[:octicons-arrow-left-24: 返回 {cn_name} 档案](../index.md)"
                content = inject_front_matter(content, page_type="analysis", competitor_name=cn_name, tier=tier, tags=["深度分析", cn_name, tier])
                content = insert_after_front_matter(content, back_link)
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(content, encoding="utf-8")

        releases_src = item / "发版追踪"
        if releases_src.exists():
            for src in sorted(releases_src.glob("*.md")):
                content = src.read_text(encoding="utf-8")
                dst = comp_dir / "releases" / src.name
                content = normalize_links(rewrite_image_refs(content), dst)
                back_link = f"[:octicons-arrow-left-24: 返回 {cn_name} 档案](../index.md)"
                content = inject_front_matter(content, page_type="release_tracking", competitor_name=cn_name, tier=tier, tags=["发版追踪", cn_name, tier])
                content = insert_after_front_matter(content, back_link)
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(content, encoding="utf-8")

        screenshots_src = item / "screenshots"
        if screenshots_src.exists():
            screenshots_dst = DOCS_ROOT / "assets" / "screenshots" / slug
            screenshots_dst.mkdir(parents=True, exist_ok=True)
            for img in screenshots_src.iterdir():
                if img.is_file():
                    shutil.copyfile(img, screenshots_dst / img.name)
    return analysis_map


def insert_after_front_matter(content: str, insertion: str) -> str:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) == 3:
            return f"---{parts[1]}---\n\n{insertion}\n\n{parts[2].lstrip()}"
    return f"{insertion}\n\n{content}"


def copy_response_outputs():
    src_root = VAULT_ROOT / "应对建议"
    dst_root = DOCS_ROOT / "actions"
    dst_root.mkdir(parents=True, exist_ok=True)
    nav = {}
    index_lines = [
        "# 应对建议",
        "",
        "> 情报的终点是行动。这里按受众分发 L9 输出，避免决策层、产品线、市场线、教研线、运营线混用。",
        "",
        "<div class=\"grid cards\" markdown>",
        "",
    ]
    for name, slug in ACTION_DIRS.items():
        src_dir = src_root / name
        files = sorted(src_dir.glob("*.md"), reverse=True) if src_dir.exists() else []
        nav[name] = []
        dst_dir = dst_root / slug
        dst_dir.mkdir(parents=True, exist_ok=True)
        index_lines.extend([
            f"-   __{name}__",
            "",
            "    ---",
            "",
            f"    {ACTION_DESCRIPTIONS[name]}",
            "",
            f"    [:octicons-arrow-right-24: 查看{name}]({slug}/index.md)",
            "",
        ])
        sub_index = [f"# {name}", "", ACTION_DESCRIPTIONS[name], ""]
        for src in files:
            write_markdown(src, dst_dir / src.name, page_type="action_output", audience=name, tags=["应对建议", name])
            sub_index.append(f"- [{src.stem}]({src.name})")
            nav[name].append((src.stem, f"actions/{slug}/{src.name}"))
        if len(sub_index) == 4:
            sub_index.append("> 暂无产出。")
        (dst_dir / "index.md").write_text("\n".join(sub_index) + "\n", encoding="utf-8")
    index_lines.extend(["</div>", ""])
    (dst_root / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    return nav


def generate_feedback_page():
    feedback_dir = DOCS_ROOT / "feedback"
    feedback_dir.mkdir(parents=True, exist_ok=True)
    content = """---
hide:
  - toc
---

# 问题反馈

欢迎对战略情报系统提出改进建议，你的反馈会直接影响内容质量。

<div class="grid cards feedback-grid" markdown>

-   :octicons-issue-opened-16:{ .lg .middle } __内容纠错__

    ---

    发现某条竞品、政策、行业或市场信息有误？

    [:octicons-arrow-right-24: 提交纠错](https://github.com/wzrong/competitor-analysis/issues/new?template=content-fix.yml)

-   :octicons-plus-16:{ .lg .middle } __补充竞品__

    ---

    发现有价值的竞品未收录？

    [:octicons-arrow-right-24: 提交补充](https://github.com/wzrong/competitor-analysis/issues/new?template=add-competitor.yml)

-   :octicons-light-bulb-16:{ .lg .middle } __功能建议__

    ---

    对分析维度或站点功能有想法？

    [:octicons-arrow-right-24: 提交建议](https://github.com/wzrong/competitor-analysis/issues/new?template=feature-request.yml)

</div>

---

> 你也可以 [浏览所有反馈](https://github.com/wzrong/competitor-analysis/issues){target="_blank"}，看看其他人提出了什么建议。

或者，你还可以关注我的微信公众号，直接给我反馈：

![微信公众号二维码](/assets/images/weixin.png){ width="180" }
"""
    (feedback_dir / "index.md").write_text(content, encoding="utf-8")


def generate_home(tiers: dict, industry_nav: list, policy_nav: list, market_nav: list, action_nav: dict, monitor_logs: list):
    today = datetime.now().strftime("%Y-%m-%d")
    tier1 = len(tiers.get("Tier 1", []))
    tier2 = len(tiers.get("Tier 2", []))
    action_count = sum(len(items) for items in action_nav.values())
    latest_industry = industry_nav[0][1] if industry_nav else "暂无"
    latest_policy = policy_nav[0][0] if policy_nav else "政策时间轴"
    latest_monitor = monitor_logs[0] if monitor_logs else "暂无"
    content = f"""---
hide:
  - navigation
  - toc
---

# 学科网战略情报系统

> 学科网的战略导航仪：回答「风向往哪吹、钱往哪里流、我们往哪打」。

<div class="grid cards intelligence-grid" markdown>

-   :material-weather-windy:{{ .lg .middle }} __行业分析__

    ---

    趋势判断：风向往哪吹。最新：{latest_industry}

    [:octicons-arrow-right-24: 查看行业分析](industry/index.md)

-   :material-sword-cross:{{ .lg .middle }} __竞争分析__

    ---

    竞品洞察：Tier 1 {tier1} 家，Tier 2 {tier2} 家。

    [:octicons-arrow-right-24: 查看竞品库](competitors/index.md)

-   :material-bank:{{ .lg .middle }} __政策分析__

    ---

    合规与机会：政策风怎么吹。最新：{latest_policy}

    [:octicons-arrow-right-24: 查看政策分析](policy/index.md)

-   :material-cash-multiple:{{ .lg .middle }} __市场监测__

    ---

    资金流向：钱往哪里流。

    [:octicons-arrow-right-24: 查看市场监测](market/index.md)

</div>

## 关键输出

<div class="grid cards" markdown>

-   __系统状态__

    ---

    当前事实入口，包含模块状态、阻塞项和下一步行动。

    [:octicons-arrow-right-24: 打开状态看板](status/index.md)

-   __应对建议__

    ---

    已沉淀 {action_count} 份 L9 输出，覆盖决策层、产品线、市场线、教研线、运营线。

    [:octicons-arrow-right-24: 查看应对建议](actions/index.md)

-   __竞争监测__

    ---

    最新周监测：{latest_monitor}

    [:octicons-arrow-right-24: 查看监测日志](monitor/index.md)

-   __方法框架__

    ---

    9层分析框架、数据质量规范和 L9 输出规范。

    [:octicons-arrow-right-24: 查看框架](framework/index.md)

</div>

## 模块状态

| 模块 | 状态 | 入口 |
|---|---|---|
| 行业分析 | 🟡 试运行 | [行业分析](industry/index.md) |
| 竞争分析 | 🟢 运行中 | [竞争分析](competitors/index.md) |
| 政策分析 | 🟢 运行中 | [政策分析](policy/index.md) |
| 市场监测 | 🟡 起步 | [市场监测](market/index.md) |

> 最后更新：{today}
"""
    (DOCS_ROOT / "index.md").write_text(content, encoding="utf-8")


def nav_item(title: str, path: str, indent: int = 2) -> str:
    return f"{' ' * indent}- {title}: {path}\n"


def generate_mkdocs_yml(tiers: dict, industry_nav: list, policy_nav: list, market_nav: list, action_nav: dict, monitor_logs: list):
    nav = f"""site_name: {SITE_NAME}
site_description: {SITE_DESCRIPTION}
site_author: 学科网产品团队

theme:
  name: material
  language: zh
  custom_dir: overrides
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: 切换到深色模式
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: black
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: 切换到浅色模式
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.expand
    - navigation.path
    - navigation.top
    - search.suggest
    - search.highlight
    - search.share
    - content.tabs.link
    - content.code.copy
    - content.tooltips
    - header.autohide
  icon:
    logo: material/chart-box

plugins:
  - search:
      lang:
        - zh
        - en
      separator: '[\\s\\u200b\\-]'

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
      title: 目录
      toc_depth: 3
  - pymdownx.arithmatex:
      generic: true
  - nl2br
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js

nav:
  - 首页: index.md
  - 行业分析:
    - 总览: industry/index.md
"""
    for subdir, title, path in industry_nav:
        nav += nav_item(title, path, 4)

    nav += "  - 竞品分析:\n    - 竞品库总览: competitors/index.md\n"
    for tier in ["Tier 1", "Tier 2"]:
        items = tiers.get(tier, [])
        if items:
            nav += f"    - {tier}:\n"
            for item in items:
                nav += nav_item(item["name"], f"competitors/{item['slug']}/index.md", 6)

    nav += "  - 政策分析:\n    - 政策时间轴: policy/index.md\n"
    for title, path in policy_nav:
        nav += nav_item(title, path, 4)

    nav += "  - 市场监测:\n    - 总览: market/index.md\n"
    current_market_group = None
    for group, title, path in market_nav:
        if group != current_market_group:
            current_market_group = group
            nav += f"    - {group}:\n"
        nav += nav_item(title, path, 6)

    nav += "  - 应对建议:\n    - 总览: actions/index.md\n"
    for name, slug in ACTION_DIRS.items():
        nav += f"    - {name}:\n      - 总览: actions/{slug}/index.md\n"
        for title, path in action_nav.get(name, []):
            nav += nav_item(title, path, 6)

    nav += "  - 监测日志:\n    - 最新监测: monitor/index.md\n"
    for log_name in monitor_logs:
        nav += nav_item(log_name, f"monitor/{log_name}.md", 4)
    nav += "  - 反馈: feedback/index.md\n"
    (WEBSITE_ROOT / "mkdocs.yml").write_text(nav, encoding="utf-8")


def main():
    print("=" * 50)
    print("学科网战略情报系统 → MkDocs 网站构建")
    print("=" * 50)
    clean_docs()
    tiers = parse_competitor_index()
    copy_extra_assets()
    copy_system_status()
    copy_framework()
    industry_nav = copy_industry_analysis()
    policy_nav = copy_policy_analysis()
    market_nav = copy_market_monitoring()
    copy_competitors(tiers)
    monitor_logs = copy_monitor_logs()
    action_nav = copy_response_outputs()
    generate_feedback_page()
    generate_home(tiers, industry_nav, policy_nav, market_nav, action_nav, monitor_logs)
    generate_mkdocs_yml(tiers, industry_nav, policy_nav, market_nav, action_nav, monitor_logs)
    print("\n✅ 构建完成！")
    print(f"   输出目录: {DOCS_ROOT}")
    print(f"   下一步: cd {WEBSITE_ROOT} && mkdocs serve")


if __name__ == "__main__":
    main()
