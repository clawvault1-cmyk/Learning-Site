# Proud Little Learners — owner launch notes

This folder is not published on proudlittlelearners.com. Paste owner-only values here, then copy checkout links into `assets/config.js` (that file is public, so put only Payhip URLs and a Pixel ID there — never a mailing address or legal name).

## 1. Open checkout (required to sell)

Edit `assets/config.js`. This is the only public file you need to change to take payment.

For each product, paste a Payhip product key or a Payhip URL:

- `https://payhip.com/b/KEY` or `https://payhip.com/buy?link=KEY`, or just `KEY`
- `checkoutUrls["k-add-beginner"]` — Beginner: Adding within 5 ($3.99)
- `checkoutUrls["k-add-intermediate"]` — Intermediate: Adding within 10 ($3.99)
- `checkoutUrls["k-add-advanced"]` — Advanced: Story problems within 10 ($3.99)
- `subscriptionUrl` — Weekly Kindergarten Math Plan ($3.99/month)
- `storeSignInUrl` — the full `https://` Payhip customer sign-in URL (used on cancel.html)
- `metaPixelId` — numbers only. Leave `""` if you are not using the Meta Pixel. The site will not load Meta’s script, and the privacy policy will hide Pixel details, until this is set.

Leave any value as `""` until you have the real one. Do not invent URLs or IDs. Empty buttons stay on “Checkout opens soon. No payment is taken yet.” and an email link lets parents ask to be notified. When a URL is filled, that button becomes “Buy now” or “Start the weekly plan” and goes to Payhip.

After you paste the links, click every Buy button and the weekly button, and confirm they open the right Payhip checkout. If you added `storeSignInUrl`, confirm the Cancel page “Sign in to cancel” button goes to Payhip sign-in.

Configure Payhip so a new weekly member immediately gets every packet already released in the current calendar month, and so a new packet is posted every Monday. The site and terms already describe that. Packets should stay in the members area for at least 30 days. If your Payhip settings cannot do this, change the site copy the same day.

Sales tax: the site tells parents tax may be added at checkout, matching the terms (Payhip collects US sales tax). Confirm that is how your Payhip account is set up.

## 2. Legal and contact details (do not invent; fill before or just after launch)

A lawyer should review the public Privacy, Terms, and Refund pages before you rely on them. The public pages no longer show fill-in brackets. Add the details below to those pages (and update “Last updated”) when you have them:

- [OWNER: legal business name]
- [OWNER: state of formation]
- [OWNER: business type, for example sole proprietorship or LLC]
- [OWNER: mailing address]
- [OWNER: inbox provider for hello@proudlittlelearners.com, for example “Google (Gmail)”, plus that provider’s privacy policy URL]
- [OWNER: one-line About bio — first name, and whether you are a parent or teacher. Publish it only on about.html, under a heading “Who we are.” Never invent this, and do not put it on the homepage.]

Lawyer questions kept off the public site (see also LEGAL-REVIEW-NOTES.md):

- [OWNER/LAWYER: confirm the subscription price-change notice in Terms section 6 matches the state laws that apply]
- [OWNER/LAWYER: decide whether to add an arbitration clause; it was left out on purpose to keep the terms simple]

## 3. Product facts already aligned on the site

The pack data checked into this repo and into `proud-little-learners-packs` on `main` is:

| Pack | Practice pages | Total pages | Price |
| --- | ---: | ---: | --- |
| Beginner: Adding within 5 | 18 | 41 | $3.99 |
| Intermediate: Adding within 10 | 18 | 41 | $3.99 |
| Advanced: Story problems within 10 | 18 | 41 | $3.99 |

The weekly page lists the first 8 weeks. An unmerged private-repo pull request rebuilds Intermediate as 20 practice pages / 45 total and adds weeks 9–16. Do not advertise those until that is the file you will actually sell, and until the site copy is updated to match.

## 4. GitHub Pages setting

In the repository Pages settings, set the source to **GitHub Actions** (not “Deploy from a branch”). A branch deploy of `main` at `/` is why internal files were still public even after a cleanup workflow ran. After you merge the launch-readiness pull request, confirm `/LEGAL-REVIEW-NOTES.md`, `/build.py`, and `/_internal/` return 404.

## 5. Public git history

Removing the pack generators from this repo does not erase them from git history. Anyone can still recover `packs/catalog.py`, `packs/layouts.py`, and the other generator files from old commits. The same generators already live (identical, as of 11 November 2026) on `main` of the private repo `clawvault1-cmyk/proud-little-learners-packs`. If you want them gone from public history, that takes a history rewrite and a force-push, which you should only do with a clear plan (it will change every commit SHA). This work does not rewrite history.
