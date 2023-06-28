/** @odoo-module **/

import PublicWidget from "web.public.widget";
import core from "web.core";
import wUtils from "website.utils";

const QWeb = core.qweb;

PublicWidget.registry.DynamicSlides = PublicWidget.Widget.extend({
  selector: ".dynamic_snippet_slides",
  start() {
    const slidesContainer = this.el.querySelector("#dynamic_slides_container");

    const websiteIdDomain = wUtils.websiteDomain(this);
    const domain = [...websiteIdDomain];

    this._rpc({
      route: "/website_slides/get_slides",
      params: {
        domain,
      },
    }).then((data) => {
      slidesContainer.innerHTML = QWeb.render(
        "website_slides_snippets.WebsiteSlides",
        {
          slides: data,
        }
      );
    });
  },
});

export default PublicWidget.registry.DynamicSlides;
