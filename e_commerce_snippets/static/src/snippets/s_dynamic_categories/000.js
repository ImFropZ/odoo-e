/** @odoo-module **/

import publicWidget from "web.public.widget";
import wUtils from "website.utils";

publicWidget.registry.DynamicCategories = publicWidget.Widget.extend({
  selector: ".dynamic_snippet_categories",
  start() {
    const categoriesContainer = this.el.querySelector(
      "#dynamic_cateogories_container"
    );

    if (categoriesContainer) {
      // Search domain setup
      var websiteIdDomain = wUtils.websiteDomain(this);
      var domain = [...websiteIdDomain];

      this.$el
        .attr("data-category-names")
        .split(",")
        .filter((val) => val !== "")
        .forEach((val) => {
          val = val.trim();
          domain.push(["name", "not ilike", val]);
        });

      this._rpc({
        route: "/e_commerce/get_product_categories",
        params: {
          domain,
        },
      }).then((data) => {
        let html = ``;
        data.forEach((category) => {
          html += `<a href="${category.website_url}">
                    <div class="item">
                      <div class="border">
                      ${
                        category.image
                          ? `<img src="data:image/jpeg;base64,${category.image}" alt="${category.name}"/>`
                          : `<img src="https://dummyimage.com/128x128/f8f6f7/f8f6f7" alt="${category.name}"/>`
                      }
                        
                      </div>
                      <div>${category.name}</div>
                    </div>
                  </a>`;
        });
        categoriesContainer.innerHTML = html;
      });
    }
  },
});

export default publicWidget.registry.DynamicCategories;
