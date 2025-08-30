(function() {
  if (window.innerWidth <= 767) { // 只在手机端执行
    function removeAds() {
      // 1. 删除左右竖条广告
      document.querySelectorAll('.nb-stick.nb-left, .nb-stick.nb-right').forEach(el => el.remove());

      // 2. 删除浮窗广告 (右下角)
      document.querySelectorAll('#nb-float, .nb-float, .nb-stick-float').forEach(el => el.remove());

      // 3. 删除弹窗广告 (全屏遮罩)
      document.querySelectorAll('.nb-modal').forEach(el => el.remove());

      // 4. 删除底部小方块广告 (三个缩略图覆盖内容的)
      document.querySelectorAll('.nb-bottombar-wrap').forEach(el => el.remove());
    }

    // 页面加载后立即执行一次
    document.addEventListener("DOMContentLoaded", removeAds);

    // 每 1 秒清理一次，防止广告脚本延迟插入
    setInterval(removeAds, 1000);
  }
})();
