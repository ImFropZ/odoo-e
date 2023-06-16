odoo.define("e_commerce_snippets.dynamic_category_row_snippet", function (require) {
  var PublicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var core = require("web.core");
  var wUtils = require("website.utils");

  var QWeb = core.qweb;

  var Dynamic = PublicWidget.Widget.extend({
    selector: ".dynamic_snippet_category_row",
    start: function () {
      var self = this;
      rpc
        .query({
          route: "/e_commerce/get_product_category_row",
          params: {
            domain: wUtils.websiteDomain(this),
          },
        })
        .then(function (result) {
          self.$el.html(
            QWeb.render("e_commerce_snippets.CategoryRow", {
              categoryRows: result,
            })
          );

          const moveBackBtn = $(".dynamic-category-row-products__moveBack");
          const moveFrontBtn = $(".dynamic-category-row-products__moveFront");

          moveBackBtn.on("click", function () {
            const container = $(this).siblings(
              ".dynamic-category-row-productsContainer"
            );
            const nextSectionOffset =
              container.scrollLeft() - container.width();

            container.animate({ scrollLeft: nextSectionOffset }, "slow");
          });

          moveFrontBtn.on("click", function () {
            const container = $(this).siblings(
              ".dynamic-category-row-productsContainer"
            );
            const nextSectionOffset =
              container.scrollLeft() + container.width();

            container.animate({ scrollLeft: nextSectionOffset }, "slow");
          });
        });
    },
  });

  PublicWidget.registry.dynamic_snippet_e_commerce_category_row = Dynamic;
  return Dynamic;
});
