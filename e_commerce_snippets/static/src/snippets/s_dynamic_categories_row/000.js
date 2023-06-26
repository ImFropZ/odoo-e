/** @odoo-module **/

import publicWidget from "web.public.widget";
import wUtils from "website.utils";
import core from "web.core";

const QWeb = core.qweb;

publicWidget.registry.DynamicCategoriesRow = publicWidget.Widget.extend({
  selector: ".dynamic_snippet_categories_row",
  start() {
    let categoriesRowContainer = this.el.querySelector(
      "#dynamic-cateogories-row-container"
    );

    if (categoriesRowContainer) {
      // Search domain setup
      var websiteIdDomain = wUtils.websiteDomain(this);
      var domain = [...websiteIdDomain];

      this._rpc({
        route: "/e_commerce/get_product_categories_row",
        params: {
          domain,
        },
      }).then((data) => {
        categoriesRowContainer.innerHTML = QWeb.render(
          "e_commerce_snippets.CategoryRow",
          {
            categoryRows: data,
          }
        );

        const moveBackBtn = $(".dynamic-category-row-products__moveBack");
        const moveFrontBtn = $(".dynamic-category-row-products__moveFront");

        moveBackBtn.on("click", function () {
          const container = $(this).siblings(
            ".dynamic-category-row-productsContainer"
          );
          const nextSectionOffset = container.scrollLeft() - container.width();

          container.animate({ scrollLeft: nextSectionOffset }, "slow");
        });

        moveFrontBtn.on("click", function () {
          const container = $(this).siblings(
            ".dynamic-category-row-productsContainer"
          );
          const nextSectionOffset = container.scrollLeft() + container.width();

          container.animate({ scrollLeft: nextSectionOffset }, "slow");
        });
      });
    }
  },
});

export default publicWidget.registry.DynamicCategoriesRow;
