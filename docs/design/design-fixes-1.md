# Design fixes, round 1 (Design/UX lead), Oct 28 2026
Scope: layout, hierarchy, spacing, images, phone UX only. Anything needing words is marked [COPY] and goes to the copy chief. No new wording is written here.
Before screenshots: /workspace/loops/s2/design/before/ (`<page>-m.png` = 390x844 full page, `-m-fold.png` = first screen, `-d.png` = 1280 wide).
References: /workspace/loops/s2/design/refs/ (Lovevery home + Play Kits, Big Life Journal home + PDF kit product, Beast Academy home + Level 1 books, KiwiCo home, TPT kindergarten addition product. Etsy returned 403.)

## What's wrong, in one paragraph
On a phone the homepage is **7,458px long, about 9 screens**, with 9 sections: hero, problem list, compare cards, 3 steps, 3 tall pack cards, sample pages, the weekly band, FAQ, and a closing CTA. The 3 pack cards alone take about 1,800px. All three cover images use the same fanned-pages layout and differ only in color, so a parent can't see what's different between levels. The real proof, the inside pages, is cropped to 200px tall and can't be read. The reference shops do the opposite. They show one big product image, give a short reason to buy, offer a compact level picker, link to readable sample pages, then put a single buy button near the top. Lovevery's Play Kits page uses age tabs and a one-line price row. Beast Academy's level page has the book image, Add to cart, a row of "Other Levels" thumbnails, and "View Sample Pages". TPT shows a "View Preview" button, a short Highlights list and a sticky "Add to cart" bar.

Target: homepage at most 4.5 phone screens (about 3,800px), 6 sections; product pages with the buy button always one tap away.

---

## 1. Homepage: cut from 9 sections to 6 (biggest win)
- **File:** assets/src/home-body.html
- **Change:** final order is `hero` → `#problem` (compare only) → `#packs` → `#how` → `#plans` band → `.faq` (4 items). Delete `section#inside` from the homepage. Its sample pages move into the pack cards (fix 3) and product pages (fix 7). Delete `section#start` (the closing CTA). Instead, put one full-width `.btn` that links to `#packs` after the FAQ, inside the same section.
- **Why:** Lovevery and KiwiCo homes go hero → choose a product → how it works → trust. Neither repeats the same idea in multiple sections. Ours repeats "what's inside" 3 times (compare card, `#inside`, product page).
- **[COPY]** Which 4 FAQ questions stay, and the label for the button after the FAQ.

## 2. Hero: one large, clear product image, and nothing between the button and the image
- **File:** assets/src/home-body.html `.hero`; css/styles.css `.hero-art`
- **Change:**
  - On phone, show ONE image only: the Beginner cover-4x3 **without the thick orange frame**. Use a cream background and `border-radius:16px`, and make it full width.
  - Order inside `.hero-copy`: h1 → lead → `.btn` → image. Move `p.micro` to directly under the button (where it is now), and cap it at one line.
  - Hide the side-scroll strip: `.hero-art img:not(:first-child){display:none}` under 1024px. It currently hides two images that look identical to the first, and nothing tells you you can swipe.
  - Tighten the spacing: `.hero{padding:16px 0 24px}`, `.hero-copy h1{font-size:32px}` on phones, so the button and the top of the image both show in the first 844px.
- **Why:** BLJ's product page and Beast Academy's level page both show a clear product image in the first screen. A swipe strip with no dots looks like one image, so the hidden images are wasted bytes.
- **[COPY]** The lead is 3 lines on a phone. Ask the copy chief for 2 lines at most.

## 3. Pack cards: change three tall cards into a compact level picker
- **File:** build.py (homepage cards, about line 248 / `#packs` in home-body.html); css `.pack-card`
- **Change:** under 768px, change `.pack-card` into a horizontal row card:
  ```css
  @media(max-width:767px){
   .pack-card{display:grid;grid-template-columns:120px 1fr;grid-template-rows:auto auto;align-items:center}
   .pack-card .mock{grid-row:1 / span 2;aspect-ratio:3/4;height:100%}
   .pack-card .mock img{object-fit:cover;object-position:top}
   .card-copy{padding:16px 16px 0}
   .card-actions{grid-column:2;padding:8px 16px 16px}
   .card-actions .btn{min-height:44px}
  }
  ```
  - Use **interior-01 (a real practice page)** as the card image instead of the fanned cover. Then each level shows what the child actually does, and the three levels look different.
  - Keep the colored level badge as the top border: `border-top:6px solid var(--marigold|--teal|--coral)`.
  - Each card shows only: badge, name, one line, and a price/button row. Drop the second `<p>`.
  - Target height is about 170px per card, so the three cards take about 520px instead of about 1,800px.
  - On desktop, keep 3 columns but also use the interior page image.
- **Why:** Beast Academy's "Other Levels" and Lovevery's age tabs let a parent compare levels in one glance. Our current covers are the same picture in 3 colors.
- **[COPY]** One line per card (what the child does). Today there are two lines: "Count two small groups…" and "Start here if…".

