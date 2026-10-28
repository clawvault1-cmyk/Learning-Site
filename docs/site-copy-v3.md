# Proud Little Learners: site copy v3
Copy chief · Wed Oct 28, 2026 · **replaces v2 in full.** Sources: s2/research-words.md, s2/test-1.md, s2/fix-1-copy.md, and the real pack guides (packs/catalog.py, packs.json, check-report.json)

**How to apply:**
- Replace each string word for word.
- **DELETE** = remove the element.
- **Any homepage, product, or weekly text not listed here is deleted.**

**Locked:**
- **Names:** "Beginner: Adding within 5" · "Intermediate: Adding within 10" · "Advanced: Story problems within 10" · "Weekly Kindergarten Math Plan".
- **Prices:** "$3.99" / "$3.99/month" only, with nothing beside them.
- **Buy buttons:** "Checkout opens soon". At launch: **Buy now** / **Start the weekly plan**.
- **No:** "deserve", "proven", reviews or counts, "free sample", offers.

**Facts used (checked in the pack source):**
- **Each pack:**
  - 18 practice pages and 18 answer-key pages.
  - A 2-page guide, a tracker, a certificate, and a cover. 41 PDF pages in all.
- **Weekly packets:** 7 practice pages (8 in weeks 6 and 8).
- **Guide quotes:** every "What you say" line below is copied from the real guide text in packs/catalog.py. Do not edit the quotes.

**Header and footer (all pages):** unchanged from v2.

---

## HOME (index.html), 274 words
- `<title>`: **Kindergarten Math Help for Parents | Proud Little Learners**
- meta: **Kindergarten math help without random worksheets. Short printable pages, easy to harder, with a guide for you. $3.99.**

### section.hero
| Element | Text |
|---|---|
| h1 | **Kindergarten math help, without random worksheets.** |
| p.lead | **Short pages, easy to harder, with a guide for you. About 10 minutes a day.** |
| a.btn → #packs | **Find my child's level** (truthful now: #packs opens with the "Which one fits?" test) |
| p.micro | DELETE |

### section#kids (NEW one-line band directly under the hero; replaces section#how)
| Element | Text |
|---|---|
| p.kids-line | **Hates worksheets? Start with cereal or toys, and stop while it's still fun.** |
| section#how (all 3 cards) | DELETE |

### section#problem (h2 changes; this is now the only pain list)
| Element | Text |
|---|---|
| h2 | **Why not free worksheets?** |
| ul above the card, p.fix | DELETE |
| Card left h3 | **Free worksheets** |
| ✗ li 1–3 | **Random order** / **Too hard, too fast** / **You guess what to say** |
| Card right h3 | **Our packs** |
| ✓ li 1 | **18 pages, from easy to harder** |
| ✓ li 2 | **The words to say when your child gets stuck** (the only "what to say" claim on the page) |
| ✓ li 3 | **An answer key for every page** |
| ✓ li 4 | **A tracker and a clear "move up" rule** |
| ✓ li 5 | **Print tonight** |

### section#say (NEW, directly under the ✓/✗ card: the proof for ✓ li 2)
| Element | Text |
|---|---|
| p.label | **From the Beginner guide, pages 5–8:** |
| blockquote | **"Count this group. Count the other group. Now count every object."** |
| p | **Still stuck? Set cereal on the pictures and count those.** |
| (layout note) | Optional: show the guide preview image (packs/k-add-beginner/preview-guide.webp) beside it, alt **Page from the Beginner parent guide** |

### section#packs
| Element | Text |
|---|---|
| h2 | **Which one fits?** |
| p.lead | **Try these with real toys. Pick the last one your child gets right.** |
| Card 1 (in order) | p.test **Can your child count 5 toys?** · h3 **Beginner: Adding within 5** · p.facts **$3.99 · 18 pages · adding up to 5** · a.btn **See inside** |
| Card 2 | p.test **Can your child add 2 toys and 3 toys?** · h3 **Intermediate: Adding within 10** · p.facts **$3.99 · 18 pages · adding up to 10** · a.btn **See inside** |
| Card 3 | p.test **Can your child add 4 toys and 5 toys?** · h3 **Advanced: Story problems within 10** · p.facts **$3.99 · 18 pages · making 10 and math stories** · a.btn **See inside** |
| Separate p.price, "what" line, "Start here if" line, badge "Level N" | DELETE (the test line leads the card, and $3.99 appears once per card inside p.facts) |
| p under cards | **Not sure? Email us. We'll help you pick.** (mailto on "Email us") |

### section#inside
DELETE the whole section. Its 4 items now live in the ✓ list.

### section#plans
| Element | Text |
|---|---|
| h2 | **Weekly Kindergarten Math Plan** |
| p | **A new packet every Monday: counting, shapes, adding, and more.** |
| p.price | **$3.99/month** |
| a.btn → weekly.html | **See the weekly plan** |
| "Best if…" + both cancel lines | DELETE (the terms stay next to the real buy button on weekly.html) |

