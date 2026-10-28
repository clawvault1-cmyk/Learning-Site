// ===== Site configuration: change the brand name & checkout here =====
window.SITE = {
  brand: "Proud Little Learners",
  email: "hello@proudlittlelearners.com",
  replyTime: "within 1 business day",
  // Paste a Payhip product key, https://payhip.com/b/KEY, or https://payhip.com/buy?link=KEY.
  // Empty keeps that button on "Checkout opens soon".
  checkoutUrls: {
    "k-add-beginner": "",
    "k-add-intermediate": "",
    "k-add-advanced": ""
  },
  subscriptionUrl: "",   // weekly membership key or Payhip buy link
  storeSignInUrl: "",    // Payhip customer sign-in page, for cancel.html
  metaPixelId: "",       // numbers only; empty loads nothing
  availability: "Checkout opens soon. No payment is taken yet."
};
