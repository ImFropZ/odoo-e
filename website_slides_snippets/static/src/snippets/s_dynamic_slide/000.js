odoo.define(
  "website_slides_snippets.dynamic_slide_snippet",
  function (require) {
    var PublicWidget = require("web.public.widget");
    var rpc = require("web.rpc");
    var core = require("web.core");
    var wUtils = require("website.utils");

    var QWeb = core.qweb;

    var Dynamic = PublicWidget.Widget.extend({
      selector: ".dynamic_snippet_slide",
      start: function () {
        var self = this;
        
        self.$("#dynamic-slide-container").html("HELLO WORLD")
        // Search domain setup
        var websiteIdDomain = wUtils.websiteDomain(this);
        var domain = [...websiteIdDomain];

        rpc
          .query({
            route: "/get_slides",
            params: {
              domain,
            },
          })
          .then(function (result) {
            self.$("#dynamic-slide-container").html(
              QWeb.render("website_slides_snippets.WebsiteSlides", {
                slides: result,
              })
            );
          });
      },
    });

    PublicWidget.registry.dynamic_snippet_website_slides_slides = Dynamic;
    return Dynamic;
  }
);
