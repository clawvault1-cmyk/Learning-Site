# Site copy v4b: changed strings only
Copy chief, Oct 28 2026. Source: repo main, read through GitHub (shell curl kept failing its auto-check), plus live WebFetch checks.
Checked against: /workspace/copy/pack-facts-final.md and the final PDFs in /workspace/qa/pdfs3.
Format: page → selector → OLD → NEW. Anything not listed stays as it is.
Rules held: no new claims, bare prices, the exact pack and plan names, "Checkout opens soon", and the weekly terms lines untouched.

---
## 1. index.html (home): S2-3 fixes. Home goes from 323 to 328 words (limit about 330)

**#say p.method** (C1: the mini-book pages B p17, I p20 and A p17 have no I do / We do)
- OLD: Every page is "I do, we do, you do," a method many teachers use: you show one, do one together, then your child tries.
- NEW: Practice pages start with "I do, we do, you do": you show one, do one together, then your child tries.

**#say p (after the blockquote)** (matches the guide's own words, "Say the line, then wait.", and frees words)
- OLD: Then wait while your child counts.
- NEW: Then wait.

**#plans .plan-card p (line 112, under h2 "Weekly Kindergarten Math Plan")** (C2: who each is for. True: every weekly PDF is one new topic and has a 1-page note)
- OLD: A new packet every Monday, with a 1-page parent note.
- NEW: A pack: one skill, start to finish, yours to keep. The plan: a new topic every Monday, with a parent note.

**#problem, "Our packs" li 3** (the cover, guide pages, tracker and certificate have no key. Only practice pages have keys)
- OLD: An answer key for every page
- NEW: An answer key for every practice page

**#questions, answer to "I'm not a teacher. Can I do this?"**
- OLD: Yes. Every page has an answer key.
- NEW: Yes. Every practice page has an answer key.

**#packs .pack-card a.mock img (3 card images, now alt="")** (each image is the only thing inside a link, so the link has no name for screen readers)
- Beginner: alt="" → alt="A practice page from Beginner: Adding within 5"
- Intermediate: alt="" → alt="A practice page from Intermediate: Adding within 10"
- Advanced: alt="" → alt="A practice page from Advanced: Story problems within 10"

**#plans .plan-card a.mock img**
- OLD: alt="Weekly Kindergarten Math Plan"
- NEW: alt="A Week 1 practice page from the Weekly Kindergarten Math Plan"

Title and meta stay as they are.

---
## 2. products/k-addition-advanced.html

