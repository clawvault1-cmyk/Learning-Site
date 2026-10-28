# Proud Little Learners: final site copy deck
Copy chief · Tue Oct 27, 2026, 11:20 PM ET · replaces every visible word on proudlittlelearners.com

## How to use this file (engineers)
- Format: `page > section > element (selector)` → **exact text**. Replace 1:1. Don't add words.
- **DELETE** means remove the element and its text from the HTML (not just hide it).
- Anything on a page that isn't listed here should be deleted.
- `[Checkout]` = the existing buy-button behavior. Empty link: button reads **Checkout opens soon** with the note **Checkout opens soon. No payment is taken yet.** under it. Live link: button reads the label shown here.
- Prices are only ever **$3.99** or **$3.99/month**. **Never** show "+ tax", "(+ tax where applicable)", "/mo", or "once" next to a price. Taxes can stay in the Terms body only.
- The weekly plan's only name is **Weekly Kindergarten Math Plan** everywhere (this replaces "Weekly Packet Plan: Kindergarten Math" and "Weekly · kindergarten"). Use the same name in Payhip.
- Pack names, always exactly like this:
  - **Beginner: Adding within 5**
  - **Intermediate: Adding within 10**
  - **Advanced: Story problems within 10**
- Level badges, always exactly like this: **Level 1**, **Level 2**, **Level 3**. They replace the "Beginner / Intermediate / Advanced" badges, which just repeated the name.

