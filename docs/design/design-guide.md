# Proud Little Learners: Design Guide v1
_Design lead research, Oct 27 2026. This is binding for the site build. The copy owner writes all the words. This guide covers layout, type, color, spacing, images, and components. Placeholder lengths below are **maximums**._

Files:
- Reference screenshots (390px and 1280px, fold and full page): `refs/`
- Current site screenshots: `current/` (home, product `k-addition-beginner`, weekly)
- Pattern crops used below: `patterns/`
- Board (current site vs. best references): `board.png`
- Measured metrics (fonts, sizes, buttons, words above the fold): `metrics.json`

---

## 0. What the research says (17 sites, 2 widths)

Sites studied: Lovevery (home + Play Kits), Big Life Journal (home + product), Beast Academy, KiwiCo (home + Koala crate), Khan Academy Kids, Homer, Yoto (home + player product page), Lucky Little Learners (home + shop), Teach Starter, Twinkl, Busy Toddler, The Good and the Beautiful, Mathseeds, a top TPT product page, and Refactoring UI (best-in-class single digital product).

What the good ones all do (measured):

| Pattern | Best sites | Our current site |
|---|---|---|
| Headline font | **Bold sans, weight 700**: Lovevery BrownPro 700 at 32px phone / 40px desktop; KiwiCo Centra 700 at 28/40; Homer 700 at 28/40; Yoto 700 at 32/60; Beast Academy bold at ~26/44 | Thin serif (Fraunces 500), **27px on phone** |
| Body text | 16–20px, near-black (Lovevery #424140, Big Life Journal #4C4C4C) | 16px **gray #5A6B78** |
| Words above the fold (phone) | Lovevery 35, KiwiCo 18, Beast Academy ~40, Refactoring UI 31 | 56 words plus an eyebrow label |
| Main button | 48–52px tall, **full width on phone** (Lovevery 342 of 390px, Homer 358px), bold 18px, one per screen | 50px pill, not full width; several gray "Checkout opens soon" buttons |
| Hero picture | A **real photo or product mockup** on every hero: kid and product (Lovevery, KiwiCo, BLJ), product render (Yoto, Refactoring UI) | Flat black-and-white worksheet scans; desktop has a 4,800px scroll animation |
| Product cards | Picture first (square or 4:3), then title, then price, then one button | **No picture**, text only |
| Choosing a level | Lovevery "Choose your starting Play Kit": one row of tappable chips, then the matching product picture | A yes/no quiz card plus 3 text cards plus a second list of links |
| Pricing | Price alone in bold. No "+ tax" or billing terms near it (Yoto, BLJ, Lovevery, TPT) | "$3.99 (+ tax where applicable)" on every card, plus a 6-line billing paragraph |
| Sections on home | 5–7 clear sections, each with its own visual | 10 sections and a 4,800px intro; mobile page is 10,300px tall |
| Product page | Gallery → title → price → buy are **all inside the first 1–1.3 screens** (BLJ, Yoto, TPT) | On phone the title, price, and buy button sit **about 3,400px down**, under 4 full-size page images |

What they **don't** do: walls of text, legal fine print by a price, gray or disabled-looking buttons, small gray body text, thin serif headlines (none of the 17), scroll-jacking, abstract sketch drawings in place of the real product, and placeholder text.

The 3 references to copy most closely:
1. **Lovevery**, https://lovevery.com/ and https://lovevery.com/products/the-play-kits. Calm, premium, and parent-focused. It has the "choose your starting level" picker, a 3-bullet "what's included" list, and one strong button. Its subscription model matches our weekly plan.
2. **Big Life Journal**, https://biglifejournal.com/products/big-life-journal-kids-second-edition. It sells printables to parents. The product page puts the product image first, then the title, price, and button, then an "Inside, your child will…" list with icon cards.
3. **Beast Academy**, https://beastacademy.com/. Kids' math. A bold centered headline, a one-line subhead, one strong colored button, a friendly picture, and "Choose your experience" picture cards with one button each.

Runners-up for single patterns: Yoto product page (desktop buy box), https://us.yotoplay.com/players/yoto-player-4; KiwiCo 3 steps, https://www.kiwico.com/; Refactoring UI hero (digital product mockup), https://www.refactoringui.com/.

Brand colors stay. The research does **not** say to change them. It says to use them more boldly: solid color blocks behind product images, not faint gradients.

---

## 1. Tokens (put these in `:root` and use only these)

### 1.1 Color
```
--navy:      #243746;  /* headlines, body text, dark band */
--navy-70:   #4A5D6B;  /* secondary text ONLY (captions). Never for paragraphs */
--cream:     #FAF8F3;  /* page background */
--white:     #FFFFFF;  /* cards */
--line:      #E8E2D6;  /* card borders, dividers */
--teal:      #1E6F69;  /* primary buttons, links */
--teal-dark: #175752;  /* button hover/active */
--teal-50:   #E4F0EE;  /* tint block behind images */
--marigold:  #FFB547;  /* highlight, Beginner color, picker selected state */
--marigold-50:#FFF1D6; /* tint block */
--coral:     #EE7F5F;  /* Advanced level color (accent only) */
--coral-50:  #FDE8E1;
```
Level colors: Beginner = marigold, Intermediate = teal, Advanced = coral. Use each one as the image tint block on its card and page, and as the badge.
Rules:
- Body text is `--navy`, never gray.
- No gradients, blurred color blobs, or glows. Use flat color blocks only.
- One saturated band per page at most: the navy weekly-plan band.

### 1.2 Type
Fonts: headings **Nunito** 800 (rounded and friendly, the free match for Lovevery, Yoto, and KiwiCo's bold sans). Body **Inter** 400/600. **Remove Fraunces.** Load from Google Fonts with `display=swap`, Nunito 700 and 800 and Inter 400 and 600 only.

| Token | Phone (<768px) | Desktop (≥1024px) | Weight | Line height | Letter spacing |
|---|---|---|---|---|---|
| `display` (H1, one per page) | 36px | 56px | 800 | 1.1 | -0.02em |
| `h2` (section titles) | 28px | 40px | 800 | 1.15 | -0.01em |
| `h3` (card titles) | 20px | 22px | 800 | 1.25 | 0 |
| `lead` (hero subhead) | 18px | 20px | 400 | 1.5 | 0 |
| `body` | 17px | 18px | 400 | 1.6 | 0 |
| `price-lg` (product page) | 32px | 36px | 800 (Nunito) | 1 | 0 |
| `price` (cards) | 24px | 24px | 800 (Nunito) | 1 | 0 |
| `button` | 17px | 18px | 700 (Inter 600 ok) | 1 | 0 |
| `small` (captions, footer) | 14px | 14px | 400 | 1.45 | 0 |

Rules:
- Nothing under 14px anywhere.
- No uppercase letter-spaced "eyebrow" labels above headlines. Delete them all.
- Paragraphs have a max width of 60ch.
- At most 2 paragraphs in a row before a picture, list, or card.
- Headlines are left-aligned on desktop. Hero and section titles can center on phone.

### 1.3 Spacing (8-pt)
Scale: `4, 8, 12, 16, 24, 32, 48, 64, 96, 128`. No other values.
- Page side padding: **20px** phone, **32px** tablet, auto-centered on desktop.
- Section padding (top and bottom): **64px** phone, **96px** desktop.
- Gap between a section title and its content: 32px phone, 48px desktop.
- Card grid gap: 16px phone, 24px desktop.
- Inside cards: 20px phone, 24px desktop.
- Heading to paragraph: 12px. Paragraph to button: 24px.

### 1.4 Widths
- Content container: **max-width 1120px**.
- Text column: **max-width 640px**.
- Hero text column on desktop: **max 520px**. The hero image takes the other ~55%.
- Breakpoints: 600, 768, 1024, 1280.

### 1.5 Radius and shadow
- Cards: radius **16px**, border `1px solid var(--line)`, shadow `0 1px 2px rgba(36,55,70,.06), 0 8px 24px rgba(36,55,70,.06)`.
- Image tint blocks: radius 16px.
- Buttons: radius **12px** (not a pill; looks less template-y, matches Lovevery and Twinkl).
- Badges: radius 999px.

---

## 2. Components

### 2.1 Buttons
| | Primary | Secondary | Text link |
|---|---|---|---|
| Height | **52px** | 52px | n/a |
| Padding | 0 28px | 0 24px | n/a |
| Background | `--teal`, hover `--teal-dark` | transparent | n/a |
| Border | none | 2px `--navy` | n/a |
| Text | white, 17/18px, 700 | navy, 17/18px, 700 | teal, 600, underline on hover only |
| Phone | **width 100%** | width 100% | n/a |
| Desktop | auto width, min 220px | auto | n/a |

Rules:
- **One primary button per screen.**
- The label may include the price, for example "[Buy · $3.99]" (copy owner decides the wording).
- **No gray or disabled buttons on the live site.** If checkout links are not set, the build must fail (or the site must not be published). Do not show "Checkout opens soon."
- Focus ring: `outline: 3px solid var(--marigold); outline-offset: 2px`.
- Minimum tap target: 48×48px.

Reference: Lovevery full-width button, `patterns/lovevery-hero-m.png`. Beast Academy single red CTA, `patterns/beast-hero-m.png`.

### 2.2 Product card (home "pick a level" and "other levels")
```
┌───────────────────────────┐
│ [IMAGE 4:3 on level tint] │  pack cover + 2 fanned pages, slight shadow
├───────────────────────────┤
│ (Beginner) badge          │  level color, 13→14px 700
│ Title, 2 lines max        │  h3
│ One line, ≤12 words       │  body, navy
│ $3.99                     │  price token
│ [ Primary button ]        │  full width inside card
└───────────────────────────┘
```
- Grid: 1 column on phone, 3 on desktop. Equal heights.
- Do **not** put paragraphs, "Start here if…" blocks, or tax text in the card.
- The whole card is clickable (to the product page). The button goes to checkout.

Reference: Beast Academy picture cards, `patterns/beast-choose-m.png`. Lovevery kit card, `patterns/lovevery-levelpicker-m.png`.

### 2.3 Level picker (replaces the yes/no quiz)
- One row of 3 chips above the cards: "[Can count to 5]", "[Can add small numbers]", "[Ready for stories]". Labels are ≤4 words, from the copy owner.
- Chip spec: 44px tall, radius 999, border 2px `--line`. Selected state: marigold fill and navy text.
- Selecting a chip scrolls to or highlights the matching card (3px marigold outline). No extra questions or panels.

Reference: Lovevery "Choose your starting Play Kit" (`patterns/lovevery-levelpicker-m.png`).

### 2.4 "What's included" list
- 3–5 rows. Each row has a 28px icon or check in a teal-50 circle, plus one line of ≤8 words.
- No sub-paragraphs.

Reference: `patterns/lovevery-included-m.png`, `patterns/blj-inside-m.png`.

### 2.5 Steps (if used)
- Exactly 3 steps in a row on desktop, stacked on phone.
- Each step has a number in a 40px marigold circle, a title of ≤4 words, and an optional line of ≤10 words. One button after the steps.

Reference: `patterns/kiwico-steps-d.png`.

### 2.6 Page preview gallery
- A horizontal scroll strip (scroll-snap) of real pages. Thumbnails are 160px wide on phone and 200px on desktop, each a white page with a soft shadow on a tint block.
- Tap opens a lightbox. Never stack full-size pages vertically.

### 2.7 Header and footer
- Header: 64px tall, cream background, 1px bottom line. Logo on the left.
- Desktop shows 3 links max: "Packs", "Weekly plan", "FAQ". Phone shows a 44px hamburger **icon** (not the word "Menu").
- No sticky promo bars.
- Footer: navy background, at most 3 short columns, small text at 14px. Legal links live here only.

---

## 3. Image treatment
This is the biggest gap. Every top site sells with pictures of the product. We have none that look like a product.

1. **Pack covers must be designed:**
   - Full-color cover with the level color as a big top band.
   - A huge Nunito 800 title (the level name).
   - A simple illustration of counters or dots and the "P" mark.
   - The current covers are plain document text, and look like a free worksheet.
2. **Mockup style for every product image:**
   - Cover on top, plus 2 inside pages fanned behind it at -6° and +4°.
   - Soft shadow `0 12px 30px rgba(36,55,70,.18)`.
   - Placed on a flat **level-color tint block** (radius 16px).
   - Optional props: a pencil, a crayon, and a few round counters or cereal pieces.
   - Export at 1600×1200 (4:3) and 1200×1500 (4:5 for the product gallery), as WebP under 200KB.
3. **Hero image:** all 3 pack mockups together, on a marigold-50 block. If a real photo of a parent and child at a kitchen table with the printed pages becomes available, use that (Lovevery, KiwiCo, and BLJ all lead with real kids). Only use real photos the owner has rights to. No stock "diverse kids laughing" photos, and no AI images of children.
4. **Banned:**
   - Abstract sketch drawings standing in for the product (the "Random pages / Too hard" pile).
   - Three.js or 3D floating pages.
   - Blurred gradient blobs and text laid over images.
   - Scroll-pinned animations.
   - Fade-ins on anything above the fold.
5. **Allowed motion:** 150–200ms hover and press states, and the gallery swipe. That's it. Remove GSAP ScrollTrigger and Lenis smooth scroll. Keep Three.js only if something genuinely needs it (nothing does).

---

## 4. Homepage: 6 sections, in this order
Target: phone page height **≤ 6,000px** (now 10,300px). Placeholder word limits are maximums.

1. **Hero**: ~1 phone screen.
   - Phone order: H1 (≤8 words) → lead (≤20 words) → primary button full width → one plain line "$3.99 per pack · Print at home" (14–17px, navy) → mockup image (4:3) below.
   - Desktop: 2 columns. Text on the left (520px), image on the right on a tint block. Hero height 560–640px.
   - **The H1, lead, and button must all be visible in the first 844px on an iPhone.**
   - Ref: `patterns/lovevery-hero-m.png`, `patterns/beast-hero-m.png`, `patterns/refactoringui-hero-d.png`.
2. **Problem → fix** (white band):
   - An H2 (≤8 words), then a 2-column comparison table (stacked on phone): "[Without a plan]" vs "[With Proud Little Learners]", 3 rows each, each ≤8 words, with a ✕ (coral) or ✓ (teal) icon.
   - Next to or under it, one image: a real practice page beside the next-level page.
   - Max 60 words total.
3. **Pick your level** (cream):
   - An H2, the level picker chips (2.3), and 3 product cards (2.2).
   - This is the main buying section, and the hero button jumps here.
4. **Look inside** (white):
   - An H2, the page gallery strip (2.6), then the "In every pack" list (2.4) with 5 rows (practice pages, answer keys, parent guide, tracker, certificate).
5. **Weekly plan** (**navy band**, white text):
   - 2 columns. On the left an H2, 3 check bullets (≤8 words each), "$3.99/month" in price-lg, a primary button (marigold background, navy text on navy band), and one line "Cancel anytime" (14px).
   - On the right, a stack of weekly packet mockups.
   - Ref: Lovevery's subscription framing.
6. **FAQ**:
   - 5 questions maximum, in an accordion. Each answer ≤40 words.
   - Then the footer.

**Delete from home:**
- The scroll intro ("story", 4,800px).
- "The hard part" sketch card.
- "What 10 minutes tonight looks like" (fold one line into section 2 if the copy owner wants it).
- The quiz card.
- The duplicate "Single pack / one level, once" price card and its link list.
- "Why the pages are set up this way" (move to the Approach page).
- "Who makes these pages", which has placeholders.
- "Coming next".

---

## 5. Product page layout (all 3 packs and weekly.html use this template)
**Phone order (all of steps 1–5 must sit within the first ~1.3 screens):**
1. Breadcrumb at 14px, *with* 20px side padding. It's currently flush with the screen edge.
2. **Gallery:**
   - One 4:5 image (the cover mockup) on the level tint, swipeable.
   - A row of 64px thumbnails underneath (cover, 3 inside pages, parent guide, tracker).
   - Ref: `patterns/blj-product-m.png`.
3. Level badge, H1 at 32px phone / 44px desktop (smaller than the home display), and one line of ≤15 words.
4. Price `price-lg`, **alone** on its line.
5. Primary button, full width.
6. Three check bullets: "[18 practice pages]", "[Answer keys]", "[Parent guide]".
7. "[Right level?]" box: a marigold-50 card with 2 lines ("Start here if…"), plus links to the other 2 levels.
8. **Look inside**: the gallery strip (more pages).
9. **What's included**: the 2.4 list, 5 rows.
10. **Details** accordion (closed): format (PDF, US Letter, B&W), delivery, license, refunds. *All the current "About this pack" mini-cards go here as one compact table.*
11. FAQ: 3 questions.
12. "Other levels": 2 product cards (2.2).

**Desktop:**
- 2 columns, 7/5 split.
- The left gallery is sticky (`position: sticky; top: 88px`).
- The right column holds items 3–7 (the buy box), max 460px.
- Sections 8+ run full width below.
- Ref: `patterns/yoto-product-d.png`. TPT (`patterns/tpt-product-d.png`) shows the same layout.

**weekly.html** uses the same template:
- Gallery of weekly packet mockups.
- Title, then "$3.99/month", then the button, then 3 bullets.
- "Weeks 1–8" as a compact 2-column checklist (not a long list).
- Billing terms appear once, inside the Details accordion and at checkout. **Not** in bold next to the price.

---

## 6. The current site's 10 worst design problems, and the exact fixes

1. **Desktop opens with a 4,800px scroll-jacked animation.**
   - Problem: Three.js/GSAP pinned "story" section. Headlines change as you scroll and a worksheet covers the giant "NO DIFFICULTY jumps" text. Most visitors see what looks like a broken, empty page. (`patterns/current-scrolljack-d.png`, `patterns/current-scrolljack2-d.png`)
   - **Fix:** Delete the `#story` section and the Three.js, GSAP, and Lenis bundles. Build a static hero as in §4.1.
2. **Product page: the title, price, and buy button are ~3,400px down on a phone,** below 4 full-size worksheet images. (`patterns/current-product-m.png`)
   - **Fix:** Use the §5 template. Gallery carousel with thumbnails, and the buy box within ~1.3 screens.
3. **Pack cards have no picture of the product.** They are text-only white boxes. (`patterns/current-packcards-m.png`)
   - **Fix:** Card spec §2.2 with a 4:3 mockup on the level tint. Picture first, ≤12-word line, price, then the button.
4. **Fine print and "+ tax" next to every price.** "$3.99 (+ tax where applicable)" wraps to 2 lines, and the weekly card has a 6-line bold billing paragraph. (`patterns/current-pricing-m.png`)
   - **Fix:** Show the price alone. Billing terms go in the Details accordion on weekly.html, the Terms page, and Payhip checkout. At most one 14px line "Cancel anytime" under the weekly button.
5. **Gray "Checkout opens soon" buttons look broken.**
   - **Fix:** Only teal or marigold primary buttons. Don't publish without checkout links. Add a build check that fails when any `checkoutUrls` value is empty.
6. **The type is small, thin, and gray.** 27px Fraunces 500 serif H1 on a phone and 16px #5A6B78 body. It reads like a law firm, not a kids' brand. Every top kids' site uses a 700-weight sans at 28–40px on phones.
   - **Fix:** The §1.2 scale. Nunito 800 headings at 36px phone, body 17px in navy.
7. **Placeholder text is live:** "[Your name]" and "[A few sentences in your own words…]". (`patterns/current-placeholder-m.png`)
   - **Fix:** Delete the "Who makes these pages" block until real text exists. Add a build check that fails on `[` + `Your` patterns.
8. **Too long and repetitive.** 10 sections, a 10,300px phone page, levels explained 4 times (quiz, cards, price card, link list), and the weekly plan explained 3 times.
   - **Fix:** The 6-section order in §4. Each idea appears once. Target ≤6,000px on a phone.
9. **The product doesn't look like a product.** Covers and previews are plain black-and-white documents with no color, cover design, or mockup. They look like free worksheets, so $3.99 feels unjustified.
   - **Fix:** §3. Designed full-color covers, fanned mockups on tint blocks, and the same mockup used on cards, the hero, the product gallery, and ads.
10. **Weekly page is a wall of text with no picture.** About 220 words in one column, an 8-item list, a repeated "Which is right for me?" paragraph, and bold billing text. A gray button and the footer fill half the desktop screen. (`patterns/current-weekly-d.png`)
    - **Fix:** The §5 product template, a weekly mockup gallery, 3 bullets, and a compact 2-column week list.

**Smaller fixes (do them in the same pass):**
- Remove uppercase eyebrow labels ("KINDERGARTEN ADDITION", "THE HARD PART").
- The mobile "Menu" text button becomes a hamburger icon.
- The breadcrumb has 0px side padding.
- Footer text is 13px; raise it to 14px.
- Remove "01 INTRO" and the "SCROLL" indicators.
- The "Random pages / Too hard" sketch drawing is replaced by §4.2.
- Desktop nav has 6 links; cut it to 3.
- Body paragraphs run up to ~75 characters wide; cap them at 60ch.

---

## 7. Acceptance checklist (the engineer checks this before shipping)
- [ ] At 390×844: H1, lead, and primary button visible without scrolling on home and on every product page (price included on product pages).
- [ ] No text under 14px. No gray body paragraphs. No Fraunces.
- [ ] No gradients, blobs, scroll-pinned sections, Three.js, GSAP, or Lenis.
- [ ] Every product card and product page has a color mockup image.
- [ ] No "+ tax", no billing paragraph next to prices, no gray or disabled buttons, no `[placeholder]` text.
- [ ] Home has ≤6 sections between header and footer. Phone page height ≤6,000px.
- [ ] Only spacing values from §1.3. Only colors from §1.1.
- [ ] Lighthouse mobile performance ≥90, accessibility ≥95. Images WebP, lazy-loaded below the fold.
- [ ] Screenshot home, one product page, and weekly at 390 and 1280. Compare against `board.png` before shipping.

Not allowed anywhere: fake reviews, star ratings, customer counts, "award-winning" or press badges, free offers or samples, and fine print near prices.
