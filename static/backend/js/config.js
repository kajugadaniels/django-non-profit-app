(function () {
  var primary = localStorage.getItem("primary") || "#15548C";
  var secondary = localStorage.getItem("secondary") || "#48A3D7";

  window.AosAdminConfig = {
    // Theme Primary Color
    primary: primary,
    // theme secondary color
    secondary: secondary,
  };
})();