**The p that starts "Make 10, find missing numbers" (the third p after h1, following p.test and the "You read the stories out loud…" p)** (C3: the ducks story is not in the pack. Leo's story is word for word on Advanced practice page 15)
- OLD: Make 10, find missing numbers, and solve short stories, like "3 ducks swim. 2 more come. How many now?"
- NEW: Make 10, find missing numbers, and solve short stories, like "Leo has four balls. Leo gets two more. How many balls now?"

**details "When it's finished" p** (C6: the pack says "feel comfortable")
- OLD: When practice pages 16, 17, and 18 feel easy with only a little help. It's the last of the three addition packs.
- NEW: When practice pages 16, 17, and 18 feel comfortable with only a little help. It's the last of the three addition packs.

**Gallery .slide img alt** (the same change on all 3 product pages, using that page's pack name)
- alt="Parent guide" → alt="Parent guide from Advanced: Story problems within 10"
- alt="Practice page" (×5) → alt="Practice page from Advanced: Story problems within 10"
- alt="Progress tracker" → alt="Progress tracker from Advanced: Story problems within 10"

## 3. products/k-addition-intermediate.html

**p.test** (C6: the pack says "already feels comfortable")
- OLD: Start here if adding up to 5 already feels easy, like 2 toys and 3 toys.
- NEW: Start here if adding up to 5 already feels comfortable, like 2 toys and 3 toys.

**Gallery alts:** as in section 2, with "Intermediate: Adding within 10".

## 4. products/k-addition-beginner.html
**Gallery alts:** as in section 2, with "Beginner: Adding within 5". No other change.

## 5. assets/products.js (data only; the page doesn't show it)
- Intermediate `pages:41` → `pages:45`. The final PDF has 45 pages.

## 6. assets/app.js: the #pack-picker quiz (dead code: no page has #pack-picker)
Removing it is the better fix. If it stays, change:
- OLD: Can your child count 5 things, like 5 pieces of cereal?
- NEW: Can your child count 5 toys?
- OLD: Is adding up to 10, like 4 + 3, easy for your child?
- NEW: Can your child add 4 toys and 5 toys?

---
## 7. weekly.html

**"In each packet" p** (the PDFs have 7 practice pages in most weeks, 8 in weeks 6, 8 and 16, and 6 in weeks 12 to 14)
- OLD: 7 or 8 practice pages, answer keys, a 1-page parent note, and a tracker.
- NEW: 6 to 8 practice pages, answer keys, a 1-page parent note, and a tracker.

**Gallery .slide img alt** (in order: week-01 practice-01, week-02 practice-05, week-03 practice-01, week-01 practice-05)
- alt="Practice page" → alt="Week 1 practice page" / "Week 2 practice page" / "Week 3 practice page" / "Week 1 practice page"

Everything else stays, including the 2 terms lines under the button. "Get this month's packets today" is backed up by Terms §6 ("all packets we have released so far in the current calendar month").

---
## 8. faq.html

**"What if a page is too hard?" p** (cereal and "go back a page" are gone. Each guide names the page to go back to)
- OLD: Go back a page, or count real things like cereal. Try again tomorrow.
- NEW: Go back to the page the guide names. Try again tomorrow.

**"I'm not a teacher. Can I do this?" p**
- OLD: Yes. Every page has an answer key, and the guide is 2 short pages in plain words.
- NEW: Yes. Every practice page has an answer key, and the guide is 2 short pages in plain words.

**"My child doesn't like worksheets. Will this help?" p** (the old line was false: the pages start on paper, not with real things)
- OLD: The pages are short, and you start with real things. Stop while it's still fun.
- NEW: Each pack has cut-and-paste and a dice game. One page, about 10 minutes, then stop while your child is still willing.

**"Are weekly packets the same as the packs?" p** (the page counts were wrong, and weekly packets have a tracker too)
- OLD: No. A weekly packet has 7 or 8 practice pages and a 1-page note. A pack goes deeper on adding, with the full 2-page guide, a tracker, and a certificate. You keep it.
- NEW: No. A weekly packet is one topic, with 6 to 8 practice pages and a 1-page note. A pack goes deeper on adding, with the full 2-page guide and a certificate. You keep it.

No other changes. "How do I cancel?" already matches cancel.html, which offers both sign-in and email.

---
## 9. our-educational-approach.html

**meta description + og:description**
- OLD: The simple ideas behind our kindergarten math packs: real things, then pictures, then numbers.
- NEW: How our kindergarten math packs teach: pictures, then numbers, and the words to say.

**p.lead**
- OLD: Our packs use a few simple ideas that teachers use every day.
- NEW: Three simple ideas many teachers use.

**h2 1 + p** (the pages start on paper. Counters are optional. Real apples or blocks only if practice page 1 is hard)
- OLD h2: Real things, then pictures, then numbers
- NEW h2: Pictures, then numbers
- OLD p: Your child counts cereal or toys first. Then dots on the page. Then numbers, like 2 + 1 = 3.
- NEW p: Your child counts pictures on the page, then writes number sentences, like 2 + 1 = 3. If counting is hard, count real apples or blocks first.

**h2 2 + p**
- OLD h2: I show you, we do it together, you try
- NEW h2: I do, we do, you do
- OLD p: You show one problem. You do the next one together. Then your child tries alone. The guide tells you what to say at each step.
- NEW p: On practice pages, you do problem 1 out loud. You do problem 2 together. Your child does the rest. The guide gives you one line to say, then you wait.

**h2 3 + p** (the old p overclaimed "each page is just a little harder", but the stories start small again)
- OLD h2: One small step at a time
- NEW h2: Easy to harder
- OLD p: Each page is just a little harder than the last. A child should feel sure of one step before the next.
- NEW p: The pages go from easy to harder. If a page is a guess, the guide names the page to go back to.

The "Where these ideas come from" sources stay as they are.

---
## 10. resources/index.html
- If the two pages in §15 are deleted, remove the li "How to Pick the Right Worksheet Level…". Nothing else changes.

## 11. resources/addition-within-5-vs-addition-within-10.html

**meta description** (a bug: the quotes aren't escaped, so the live meta reads only "What ")
- NEW: content="What &quot;within 5&quot; and &quot;within 10&quot; mean, why the order matters, and how to know when your child is ready to move up."
- Apply the same to og:description if it has the same quotes.

**Intro p:** delete the filler sentence "These small phrases make a big difference in how a worksheet feels to your child."

**"How to tell your child is ready to move up," new p after the ul** (ties the article to the real pack rule)
- ADD: In our Beginner pack, the rule is simple: move up when the story pages (15 to 17) and practice page 18 are right with only a little help.

**"The big picture" p, last sentence** (removes an absolute)
- OLD: …is the best guide to when it's time to move on.
- NEW: …is a good guide to when it's time to move on.

**CTA p**
- OLD: If your child is ready, our Kindergarten Addition packs start with small sums and pictures, then move forward one step at a time. The weekly plan sends a new packet every week.
- NEW: Our three addition packs go in order, from adding within 5 to story problems within 10, with a guide for you. The weekly plan brings a new packet every Monday.

**a.rs-btn**
- OLD: See the Kindergarten Addition packs
- NEW: See the packs

## 12. resources/how-to-know-if-your-kindergartener-is-ready-for-addition.html

**Intro p, last sentence**
- OLD: The good news is that you can check readiness at home in a few minutes, with no tests and no pressure.
- NEW: You can check at home in a few minutes.

**"When you're ready to start," last p** (removes a promise of results)
- OLD: …Checking first means your child's first experience with addition is far more likely to be a success.
- NEW: …delete that last sentence.

**CTA p**
- OLD: If your child is ready, our Kindergarten Addition packs start with small sums and pictures, then move forward one step at a time. The weekly plan sends a new packet every week.
- NEW: A quick check: can your child count 5 toys? Start with Beginner: Adding within 5. The weekly plan brings a new packet every Monday.

**a.rs-btn**
- OLD: See the Beginner Addition pack
- NEW: See Beginner: Adding within 5

## 13. resources/how-to-help-your-child-practice-without-frustration.html

**meta description**
- OLD: Practical ways to keep at-home practice short, calm, and positive for kids ages 4 to 8.
- NEW: Simple ways to keep kindergarten math practice short and calm.

**§3 p** (one page is our rule)
- OLD: …like "two pages after breakfast on Saturdays,"…
- NEW: …like "one page after breakfast on Saturdays,"…

**§7 li 3** (a reading line in a math article)
- OLD: "Read me the sounds one more time."
- NEW: "Count them with me one more time."

**§8 p** (a reading example)
- OLD: …reading signs on a walk, or playing "I spy something that starts with /b/" all build the same skills.
- NEW: …or counting stairs on a walk all build the same skills.

**CTA p** (false: there is only one grade)
- OLD: The weekly plan sends a new packet every week for the grade you pick.
- NEW: The weekly plan brings a new kindergarten math packet every Monday.

**a.rs-btn.alt**
- OLD: Browse Kindergarten Addition
- NEW: See the packs

## 14. Legal pages (terms, privacy, refund)
I checked them for product facts only. Pack names, $3.99, $3.99 per month and the license all match. **No changes.** The tax sentence in Terms §2 is legal text and isn't next to a price shown to shoppers, so it stays.

## 15. 404 (none exists, so GitHub Pages shows its own default page)
New file /404.html, using the normal header and footer:
- title: Page not found | Proud Little Learners
- meta name="robots" content="noindex"
- h1: This page isn't here.
- p: <a href="/#packs">See the packs</a> or <a href="/weekly.html">the weekly plan</a>.

## 16. Footer (all pages)
No text change. "Printable kindergarten math for parents." stays, and all links resolve. If the pages in the delete list go, no footer link needs to change.

---
## Delete or redirect (recommendations)
1. **resources/cvc-words-explained-for-parents.html: DELETE.** It's live, but not in the sitemap and not linked anywhere. It's about reading, which we don't sell, and its CTA says "for the grade you pick", which is false.
2. **kindergarten-math.html: REDIRECT to /#packs.** It's a copy of the home chooser. Use the same noindex + meta-refresh stub as free-printables.html, and remove it from sitemap.xml.
3. **resources/how-to-choose-the-right-worksheet-difficulty.html: REDIRECT to /resources/.** It's generic, half of it is about reading, and it repeats the "within 5 vs 10" and "frustration" articles. If it stays, fix these: delete "For reading, do they know letter sounds? Can they blend three sounds into a word?"; change "isn't only about the math or reading" to "isn't only about the math"; change the button "See the Beginner Addition pack" to "See Beginner: Adding within 5". It's also linked from the frustration article, §1 ("choosing the right worksheet difficulty"). Drop that sentence if this page goes.
4. **free-printables.html and products/k-addition-bundle.html:** already noindex redirect stubs. They're fine as they are; they can be deleted later.
5. **LEGAL-REVIEW-NOTES.md, NOTES-design-research.md, README.md, build.py and packs/*.py/json are publicly served** (the deploy includes .nojekyll). I confirmed https://proudlittlelearners.com/LEGAL-REVIEW-NOTES.md is live. It shows internal legal notes, including an unpublished "Version B" guarantee, while claiming "They are not published." The engineer should exclude them from the Pages deploy (pages.yml).
