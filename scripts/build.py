#!/usr/bin/env python3
"""
构建脚本：将 Obsidian 竞品分析工作台转换为 MkDocs 网站源文件。

功能：
1. 读取 Obsidian 源文件
2. 按 slug 映射规则复制到 website/docs/ 目录
3. 重写图片引用路径（Obsidian 路径 → MkDocs 根相对路径）
4. 注入 YAML front matter（标签、日期等）
5. 生成 mkdocs.yml 导航配置
"""

import shutil
import re
from pathlib import Path
from datetime import datetime

# ── 配置 ──────────────────────────────────────────────────────────────

# Obsidian 知识库中的竞品分析工作台根目录
VAULT_ROOT = Path("/Users/wzrong/Documents/Claude/Projects/竞品分析工作台")

# MkDocs 网站项目根目录（本脚本所在目录的上级）
WEBSITE_ROOT = Path(__file__).parent.parent
DOCS_ROOT = WEBSITE_ROOT / "docs"

# 竞品名 → URL slug 映射
SLUG_MAP = {
    "希沃": "seewo",
    "好未来-九章爱学": "tal-jiuzhang",
    "猿辅导-飞象老师": "yuanfudao-feixiang",
    "智学网": "zhixue",
    "国家中小学智慧教育平台": "smartedu",
    "百度文库教育专区": "baidu-wenku-edu",
    "作业帮教师版": "zuoyebang-teacher",
    "猿题库": "yuantiku",
    "洋葱学园": "yangcong",
    "21世纪教育网": "21cnjy",
    "菁优网": "jyeoo",
    "橡皮网": "xiangpi",
    "教习网": "51jiaoxi",
    "正确云": "zhengqueyun",
    "dokie": "dokie",
    "小盒科技": "xiaohe",
    "一起教育科技": "17zuoye",
    "翼鸥ClassIn": "classin",
    "鸿合科技": "hitevision",
    "高考网": "gaokao",
    "豆神教育": "doushen",
    "纳米盒": "namibox",
}


def slugify(name: str) -> str:
    """将竞品中文名转换为 URL slug。"""
    return SLUG_MAP.get(name, name.lower().replace(" ", "-"))


def parse_relevance_from_index(index_text: str) -> dict:
    """
    从 INDEX.md 的表格中解析每个竞品的相关度。
    返回 {竞品名: 相关度}
    """
    relevance_map = {}

    # 直接竞品部分（🔴 和 🟡）
    direct_match = re.search(r'## 直接竞品.*?(?=## 间接竞品|$)', index_text, re.DOTALL)
    if direct_match:
        for line in direct_match.group(0).split('\n'):
            # 匹配表格数据行：| 竞品名 | 🔴/🟡 | ... |
            match = re.match(r'\| ([^|]+?) \| (🔴|🟡)', line)
            if match:
                name = match.group(1).strip()
                emoji = match.group(2)
                relevance_map[name] = "核心直接竞品" if emoji == "🔴" else "直接竞品"

    # 间接竞品部分（🟢）
    indirect_match = re.search(r'## 间接竞品.*?(?=## |$)', index_text, re.DOTALL)
    if indirect_match:
        for line in indirect_match.group(0).split('\n'):
            match = re.match(r'\| ([^|]+?) \| 🟢', line)
            if match:
                name = match.group(1).strip()
                relevance_map[name] = "间接竞品"

    return relevance_map


def rewrite_image_refs(content: str) -> str:
    """
    重写 Markdown 中的图片引用路径。

    Obsidian 格式：![alt](竞品库/{竞品名}/screenshots/xxx.png)
    MkDocs 格式：![alt](/assets/screenshots/{slug}/xxx.png)
    """
    def repl(match):
        alt_text = match.group(1)
        old_path = match.group(2)
        # old_path 示例：竞品库/希沃/screenshots/希沃-首页-20260518.png
        parts = old_path.split("/")
        if len(parts) >= 3 and parts[0] == "竞品库":
            cn_name = parts[1]
            slug = slugify(cn_name)
            # 跳过 screenshots/ 目录前缀，避免重复
            if len(parts) >= 4 and parts[2] == "screenshots":
                rest = "/".join(parts[3:])
            else:
                rest = "/".join(parts[2:])
            return f"![{alt_text}](/assets/screenshots/{slug}/{rest})"
        return match.group(0)

    pattern = r'!\[(.*?)\]\((竞品库/[^)]+)\)'
    return re.sub(pattern, repl, content)


def has_front_matter(content: str) -> bool:
    """检查 Markdown 是否已有 YAML front matter。"""
    return content.startswith("---")


def inject_front_matter(content: str, **fields) -> str:
    """在 Markdown 内容前注入 YAML front matter。"""
    if has_front_matter(content):
        return content

    lines = ["---"]
    for k, v in fields.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")

    return "\n".join(lines) + content


