# Design fixes, round 2 (after PR #30 went live about 6:45 PM ET), checked 7:35 PM ET Oct 28
After screenshots: /workspace/loops/s2/design/after-1/ (`<page>-m.png` / `-m-fold.png` at 390x844, `-d.png` / `-d-fold.png` at 1280; plus `crop-packs.png`, `crop-weekly.png`, `crop-compare.png`, `*-m-scroll*.png`, `beginner-m-slide3.png`).
Layout only. Anything needing words is marked [COPY].

**What improved:** the homepage on phone went from 7,458px to 4,013px. Product pages went from about 3,700px to about 2,480px, and weekly went from 2,099px to 1,661px. There's no horizontal overflow (scrollWidth 390). The hero button is on the first screen. The sample pages on product pages are now readable at full width with a peek and a "3 / 8" counter (`beginner-m-slide3.png`). The sticky buy bar works, and `body.product` has 72px bottom padding, so the footer isn't trapped.

---

## 1. BROKEN: in the level-picker rows and the weekly card, the image runs under the text
- **Where:** home `#packs .pack-card` (3 rows) and home `#plans .plan-card`; also kindergarten-math.html. See `after-1/crop-packs.png` and `crop-weekly.png`. The practice page shows through the headings, and on the weekly card "Weekly Kindergarten Math Plan / A new packet…" is printed on top of the cover. This is the most "cheap/broken" thing on the site right now.
- **Cause:** the `.mock` has `aspect-ratio:3/4; height:100%` and spans 2 rows. Its height comes from the text column (about 210px), so the aspect ratio forces its width to about 160px. That spills out of the 120px grid track, and grid items don't shrink below that size by default.
- **Fix (css/styles.css, at ≤767px for .pack-card and globally for .plan-card):**
  ```css
  .pack-card .mock,.plan-card .mock{aspect-ratio:auto;width:100%;min-width:0;height:auto;align-self:stretch;position:relative;overflow:hidden}
  .pack-card .mock img,.plan-card .mock img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top left}
  ```
  - Also give the weekly card a real page image instead of the 4:3 fanned cover. The cover crops to a dark slab in a 120px column. Use `assets/img/packs/weekly/…interior` if it exists. If not, use `object-position:center` on the cover-1x1.
  - Desktop .plan-card (220px column) needs the same rule.

## 2. Level rows: the text hierarchy fights itself, and the price line wraps
- **Where:** `.pack-card .card-copy` (home and kindergarten-math.html). Each row shows a bold question, then a bold pack name at almost the same size, then "$3.99 · 18 pages · adding up to 5" wrapping over 2 lines.
- **Fix:**
  ```css
  .pack-card .card-copy h3{font-size:17px;line-height:1.25;margin:0 0 4px}           /* the question */
  .pack-card .card-copy .pack-name{font:700 14px/1.3 Inter,sans-serif;color:var(--navy-70);margin:0 0 6px}
  .pack-card .price{font-size:20px;margin:4px 0 0}
  .pack-card .meta{display:block;font:400 13px/1.35 Inter,sans-serif;color:var(--navy-70)}
  ```
  - In build.py, split the line into `<p class="price">$3.99</p><span class="meta">…</span>` so the price sits on its own line and the details go on a smaller second line. The existing words stay; this is markup only.
  - Put a small 6px color bar (or the level badge) next to the name, so the three levels read as Level 1 / 2 / 3 at a glance. The top border is currently hidden by the overflow bug.
  - Target: each row is 180px or less, with the button never touching the image.

## 3. Product page and desktop: the cover slide is cropped and blurry
- **Where:** `.slides` first slide on all 3 product pages and weekly.html. On phone, the 4:3 cover is cropped into a 3:4 frame ("pples" cut off on the left, `products_k-addition-beginner-m-fold.png`). On desktop, the same crop is scaled up from the 960px file and looks soft (`products_k-addition-beginner-d-fold.png`).
- **Fix:** in build.py `gallery()`, give the cover slide its own class and use the square or contained image:
  ```css
  .slides .slide-cover img{object-fit:contain;background:var(--cream);padding:8px}
  ```
  - Alternatively, use `cover-1x1-1200.webp` with `object-fit:cover`.
  - On desktop, set `sizes="(min-width:1024px) 560px, 80vw"` so it loads the 1200/1600 file.
  - Also add `loading="eager"` (or at least a `decoding="async"` fetch) to slides 7–8. They returned an empty `currentSrc` until scrolled, which can show a blank card on a fast swipe.

