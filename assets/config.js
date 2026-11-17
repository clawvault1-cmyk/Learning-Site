// ===== Site configuration: paste Payhip links and the Meta Pixel ID here =====
// This is the only file you need to edit to open checkout.
// Full step-by-step notes are in _internal/LAUNCH.md (not published on the site).
//
// checkoutUrls and subscriptionUrl accept any of:
//   - a Payhip product key, such as AbCdE
//   - https://payhip.com/b/AbCdE
//   - https://payhip.com/buy?link=AbCdE
// Leave a value as "" to keep that button on "Checkout opens soon."
// No payment is taken while a value is empty. Do not invent URLs or IDs.
window.SITE = {
  brand: "Proud Little Learners",
  email: "hello@proudlittlelearners.com",
  replyTime: "within 1 business day",
  checkoutUrls: {
    "k-add-beginner": "",
    "k-add-intermediate": "",
    "k-add-advanced": ""
  },
  subscriptionUrl: "",   // weekly plan key or Payhip buy link
  storeSignInUrl: "",    // full https URL to the Payhip customer sign-in page, for cancel.html
  metaPixelId: "",       // numbers only; empty loads nothing and hides Pixel policy text
  availability: "Checkout opens soon. No payment is taken yet."
};