# ── 构建步骤 ──────────────────────────────────────────────────────────

def clean_docs():
    """清空并重建 docs/ 目录。"""
    old_docs = None
    if DOCS_ROOT.exists():
        old_docs = WEBSITE_ROOT / f".docs-old-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        DOCS_ROOT.rename(old_docs)
    DOCS_ROOT.mkdir(parents=True)
    (DOCS_ROOT / "assets" / "screenshots").mkdir(parents=True)
    (DOCS_ROOT / "stylesheets").mkdir()
    (DOCS_ROOT / "javascripts").mkdir()

    if old_docs is not None:
        shutil.rmtree(old_docs, ignore_errors=True)


def copy_framework():
    """复制分析框架和报告模板。"""
    # 分析框架
    src = VAULT_ROOT / "分析框架.md"
    dst_dir = DOCS_ROOT / "framework"
    dst_dir.mkdir()
    content = src.read_text(encoding="utf-8")
    content = rewrite_image_refs(content)
    content = inject_front_matter(content, page_type="framework", tags=["方法论"])
    (dst_dir / "index.md").write_text(content, encoding="utf-8")

    # 报告模板
    src = VAULT_ROOT / "报告模板.md"
    dst_dir = DOCS_ROOT / "report-templates"
    dst_dir.mkdir()
    content = src.read_text(encoding="utf-8")
    content = rewrite_image_refs(content)
    content = inject_front_matter(content, page_type="template", tags=["方法论", "模板"])
    (dst_dir / "index.md").write_text(content, encoding="utf-8")


def rewrite_index_table(content: str, relevance_map: dict, analysis_map: dict) -> str:
    """
    重写 INDEX.md 表格中的链接：
    - 竞品名 → 链接到档案页
    - 最新分析 → 链接到对应的分析文件（如果存在）
    """
    def repl_row(match):
        name = match.group(1).strip()
        relevance = match.group(2).strip()
        track = match.group(3).strip()
        company = match.group(4).strip()
        url = match.group(5).strip()
        latest_analysis = match.group(6).strip()
        last_update = match.group(7).strip()

        # 跳过表头行（"竞品名" 或纯横线/空格）
        if name in ("竞品名", "---") or re.match(r'^[\s\-|]+$', name):
            return match.group(0)

        slug = slugify(name)

        # 竞品名 → 链接到档案页
        name_link = f"[{name}](./{slug}/index.md)"

        # URL → 可点击链接（JS 会给外部链接加 target="_blank"）
        url_link = f"[{url}]({url})"

        # 最新分析 → 链接到对应的分析文件
        analysis_link = latest_analysis
        if name in analysis_map and analysis_map[name]:
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', latest_analysis)
            if date_match:
                date_str = date_match.group(1)
                for fname in analysis_map[name]:
                    if date_str in fname:
                        analysis_link = f"[{latest_analysis}](./{slug}/analyses/{fname})"
                        break

        return f"| {name_link} | {relevance} | {track} | {company} | {url_link} | {analysis_link} | {last_update} |"

    # 匹配表格数据行（7列）
    pattern = r'\| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|'
    return re.sub(pattern, repl_row, content)