## 4. Weekly sticky bar: the button wraps onto 2 lines
- **Where:** weekly.html `.buybar` (`after-1/sheet-scroll.png`, third panel). "$3.99/month" is wide, so "Checkout opens soon" wraps and the bar looks cramped.
- **Fix:**
  ```css
  .buybar-price{font-size:18px}
  .buybar .btn{white-space:nowrap;padding:0 16px;font-size:16px}
  @media(max-width:360px){.buybar-price{font-size:16px}.buybar .btn{font-size:15px}}
  ```
  - The bar itself is fine on the pack pages, and the 72px padding keeps the footer copyright visible at the very bottom.

## 5. Comparison cards: the "Free worksheets" card floats in empty space
- **Where:** home `#problem .compare` (`crop-compare.png`). The left card is the same height as the right one, but its content is vertically centered, so there's about 80px of blank white above and below it. That reads as unfinished.
- **Fix:** delete the leftover rule `.compare-card:first-child{display:flex;flex-direction:column;justify-content:center}`. Add `.compare{align-items:start}` and `.compare-card{padding:16px}`. Use 14px for the list text inside `.compare-card` on phone, so the "Our packs" card is no longer 7 lines taller than its neighbor.
- **[COPY]** if the copy chief can trim the "Our packs" list from 5 lines to 4, the two cards will line up.

## 6. Parent guide image: an unreadable wall of tiny text (looks cheap)
- **Where:** home `#say` figure (the full guide page at about 240px wide), with the quote below it. On desktop, the guide thumbnail sits far left with a big empty gap before the quote.
- **Fix:** show a readable crop instead of the whole page, so the scaled-down text is legible.
  ```css
  #say .guide-shot{width:100%;aspect-ratio:16/10;object-fit:cover;object-position:0 38%;border:1px solid var(--line);border-radius:12px;background:#fff}
  @media(min-width:768px){#say .wrap-say{display:grid;grid-template-columns:minmax(0,420px) 1fr;gap:32px;align-items:center}}
  ```
  - Use `guide-1200.webp`. Crop to the "I do, we do, you do" block that the quote comes from.
  - If a clean crop doesn't read at 390px, drop the image and keep only the quote card with the teal left rule. That is tidier than an unreadable page.

## 7. Weekly page: the heavy navy frame, and no sample pages
- **Where:** weekly.html `.gallery-main` / first image. The thick dark navy frame around the cover is the only dark block left on the site, and it makes the plan feel heavier than the packs. The page also has just one image, while every pack page has an 8-slide scroller. A parent can't see a weekly packet page.
- **Fix:**
  - Reuse the product `gallery()` on weekly.html with the cover (contained, per #3) plus 3–4 interior pages from Weeks 1–3. Those images already exist from the earlier preview work in `assets/img/packs/weekly/` or the week preview folders.
  - Remove the navy tint so it matches the cream background used on the pack pages: `.tint-weekly` → `background:var(--marigold-50)`.
  - Keep the terms lines exactly where they are, under the button.

## 8. Spacing and rhythm consistency
- **Where:** global. Sections are now 40px apart on phones, but a few spots break the rhythm:
  - (a) the `#kids` strip (82px, teal-50) sits directly against the hero with no gap, and reads like a cookie banner;
  - (b) `#start` "Print one page tonight" is a huge empty band on desktop, with a 220px section mostly blank;
  - (c) product pages have 3 small grey lines (ink / pencil / instant download) stacked at 14px under the "What's inside" grid. That looks like fine print.
- **Fix:**
  - (a) `#kids{margin:0 20px;border-radius:16px;padding:14px 16px}` turns it into a rounded callout inside the cream hero. Or move it under the hero button as a `.chip`.
  - (b) at ≥1024px, `#start{padding:64px 0}` and `#start .wrap{display:flex;align-items:center;justify-content:space-between}` put the heading and button on one row.
  - (c) put the 3 lines in one `.inside-notes{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:14px}` row with small icons (printer, pencil, download). Or ask the copy chief to merge them into one line. **[COPY]**
  - Use one shadow token (`--shadow`) on `.compare-card`, `.pack-card`, `.plan-card`, `.level-card` and `.faq details`. Right now the FAQ items have a border but no shadow, and the cards have both.

---
### Not issues (checked)
- No overflow at 390px.
- The buy bar hides while the main button is on screen and never covers the main button.
- Checkout buttons are solid teal with "Checkout opens soon".
- No reviews, badges, countdowns or stock photos.
