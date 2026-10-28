# Proud Little Learners: site copy v2 (shorter)
Copy chief · Wed Oct 28, 2026, 6:50 PM ET · replaces site-copy.md and copy-fixes-r3.md for every page listed here

**How to apply:**
- Replace each string word for word.
- **DELETE** means remove the element.
- **Anything on these pages that isn't listed here gets deleted.**

**Locked words:**
- **Pack names:** "Beginner: Adding within 5" · "Intermediate: Adding within 10" · "Advanced: Story problems within 10".
- **Plan name:** "Weekly Kindergarten Math Plan".
- **Prices:** only "$3.99" or "$3.99/month", with nothing next to them.
- **Buy buttons:** say **Checkout opens soon** until a checkout link exists in config.js. At launch: **Buy now** (packs) / **Start the weekly plan** (weekly). Keep the existing note "Checkout opens soon. No payment is taken yet." (one per page, under the buy button).
- **Banned words:** "deserve", "proven", and any review, rating, or count claims.

**Header (all pages):** logo **Proud Little Learners** · nav **Packs** · **Weekly plan** · **Questions** (unchanged)
**Footer (all pages):** keep the current links. Tagline: **Printable kindergarten math for parents.** · **© 2026 Proud Little Learners**

---

## HOME (index.html)
- `<title>`: **Kindergarten Math Help for Parents | Proud Little Learners**
- meta description: **Not sure how to help with kindergarten math? Printable pages in the right order, with a guide that tells you what to say. $3.99.**

### section.hero
| Element | Text |
|---|---|
| h1 | **Not sure how to help with kindergarten math?** |
| p.lead | **Print pages in the right order. A short guide tells you what to say. 10 minutes a day.** |
| a.btn → #packs | **Find my child's level** |
| p.micro "$3.99 for 18 pages…" | DELETE (only the headline, subline, and button stay above the fold) |

### section#problem
| Element | Text |
|---|---|
| h2 | **Sound familiar?** |
| ul (3 li: "You want to help…", "Free worksheets…", "Your child gets stuck…") | DELETE (the ✗/✓ card says it) |
| p.fix | DELETE |
| Card left h3 | **Random worksheets** |
| Card left ✗ li 1 / 2 / 3 | **Where do I start?** / **Too hard, too fast** / **Ends in tears** |
| Card left ✗ li 4 ("You guess what's next") | DELETE |
| Card right h3 | **Our packs** |
| Card right ✓ li 1 / 2 / 3 | **Start at the right level** / **Small steps, in order** / **A guide tells you what to say** |
| Card right ✓ li 4 ("A tracker shows when to move on") | DELETE |

### section#how
| Element | Text |
|---|---|
| h2 | **10 minutes a day** |
| card 1 h3 / p | **Print one page.** / DELETE p |
| card 2 h3 / p | **Do it together.** / **Count cereal first, then the page.** |
| card 3 h3 / p | **Let your child try.** / **The guide tells you what to say.** |

### section#packs
| Element | Text |
|---|---|
| h2 | **Pick a starting level** |
| p.lead | **$3.99 each. Yours to keep.** |
| Card 1 | badge **Level 1** · h3 **Beginner: Adding within 5** · p **For kids who can count to 10.** · p.price **$3.99** · a.btn **See inside** |
| Card 2 | badge **Level 2** · h3 **Intermediate: Adding within 10** · p **For kids who can add up to 5.** · p.price **$3.99** · a.btn **See inside** |
| Card 3 | badge **Level 3** · h3 **Advanced: Story problems within 10** · p **For kids who can add up to 10.** · p.price **$3.99** · a.btn **See inside** |
| Each card's "what" line ("Count two small groups…", "Go from pictures…", "Make 10, find…") and old "Start here if" line | DELETE (one line per card now) |
| p under cards (new) | **Not sure? Email us. We'll help you pick.** (mailto on "Email us") |

### section#inside
| Element | Text |
|---|---|
| h2 | **In every pack** |
| li 1–4 | **18 practice pages** / **An answer key for every page** / **A 2-page parent guide** / **A tracker and a certificate** |
| p.micro (color/ink line) | DELETE (it stays on the product pages) |