def copy_competitors() -> dict:
    """
    复制所有竞品数据。
    返回分类信息：{"核心直接竞品": [...], "直接竞品": [...], "间接竞品": [...]}
    """
    lib_root = VAULT_ROOT / "竞品库"
    competitors_dir = DOCS_ROOT / "competitors"
    competitors_dir.mkdir()

    categories = {"核心直接竞品": [], "直接竞品": [], "间接竞品": []}

    # ── 第一阶段：收集所有信息 ──────────────────────────────────
    relevance_map = {}
    analysis_map = {}   # {竞品名: [分析文件名, ...]}

    index_src = lib_root / "INDEX.md"
    if index_src.exists():
        index_text = index_src.read_text(encoding="utf-8")
        relevance_map = parse_relevance_from_index(index_text)

    for item in sorted(lib_root.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue
        cn_name = item.name
        analyses_src = item / "analyses"
        if analyses_src.exists():
            analysis_map[cn_name] = [f.name for f in sorted(analyses_src.glob("*.md"))]
        else:
            analysis_map[cn_name] = []

    # ── 第二阶段：复制 INDEX.md（重写链接） ─────────────────────
    if index_src.exists():
        index_text = index_src.read_text(encoding="utf-8")
        index_text = rewrite_image_refs(index_text)
        index_text = rewrite_index_table(index_text, relevance_map, analysis_map)
        index_text = inject_front_matter(index_text, page_type="competitor_index", tags=["索引"])
        (competitors_dir / "index.md").write_text(index_text, encoding="utf-8")

    # ── 第三阶段：逐个复制竞品文件 ────────────────────────────
    for item in sorted(lib_root.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue

        cn_name = item.name
        slug = slugify(cn_name)
        comp_dir = competitors_dir / slug
        comp_dir.mkdir()

        relevance = relevance_map.get(cn_name, "间接竞品")
        categories[relevance].append((cn_name, slug))
        analysis_files = analysis_map.get(cn_name, [])

        # 复制 profile.md → index.md，底部追加深度分析链接
        profile_src = item / "profile.md"
        if profile_src.exists():
            content = profile_src.read_text(encoding="utf-8")
            content = rewrite_image_refs(content)

            if analysis_files:
                content += "\n\n---\n\n## 深度分析\n\n"
                for fname in analysis_files:
                    stem = Path(fname).stem
                    content += f"- [{stem}](analyses/{fname})\n"

            content = inject_front_matter(
                content,
                page_type="competitor_profile",
                competitor_name=cn_name,
                relevance=relevance,
                tags=["竞品档案", relevance],
            )
            (comp_dir / "index.md").write_text(content, encoding="utf-8")

        # 复制 analyses/
        if analysis_files:
            analyses_dst = comp_dir / "analyses"
            analyses_dst.mkdir()
            analyses_src = item / "analyses"
            for analysis in sorted(analyses_src.glob("*.md")):
                content = analysis.read_text(encoding="utf-8")
                content = rewrite_image_refs(content)
                date_match = re.match(r'(\d{4}-\d{2}-\d{2})-', analysis.stem)
                analysis_date = date_match.group(1) if date_match else None

                back_link = f"[:octicons-arrow-left-24: 返回 {cn_name} 档案](../index.md)"
                content = inject_front_matter(
                    content,
                    page_type="analysis",
                    competitor_name=cn_name,
                    analysis_date=analysis_date,
                    tags=["深度分析", cn_name, relevance],
                )
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        content = f"---{parts[1]}---\n\n{back_link}\n\n{parts[2].lstrip()}"
                else:
                    content = f"{back_link}\n\n{content}"

                (analyses_dst / analysis.name).write_text(content, encoding="utf-8")

        # 复制 screenshots/
        screenshots_src = item / "screenshots"
        if screenshots_src.exists():
            screenshots_dst = DOCS_ROOT / "assets" / "screenshots" / slug
            screenshots_dst.mkdir(parents=True, exist_ok=True)
            for img in screenshots_src.iterdir():
                if img.is_file():
                    shutil.copyfile(img, screenshots_dst / img.name)

    return categories


def copy_monitor_logs():
    """复制监测日志。"""
    monitor_src = VAULT_ROOT / "监测日志"
    monitor_dst = DOCS_ROOT / "monitor"
    monitor_dst.mkdir()

    # 生成监测日志索引页
    index_lines = ["# 监测日志", "", "> 每周竞品监测简报汇总，按时间倒序排列。", ""]

    log_files = sorted(monitor_src.glob("*.md"), reverse=True)
    for log_file in log_files:
        # 解析日期
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})-', log_file.stem)
        date_str = date_match.group(1) if date_match else log_file.stem

        content = log_file.read_text(encoding="utf-8")
        content = rewrite_image_refs(content)

        # 在顶部添加返回链接（移动端需要）
        back_link = "[:octicons-arrow-left-24: 返回监测日志](./index.md)"
        content = inject_front_matter(
            content,
            page_type="monitor_log",
            date=date_str,
            tags=["监测简报"],
        )
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                content = f"---{parts[1]}---\n\n{back_link}\n\n{parts[2].lstrip()}"
        else:
            content = f"{back_link}\n\n{content}"

        (monitor_dst / log_file.name).write_text(content, encoding="utf-8")

    # 生成监测日志索引页（列表包裹在特定 class 的 div 中，用于已访问链接变色）
    index_lines.append('')
    index_lines.append('<div class="monitor-log-list" markdown>')
    index_lines.append('')
    for log_file in log_files:
        index_lines.append(f"- [{log_file.stem}]({log_file.name})")
    index_lines.append('')
    index_lines.append('</div>')
    index_lines.append('')

    (monitor_dst / "index.md").write_text("\n".join(index_lines), encoding="utf-8")