## 4. Problem section: one side-by-side comparison, with less reading
- **File:** home-body.html `#problem`; css `.compare`, `.problem-list`, `.fix`
- **Change:**
  - Keep the h2 and turn `.problem-list` into **3 short rows with icons**, no dividers: `display:grid;gap:8px`, each row 15/16px with a 24px coral icon.
  - Remove `p.fix` as a separate bold paragraph. Its point is already made by the compare card.
  - Keep `.compare` **2 columns even at 390px**: delete the `@media(max-width:480px){.compare{grid-template-columns:1fr}}` rule. Remove `.mock` from the "Our packs" card. Each card is a header plus 4 ✕/✓ lines at 15px, and the "Our packs" card gets `border:2px solid var(--teal);background:var(--teal-50)`.
  - Target section height is about 650px (currently about 1,200px).
- **Why:** a side-by-side ✕/✓ table is the fastest comparison to scan on a phone, and stacking it hides the comparison. The repeated mock image adds height without new information.
- **[COPY]** The ✕/✓ lines must fit about 18 characters each to work in 2 columns at 390px.

## 5. Show the steps with pictures, not three text cards
- **File:** home-body.html `#how`; css `.steps.tonight`, `.step-img`
- **Change:**
  - On phone, use a vertical timeline: a 32px marigold number dot, a 2px dashed line connecting the dots (`.steps li:not(:last-child)::after{content:"";position:absolute;left:27px;top:46px;bottom:-12px;border-left:2px dashed var(--line)}`), no card borders, and `padding:12px 0 12px 52px`.
  - Give each step a small 64px illustration on the right in the same flat style as step-cereal.svg (page, cereal, check mark), or reuse one illustration at full width only under step 2.
  - Drop the white card boxes. 3 bordered cards inside a section that sits between other bordered cards make the page feel busy.
- **Why:** KiwiCo and Lovevery show "how it works" as a short visual row, not paragraphs in boxes.
- **[COPY]** Each step body should be one line.

## 6. Make the Weekly band match the cards, and move terms next to the button they belong to
- **File:** home-body.html `section.band#plans`; css `.band`
- **Change:**
  - Replace the full-bleed navy band with a `.card` that looks like the pack cards: `background:var(--marigold-50);border:1px solid var(--line);border-radius:20px;padding:24px`. Inside it goes the image (weekly cover, 3/4 crop), the name, one line, the price and the button.
  - On phone, the navy band is the darkest, heaviest block on the site, and it puts the most attention on the secondary offer.
  - **[COPY/decision]** The homepage card currently has 2 terms lines plus "Best if…". Recommend keeping the full renewal/cancel/refund terms directly under the button **on weekly.html**, where checkout happens, and showing the homepage card without terms, since its button goes to weekly.html and not to checkout. The copy chief and owner must confirm this is OK for compliance. No text is written here.
- **Why:** Lovevery shows the subscription as a product card with a single price row ("Every 2 months | $88 per Play Kit") and puts the terms in the checkout flow. Consistent cards read as one shop.

## 7. Product pages: sticky buy bar on phone
- **Files:** build.py product template (about line 185–199) and weekly (about line 213–221); css; assets/app.js (small, no library)
- **Change:** add once per product page, before `</main>`:
  ```html
  <div class="buybar" hidden><span class="buybar-price">$3.99</span><a class="btn buy" aria-disabled="true" data-checkout="…" …>Checkout opens soon</a></div>
  ```
  ```css
  .buybar{position:fixed;left:0;right:0;bottom:0;z-index:45;display:flex;align-items:center;gap:12px;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:#fff;border-top:1px solid var(--line);box-shadow:0 -4px 16px rgba(36,55,70,.08)}
  .buybar .btn{flex:1;min-height:48px;width:auto}
  .buybar-price{font:800 20px Nunito,sans-serif}
  @media(min-width:1024px){.buybar{display:none!important}}
  ```
  ```js
  const main=document.querySelector('.buybox .btn.buy'),bar=document.querySelector('.buybar');
  if(main&&bar)new IntersectionObserver(([e])=>bar.hidden=e.isIntersecting||e.boundingClientRect.top>0).observe(main);
  ```
  - The weekly page uses `$3.99/month`.
  - Add `padding-bottom:72px` to `body.product` on phone, so the footer isn't covered.
  - The button stays solid teal and reads "Checkout opens soon", using the same text and data attributes as the main button, so app.js wires both the same way.
- **Why:** TPT's product page keeps "Add to cart" pinned at the bottom while you read the description and reviews. Our product pages are about 3,700px, and the only buy button is on screen 1.