### section#questions
| Element | Text |
|---|---|
| h2 | **Questions** |
| Q1 / A1 | **I'm not a teacher. Can I do this?** / **Yes. Every page has an answer key, and the guide is 2 short pages in plain words.** |
| Q2 / A2 | **Is it on a screen?** / **No. You print it, and your child uses a pencil.** |
| All other Qs | DELETE (the worksheet question is answered in #kids) |
| p.more | **More questions** |

### section#start
| Element | Text |
|---|---|
| h2 | **Print one page tonight.** |
| p | DELETE |
| a.btn → #packs | **Find my child's level** |

---

## PRODUCT PAGES (same layout ×3)
**Order on each page:**
1. badge (DELETE "Level N")
2. h1
3. p.test
4. p.sub
5. p.price
6. a.btn.buy
7. What's inside
8. What you say
9. When to move up
10. Other packs

**Shared strings:**
| Element | Text |
|---|---|
| breadcrumb | **Packs** |
| p.price | **$3.99** |
| a.btn.buy | **Checkout opens soon** |
| h2 | **What's inside** |
| li 1–6 | **18 practice pages, easy to harder** / **An answer key for every page** / **A 2-page parent guide** / **A tracker and a certificate** / **Color cover. Black-and-white pages save ink.** / **You'll need a pencil and some cereal or toys.** |
| p.micro | **Instant download. Print for your family or one classroom.** |
| h2 | **What you say** (the quote is from that pack's guide; style it as a blockquote) |
| h2 | **When to move up** |
| h2 | **Other packs** |
| "What your child will practice" h2 + p, and the "Common Core" p | DELETE (p.sub covers practice) |
| Other-pack card | p.test + name + **$3.99** (same strings as the homepage cards, no facts line) |

### products/k-addition-beginner.html
| Element | Text |
|---|---|
| `<title>` / meta | **Beginner: Adding within 5 \| Proud Little Learners** / **Kindergarten math printables: count two groups, then put them together. Totals up to 5. Guide and answer keys. $3.99.** |
| h1 | **Beginner: Adding within 5** |
| p.test | **Start here if your child can count 5 toys.** |
| p.sub | **Count two groups, then put them together, like 2 + 1 = 3.** |
| What you say: blockquote | **"Count this group. Count the other group. Now count every object."** |
| What you say: p | **When the plus sign shows up: "Plus means we put the groups together."** |
| When to move up: p | **When pages 16, 17, and 18 are right with only a little help.** |

### products/k-addition-intermediate.html
| Element | Text |
|---|---|
| `<title>` / meta | **Intermediate: Adding within 10 \| Proud Little Learners** / **Kindergarten math printables: go from pictures to adding, like 4 + 3 = 7. Totals up to 10. Guide and answer keys. $3.99.** |
| h1 | **Intermediate: Adding within 10** |
| p.test | **Start here if your child can add 2 toys and 3 toys.** |
| p.sub | **Go from pictures to adding, like 4 + 3 = 7.** |
| What you say: blockquote | **"Fill the top row first. A full top row is 5. Now count the rest."** |
| What you say: p | **The guide shows this on a box with 10 spaces. Fill it with cereal first.** |
| When to move up: p | **When your child can add up to 10 with only a little help, including page 18.** |

### products/k-addition-advanced.html
| Element | Text |
|---|---|
| `<title>` / meta | **Advanced: Story problems within 10 \| Proud Little Learners** / **Kindergarten math printables: making 10, missing numbers, and short stories you read aloud. Guide and answer keys. $3.99.** |
| h1 | **Advanced: Story problems within 10** |
| p.test | **Start here if your child can add 4 toys and 5 toys.** |
| p.sub | **Make 10, find missing numbers, and solve short stories you read aloud, like "3 ducks swim. 2 more come. How many now?"** |
| What you say: blockquote | **"What happened?" Then ask, "How many?"** |
| What you say: p | **Act the story out with cereal or coins. Your child doesn't need to read.** |
| When to move up: p | **When these pages feel easy, your child has finished all three packs.** |

---

## WEEKLY (weekly.html)
| Element | Text |
|---|---|
| `<title>` / meta | **Weekly Kindergarten Math Plan \| Proud Little Learners** / **A new printable kindergarten math packet every Monday. $3.99/month.** |
| badge / h1 | **Weekly plan** / **Weekly Kindergarten Math Plan** |
| p.lead | **A new packet every Monday: counting, shapes, adding, and more. Get this month's packets today.** |
| p.price | **$3.99/month** |
| a.btn.buy | **Checkout opens soon** |
| p.cancel-line 1 (directly under the button) | **Renews monthly until you cancel. Cancel online anytime.** |
| p.cancel-line 2 | **Access ends when you cancel. New members: full refund within 7 days.** |
| h2 / p | **In each packet** / **7 or 8 practice pages, answer keys, a 1-page parent note, and a tracker.** (the weekly build uses "A one-page note for the grown-up", not a guide) |
| h2 / ol | **The first 8 weeks** / **Counting to 5 · Counting to 10 · More and fewer · Adding within 5 · Math stories within 5 · Adding within 10 · Taking away within 5 · Shapes and patterns** |
| p (link) | **Want to focus on adding? See the packs.** |

---

## FAQ (faq.html)
Same as v2 (12 Qs), with these changes:
- **Q1 answer:** **Beginner: Adding within 5, if your child can count 5 toys. Not sure? Try the three toy tests on the home page.**
- **Q2 answer:** **Yes. Every page has an answer key, and the guide is 2 short pages in plain words.**
- **Q4 answer:** **When the last 3 pages are right with only a little help. The guide says which pages.**

## ABOUT (about.html)
Same as v2. [OWNER] A real first name and one true sentence are still needed.
