# Site copy v5: the brand reaches past kindergarten (final, revised against value-research.md)
Copy chief, Oct 28 2026, 8:50 PM ET. Built on the live index.html (the v4b home changes are already live).
Format: selector → OLD → NEW. Only changed strings are listed.

Rules this follows:
- Proud Little Learners is the brand for every grade. Kindergarten math is the first set, and it's the only thing for sale today.
- Nothing suggests other grades can be bought, and no dates are given.
- The pack names and "Weekly Kindergarten Math Plan" stay exactly as they are. Prices are just $3.99 and $3.99/month.
- No urgency, no "deserve", no promised results. Owner direction t35u and t36u is carried in fresh words ("start strong"), not the owner's own words.
- Home is 326 words (limit about 330; counted in /workspace/copy/v5count.py).

---
## A. HERO: 3 options, ranked (my pick first). Revised against value-research.md "Message hierarchy"
Hierarchy mapping: H1 = #1 (the parent's hope + about 10 minutes). Subline = #3 (we made the pages, easy to harder, words to say) + #5 (first up: kindergarten). The line under the hero = #2 (why it matters). The tracker (#4) is already in #problem. Prices (#5) are in #packs and #plans.
The research's own line, "head start", is NOT used: the owner (t35u) said not to use his words literally. "Start strong" carries the same hope, and it works for every grade.

**1. PICK**
- H1: Help your child start strong, in about 10 minutes a day.
- Subline: We made the printable pages, easy to harder, with the words to say. First up: kindergarten math.
- Button: Start with kindergarten math

**2.**
- H1: Ready-to-print pages that help your child start strong.
- Subline: Easy to harder, about 10 minutes a day, with the words to say. First up: kindergarten math.
- Button: Start with kindergarten math

**3.**
- H1: No time to make worksheets? We made them for you.
- Subline: Easy to harder, about 10 minutes a day, with the words to say. First up: kindergarten math.
- Button: Start with kindergarten math

Why #1:
- It leads with the parent's hope for the child, then the small time cost. That's the order of hierarchy #1.
- "We made the pages" speaks to the busy parent without blame.
- It covers every grade, and the subline makes clear that only kindergarten math exists today.

Why the others rank lower:
- #2 hides the 10 minutes in the subline.
- #3 is about the parent's problem, not the child's reason. It's a good fallback if the owner wants "busy" to come first.

