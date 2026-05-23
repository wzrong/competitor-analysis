/* 外部链接在新窗口打开 */
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="http"]').forEach(function(link) {
    if (!link.hasAttribute('target') || link.getAttribute('target') !== '_blank') {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener');
    }
  });
});