## 8. Product pages: big, readable sample pages instead of tiny thumbnails
- **File:** build.py `gallery()` (about line 125–135); css `.slides`, `.thumbs`
- **Change:**
  - Slides: remove `max-height:260px` on phone. Use `aspect-ratio:3/4` for interior pages, keep 4/3 for the cover slide, and use `object-fit:contain` on white with a 1px `var(--line)` border.
  - Replace the 64px `.thumbs` row on phone with **dots plus a "1 / 7" counter**: `.thumbs{display:none}` under 768px, and add `<div class="dots">` that app.js updates on scroll. The current 64px thumbs show nearly blank white rectangles.
  - Keep the thumbs on desktop, but make them 88px.
  - Add a peek: `.slides img{flex:0 0 88%}` plus `gap:12px` on phone, so the next page visibly peeks in and invites a swipe.
- **Why:** Beast Academy has a "View Sample Pages" section with full readable spreads, and TPT has a large "View Preview" image carousel with dots. For a $3.99 printable, seeing a real readable page is the main reason to trust it.

## 9. Product pages: collapse the 4 text sections into 3 tidy accordions
- **File:** build.py product template, sections "What's inside", "What your child will practice", "How you help", "When to move on" (about line 192–198)
- **Change:**
  - Keep "What's inside" open as a compact **2x2 icon grid**, not a 6-row tick list: `.inside-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}`. Each tile is a 48px thumbnail (page, answer key, guide, tracker) plus a 2–4 word label. Show the pencil/cereal and ink notes as a single small line under the grid.
  - Put "What your child will practice", "How you help" and "When to move on" in `<details class="details">` (the style already exists), all closed by default.
  - Target: the product page drops from about 3,700px to about 2,200px on phone.
- **Why:** TPT uses a short "Highlights" list (Pages 8, Grades, PDF) and hides the long description behind "Show more". Beast Academy uses tabs (Description / Skills & Sequence / Choose the Right Level).
- **[COPY]** The 2–4 word labels for the 4 tiles.

## 10. "Other levels" on product pages: one compact row, not two tall cards
- **File:** build.py `others` (about line 181); css `.level-card`, `.level-grid`
- **Change:**
  - On phone: `.level-grid{grid-template-columns:1fr 1fr;gap:12px}`.
  - `.level-card .mock{aspect-ratio:3/4}` with the interior-01 image, `h3{font-size:16px;margin:8px 12px}` and `.price{margin:0 12px 12px;font-size:18px}`.
  - Target is about 300px total, down from about 560px.
  - Move the standards sentence ("These are kindergarten skills from the Common Core…") into the "What your child will practice" accordion.
- **Why:** Beast Academy's level page shows "Other Levels" as a single row of small thumbnails.

## 11. One alignment and spacing system across all pages
- **File:** css/styles.css
- **Change:**
  - **Left-align** all section h2s and body text on phone: remove `.sec > .wrap > h2{text-align:center}` and `.hero-copy,.band-copy{text-align:center}` in the 767px query. The current mix of centered headings over left-aligned lists makes the page look unfinished. Every reference product page is left-aligned on phone.
  - Spacing scale: sections `padding:40px 0` on phone, with alternating cream/white backgrounds only. Card radius is 16px everywhere and the weekly card is 20px.
  - Use one shadow token: `--shadow:0 1px 2px rgba(36,55,70,.06),0 8px 24px rgba(36,55,70,.06)`.
  - Body text is 16px on phone with line-height 1.55, and `p.micro` is 14px. Inter at 17px with 1.6 line-height makes every paragraph 1 line longer on a 390px screen.
  - Fix the swapped badge classes: `.badge.peach` is teal and `.badge.teal` is coral. Rename them to `.badge.b1/.b2/.b3`, or `.lv-beginner/-intermediate/-advanced`, so level colors can't get mixed up later.
- **Why:** consistency is what makes a small shop look trustworthy (design guide §"consistent cards"; Lovevery's single type and spacing system).

## 12. Packs index page (kindergarten-math.html): use the compact card
- **File:** build.py about line 245–254 (kindergarten-math.html); css
- **Change:** reuse fix 3's horizontal `.pack-card` (with the interior-01 image) and the weekly card from fix 6. Today the page stacks 4 tall cards, about 2,900px on phone; the target is about 1,300px. (Checked: free-printables.html and k-addition-bundle.html already redirect to the homepage and aren't in sitemap.xml, so nothing is needed there.)
- **Why:** this is the same level-picker pattern as Beast Academy's "Other Levels", and it means a pack looks the same everywhere it appears.

---

### Guardrails these fixes keep
- No stock family photos, no customer faces, no reviews, ratings, badges or counts, no countdowns, and no new fine print.
- Checkout buttons stay solid teal and read "Checkout opens soon".
- JS added is about 10 lines in the existing app.js (IntersectionObserver plus dots). No libraries are added.

### Size targets to check after the build (390x844)
- Homepage at most 3,800px (now 7,458).
- Product page at most 2,300px (now about 3,700).
- weekly.html at most 1,900px (now 2,099).
- In the first screen: the h1, the button and at least half of the hero image.
