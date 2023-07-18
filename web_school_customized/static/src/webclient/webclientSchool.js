import { WebClient } from "@web/static/src/webclient/webclient";

export class CustomWebClient extends WebClient {
  setup() {
    console.log("Customized Web.");
    super.setup();
  }

  // Add other methods or override existing methods as needed
}

// Use the CustomWebClient class instead of the original WebClient class
