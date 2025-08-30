(function() {
  if (window.innerWidth <= 767) { // 只在手机端执行
    function removeAds() {
      // 删除左右竖条
      document.querySelectorAll('.nb-stick.nb-left, .nb-stick.nb-right').forEach(el => el.remove());

      // 删除浮窗广告
      document.querySelectorAll('#nb-float, .nb-float, .nb-stick-float').forEach(el => el.remove());

      // 删除弹窗广告
      document.querySelectorAll('.nb-modal').forEach(el => el.remove());

      // 删除底部小方块广告容器
      document.querySelectorAll('.nb-bottombar-wrap').forEach(el => el.remove());

      // 删除可能重新插入的覆盖广告 iframe
      document.querySelectorAll('iframe').forEach(el => {
        const w = parseInt(el.width) || el.offsetWidth;
        const h = parseInt(el.height) || el.offsetHeight;
        if ((w === 300 && h === 250) || (w === 320 && h === 50) || (w === 300 && h === 100)) {
          // 保留常见横幅尺寸
          return;
        }
        // 删除其他奇怪大小的 iframe（常见就是小方块广告）
        if (el.src && el.src.includes("juicyads")) {
          el.remove();
        }
      });
    }

    document.addEventListener("DOMContentLoaded", removeAds);
    setInterval(removeAds, 1000); // 每秒清理一次，防止广告脚本不断插入
  }
})();