### section#plans
| Element | Text |
|---|---|
| h2 | **Weekly Kindergarten Math Plan** |
| p | **A new packet every Monday. Get this month's packets today.** |
| p "Best if…" | DELETE |
| p.price | **$3.99/month** |
| a.btn → weekly.html | **See the weekly plan** |
| both p.cancel-line | DELETE here. This button only opens weekly.html, and the terms sit next to the real buy button there. |

### section#questions
| Element | Text |
|---|---|
| h2 | **Questions** |
| Q1 summary / answer | **I'm not a teacher. Can I do this?** / **Yes. The guide tells you what to say. Every page has an answer key.** |
| Q2 summary / answer | **My child doesn't like worksheets. Will this help?** / **The pages are short, and you start with real things like cereal. Stop while it's still fun.** |
| Q3 summary / answer | **Is it on a screen?** / **No. You print it, and your child uses a pencil.** |
| All other Qs | DELETE (they're on faq.html) |
| p.more | **More questions** |

### section#start
| Element | Text |
|---|---|
| h2 | **Give your child a strong start in math.** |
| p | **Small steps, with help when they need it.** |
| a.btn → #packs | **Find my child's level** |

---

## PRODUCT PAGES (same layout ×3)
**Shared strings:**
| Element | Text |
|---|---|
| breadcrumb link | **Packs** |
| p.price | **$3.99** |
| a.btn.buy | **Checkout opens soon** (at launch: **Buy now**) |
| h2 (inside) | **What's inside** |
| inside li 1–5 | **18 practice pages** / **An answer key for every page** / **A 2-page parent guide** / **A tracker and a certificate** / **Color cover. Black-and-white pages save ink.** |
| inside li 6 | **You'll need a pencil and some cereal or buttons.** |
| p.micro | **Instant download. Print for your family or one classroom.** |
| h2 | **What your child does** |
| h2 | **What you say** |
| h2 "When to move on" | DELETE heading and paragraph (the "Start here" line on the next level covers it) |
| h2 / cards | **Other levels** / badge · exact name · **$3.99** |
| p "These are kindergarten skills from the Common Core math standards." | DELETE |

### products/k-addition-beginner.html
| Element | Text |
|---|---|
| `<title>` | **Beginner: Adding within 5 \| Proud Little Learners** |
| meta | **Kindergarten math printables: count two small groups and add them, up to 5. Parent guide and answer keys. $3.99.** |
| badge / h1 | **Level 1** / **Beginner: Adding within 5** |
| sub p | **Count two small groups. Put them together.** |
| fit p | **Start here if your child can count to 10.** |
| What your child does p | **Count 2 dots and 1 more dot. Write 2 + 1 = 3. Totals stay at 5 or less.** |
| What you say p | **"Point to the two groups. How many in all?" Stuck? Count the first group together.** |

### products/k-addition-intermediate.html
| Element | Text |
|---|---|
| `<title>` | **Intermediate: Adding within 10 \| Proud Little Learners** |
| meta | **Kindergarten math printables: go from pictures to adding, like 4 + 3 = 7, up to 10. Parent guide and answer keys. $3.99.** |
| badge / h1 | **Level 2** / **Intermediate: Adding within 10** |
| sub p | **Go from pictures to adding, like 4 + 3 = 7.** |
| fit p | **Start here if adding up to 5 is easy.** |
| What your child does p | **Count the pictures, then write the math. Totals stay at 10 or less.** |
| What you say p | **"Start at 4. Now count on: 5, 6, 7." Then let your child try the next one.** |

### products/k-addition-advanced.html
| Element | Text |
|---|---|
| `<title>` | **Advanced: Story problems within 10 \| Proud Little Learners** |
| meta | **Kindergarten math printables: making 10, missing numbers, and short math stories you read aloud. Parent guide and answer keys. $3.99.** |
| badge / h1 | **Level 3** / **Advanced: Story problems within 10** |
| sub p | **Make 10, find missing numbers, and solve short math stories.** |
| fit p | **Start here if adding up to 10 is easy.** |
| What your child does p | **"3 ducks swim. 2 more come. How many now?" You read the story. Your child solves it.** |
| What you say p | **"What's happening?" Then act it out with cereal before you ask "How many?"** |

---

## WEEKLY (weekly.html)
| Element | Text |
|---|---|
| `<title>` | **Weekly Kindergarten Math Plan \| Proud Little Learners** |
| meta | **A new printable kindergarten math packet every Monday. $3.99/month.** |
| badge | **Weekly plan** |
| h1 | **Weekly Kindergarten Math Plan** |
| p (lead) | **A new math packet every Monday. Get this month's packets today.** |
| p.price | **$3.99/month** |
| p.bestif | DELETE |
| a.btn.buy | **Checkout opens soon** (at launch: **Start the weekly plan**) |
| p.cancel-line 1 (directly under the button) | **Renews monthly until you cancel. Cancel online anytime.** |
| p.cancel-line 2 | **Access ends when you cancel. New members: full refund within 7 days.** |
| h2 | **In each packet** |
| p | **7 or 8 practice pages, answer keys, a parent guide, and a tracker.** |
| h2 | **The first 8 weeks** |
| li 1–8 | **Counting to 5** / **Counting to 10** / **More and fewer** / **Adding within 5** / **Math stories within 5** / **Adding within 10** / **Taking away within 5** / **Shapes and patterns** (drop the "Week N:" prefix; the list is numbered 1–8) |
| p (link) | **Want to focus on adding? See the packs.** |

---

## FAQ (faq.html)
- `<title>`: **Questions | Proud Little Learners** · meta: **Answers about packs, the weekly plan, downloads, and refunds.**
- h1: **Questions**

| # | Question | Answer |
|---|---|---|
| 1 | **Which pack should we start with?** | **Beginner: Adding within 5, if your child can count to 10.** |
| 2 | **I'm not a teacher. Can I do this?** | **Yes. The guide tells you what to say. Every page has an answer key.** |
| 3 | **What if a page is too hard?** | **Go back a page, or count real things like cereal. Try again tomorrow.** |
| 4 | **When do we move up?** | **When your child does most pages with little help.** |
| 5 | **My child doesn't like worksheets. Will this help?** | **The pages are short, and you start with real things. Stop while it's still fun.** |
| 6 | **Is it on a screen?** | **No. You print it, and your child uses a pencil.** |
| 7 | **How do I get my files?** | **You get a download link right after you pay, and by email.** |
| 8 | **How does the weekly plan work?** | **$3.99/month. This month's packets today, then a new one every Monday. Cancel anytime. Access ends when you cancel.** |
| 9 | **Are weekly packets the same as the packs?** | **No. They're shorter and cover more, like counting and shapes. Packs go deeper on adding.** |
| 10 | **How do I cancel?** | **Sign in and cancel, or email us.** (link "cancel" → cancel.html) |
| 11 | **Can I get a refund?** | **If a file has a problem, we'll fix it or refund you. New weekly members can get a full refund within 7 days.** (link → refund-policy.html) |
| 12 | **Can I share the files?** | **Print them for your family or one classroom. Please don't share the files.** |

DELETE: "How much should I help?", "What's in a pack?" (the pack pages show it).

---

## ABOUT (about.html)
| Element | Text |
|---|---|
| `<title>` / meta | **About Us \| Proud Little Learners** / **Printable kindergarten math for parents who want to help at home.** |
| h1 | **About us** |
| p.lead | **We make kindergarten math pages for parents who want to help but don't know where to start.** |
| h2 "What you get" + 3 li | DELETE (the homepage says it) |
| p | **Questions? Email hello@proudlittlelearners.com.** |
| [OWNER] | When you send a first name and one true sentence, add h2 **Who we are** + that sentence above the email line. |

## Not changed in v2
cancel.html, contact.html, How we teach, Parent tips, the legal pages, and the redirect pages keep the site-copy.md text. Their copy is already short, and nobody reads them before buying.
