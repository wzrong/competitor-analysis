/* 外部链接在新窗口打开，并增强战略情报标签显示 */
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="http"]').forEach(function(link) {
    if (!link.hasAttribute('target') || link.getAttribute('target') !== '_blank') {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener');
    }
  });

  const badgeRules = [
    { pattern: /^(🟢|.*运行中.*|.*已成型.*|.*完成.*)$/, className: 'intel-badge--green' },
    { pattern: /^(🟡|.*试运行.*|.*搭建中.*|.*起步.*|.*修复中.*|.*部分闭环.*|.*待核实.*)$/, className: 'intel-badge--yellow' },
    { pattern: /^(🔴|.*阻塞.*|.*未激活.*)$/, className: 'intel-badge--red' },
    { pattern: /^(Tier [123]|T[123])$/, className: 'intel-badge--tier' },
    { pattern: /^(T1|\[T1)/, className: 'intel-badge--t1' },
    { pattern: /^(T2|\[T2)/, className: 'intel-badge--t2' },
    { pattern: /^(T3|\[T3)/, className: 'intel-badge--t3' }
  ];

  document.querySelectorAll('.md-typeset table td').forEach(function(cell) {
    const text = cell.textContent.trim();
    if (cell.children.length > 0 || text.length > 16) return;
    const rule = badgeRules.find(function(item) { return item.pattern.test(text); });
    if (!rule) return;
    const badge = document.createElement('span');
    badge.className = 'intel-badge ' + rule.className;
    badge.textContent = text;
    cell.textContent = '';
    cell.appendChild(badge);
  });
});