Rejected:
- "excel", "head start", "stand out", "get ahead" (the owner's words, or a promised result)
- "Is your child falling behind?" (shaming; research §4)

**Selectors (option 1)**
- `.hero h1`: Kindergarten math help, without random worksheets. → Help your child start strong, in about 10 minutes a day.
- `.hero p.lead`: Short pages, easy to harder, with a guide for you. About 10 minutes a day. → We made the printable pages, easy to harder, with the words to say. First up: kindergarten math.
- `.hero a.btn` (href #packs stays): Find my child's level → Start with kindergarten math

## B. Section under the hero, #kids: answers "why does my child need this?" (t36u, hierarchy #2)
- `#kids .kids-line p`, OLD: Hates worksheets? Each pack has cut-and-paste and a dice game. One page, about 10 minutes, then stop.
- NEW: Early math skills are a strong sign of how kids do later in school. Each pack builds them one small step at a time.
- Why it's true:
  - Duncan et al. 2007, a study of 6 long-term studies, found that school-entry math skills predicted later achievement most strongly. We say only "a strong sign", and we don't claim our packs cause anything.
  - Engineer: add a source line to the FAQ: "Why start with math? Early math skills are one of the strongest signs of later school success (Duncan et al., 2007)." Link https://pubmed.ncbi.nlm.nih.gov/18020822/.
- "Hates worksheets? … cut-and-paste and a dice game" is cut to stay under the word limit. The 2 preview images and their alts ("Cut-and-paste page", "Dice game page") still show it.
- fix-4 C3 (only if layout makes the previews bigger): add captions "Cut and paste" and "Roll and add" under the images. Check them against the page titles in the PDFs first.
- I didn't add a tracker line here: the #problem list already says "A tracker and a clear 'move up' rule" (hierarchy #4).

## C. title, meta, og
- `<title>` and `og:title`: Kindergarten Math Help for Parents | Proud Little Learners → Proud Little Learners | Printable pages for kids, starting with kindergarten math
- `meta description` and `og:description`: Kindergarten math help without random worksheets. Short printable pages, easy to harder, with a guide for you. $3.99. → Help your child start strong in about 10 minutes a day. Printable pages, easy to harder, with the words to say. First up: kindergarten math, $3.99.

## D. Section intro above the 3 packs (#packs)
- `#packs h2` stays: Which one fits?
- `#packs p.lead`: Try these with real toys. Start with the hardest one your child can do. → Our first packs: kindergarten math. Start with the hardest one your child can do.
  - The toy tests on each card ("Can your child count 5 toys?") still carry the toy idea.
- `#packs` last p: Each pack: the full 2-page guide, answer keys, a tracker, and a certificate. Yours to keep and reprint. → Each pack: the 2-page guide, answer keys, a tracker, and a certificate. Yours to keep.

## E. "Coming next": a NEW section (nothing like it exists today)
Put it after `#plans` and before `#questions`: `<section id="next" class="sec"><div class="wrap">`
- h2: Coming next
- p: More grades, one at a time.
- No dates, no sign-up form, no "notify me". Add a sign-up only if the owner wants one later, and only once it really works.

## F. Other home changes (fix-4 and word budget)
- `#say p.method` (fix-4 C1: the mini-book pages, Beginner p17, Intermediate p20 and Advanced p17, have no I do / We do, so "Practice pages start with" is still false):
  - OLD: Practice pages start with "I do, we do, you do": you show one, do one together, then your child tries.
  - NEW: Most practice pages start with "I do, we do, you do": you show one, do one together, then your child tries.
- `#problem` "Our packs", li 5: delete "Print tonight". The closing section already says "Print one page tonight."
- `#plans .plan-card p`:
  - OLD: A pack: one skill, start to finish, yours to keep. The plan: a new topic every Monday, with a parent note.
  - NEW: Packs: one skill, start to finish, yours to keep. The plan: a new topic every Monday.
  - The 1-page parent note is still listed on weekly.html.
- `#questions`: delete the second details, "Is it on a screen?". It stays on faq.html. "Printable" is now in the hero subline.
- `#start a.btn` stays: Find my child's level

---
## G. Brand-wide spots that describe the brand as kindergarten-only
1. **Footer tagline, every page** (`footer.site .wrap > p`, the line after p.brand-name):
   - Printable kindergarten math for parents. → Printable learning pages for kids. Kindergarten math first.
2. **about.html**:
   - `p.lead`: We make kindergarten math pages for parents who want to help but don't know where to start. → We make printable learning pages for parents who want to help but don't know where to start. Kindergarten math is our first set.
   - `meta description` and `og:description`: Printable kindergarten math for parents who want to help at home. → Printable learning pages for parents who want to help at home. Kindergarten math is our first set.
   - The maker comment slot stays hidden, as it is now.
3. **og-share.png, used for link previews on every page.** This one is serious. The image says "Give your child the head start they deserve" ("deserve" is banned) and "Printable kindergarten math packets." The headline is also cut off at the right edge ("they deser…"). The designer should redo it:
   - Line 1: Proud Little Learners
   - Line 2: Help your child start strong.
   - Line 3: First up: kindergarten math.
4. **Product page titles** don't say kindergarten-only. Now that the brand is wider, they should say the grade:
   - `products/k-addition-beginner.html <title>` and `og:title`: Beginner: Adding within 5 | Proud Little Learners → Beginner: Adding within 5 (Kindergarten Math) | Proud Little Learners
   - Intermediate and Advanced: the same pattern.
   - Product meta lines already start "Kindergarten math printables:" and are fine.
5. **Nav** ("Packs", "Weekly plan", "Questions"): not kindergarten-only, no change.
   - Option: rename "Packs" to "Kindergarten math" so visitors see the grade. I'm not recommending it now; it makes the menu longer on mobile.
6. **Fine as they are:**
   - weekly.html title and meta (the plan really is kindergarten).
   - Terms §2 "packs for kindergarten math" (true today).
   - JSON-LD brand, config.js and the logo.
7. **kindergarten-math.html:** this changes my v4b advice. Instead of redirecting it, it can later become the kindergarten hub when other grades launch. For now, still redirect it to /#packs.

## H. fix-4 items outside home
- **our-educational-approach.html, second h2's p** (from v4b, now scoped to be fully true):
  - NEW: On most practice pages, you do problem 1 out loud. You do problem 2 together. Your child does the rest. The guide gives you one line to say, then you wait.
- **faq.html "I'm not a teacher" p** (same as v4b):
  - NEW: Yes. Every practice page has an answer key, and the guide is 2 short pages in plain words.
- **weekly.html "In each packet" p** (fix-4 C4: drop the number):
  - OLD: 7 or 8 practice pages, answer keys, a 1-page parent note, and a tracker.
  - NEW: Practice pages, answer keys, a 1-page parent note, and a tracker.
  - Why: the newest weekly PDFs on the box (/workspace/qa/pdfs3, 00:40) have 6 practice pages in weeks 12 to 14, 7 in most weeks, and 8 in weeks 6, 8 and 16. But nobody has confirmed that's the Payhip upload. So no number, until the owner confirms.
- **faq.html "Are weekly packets the same as the packs?" p**, for the same reason:
  - NEW: No. A weekly packet is one topic, with practice pages and a 1-page note. A pack goes deeper on adding, with the full 2-page guide and a certificate. You keep it.

## I. Status
- value-research.md appeared at 8:41 PM ET. The hero and #kids (A, B) are revised against its Message hierarchy.
- Owner calls still open:
  - Ok to use "start strong" (instead of "head start")?
  - Ok to cite Duncan 2007 in the FAQ?
  - The weekly page count.
  - New og-share.png text.