def generate_index(categories: dict):
    """生成网站首页，分类数量动态计算。"""
    today = datetime.now().strftime("%Y-%m-%d")
    core_count = len(categories.get("核心直接竞品", []))
    direct_count = len(categories.get("直接竞品", []))
    indirect_count = len(categories.get("间接竞品", []))
    total_count = core_count + direct_count + indirect_count

    content = f"""---
hide:
  - navigation
  - toc
---

# 竞品分析知识库

<div class="grid cards" markdown>

-   :material-chart-box:{{ .lg .middle }} __分析框架__

    ---

    四维度竞品分析方法论

    [:octicons-arrow-right-24: 查看框架](framework/index.md)

-   :material-file-document-outline:{{ .lg .middle }} __报告模板__

    ---

    单竞品深度分析 & 多竞品对比模板

    [:octicons-arrow-right-24: 查看模板](report-templates/index.md)

-   :material-database:{{ .lg .middle }} __竞品库__

    ---

    {total_count} 家竞品完整档案与深度分析

    [:octicons-arrow-right-24: 浏览竞品](competitors/index.md)

-   :material-bell-ring:{{ .lg .middle }} __监测日志__

    ---

    每周竞品动态监测简报

    [:octicons-arrow-right-24: 查看日志](monitor/index.md)

</div>

## 竞品概览

| 类别 | 数量 | 说明 |
|------|------|------|
| 🔴 核心直接竞品 | {core_count} | 同一场景/预算/用户的直接竞争 |
| 🟡 直接竞品 | {direct_count} | 交叉竞争，切入角度不同 |
| 🟢 间接竞品 | {indirect_count} | 赛道相邻，值得跟踪 |

> 最后更新：{today}
"""
    (DOCS_ROOT / "index.md").write_text(content, encoding="utf-8")


def generate_mkdocs_yml(categories: dict):
    """根据实际竞品数据生成 mkdocs.yml 导航配置。"""
    nav = """site_name: 竞品分析知识库
site_description: 学科网竞品分析工作台 — 全量竞品档案、深度分析与监测追踪
site_author: 学科网产品团队

theme:
  name: material
  language: zh
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
      primary: indigo
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
  # git-revision-date-localized 插件在本地预览时可能因新文件未提交而报错
  # 如需显示页面最后更新时间，可取消下面注释
  # - git-revision-date-localized:
  #     type: date
  #     enable_creation_date: true
  #     fallback_to_build_date: true

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
  - pymdownx.betterem:
      smart_enable: all
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
  - 分析框架: framework/index.md
  - 报告模板: report-templates/index.md
  - 竞品库:
    - competitors/index.md
    - 核心直接竞品:
"""
    for cn_name, slug in sorted(categories["核心直接竞品"]):
        nav += f"      - {cn_name}: competitors/{slug}/index.md\n"

    nav += "    - 直接竞品:\n"
    for cn_name, slug in sorted(categories["直接竞品"]):
        nav += f"      - {cn_name}: competitors/{slug}/index.md\n"

    nav += "    - 间接竞品:\n"
    for cn_name, slug in sorted(categories["间接竞品"]):
        nav += f"      - {cn_name}: competitors/{slug}/index.md\n"

    nav += "  - 监测日志: monitor/index.md\n"

    yml_path = WEBSITE_ROOT / "mkdocs.yml"
    yml_path.write_text(nav, encoding="utf-8")
    print(f"Generated: {yml_path}")


def copy_extra_assets():
    """复制自定义 CSS/JS（如果存在）。"""
    css_src = WEBSITE_ROOT / "overrides" / "extra.css"
    css_dst = DOCS_ROOT / "stylesheets" / "extra.css"
    if css_src.exists():
        shutil.copyfile(css_src, css_dst)
    else:
        css_dst.write_text("/* Custom styles will go here */\n", encoding="utf-8")

    js_src = WEBSITE_ROOT / "overrides" / "extra.js"
    js_dst = DOCS_ROOT / "javascripts" / "extra.js"
    if js_src.exists():
        shutil.copyfile(js_src, js_dst)
    else:
        js_dst.write_text("// Custom scripts will go here\n", encoding="utf-8")


# ── 主入口 ────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("竞品分析工作台 → MkDocs 网站构建")
    print("=" * 50)

    print("\n[1/7] 清理 docs/ 目录...")
    clean_docs()

    print("[2/7] 复制分析框架和报告模板...")
    copy_framework()

    print("[3/7] 复制竞品数据...")
    categories = copy_competitors()
    total = sum(len(v) for v in categories.values())
    print(f"      已处理 {total} 个竞品：")
    for rel, items in categories.items():
        print(f"        - {rel}: {len(items)} 家")

    print("[4/7] 复制监测日志...")
    copy_monitor_logs()

    print("[5/7] 复制自定义样式和脚本...")
    copy_extra_assets()

    print("[6/7] 生成首页...")
    generate_index(categories)

    print("[7/7] 生成 mkdocs.yml...")
    generate_mkdocs_yml(categories)

    print("\n✅ 构建完成！")
    print(f"   输出目录: {DOCS_ROOT}")
    print(f"   下一步: cd {WEBSITE_ROOT} && mkdocs serve")


if __name__ == "__main__":
    main()
