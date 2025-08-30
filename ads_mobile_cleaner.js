(function() {
  if (window.innerWidth <= 767) {
    function removeAds() {
      // 删除竖条、浮窗、弹窗
      document.querySelectorAll(
        '.nb-stick.nb-left, .nb-stick.nb-right, #nb-float, .nb-float, .nb-stick-float, .nb-modal'
      ).forEach(el => el.remove());

      // 删除覆盖在内容上的“方块广告”，但保留横幅
      document.querySelectorAll('div').forEach(el => {
        const style = window.getComputedStyle(el);
        const w = parseInt(style.width);
        const h = parseInt(style.height);

        // 过滤掉横幅常见尺寸 (728x90, 320x50, 300x100, 774x290)
        const isBannerSize = (
          (w >= 300 && w <= 330 && (h === 50 || h === 100)) ||
          (w === 728 && h === 90) ||
          (w === 774 && h === 290)
        );

        if ((style.position === "fixed" || style.position === "absolute") &&
            !isBannerSize &&
            (el.innerHTML.includes("juicy") || el.innerHTML.includes("adsbyjuicy") || el.querySelector("iframe"))) {
          el.remove();
        }
      });
    }

    document.addEventListener("DOMContentLoaded", removeAds);
    setInterval(removeAds, 1000);
  }
})();