## Global strings (every page)
| Where | Text |
|---|---|
| Header > logo (a.logo) | **Proud Little Learners** |
| Header > menu button (.nav-toggle) | **Menu** |
| Header > nav item 1 | **Packs** → `index.html#packs` |
| Header > nav item 2 | **Weekly plan** → `weekly.html` |
| Header > nav item 3 | **Questions** → `faq.html` |
| Header > nav item 4 | **Contact** → `contact.html` |
| Header > nav | DELETE "Home" (the logo goes home), "How it works", "Kindergarten packs", and "Plans and prices" |
| Skip link (a.skip) | **Skip to content** |
| Footer > tagline (under brand) | **Printable kindergarten math for parents.** |
| Footer > column 1 heading | **Shop** |
| Footer > column 1 links | **Packs** (index.html#packs) · **Weekly plan** (weekly.html) |
| Footer > column 2 heading | **Help** |
| Footer > column 2 links | **Questions** · **Contact** · **Cancel weekly plan** (cancel.html) |
| Footer > column 3 heading | **About** |
| Footer > column 3 links | **About us** (about.html) · **How we teach** (our-educational-approach.html) · **Parent tips** (resources/index.html) |
| Footer > column 4 heading | **Policies** |
| Footer > column 4 links | **Privacy** · **Terms** · **Refunds** |
| Footer > p.fine | **© 2026 Proud Little Learners** (DELETE "For parents, caregivers, and teachers. We do not knowingly collect information from children." That line belongs in the Privacy body, where it already is.) |
| Footer | DELETE the duplicate "Kindergarten Math" and "Plans and prices" links |
| Every page, every in-page link row like "Terms · Refunds · Cancel · Contact" | DELETE (the footer covers it) |
| config.js `availability` | **Checkout opens soon. No payment is taken yet.** (unchanged) |

---

## PAGE: Homepage (index.html)
- `<title>`: **Kindergarten Math Printables for Parents | Proud Little Learners**
- meta description: **Help your kindergartner with math at home. Printable pages in small steps, with a parent guide that tells you what to say. $3.99 a pack.**

The order on the page, top to bottom: Hero → Problem → 10 minutes → Packs and quiz → What's inside → Plans → Questions → Final call. Nothing else.

### 1. Hero
| Element | Text |
|---|---|
| div.bigtype "No difficulty jumps." | DELETE |
| span.eyebrow | **Kindergarten math** |
| h1.display | **Help your kindergartner with math, step by step.** |
| p.lead | **Printable pages in the right order, with a short guide that tells you what to say. About 10 minutes a day.** |
| a.btn.mag | **Find my child's level** → `#packs` |
| Small line under the button (new p.micro) | **$3.99 a pack. Print it tonight.** |

### 2. Scroll scene (the 3D stack, level ticker, and progress ring)
| Element | Text |
|---|---|
| span.lt-title "Three levels." + ticker li "Level 1 within 5 / Level 2 within 10 / Level 3 stories" | DELETE |
| The three h2.display pack names inside the scene | DELETE (the pack cards below show them) |
| p.jump-lead "No big jumps. Just the next step." | DELETE |
| h2.display "Three levels." | DELETE |
| Floating a.pack chips (if the scene keeps them) | **Beginner: Adding within 5 · $3.99** / **Intermediate: Adding within 10 · $3.99** / **Advanced: Story problems within 10 · $3.99** / **Weekly Kindergarten Math Plan · $3.99/month** |
| div.progress "01 Intro" + div.scroll-hint "Scroll" | DELETE |

### 3. The problem (#problem)
| Element | Text |
|---|---|
| span.eyebrow "The hard part" | DELETE |
| h2.display | **Sound familiar?** |
| Line 1 (p, or li in a 3-item list) | **You want to help, but you don't know what to practice first.** |
| Line 2 | **Free worksheets online jump from too easy to too hard.** |
| Line 3 | **Your child gets stuck, and practice turns into a fight.** |
| Old p.lead "A lot of worksheets online are a random mix…" | DELETE (lines 1–3 replace it) |
| Old p "These packs stay in order…" → replace with p.fix (bold) | **Our packs fix that. Each page is one small step past the last one, and the guide tells you what to say when your child gets stuck.** |
| Picture > pile labels (div.pile-page .p1/.p2/.p3) | **Too easy** / **Too hard** / **Skips ahead** (replaces "Too hard / Subtract / Random". "Subtract" made no sense.) |
| Picture > left h3 | **Random worksheets** |
| Picture > left p | **Too easy, then too hard.** |
| Picture > right list | **1. Adding within 5** / **2. Adding within 10** / **3. Story problems** |
| Picture > right h3 | **Our packs** |
| Picture > right p | **One small step at a time.** |

### 4. What 10 minutes looks like (#how)
| Element | Text |
|---|---|
| h2.display | **What 10 minutes looks like** |
| Card 1 h3 / p | **Print one page.** / **Use the pack that fits what your child can do now.** |
| Card 2 h3 / p | **Show it, then do it together.** / **Count real things first, like cereal or buttons. Then try the page.** |
| Card 3 h3 / p | **Let your child try.** / **If they get stuck, the guide tells you what to say. Then they color a star on the tracker.** |

(The three cards follow "I show you, we do it together, you try". The research idea is named in plain words and nowhere else on the homepage.)

### 5. Packs and quiz (#packs)
| Element | Text |
|---|---|
| h2.display | **Pick a starting level** |
| p.lead | **$3.99 each. Yours to keep.** |
| p.weekly-line "Not sure? $3.99 a month gets…" | DELETE (it clashed with the quiz, which also says "Not sure?") |
| Card 1 span.badge | **Level 1** |
| Card 1 h3 | **Beginner: Adding within 5** |
| Card 1 p (what) | **Count two small groups and put them together.** |
| Card 1 p (fit) | **Start here if your child can count to 10.** |
| Card 1 p.price | **$3.99** |
| Card 2 span.badge | **Level 2** |
| Card 2 h3 | **Intermediate: Adding within 10** |
| Card 2 p (what) | **Turn pictures into problems like 4 + 3 = 7.** |
| Card 2 p (fit) | **Start here if adding up to 5 is easy.** |
| Card 2 p.price | **$3.99** |
| Card 3 span.badge | **Level 3** |
| Card 3 h3 | **Advanced: Story problems within 10** |
| Card 3 p (what) | **Solve short story problems you read out loud.** |
| Card 3 p (fit) | **Start here if adding up to 10 is easy.** |
| Card 3 p.price | **$3.99** |
| Quiz h3 | **Not sure? Answer 3 quick questions.** |
| Quiz buttons | **Yes** / **Not yet** |
| app.js steps[0].q | **Can your child count 5 things, like 5 pieces of cereal?** |
| app.js steps[1].q | **Can your child add 2 + 1 with a little help or none?** (replaces the fingers question. Using fingers is normal in kindergarten.) |
| app.js steps[2].q | **Is adding up to 10, like 4 + 3, easy for your child?** |
| app.js result heading (qEl after finish) | **Start here:** |
| app.js rec.beginner.why | **Your child will count two small groups and put them together.** |
| app.js rec.intermediate.why | **Your child will turn pictures into problems like 4 + 3.** |
| app.js rec.advanced.why | **Your child will solve short story problems you read out loud.** |
| app.js result link / reset | **See this pack** / **Start over** |
| p.which "Which is right for me? Single pack…" | DELETE |

### 6. What's inside (#inside)
| Element | Text |
|---|---|
| h2.display | **What's in each pack** |
| p.lead | DELETE |
| figcaptions 1–4 | **Practice page** / **Practice page** / **Parent guide** / **Progress tracker** |
| List (new ul, 4 items) | **18 practice pages, from easy to a little harder** / **An answer key for every page** / **A 2-page parent guide: what to say and when to move on** / **A progress tracker and a certificate** |
| Small line | **Black-and-white PDF. Prints on regular paper.** |

### 7. Plans (#plans): move this whole block here, below "What's inside"
| Element | Text |
|---|---|
| h2.display | **One pack, or a new one every week** |
| Card A span.badge | **One pack** |
| Card A h3 | **One level** |
| Card A p.price | **$3.99** |
| Card A p | **Pay once. Yours to keep.** |
| Card A list (3 li) | DELETE (the cards above already list the packs) |
| Card A button | **Pick a level** → `#packs` |
| Card B span.badge | **Weekly plan** |
| Card B h3 | **Weekly Kindergarten Math Plan** |
| Card B p.price | **$3.99/month** |
| Card B p | **A new packet every Monday. Get this month's packets right away.** |
| Card B p.renew-note (whole long paragraph) | Replace with: **Renews monthly. Cancel anytime.** |
| Card B a.btn.buy | [Checkout] live label: **Start the weekly plan** |
| p.status-line.pay-note | **Checkout opens soon. No payment is taken yet.** (one copy only, under the plan cards) |

### 8. DELETE these homepage sections entirely
- **"Why the pages are set up this way"** (h2 + paragraph + "Read the learning ideas" link). The 10-minute cards now say this in plain words.
- **"Who makes these pages"** with "[Your name]" / "[A few sentences…]". These placeholders are visible to buyers right now. Put it back only after the owner writes it.
- **"Coming next"** (h2 + paragraph).

### 9. Questions (#questions)
| Element | Text |
|---|---|
| h2.display | **Questions parents ask** |
| Q1 summary | **I'm not a teacher. Can I do this?** |
| Q1 answer | **Yes. The guide tells you what to say, and every page has an answer key.** |
| Q2 summary | **Which pack should we start with?** |
| Q2 answer | **Beginner: Adding within 5, if your child can count to 10. Not sure? Take the 3-question quiz above.** |
| Q3 summary | **My child doesn't like worksheets. Will this help?** |
| Q3 answer | **The pages are short, and you start with real things like cereal before the paper. Do one page, stop while it's going well, and do the next one tomorrow.** |
| Q4 summary | **How do I get it?** |
| Q4 answer | **You get a download link right after you pay, plus an email with the same link. Print at home.** |
| Q5 summary | **What's the difference between a pack and the weekly plan?** |
| Q5 answer | **A pack is one level for $3.99, and you keep it. The weekly plan is $3.99/month for a new packet every Monday. Cancel anytime.** |
| Old "What if a page feels too hard?" and "What do I get?" | DELETE (the guide and "What's inside" cover them) |
| Link (p.reveal "More questions") | **More questions** → faq.html |

### 10. Final call (new section #start, right above the footer)
| Element | Text |
|---|---|
| h2.display | **Give your child the head start they deserve.** |
| p | **About 10 minutes a day, one small step at a time.** |
| a.btn | **Find my child's level** → `#packs` |

---

## PAGES: Product pages (same layout for all three)
Order on the page: Top block → What's inside → What your child will practice → How you help → When to move on → Other levels.

**DELETE on all three:**
- The whole "About this pack" grid: Activity pages, Supporting pages, Skills, Before you start, File and paper, Printing, What you receive, What you need, License, Delivery, and Help. Each item is replaced below or covered by the footer.
- "Is this a suitable starting point?" and "How does practice progress?"
- The "full kindergarten path" list (Count groups / Combine / Pictures to equations / Simple stories). Its highlighting didn't match the pack.
- The second "What's included?" list and p.micro.
- "Learning goals" with the K.OA codes.
- Breadcrumb "Home › Kindergarten Math". Use **Packs** → `../index.html#packs` instead.

**Shared elements (all three pages):**
| Element | Text |
|---|---|
| p.price | **$3.99** |
| a.btn.buy | [Checkout] live label: **Buy now** |
| p.status-line.pay-note | **Checkout opens soon. No payment is taken yet.** |
| h2 "What's inside" | **What's inside** |
| What's inside list | **18 practice pages** / **An answer key for every page** / **A 2-page parent guide** / **A progress tracker and a certificate** / **Black-and-white PDF for regular paper** / **You'll need a pencil and small things to count, like cereal or buttons** |
| Line under list (p.small) | **Download right after you pay. Print for your family or one classroom.** |
| h2 | **What your child will practice** |
| h2 | **How you help** |
| h2 | **When to move on** |
| h2 "Other levels" | **Other levels** |
| Other-level cards | badge **Level N** · h3 exact pack name · p **$3.99** |
| Last line on page (new p, above footer) | **These are kindergarten skills from the Common Core math standards.** |

### Beginner (products/k-addition-beginner.html)
| Element | Text |
|---|---|
| `<title>` | **Beginner: Adding within 5 | Proud Little Learners** |
| meta description | **Kindergarten math printables. Your child counts two small groups and puts them together, with totals up to 5. Parent guide and answer keys included. $3.99.** |
| span.badge | **Level 1** |
| h1 | **Beginner: Adding within 5** |
| p (sub) | **Your child counts two small groups and puts them together.** |
| p.fit (new, under price) | **Start here if your child can count to 10.** |
| Practice p | **A page shows 2 dots and 1 more dot. Your child counts them all and writes 2 + 1 = 3. Totals stay at 5 or less. The last pages have a short story problem you read out loud.** |
| How you help p | **Sit next to your child. Ask, "Point to the two groups. How many in all?" If they get stuck, count the first group together, then let them count the rest.** |
| When to move on p | **Move to Intermediate: Adding within 10 when these pages feel easy. If you're still helping on most problems, do a few pages again.** |

### Intermediate (products/k-addition-intermediate.html)
| Element | Text |
|---|---|
| `<title>` | **Intermediate: Adding within 10 | Proud Little Learners** |
| meta description | **Kindergarten math printables. Your child turns pictures into problems like 4 + 3 = 7, with totals up to 10. Parent guide and answer keys included. $3.99.** |
| span.badge | **Level 2** |
| h1 | **Intermediate: Adding within 10** |
| p (sub) | **Your child turns pictures into problems like 4 + 3 = 7.** |
| p.fit | **Start here if adding up to 5 is easy.** |
| Practice p | **Your child goes from counting pictures to writing the problem, like 4 + 3 = 7. Some pages use a box with 10 spaces so numbers up to 10 are easy to see. Totals stay at 10 or less.** |
| How you help p | **Point to the bigger number and say it. Then count on together: "4… 5, 6, 7." Let your child do the next one. If the 10-space box is new, fill it with cereal first.** |
| When to move on p | **Move to Advanced: Story problems within 10 when adding up to 10 feels easy. If your child is still guessing, do a few pages again.** |

### Advanced (products/k-addition-advanced.html)
| Element | Text |
|---|---|
| `<title>` | **Advanced: Story problems within 10 | Proud Little Learners** |
| meta description | **Kindergarten math printables. Short story problems you read aloud, plus making 10 and finding missing numbers. Parent guide and answer keys included. $3.99.** |
| span.badge | **Level 3** |
| h1 | **Advanced: Story problems within 10** |
| p (sub) | **Your child solves short story problems you read out loud.** |
| p.fit | **Start here if adding up to 10 is easy.** |
| Practice p | **Your child splits a number into two parts, like 7 is 4 and 3. They find a missing number, like 4 + ? = 7, and what makes 10. Then they solve short stories, like "3 ducks swim. 2 more come. How many now?" You read the stories, and your child doesn't need to read.** |
| How you help p | **Act out the story with cereal or toys. Ask "What's happening?" before "How many?" If a missing number is hard, go back to two groups your child can see.** |
| When to move on p | **When these pages feel easy, your child has finished all three levels. If missing numbers are still hard, do a few pages again.** |

### Old bundle page (products/k-addition-bundle.html) and free-printables.html
| Element | Text |
|---|---|
| `<title>` | **Page moved | Proud Little Learners** |
| meta description | **This page has moved.** (Also add `<meta name="robots" content="noindex">` and remove both pages from sitemap.xml.) |
| h1 | **This page moved** |
| p | **See the kindergarten math packs.** → `index.html#packs` |

Note: "free-printables" can't appear in any visible text. There are no free offers.

---

## PAGE: Weekly plan (weekly.html)
| Element | Text |
|---|---|
| `<title>` | **Weekly Kindergarten Math Plan | Proud Little Learners** |
| meta description | **A new printable kindergarten math packet every Monday, plus this month's packets right away. $3.99/month. Cancel anytime.** |
| span.badge | **Weekly plan** |
| h1 | **Weekly Kindergarten Math Plan** |
| p.lead | **A new printable math packet every Monday. Get this month's packets right away.** |
| p.which "Which is right for me?…" | DELETE |
| p.price | **$3.99/month** |
| a.btn.buy | [Checkout] live label: **Start the weekly plan** |
| Small line under button (replaces the whole p.renew-note) | **Renews monthly. Cancel anytime.** |
| p.status-line.pay-note | **Checkout opens soon. No payment is taken yet.** |
| h2 (new) | **What's in each packet** |
| p (replaces "Eight kindergarten packets are written…") | **7 or 8 practice pages, answer keys, a short parent guide, and a tracker.** |
| h2 (new) | **The first 8 weeks** |
| list | **Week 1: Counting to 5** / **Week 2: Counting to 10** / **Week 3: More and fewer** / **Week 4: Adding within 5** / **Week 5: Story problems within 5** / **Week 6: Adding within 10** / **Week 7: Taking away within 5** / **Week 8: Shapes and patterns** |
| p ("Reading and other grades are coming next. See the three kindergarten packs.") | Replace with: **Want just one level? See the packs.** → `index.html#packs` |
| "Terms · Refunds · Cancel" row | DELETE |

---

## PAGE: Questions (faq.html)
- `<title>`: **Questions | Proud Little Learners**
- meta description: **Answers about which pack to pick, how to help, downloads, the weekly plan, and refunds.**
- h1: **Questions**

| # | summary | answer |
|---|---|---|
| 1 | **Which pack should we start with?** | **Beginner: Adding within 5, if your child can count to 10. Move up when the pages feel easy.** |
| 2 | **I'm not a teacher. Can I do this?** | **Yes. The 2-page guide tells you what to say. Every page has an answer key.** |
| 3 | **How much should I help?** | **Show one problem, do the next one together, then let your child try. Help less as it gets easier.** |
| 4 | **What if a page is too hard?** | **Stop and count real things, like cereal, instead. Or go back a few pages. Try again tomorrow.** |
| 5 | **When should we move on?** | **When your child does most of a pack with little help. One easy page isn't enough to tell.** |
| 6 | **My child doesn't like worksheets. Will this help?** | **The pages are short, and you start with real things before the paper. Do one page and stop while it's going well.** |
| 7 | **Is any of this on a screen?** | **No. You print the pages, and your child uses a pencil.** |
| 8 | **What's in a pack?** | **18 practice pages, 18 answer keys, a 2-page parent guide, a cover, a progress tracker, and a certificate.** |
| 9 | **How do I get my files?** | **Right after you pay, you see a download page. You also get an email with the link. Check spam if you don't see it.** |
| 10 | **How does the weekly plan work?** | **It's $3.99/month. You get this month's packets right away, then a new one every Monday. Cancel anytime. When you cancel, access ends, so download the packets you want to keep.** |
| 11 | **How do I cancel?** | **Sign in to your account and cancel, or email us. See how to cancel.** (link → cancel.html) |
| 12 | **Can I share the files?** | **You can print them for your family or one classroom. Please don't share or sell the files.** |
| 13 | **Can I get a refund?** | **If a file doesn't work or isn't what we described, we'll fix it. If we can't, we'll refund you. If you're new to the weekly plan and cancel within 7 days of your first charge, we'll refund that charge. See our refund policy.** (link → refund-policy.html. Keep this answer matched to Refund Policy section 1.) |

**DELETE:** "Why an organized pack instead of a loose page?", "How do I choose a grade?", "What format are the worksheets?" (merged into 8 and 9), "Is there a weekly plan?", "What learning standards and teaching methods inform the worksheets?", "Do you collect information from children?" (Privacy covers it), and every use of "scaffolding" and "IES".

---

## PAGE: Cancel (cancel.html)
| Element | Text |
|---|---|
| `<title>` | **Cancel the Weekly Kindergarten Math Plan | Proud Little Learners** |
| meta description | **Cancel the weekly plan online or by email.** |
| h1 | **Cancel the weekly plan** |
| p.lead | **When you cancel, billing stops and access ends. Download any packets you want to keep first.** |
| steps (ol li) | **Sign in** / **Go to Subscriptions** / **Click Cancel** |
| a.btn.buy | **Sign in to cancel** |
| app.js text when no sign-in URL | **Email us and we'll cancel for you.** |
| a.btn.alt | **Email us to cancel** |
| p | **Send the email address you signed up with. We'll cancel within 1 business day and email you when it's done.** |
| "Weekly plan terms · Refunds" row | DELETE |

## PAGE: Contact (contact.html)
| Element | Text |
|---|---|
| `<title>` | **Contact | Proud Little Learners** |
| meta description | **Email us with a question about a pack, a download, or the weekly plan.** |
| h1 | **Contact us** |
| p.lead | **Questions about a pack, a download, or the weekly plan? Email us.** |
| p | **hello@proudlittlelearners.com** (mailto link) |
| p | **We reply within 1 business day.** |
| p "For parents, caregivers, and teachers only." | DELETE |

## PAGE: About (about.html)
| Element | Text |
|---|---|
| `<title>` | **About Us | Proud Little Learners** |
| meta description | **We make printable kindergarten math packs that help parents practice at home, one small step at a time.** |
| h1 | **About us** |
| p.lead | **We make printable kindergarten math for parents who want to help at home but don't know where to start.** |
| h2 "Who makes these pages" + owner-note placeholders | DELETE until the owner writes it. **[OWNER]** Then use h2 **Who we are** and the owner's own 2–3 sentences. |
| h2 | **What you get** |
| li 1 | **Pages in the right order, so each one is a small step.** |
| li 2 | **A guide that tells you what to say.** |
| li 3 | **An answer key and a tracker, so you know when to move on.** |
| h2 "Where we are now" + p | DELETE |
| Closing p (new) | **Questions or ideas? Email hello@proudlittlelearners.com.** |

## PAGE: How we teach (our-educational-approach.html)
Replace the whole page with this. Delete everything else on it, including the eyebrow, the four-item list, the "Learning ideas behind the design" list, the sources table, and the whole reading section.
| Element | Text |
|---|---|
| `<title>` | **How We Teach | Proud Little Learners** |
| meta description | **The simple ideas behind our kindergarten math packs: real things, then pictures, then numbers.** |
| h1 | **How we teach** |
| p.lead | **Our packs use a few simple ideas that teachers use every day.** |
| h2 | **Real things, then pictures, then numbers** |
| p | **Your child counts cereal or toys first. Then dots on the page. Then numbers, like 2 + 1 = 3.** |
| h2 | **I show you, we do it together, you try** |
| p | **You show one problem. You do the next one together. Then your child tries alone. The guide tells you what to say at each step.** |
| h2 | **One small step at a time** |
| p | **Each page is just a little harder than the last. A child should feel sure of one step before the next.** |
| h2 | **Where these ideas come from** |
| list (links kept) | **Teaching Math to Young Children, a free guide from the U.S. Department of Education's research office (IES)** / **The Common Core kindergarten math standards** |

## PAGE: Packs (kindergarten-math.html)
| Element | Text |
|---|---|
| `<title>` | **Kindergarten Math Packs | Proud Little Learners** |
| meta description | **Three printable kindergarten math packs, $3.99 each: Adding within 5, Adding within 10, and Story problems within 10.** |
| breadcrumb, span.eyebrow | DELETE |
| h1 | **Kindergarten math packs** |
| p.lead | **Start with the level that fits your child. $3.99 each.** |
| h2 "Your child's next steps, already organized." + its 3-item list | DELETE |
| Pack cards | Use homepage section 5 card text exactly (badge, name, what, fit, price). Buttons: **See this pack** |
| p.weekly-line | DELETE |
| Weekly card | badge **Weekly plan** · h3 **Weekly Kindergarten Math Plan** · p **A new packet every Monday. Get this month's packets right away.** · price **$3.99/month** · button **See the weekly plan** |
| h2 "Coming soon" + all 3 coming-soon cards | DELETE |
| p.status-line | **Checkout opens soon. No payment is taken yet.** |

(The homepage now does this page's job. Fine to make this page redirect to `index.html#packs` instead.)

## PAGE: Parent tips (resources/index.html)
| Element | Text |
|---|---|
| `<title>` | **Parent Tips | Proud Little Learners** |
| meta description | **Short, plain guides for helping your kindergartner with math at home.** |
| Top nav | Use the global header. DELETE "Choose a Grade" (it links to a section that doesn't exist). |
| p.rs-kicker | DELETE |
| h1 | **Parent tips** |
| p | **Short guides for helping your child with math at home.** |
| Article 1 | **Is My Child Ready to Add?** · **Simple signs your kindergartner is ready, and what to do if they need more time.** |
| Article 2 | **Adding Within 5 vs. Within 10** · **What these mean, and when to move up.** |
| Article 3 | **How to Pick the Right Worksheet Level** · **How to find pages that aren't too easy or too hard.** |
| Article 4 | **How to Keep Practice From Turning Into a Fight** · **Ways to keep practice short and calm.** |
| Article 5 (CVC words) | DELETE from this list and sitemap. It's about reading, and we only sell math. The page can stay live, but don't link to it. |
| h2 "Want a plan that keeps going?" | **Want the next page ready for you?** |
| p | **Get a new kindergarten math packet every Monday.** (replaces "for the grade you pick". There's only one grade.) |
| buttons | **See the weekly plan** / **See the packs** → `../index.html#packs` |
| h2 "Sources" + list | DELETE (each article keeps its own source links) |
| Article bodies | Keep the article text, but apply the swap list below. The article h1s should match the titles above. |

## PAGES: Privacy, Terms, Refund Policy (headers only)
| Page | `<title>` | meta | h1 |
|---|---|---|---|
| privacy.html | **Privacy Policy | Proud Little Learners** | **What we collect, why, and who we share it with. We don't sell your information.** | **Privacy Policy** |
| terms.html | **Terms | Proud Little Learners** | **Terms for buying and using our printable packs and the weekly plan.** | **Terms** |
| refund-policy.html | **Refund Policy | Proud Little Learners** | **How refunds work for packs and the weekly plan.** | **Refund Policy** |
- Keep the section headings as they are. In all bodies, replace "Weekly Packet Plan" with **Weekly Kindergarten Math Plan**.
- **Terms: add this line** at the end of section 5 ("Content and educational information"): **Proud Little Learners is not affiliated with or endorsed by any school, school district, or standards organization.** This is the only place that line appears.

---

## Swap list (apply anywhere these appear: bodies, JS, alt text, JSON)
| Find | Replace with |
|---|---|
| (+ tax where applicable), + tax, plus tax where applicable | delete |
| /mo | /month |
| $3.99 once | $3.99 |
| Weekly Packet Plan: Kindergarten Math, Weekly Packet Plan, Weekly · kindergarten | Weekly Kindergarten Math Plan |
| scaffolding | help, then less help |
| manipulatives, counters | small things to count, like cereal or buttons |
| number sentence(s), equation(s) | problem(s), like 2 + 1 = 3 |
| ten-frame | a box with 10 spaces |
| zone of proximal development, research-informed, established learning standards | delete the sentence |
| A fit when | Start here if |
| Is this a suitable starting point? | delete |
| Coming soon (any skill or grade) | delete |
| products.js `pages:"TBD"` | `pages:41` |
| products.js summaries | Use the product-page sub lines exactly: Beginner **Your child counts two small groups and puts them together.** · Intermediate **Your child turns pictures into problems like 4 + 3 = 7.** · Advanced **Your child solves short story problems you read out loud.** |
| products.js coming-soon entries | delete (nothing on the site should show them) |
| app.js grade picker strings ("Pick a grade to begin…", "Math or reading?", "Choose a skill", "Coming soon. The weekly plan is where…", "Words a reader recognizes automatically, instantly.") | delete the dead grade-picker code. No page uses it. |

---

## Self-review: 3 parents on a phone (done, and the fixes are already in the copy above)
1. **Busy working mom, 30 seconds between things.** She needs to know what it is, what it costs, and how long it takes. The hero says "kindergarten math," "about 10 minutes a day," and "$3.99 a pack" above the fold. Fixed: the plan card used to have a 60-word renewal paragraph. It's now "Renews monthly. Cancel anytime."
2. **Dad who doesn't know what kindergarten math is.** "Adding within 5" means nothing to him. Fixed: every card says what the child actually does ("count two small groups and put them together") and gives one real example (2 + 1 = 3, 4 + 3 = 7, the ducks story). Removed "number sentence," "ten-frame," "K.OA," and "scaffolding."
3. **Parent of a kid who hates worksheets.** Fixed: the 10-minute cards and the FAQ say you start with real things like cereal before the paper, and you stop while it's going well. No promise of "no tears."

Read-aloud pass: I cut "Three levels." (said 3 times), "No big jumps. Just the next step.", "Use the parent line", "A fit when", "is sticky", "Pictures to equations", and every repeated "Checkout opens soon" except one per page.

## [OWNER] items this copy needs
- Owner bio for About (2–3 sentences). Hidden until then.
- Confirm the weekly plan's name in Payhip is exactly **Weekly Kindergarten Math Plan**.
- Legal note: "Renews monthly. Cancel anytime." next to the button is the shortest clear auto-renew notice. Keep it unless your lawyer says to add more.
