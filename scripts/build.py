#!/usr/bin/env python3
"""将 Obsidian 战略情报系统转换为 MkDocs 网站源文件。"""

import csv
import hashlib
import html
import os
import re
import shutil
from datetime import date, datetime, timedelta
from pathlib import Path

VAULT_ROOT = Path("/Users/wzrong/Documents/Claude/Projects/竞品分析工作台")
AI_BRIEFING_ROOT = Path("/Users/wzrong/Documents/Claude/Projects/AI信息聚合")
WEBSITE_ROOT = Path(__file__).parent.parent
DOCS_ROOT = WEBSITE_ROOT / "docs"
MONITOR_ROOT = VAULT_ROOT / "竞品库" / "监测日志"

SITE_NAME = "学科网战略情报系统"
SITE_DESCRIPTION = "行业分析、竞争分析、政策分析、市场监测与应对建议门户"

INTERNAL_SECTION_HEADINGS = {
    "L9 触发建议汇总",
    "联动建议",
    "联动出口",
}

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
    "理想众望": "item-221d239f",
    "理想众望（试题网）": "item-221d239f",
}

COMPETITOR_NAME_ALIASES = {
    "理想众望（试题网）": "理想众望",
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


def canonical_competitor_name(name: str) -> str:
    return COMPETITOR_NAME_ALIASES.get(name, name)


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
    if decoded in ("../政策分析/解读/", "../../政策分析/解读/", "政策分析/解读/"):
        return f"{site_relative(dst, 'policy/index.md')}{anchor}"
    if decoded.startswith(("../政策分析/解读/", "../../政策分析/解读/", "政策分析/解读/")):
        filename = decoded.rsplit("/", 1)[1]
        return f"{site_relative(dst, f'policy/解读/{filename}')}{anchor}"
    if decoded.startswith(("../行业分析/日情报/", "../../行业分析/日情报/", "行业分析/日情报/")):
        filename = decoded.rsplit("/", 1)[1]
        return f"{site_relative(dst, f'industry/日情报/{filename}')}{anchor}"
    if decoded.startswith("../政策分析/") or decoded.startswith("../../政策分析/"):
        return f"{site_relative(dst, 'policy/index.md')}{anchor}"
    if decoded.startswith(("../profile.md", "./profile.md")):
        return "../index.md"
    if decoded.startswith(("../理想众望/analyses/", "../../理想众望/analyses/", "理想众望/analyses/")):
        filename = decoded.rsplit("/", 1)[1]
        competitor_slug = slugify("理想众望")
        return f"{site_relative(dst, f'competitors/{competitor_slug}/analyses/{filename}')}{anchor}"
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
    if dst.is_relative_to(DOCS_ROOT / "ai-briefings") and decoded.startswith("briefings/"):
        return f"{decoded.split('/', 1)[1]}{anchor}"
    return target


def normalize_links(content: str, dst: Path) -> str:
    def repl(match):
        label = match.group(1)
        target = match.group(2)
        if (
            dst.is_relative_to(DOCS_ROOT / "ai-briefings")
            and (
                target == "#深度阅读推荐"
                or target.startswith("#-")
                or target.startswith("#⭐")
                or (target.startswith("#") and ("深度推荐" in label or "深度阅读" in label))
            )
        ):
            return f"[{label}](#_2)"
        if target.startswith(("http://", "https://", "mailto:", "#", "/assets/")):
            return match.group(0)
        return f"[{label}]({rewrite_obsidian_link(target, dst)})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, content)


def strip_internal_sections(content: str) -> str:
    """移除仅供内部协作使用、不适合站点公开展示的章节。"""
    lines = content.splitlines()
    kept = []
    skip_level = None
    for line in lines:
        heading = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip()
            if skip_level is not None and level <= skip_level:
                skip_level = None
            normalized_title = re.sub(r"[：:].*$", "", title).strip()
            is_internal_heading = (
                normalized_title in INTERNAL_SECTION_HEADINGS
                or "联动建议" in normalized_title
                or "联动出口" in normalized_title
                or normalized_title.startswith("L9 触发建议")
            )
            if is_internal_heading:
                skip_level = level
                continue
        if skip_level is not None:
            continue
        kept.append(line)
    return "\n".join(kept).rstrip() + "\n"


def sanitize_public_text(content: str) -> str:
    content = re.sub(r"\[([^\]]+)\]\((?:\.\./)*status/[^)]+\)", r"\1", content)
    content = re.sub(r"\[([^\]]+)\]\((?:\.\./)*系统状态/[^)]+\)", r"\1", content)
    content = re.sub(r"\[([^\]]+)\]\((?:\.\./)*学科网/教辅出版威胁地图-2026-07\.md\)", r"\1", content)
    content = re.sub(r"\[([^\]]+)\]\((?:\.\./)*理想众望竞争分析_V3_20260616\.docx\)", r"\1", content)
    content = re.sub(r"\[((?:\.\./)*政策分析/解读/)\]", "[政策解读]", content)
    content = content.replace("../../学科网/教辅出版威胁地图-2026-07.md", "教辅出版威胁地图-2026-07")
    content = content.replace("../../../理想众望竞争分析_V3_20260616.docx", "理想众望竞争分析_V3_20260616.docx")
    lines = []
    skip_phrases = [
        "联动待办池",
        "联动建议",
        "LNK-",
        "按 L9 规则判断是否触发应对建议产出",
        "按 L9 规则判断是否触发",
    ]
    for line in content.splitlines():
        if any(phrase in line for phrase in skip_phrases):
            continue
        line = line.replace("行业分析/应对建议", "行业分析")
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def write_markdown(src: Path, dst: Path, **front_matter):
    content = src.read_text(encoding="utf-8")
    content = rewrite_image_refs(content)
    content = strip_internal_sections(content)
    content = sanitize_public_text(content)
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


def add_intro_after_title(dst: Path, intro: str):
    content = dst.read_text(encoding="utf-8")
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            lines[index + 1:index + 1] = ["", intro]
            dst.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            return
    dst.write_text(f"{intro}\n\n{content}", encoding="utf-8")


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
    index_dst = dst_dir / "index.md"
    write_markdown(VAULT_ROOT / "行业分析" / "INDEX.md", index_dst, page_type="industry_index", tags=["行业分析"])
    add_intro_after_title(index_dst, "> 趋势判断：风向往哪吹。聚合 AI+教育行业日情报、关键信号和对学科网的影响分析。")
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
    index_dst = dst_dir / "index.md"
    write_markdown(VAULT_ROOT / "政策分析" / "policy_timeline.md", index_dst, page_type="policy_timeline", tags=["政策分析"])
    add_intro_after_title(index_dst, "> 合规与机会：政策风怎么吹。跟踪教育政策、AI 监管与区域政策变化，提炼机会和风险。")
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
    index_dst = dst_dir / "index.md"
    write_markdown(VAULT_ROOT / "市场监测" / "INDEX.md", index_dst, page_type="market_index", tags=["市场监测"])
    add_intro_after_title(index_dst, "> 资金流向：钱往哪里流。跟踪招投标、采购与区域市场信号，用于判断机会窗口。")
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
    monitor_src = MONITOR_ROOT
    monitor_dst = DOCS_ROOT / "monitor"
    monitor_dst.mkdir(parents=True, exist_ok=True)
    dated_logs = [src for src in monitor_src.glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}-", src.stem)]
    log_files = sort_markdown_by_date(dated_logs)
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
        (monitor_dst / "index.md").write_text("# 竞品周情报\n\n> 暂无竞品周情报。\n", encoding="utf-8")
    return [f.stem for f in log_files]


def build_competitor_index(tiers: dict, analysis_map: dict) -> str:
    lines = [
        "# 竞争分析 · 竞品库",
        "",
        "> 竞品洞察：看清谁在威胁我们、谁在改变赛道。Tier 1/2 进入持续跟踪，观察池用于捕捉潜在变量。",
        "",
        "> 按新版战略情报系统分层展示。Tier 1 执行完整9层分析，Tier 2 执行 L1-L5，Tier 3 进入观察池。",
        "",
        "## 快速入口",
        "",
        "- [深度分析索引](analyses/index.md)",
        "- [竞品监测日志](../monitor/index.md)",
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
            analysis_key = canonical_competitor_name(item["name"])
            if analysis_key in analysis_map and analysis_map[analysis_key]:
                latest_file = analysis_map[analysis_key][-1]
                latest_label = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", latest)
                latest = f"[{latest_label}](./{item['slug']}/analyses/{latest_file})"
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


def build_analysis_index(analysis_entries: list[dict]) -> str:
    lines = [
        "---",
        "page_type: analysis_index",
        "tags:",
        "  - 竞争分析",
        "  - 深度分析",
        "---",
        "# 竞争分析 · 深度分析索引",
        "",
        "> 汇总所有竞品深度分析，按时间倒序排列。用于快速查找专题分析，不需要先进入具体竞品档案。",
        "",
        "| 日期 | 竞品 | 分析主题 | 层级 |",
        "|---|---|---|---|",
    ]
    if not analysis_entries:
        lines.append("| — | — | 暂无深度分析 | — |")
    for entry in sorted(analysis_entries, key=lambda item: (item["date"], item["competitor"], item["title"]), reverse=True):
        lines.append(
            f"| {entry['date']} | [{entry['competitor']}](../{entry['slug']}/index.md) | "
            f"[{entry['title']}](../{entry['slug']}/analyses/{entry['filename']}) | {entry['tier']} |"
        )
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

    tier_by_name = {}
    for tier, items in tiers.items():
        for item in items:
            tier_by_name[item["name"]] = tier
            tier_by_name[canonical_competitor_name(item["name"])] = tier
    analysis_entries = []
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
            content = sanitize_public_text(strip_internal_sections(normalize_links(rewrite_image_refs(content), dst)))
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
                content = sanitize_public_text(strip_internal_sections(normalize_links(rewrite_image_refs(content), dst)))
                back_link = f"[:octicons-arrow-left-24: 返回 {cn_name} 档案](../index.md)"
                content = inject_front_matter(content, page_type="analysis", competitor_name=cn_name, tier=tier, tags=["深度分析", cn_name, tier])
                content = insert_after_front_matter(content, back_link)
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(content, encoding="utf-8")
                date_match = re.match(r"(\d{4}-\d{2}-\d{2})-", src.stem)
                analysis_entries.append({
                    "date": date_match.group(1) if date_match else "未标注",
                    "competitor": cn_name,
                    "slug": slug,
                    "title": src.stem,
                    "filename": src.name,
                    "tier": tier,
                })

        releases_src = item / "发版追踪"
        if releases_src.exists():
            for src in sorted(releases_src.glob("*.md")):
                content = src.read_text(encoding="utf-8")
                dst = comp_dir / "releases" / src.name
                content = sanitize_public_text(strip_internal_sections(normalize_links(rewrite_image_refs(content), dst)))
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
    analyses_index = competitors_dir / "analyses" / "index.md"
    analyses_index.parent.mkdir(parents=True, exist_ok=True)
    analyses_index.write_text(build_analysis_index(analysis_entries), encoding="utf-8")
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


def copy_ai_briefings():
    src_dir = AI_BRIEFING_ROOT / "briefings"
    dst_dir = DOCS_ROOT / "ai-briefings"
    dst_dir.mkdir(parents=True, exist_ok=True)

    files = sort_markdown_by_date(list(src_dir.glob("*.md"))) if src_dir.exists() else []
    nav = []
    for src in files:
        report_type = "周末汇总" if "周末汇总" in src.stem else "每日简报"
        write_markdown(src, dst_dir / src.name, page_type="ai_briefing", tags=["AI简报", report_type])
        nav.append((src.stem, f"ai-briefings/{src.name}", report_type))

    latest_title = "暂无"
    latest_path = "ai-briefings/index.md"
    if files:
        latest = files[0]
        latest_title = latest.stem
        latest_path = f"ai-briefings/{latest.name}"
        latest_content = (dst_dir / latest.name).read_text(encoding="utf-8")
        (dst_dir / "latest.md").write_text(latest_content, encoding="utf-8")

    index_lines = [
        "---",
        "page_type: ai_briefing_index",
        "tags:",
        "  - AI简报",
        "---",
        "# AI 简报归档",
        "",
        "> AI 行业动态雷达：跟踪大模型、AI 产品、研究前沿与产业变化，帮助同事快速把握外部技术风向。",
        "",
        "> 汇总 AI 信息聚合项目的每日简报与周末汇总。这里只展示成品简报，不展示信源配置、抓取日志和推送维护材料。",
        "",
        f"最新简报：[最新简报](latest.md)（{latest_title}）",
        "",
        "| 日期 | 类型 | 简报 |",
        "|---|---|---|",
    ]
    if not nav:
        index_lines.append("| — | — | 暂无简报 |")
    for title, path, report_type in nav:
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})-", title)
        date = date_match.group(1) if date_match else "未标注"
        filename = Path(path).name
        index_lines.append(f"| {date} | {report_type} | [{title}]({filename}) |")
    (dst_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    return {
        "items": nav,
        "latest_title": latest_title,
        "latest_path": latest_path,
    }


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


TAG_META = {
    "industry": ("行业", "home-row--industry", "home-feed-tag--industry"),
    "monitor": ("竞品", "home-row--competitor", "home-feed-tag--competitor"),
    "policy": ("政策", "home-row--policy", "home-feed-tag--policy"),
    "market": ("市场", "home-row--market", "home-feed-tag--market"),
    "ai": ("AI", "home-row--ai", "home-feed-tag--ai"),
    "competitor": ("竞品", "home-row--competitor", "home-feed-tag--competitor"),
    "action": ("行动", "home-row--action", "home-feed-tag--action"),
}


def strip_markdown_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`#>]+", "", text)
    return html.escape(text.strip())


def first_date(text: str, fallback: str = "0000-00-00") -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", text or "")
    if match:
        return match.group(0)
    compact = re.search(r"(20\d{2})(0[1-9]|1[0-2])", text or "")
    if compact:
        return f"{compact.group(1)}-{compact.group(2)}-01"
    return fallback


def date_value(text: str) -> date | None:
    value = first_date(text)
    if value == "0000-00-00":
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def source_path_for_site_path(path: str) -> Path | None:
    if path.startswith("industry/日情报/"):
        return VAULT_ROOT / "行业分析" / "日情报" / Path(path).name
    if path.startswith("policy/解读/"):
        return VAULT_ROOT / "政策分析" / "解读" / Path(path).name
    if path.startswith("market/周报/"):
        return VAULT_ROOT / "市场监测" / "周报" / Path(path).name
    if path.startswith("ai-briefings/"):
        return AI_BRIEFING_ROOT / "briefings" / Path(path).name
    if path.startswith("monitor/"):
        return MONITOR_ROOT / Path(path).name
    return None


def monitor_source_path(name: str) -> Path:
    return MONITOR_ROOT / f"{name}.md"


def first_meaningful_line(path: Path | None, fallback: str) -> str:
    if path is None or not path.exists():
        return fallback
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("#") and ">" in line:
            line = line.split(">", 1)[1].strip()
        if not line or line.startswith(("#", "---", "page_type:", "tags:", "- ", "  - ")):
            continue
        line = re.sub(r"^>\s*", "", line).strip()
        if line:
            return line
    return fallback


def compact_focus_text(text: str, limit: int = 34) -> str:
    text = re.sub(r"\s+", " ", strip_markdown_inline(text))
    text = re.sub(r"^本期覆盖\s*\d{4}-\d{2}-\d{2}（[^）]*）[。，；;]?", "", text)
    text = re.sub(r"^今日主线由", "", text)
    text = re.sub(r"^本期主线由", "", text)
    text = re.sub(r"^扫描对象[：:]\s*", "", text)
    text = text.strip(" ：:，,。；;")
    if len(text) <= limit:
        return text
    return text[:limit].rstrip(" ，,。；;") + "..."


def focus_topic_title(kind: str, source_title: str, source_line: str) -> str:
    plain_title = strip_markdown_inline(source_title)
    plain_line = strip_markdown_inline(source_line)
    quoted = re.findall(r"[「“](.+?)[」”]", plain_line)
    if quoted:
        return compact_focus_text("与".join(quoted[:2]), 28)
    if kind == "industry" and "主线为" in plain_line:
        if "WAIC" in plain_line and "视源股份" in plain_line:
            return "WAIC 教育 AI 与希沃母公司业绩信号"
        topic = plain_line.split("主线为", 1)[1]
        topic = re.split(r"[。；;]", topic, maxsplit=1)[0]
        return compact_focus_text(topic, 28)
    if kind == "industry" and "合规信号" in plain_line:
        return "AI 拟人化互动合规窗口"
    if kind == "industry" and "通用大模型进展" in plain_line:
        return "通用大模型进展与竞品信号澄清"
    if kind == "ai" and "两条叙事" in plain_line:
        topic = plain_line.split("两条叙事", 1)[0]
        return compact_focus_text(topic, 28)
    if kind == "ai" and "安全与信任" in plain_line:
        return "大模型安全与身份验证压力"
    if kind == "competitor":
        return compact_focus_text(plain_line, 28)
    if kind == "market":
        if "真实数据周报" in plain_title:
            return "招投标真实数据与市场线索"
        if "合并周报" in plain_title:
            return "近 6 周市场监测补录"
        return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", plain_title)
    if kind == "policy":
        return re.sub(r"^\d{4}-\d{2}-", "", plain_title)
    if kind == "action":
        return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", plain_title)
    fallback_title = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", plain_title)
    if fallback_title in {"情报简报", "AI每日简报", "监测简报"}:
        return compact_focus_text(plain_line, 28)
    return fallback_title


def focus_importance(kind: str, source_title: str, source_desc: str, topic_title: str) -> int:
    text = f"{source_title} {source_desc} {topic_title}"
    score = {
        "competitor": 45,
        "policy": 40,
        "market": 35,
        "industry": 34,
        "ai": 30,
        "action": 28,
    }.get(kind, 20)
    for keyword, weight in [
        ("战略", 18),
        ("重要", 16),
        ("风险", 14),
        ("威胁", 14),
        ("合规", 12),
        ("政策", 12),
        ("招投标", 12),
        ("采购", 10),
        ("竞品", 10),
        ("WAIC", 10),
        ("希沃", 10),
        ("视源股份", 10),
        ("模型", 8),
        ("Agent", 8),
        ("AI", 6),
    ]:
        if keyword in text:
            score += weight
    return score


def build_feed_item(kind: str, title: str, desc: str, href: str, css_class: str = "home-feed-item") -> str:
    label, row_class, tag_class = TAG_META[kind]
    return f"""<a class="{css_class} {row_class}" href="{href}">
  <span class="home-feed-tag {tag_class}">{label}</span>
  <span class="home-feed-body"><strong>{strip_markdown_inline(title)}</strong><small>{strip_markdown_inline(desc)}</small></span>
  <span class="home-feed-arrow">→</span>
</a>"""


def latest_action_output(action_nav: dict) -> tuple[str, str, str]:
    candidates = []
    for audience, items in action_nav.items():
        for title, path in items:
            candidates.append((first_date(title), title, path, audience))
    if not candidates:
        return ("应对建议", "actions/index.md", "查看按角色分发的行动材料")
    _, title, path, audience = max(candidates, key=lambda item: (item[0], item[1]))
    return (title, path, f"{audience} · 最新可用材料")


def monitor_focus_summary(latest_monitor: str, monitor_path: Path) -> str:
    if not monitor_path.exists():
        return "查看最新竞品监测变化"
    text = monitor_path.read_text(encoding="utf-8")
    match = re.search(r"\*\*有变化的竞品[^：:]*[：:]\*\*\s*\n\n?-\s*(.+)", text)
    if match:
        return match.group(1).strip()
    match = re.search(r"本周监测发现\*\*(.+?)\*\*", text)
    if match:
        return match.group(1).strip()
    return f"查看 {latest_monitor}，跟踪 Tier 1 变化"


def monitor_overview_line(latest_monitor: str) -> str:
    monitor_path = monitor_source_path(latest_monitor)
    if not monitor_path.exists():
        return f"最新监测：{strip_markdown_inline(latest_monitor)}"
    text = monitor_path.read_text(encoding="utf-8")
    execution = re.search(r"\*\*执行日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})", text)
    period = re.search(r"\*\*监测周期\*\*[：:]\s*([^\n]+)", text)
    execution_date = execution.group(1) if execution else first_date(latest_monitor, latest_monitor)
    if period:
        clean_period = re.sub(r"（[^）]*）", "", period.group(1)).strip()
        clean_period = re.sub(r"\s*至\s*", " 至 ", clean_period)
        return f"最新监测：{execution_date} · 覆盖 {strip_markdown_inline(clean_period)}"
    return f"最新监测：{execution_date}"


def clean_overview_title(title: str) -> str:
    title = strip_markdown_inline(title)
    title = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", title)
    return title


def home_overview_line(latest_industry: str, latest_monitor: str, latest_market_title: str,
                       latest_policy: str, latest_ai: str) -> str:
    latest_dates = [
        date for date in [
            first_date(latest_industry),
            first_date(latest_monitor),
            first_date(latest_market_title),
            first_date(latest_ai),
            first_date(latest_policy),
        ]
        if date != "0000-00-00"
    ]
    updated = max(latest_dates) if latest_dates else datetime.now().strftime("%Y-%m-%d")
    module_dates = [
        f"行业 {first_date(latest_industry, '—')}",
        f"竞品 {first_date(latest_monitor, '—')}",
        f"市场 {first_date(latest_market_title, '—')}",
        f"AI {first_date(latest_ai, '—')}",
    ]
    if latest_policy and latest_policy != "政策时间轴":
        module_dates.append(f"政策 {first_date(latest_policy, '2026Q1Q2')}")
    return f"全站更新：{updated} · 行业 / 竞品 / 市场 / AI / 政策已同步（" + "，".join(module_dates) + "）"


def build_focus_items(industry_nav: list, policy_nav: list, market_nav: list, action_nav: dict,
                      monitor_logs: list, ai_nav: dict) -> str:
    candidates = []

    def add_item(kind: str, source_title: str, source_desc: str, path: str):
        item_date = date_value(f"{source_title} {path}")
        if item_date is None:
            return
        topic_title = focus_topic_title(kind, source_title, source_desc)
        desc = f"来源：{strip_markdown_inline(source_title)}"
        candidates.append({
            "date": item_date,
            "kind": kind,
            "topic": topic_title,
            "source": source_title,
            "desc": desc,
            "html": build_feed_item(kind, topic_title, desc, public_href(path), "focus-item"),
            "score": focus_importance(kind, source_title, source_desc, topic_title),
        })

    for _subdir, title, path in industry_nav:
        add_item("industry", title, first_meaningful_line(source_path_for_site_path(path), "查看行业情报，关注外部趋势变化"), path)

    for title, path, _report_type in ai_nav.get("items", []):
        add_item("ai", title, first_meaningful_line(source_path_for_site_path(path), "查看 AI 每日简报，关注外部技术动态"), path)

    for title, path in policy_nav:
        add_item("policy", title, first_meaningful_line(source_path_for_site_path(path), "查看政策解读，关注合规边界与机会窗口"), path)

    for log_name in monitor_logs:
        monitor_path = monitor_source_path(log_name)
        add_item("competitor", log_name, monitor_focus_summary(log_name, monitor_path), f"monitor/{log_name}.md")

    for group, title, path in market_nav:
        if group == "周报":
            add_item("market", title, "查看市场监测，关注区域采购与资金流向变化", path)

    for audience, outputs in action_nav.items():
        for title, path in outputs:
            add_item("action", title, f"{audience} · 可用行动材料", path)

    if not candidates:
        return ""

    anchor = max(item["date"] for item in candidates)
    week_start = anchor - timedelta(days=anchor.weekday())
    week_end = week_start + timedelta(days=6)
    weekly_items = [item for item in candidates if week_start <= item["date"] <= week_end]
    if len(weekly_items) < 5:
        weekly_items = candidates

    unique_items = []
    seen_topics = set()
    kind_counts = {}
    for item in sorted(
        weekly_items,
        key=lambda row: (row["score"] + (row["date"] - week_start).days * 8, row["date"], row["topic"]),
        reverse=True,
    ):
        normalized_topic = re.sub(r"\W+", "", item["topic"])
        if normalized_topic in seen_topics:
            continue
        if kind_counts.get(item["kind"], 0) >= 2:
            continue
        seen_topics.add(normalized_topic)
        kind_counts[item["kind"]] = kind_counts.get(item["kind"], 0) + 1
        unique_items.append(item)
        if len(unique_items) == 5:
            break

    return "\n\n".join(item["html"] for item in unique_items)


def build_latest_items(latest_industry: str, latest_industry_href: str, latest_monitor: str,
                       latest_policy: str, latest_policy_href: str, latest_market_title: str,
                       latest_market_href: str, latest_ai: str, latest_ai_href: str) -> str:
    items = [
        (first_date(f"{latest_industry} {latest_industry_href}"), build_feed_item("industry", latest_industry, "行业情报 · 含对学科网的影响分析", latest_industry_href)),
        (first_date(latest_monitor), build_feed_item("monitor", latest_monitor, "竞争分析 / 竞品周情报", "monitor/")),
        (first_date(f"{latest_policy} {latest_policy_href}"), build_feed_item("policy", latest_policy, "政策解读 · 机会 / 风险已提炼", latest_policy_href)),
        (first_date(f"{latest_market_title} {latest_market_href}"), build_feed_item("market", latest_market_title, "市场监测 · 招投标线索", latest_market_href)),
        (first_date(f"{latest_ai} {latest_ai_href}"), build_feed_item("ai", latest_ai, "外部技术动态 · AI每日简报", latest_ai_href)),
    ]
    items.sort(key=lambda item: item[0], reverse=True)
    return "\n\n".join(item_html for _date, item_html in items)


def competitor_aliases(name: str) -> list[str]:
    aliases = [name, canonical_competitor_name(name)]
    aliases.extend(name.replace("·", "").split("-"))
    if "作业帮" in name:
        aliases.extend(["作业帮", "作业帮教师版"])
    if "金太阳" in name:
        aliases.extend(["金太阳", "中课云"])
    if "猿辅导" in name:
        aliases.extend(["飞象老师", "猿辅导"])
    if "好未来" in name:
        aliases.extend(["九章爱学", "好未来"])
    return [alias for alias in dict.fromkeys(alias.strip() for alias in aliases) if alias]


def competitor_monitor_score(name: str, monitor_text: str) -> tuple[int, str]:
    score = 0
    signal = ""
    for alias in competitor_aliases(name):
        if alias and alias in monitor_text:
            score = max(score, 10)
            section = re.search(rf"###\s+{re.escape(alias)}[^\n]*\n(?P<body>.*?)(?=\n---\n|\n###\s+|\n##\s+|\Z)", monitor_text, re.S)
            if section:
                body = section.group("body")
                if "🚨" in body or "战略级" in body:
                    score = max(score, 100)
                    signal = "战略级信号"
                elif "⚠️" in body or "重要" in body or "建议深度分析" in body:
                    score = max(score, 90)
                    signal = "重要信号"
                elif "一般" in body or "无显著变化" in body:
                    score = max(score, 30)
                    signal = "常规监测"
            elif re.search(rf"{re.escape(alias)}.*?(战略级|重要|建议深度分析|⚠️|🚨)", monitor_text):
                score = max(score, 90)
                signal = "重要信号"
            break
    return score, signal


def recent_monitor_texts(monitor_logs: list[str], window_days: int = 30) -> list[tuple[date, str, str]]:
    dated_logs = []
    for log_name in monitor_logs:
        log_date = date_value(log_name)
        path = monitor_source_path(log_name)
        if log_date and path.exists():
            dated_logs.append((log_date, log_name, path.read_text(encoding="utf-8")))
    if not dated_logs:
        return []
    anchor = max(log_date for log_date, _name, _text in dated_logs)
    cutoff = anchor - timedelta(days=window_days)
    return [(log_date, name, text) for log_date, name, text in dated_logs if cutoff <= log_date <= anchor]


def build_threat_items(tiers: dict, monitor_logs: list[str]) -> tuple[str, int, str]:
    recent_logs = recent_monitor_texts(monitor_logs)
    anchor = max((log_date for log_date, _name, _text in recent_logs), default=None)
    ranked = []
    for index, item in enumerate(tiers.get("Tier 1", [])):
        best_score = 0
        best_signal = ""
        best_date = None
        for log_date, _log_name, monitor_text in recent_logs:
            score, signal = competitor_monitor_score(item["name"], monitor_text)
            if score > best_score or (score == best_score and (best_date is None or log_date > best_date)):
                best_score = score
                best_signal = signal
                best_date = log_date
        updated = first_date(item.get("updated", ""), "0000-00-00")
        latest = strip_markdown_inline(item.get("latest", ""))
        desc = f"{item['track']} · {item['company']} · {latest}"
        recency_bonus = (best_date - (anchor - timedelta(days=30))).days if best_date and anchor else 0
        ranked.append((best_score, recency_bonus, updated, -index, item, best_signal, desc))
    ranked.sort(reverse=True, key=lambda row: (row[0], row[1], row[2], row[3]))
    selected = ranked[:5]
    high_count = sum(1 for score, *_ in ranked if score >= 90)
    high_names = [row[4]["name"] for row in ranked if row[0] >= 90]
    top_names = " / ".join((high_names or [row[4]["name"] for row in selected[:3]])) if selected else "暂无"
    rows = []
    for index, (score, _recency, _updated, _order, item, signal, desc) in enumerate(selected, start=1):
        level_class = "threat-level--high" if score >= 90 else "threat-level--medium"
        row_class = "home-row--danger" if score >= 90 else "home-row--warning"
        level = "高 ↑" if score >= 90 else "中 →"
        desc_text = f"{signal} · {desc}" if signal else desc
        rows.append(f"""<a class="threat-row {row_class}" href="competitors/{item['slug']}/">
  <span class="threat-avatar threat-avatar--tone-{index}">{html.escape(item['name'][:1])}</span>
  <span class="threat-body"><strong>{html.escape(item['name'])}</strong><small>{desc_text}</small></span>
  <span class="threat-level {level_class}">{level}</span>
</a>""")
    return "\n\n".join(rows), high_count, top_names


def generate_home(tiers: dict, industry_nav: list, policy_nav: list, market_nav: list, action_nav: dict, monitor_logs: list, ai_nav: dict):
    tier1 = len(tiers.get("Tier 1", []))
    tier2 = len(tiers.get("Tier 2", []))
    action_count = sum(len(items) for items in action_nav.values())
    competitor_total = tier1 + tier2 + 150
    policy_count = len(policy_nav)
    executive_count = len(action_nav.get("决策层简报", []))
    battlecard_count = len(action_nav.get("Battlecard", []))
    sales_count = len(action_nav.get("销售话术卡", []))
    teaching_count = len(action_nav.get("教研参考卡", []))
    operation_count = len(action_nav.get("运营参考卡", []))
    latest_industry = industry_nav[0][1] if industry_nav else "暂无"
    latest_industry_path = industry_nav[0][2] if industry_nav else "industry/index.md"
    latest_policy = policy_nav[0][0] if policy_nav else "政策时间轴"
    latest_policy_path = policy_nav[0][1] if policy_nav else "policy/index.md"
    latest_monitor = monitor_logs[0] if monitor_logs else "暂无"
    market_weeklies = [item for item in market_nav if item[0] == "周报"]
    latest_market = max(market_weeklies, key=lambda item: first_date(f"{item[1]} {item[2]}")) if market_weeklies else None
    latest_market_title = latest_market[1] if latest_market else "市场监测总览"
    latest_market_path = latest_market[2] if latest_market else "market/index.md"
    latest_ai = ai_nav.get("latest_title", "暂无")
    latest_ai_path = ai_nav.get("latest_path", "ai-briefings/latest.md")
    latest_industry_href = public_href(latest_industry_path)
    latest_policy_href = public_href(latest_policy_path)
    latest_market_href = public_href(latest_market_path)
    latest_ai_href = public_href(latest_ai_path)
    overview_line = home_overview_line(
        latest_industry,
        latest_monitor,
        latest_market_title,
        latest_policy,
        latest_ai,
    )
    latest_items = build_latest_items(
        latest_industry,
        latest_industry_href,
        latest_monitor,
        latest_policy,
        latest_policy_href,
        latest_market_title,
        latest_market_href,
        latest_ai,
        latest_ai_href,
    )
    focus_items = build_focus_items(
        industry_nav,
        policy_nav,
        market_nav,
        action_nav,
        monitor_logs,
        ai_nav,
    )
    threat_items, high_threat_count, high_threat_names = build_threat_items(tiers, monitor_logs)
    content = f"""---
hide:
  - navigation
  - toc
---

<div class="home-dashboard" markdown>

# 情报总览

> {overview_line}

<div class="home-metrics" markdown>

[:material-database-search: __竞品库__<br><span class="home-metric-number">{competitor_total}</span> <span class="home-muted">家</span><br><span class="home-muted">Tier 1 · {tier1} / Tier 2 · {tier2} / 观察池 · 150+</span>](competitors/index.md)

[:material-alert-decagram: __高威胁竞品__<br><span class="home-metric-number home-danger">{high_threat_count}</span> <span class="home-danger-label">个重点</span><br><span class="home-muted">{high_threat_names}</span>](monitor/index.md)

[:material-target-account: __应对建议（L9）__<br><span class="home-metric-number">{action_count}</span> <span class="home-muted">份 · 五线输出</span><br><span class="home-muted">简报 {executive_count} · Battlecard {battlecard_count} · 话术 {sales_count} · 教研 {teaching_count} · 运营 {operation_count}</span>](actions/index.md)

[:material-file-document-check: __政策解读__<br><span class="home-metric-number">{policy_count}</span> <span class="home-muted">份</span><br><span class="home-muted">最新：{latest_policy}</span>](policy/index.md)

</div>

<div class="home-workbench home-workbench--threat" markdown>

<div class="home-side-stack" markdown>
<section class="home-panel latest-output" markdown>
## <span class="section-kicker section-kicker--new">NEW</span> 最新情报

{latest_items}
</section>
</div>

<div class="home-side-stack" markdown>
<section class="home-panel focus-panel" markdown>
## <span class="section-kicker section-kicker--focus">重点</span> 本周重点关注

<div class="focus-list">

{focus_items}

</div>
</section>
</div>

<section class="home-panel threat-panel" markdown>
<div class="home-panel-header" markdown>
## <span class="section-kicker section-kicker--threat">威胁</span> 重点竞品威胁看板

[查看全部 →](competitors/index.md)
</div>

{threat_items}

</section>

</div>

<section class="home-panel role-access role-access--wide" markdown>
## 按角色取用

<div class="role-grid">

<a class="role-card role-card--executive" href="actions/executive-briefs/">
  <strong>决策层</strong>
  <span>战略简报 2026Q2 · {executive_count} 份</span>
</a>

<a class="role-card role-card--product" href="actions/battlecards/">
  <strong>产品线</strong>
  <span>Battlecard 202606 · {battlecard_count} 份</span>
</a>

<a class="role-card role-card--sales" href="actions/sales-cards/">
  <strong>市场 / 销售</strong>
  <span>销售话术卡 · {sales_count} 份</span>
</a>

<a class="role-card role-card--teaching" href="actions/teaching-cards/">
  <strong>教研</strong>
  <span>教研参考卡 · {teaching_count} 份</span>
</a>

<a class="role-card role-card--operation" href="actions/operation-cards/">
  <strong>运营</strong>
  <span>运营参考卡 · {operation_count} 份</span>
</a>

</div>
</section>

</div>
"""
    (DOCS_ROOT / "index.md").write_text(content, encoding="utf-8")


def nav_item(title: str, path: str, indent: int = 2) -> str:
    return f"{' ' * indent}- {title}: {path}\n"


def public_href(path: str) -> str:
    """将 MkDocs 源文件路径转成 raw HTML href 可直接访问的站点路径。"""
    if path.endswith("index.md"):
        return path[:-len("index.md")]
    if path.endswith(".md"):
        return f"{path[:-3]}/"
    return path


def generate_mkdocs_yml(tiers: dict, industry_nav: list, policy_nav: list, market_nav: list, action_nav: dict, monitor_logs: list, ai_nav: dict):
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

    nav += "  - 竞品分析:\n    - 竞品库总览: competitors/index.md\n    - 深度分析: competitors/analyses/index.md\n    - 竞品监测:\n      - 最新监测: monitor/index.md\n"
    for log_name in monitor_logs:
        nav += nav_item(log_name, f"monitor/{log_name}.md", 6)
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

    nav += "  - AI简报:\n    - 最新简报: ai-briefings/latest.md\n    - 简报归档: ai-briefings/index.md\n"
    for title, path, _report_type in ai_nav.get("items", []):
        nav += nav_item(title, path, 4)

    (WEBSITE_ROOT / "mkdocs.yml").write_text(nav, encoding="utf-8")


def main():
    print("=" * 50)
    print("学科网战略情报系统 → MkDocs 网站构建")
    print("=" * 50)
    clean_docs()
    tiers = parse_competitor_index()
    copy_extra_assets()
    copy_framework()
    industry_nav = copy_industry_analysis()
    policy_nav = copy_policy_analysis()
    market_nav = copy_market_monitoring()
    copy_competitors(tiers)
    monitor_logs = copy_monitor_logs()
    action_nav = copy_response_outputs()
    ai_nav = copy_ai_briefings()
    generate_feedback_page()
    generate_home(tiers, industry_nav, policy_nav, market_nav, action_nav, monitor_logs, ai_nav)
    generate_mkdocs_yml(tiers, industry_nav, policy_nav, market_nav, action_nav, monitor_logs, ai_nav)
    print("\n✅ 构建完成！")
    print(f"   输出目录: {DOCS_ROOT}")
    print(f"   下一步: cd {WEBSITE_ROOT} && mkdocs serve")


if __name__ == "__main__":
    main()
