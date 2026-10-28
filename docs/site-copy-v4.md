# Proud Little Learners: site copy v4 (targeted revision of v3)
Copy chief · Wed Oct 28, 2026, ~8:10 PM ET

**Sources:** pack-facts-final.md (wins on every fact), s2/test-2.md, s2/fix-2-copy.md, and a text check of the 2-page guides in /workspace/qa/pdfs3/. Those PDFs match pack-facts-final.md: 41 / 45 / 41 pages, and the quote reads "every picture".

**How to apply:**
- Each string below replaces the matching v3 string word for word.
- Strings marked **(v3, unchanged)** stay as they are.
- **DELETE** means remove the element.

**Locked:**
- **Names and prices:** pack names, "Weekly Kindergarten Math Plan", "$3.99" and "$3.99/month" stay unchanged.
- **Buy buttons:** "Checkout opens soon".
- **Banned:** "deserve", "proven", reviews, free samples.
- **Quotes:** any quoted guide line must match pack-facts-final.md character for character.

---

## HOME (index.html): 323 words (v3: 274)
- `<title>`: (v3, unchanged)
- meta: (v3, unchanged)

### section.hero (v3, unchanged)
- h1: **Kindergarten math help, without random worksheets.**
- p.lead: **Short pages, easy to harder, with a guide for you. About 10 minutes a day.**
- a.btn → #packs: **Find my child's level**

### section#kids
| Element | Text |
|---|---|
| p.kids-line | **Hates worksheets? Each pack has cut-and-paste and a dice game. One page, about 10 minutes, then stop.** |

Source for each claim in this line:
- Cut-and-paste: Beginner practice page 12, Intermediate page 17, Advanced page 13.
- Dice game: practice page 14 in Beginner, page 18 in Intermediate and Advanced.
- "About 10 minutes, then stop while your child is still willing" comes from each guide.

### section#problem
| Element | Text |
|---|---|
| h2 | **Why not free worksheets?** (v3) |
| ✗ h3 + li 1–3 | **Free worksheets** · **Random order** · **Too hard, too fast** · **You guess what to say** (v3) |
| ✓ h3 | **Our packs** (v3) |
| ✓ li 1 | **Pages in order, from easy to harder** (was "18 pages, from easy to harder". Intermediate has 20, so no number here) |
| ✓ li 2–5 | **The words to say when your child gets stuck** · **An answer key for every page** · **A tracker and a clear "move up" rule** · **Print tonight** (v3) |

### section#say
| Element | Text |
|---|---|
| p.label | **Beginner guide, practice pages 5 to 8. You say:** |
| blockquote | **"Count this group. Count the other group. Now count every picture."** |
| p | **Then wait while your child counts.** (the guide says "Say the line, then wait.") |
| p.method (new) | **Every page is "I do, we do, you do," a method many teachers use: you show one, do one together, then your child tries.** (each practice page marks problem 1 "I do" and problem 2 "We do") |
| Image (if shown) | alt **Parent guide page from Beginner: Adding within 5** |

### section#packs
| Element | Text |
|---|---|
| h2 | **Which one fits?** (v3) |
| p.lead | **Try these with real toys. Start with the hardest one your child can do.** |
| Card 1 | p.test **Can your child count 5 toys?** · h3 **Beginner: Adding within 5** · p.facts **$3.99 · 18 practice pages · adding up to 5** · **See inside** |
| Card 2 | p.test **Can your child add 2 toys and 3 toys?** · h3 **Intermediate: Adding within 10** · p.facts **$3.99 · 20 practice pages · adding up to 10** · **See inside** |
| Card 3 | p.test **Can your child add 4 toys and 5 toys?** · h3 **Advanced: Story problems within 10** · p.facts **$3.99 · 18 practice pages · making 10 and math stories** · **See inside** |
| p.notyet (new, under cards) | **Can't count 5 toys yet? Count apples or blocks up to 5 for a few days first.** |
| p.pack-value (new) | **Each pack: the full 2-page guide, answer keys, a tracker, and a certificate. Yours to keep and reprint.** |
| p "Not sure? Email us…" | DELETE (the line above it covers not-ready kids; the Contact link stays in the footer) |

### section#plans
| Element | Text |
|---|---|
| h2 | **Weekly Kindergarten Math Plan** (v3) |
| p | **A new packet every Monday, with a 1-page parent note.** |
| p.price / a.btn | **$3.99/month** / **See the weekly plan** (v3) |

### section#questions
| Element | Text |
|---|---|
| Q1 / A1 | **I'm not a teacher. Can I do this?** / **Yes. Every page has an answer key.** |
| Q2 / A2, p.more | (v3, unchanged) |

### section#start (v3, unchanged)
- h2: **Print one page tonight.**
- Button: **Find my child's level**

---

## PRODUCT PAGES
**Shared changes:**
- Quotes go in a blockquote. Before each quote, add a p.label: **On practice pages X to Y, you say:**
- After the last quote, add p: **Say the line, then wait.**
- Shared "What's inside" li 6: **You'll need a pencil, crayons, scissors, and glue or tape.**
  - Beginner adds: **Two dice make page 14 more fun.**
  - Intermediate and Advanced add: **Two dice make page 18 more fun.**
  - (was "a pencil and some cereal or toys")
- p.micro: **Instant download. Print for your family, homeschool, or one classroom.** (matches the PDF license: "Personal, homeschool, and single-classroom use")
- Other-pack cards: p.test + name + **$3.99** (v3).

### products/k-addition-beginner.html
| Element | Text |
|---|---|
| p.test | **Start here if your child can count 5 toys.** (v3) |
| p.notyet (new) | **If practice page 1 is hard, count real apples or blocks up to 5 for a few days, then start again.** |
| p.sub | **Count two groups, then put them together, like 2 + 1 = 3.** (v3) |
| inside li 1 | **18 practice pages, easy to harder** |
| inside li 2–5 | **An answer key for every page** · **A 2-page parent guide** · **A tracker and a certificate** · **Color cover. Black-and-white pages save ink.** |
| What you say | label **On practice pages 5 to 8, you say:** · blockquote **"Count this group. Count the other group. Now count every picture."** · label **On practice pages 15 to 17, you say:** · blockquote **"What happened in the story? How many now?"** · p **Say the line, then wait.** |
| DELETE | "When the plus sign shows up: 'Plus means we put the groups together.'" (not in the final guide) |
| When to move up | **When the story pages (15 to 17) and practice page 18 are right with only a little help. Still helping with most of them? Stay with this pack.** |
| meta | **Kindergarten math printables: count two groups, then put them together. Totals up to 5. 18 practice pages, guide, and answer keys. $3.99.** |

### products/k-addition-intermediate.html
| Element | Text |
|---|---|
| p.test | **Start here if adding up to 5 already feels easy, like 2 toys and 3 toys.** (the guide says "Start here only if adding within 5 already feels comfortable.") |
| p.sub | **Go from pictures to adding, like 4 + 3 = 7.** (v3) |
| inside li 1 | **20 practice pages, easy to harder** (was 18) |
| inside li 2–5 | same as Beginner |
| What you say | label **On practice pages 5 to 10, you say:** · blockquote **"Fill the top row first. A full top row is 5. Now count the rest."** · label **On practice pages 12 to 15, you say:** · blockquote **"Put your finger on the first number. Jump one space for each in the second number. Do not count the space you start on."** · p **Say the line, then wait.** |
| DELETE | "The guide shows this on a box with 10 spaces. Fill it with cereal first." |
| When to move up | **When your child can add up to 10 with only a little help, including the mini-book on practice page 20. Too big? Go back to Adding within 5 and finish those stories first.** |
| meta | **Kindergarten math printables: go from pictures to adding, like 4 + 3 = 7. Totals up to 10. 20 practice pages, guide, and answer keys. $3.99.** |

### products/k-addition-advanced.html
| Element | Text |
|---|---|
| p.test | **Start here if your child can add up to 10 with pictures to count, like 4 toys and 5 toys.** |
| p.read (new) | **You read the stories out loud. Still guessing in Adding within 10? Finish that pack first.** |
| p.sub | **Make 10, find missing numbers, and solve short stories, like "3 ducks swim. 2 more come. How many now?"** (the v3 "you read aloud" moves to p.read) |
| inside li 1 | **18 practice pages, easy to harder** |
| What you say | label **On practice pages 11 and 12, you say:** · blockquote **"How many empty spaces? That is how many more make 10."** · label **On practice pages 14 to 17, you say:** · blockquote **"What happened in the story? How many now?"** · p **Say the line, then wait.** |
| DELETE | the v3 lines "'What happened?' Then ask, 'How many?'" and "Act the story out with cereal or coins. Your child doesn't need to read." |
| h2 "When to move up" | rename to **When it's finished** |
| p | **When practice pages 16, 17, and 18 feel easy with only a little help. It's the last of the three addition packs.** |

---

## WEEKLY (weekly.html)
Unchanged from v3 except one string:

| Element | Text |
|---|---|
| p under "In each packet" | **7 or 8 practice pages, answer keys, a 1-page parent note, and a tracker.** (v3) |
| p (link, new text) | **Want the full 2-page guide and a certificate? See the packs.** |

---

## FAQ (faq.html)
| Q | New answer |
|---|---|
| Which pack should we start with? | **Beginner: Adding within 5, if your child can count 5 toys. Can't yet? Count apples or blocks up to 5 for a few days first.** |
| When do we move up? | **When the last few practice pages are right with only a little help. The guide names the pages.** |
| Are weekly packets the same as the packs? | **No. A weekly packet has 7 or 8 practice pages and a 1-page note. A pack goes deeper on adding, with the full 2-page guide, a tracker, and a certificate. You keep it.** |
| Can I share the files? | **Print them for your family, homeschool, or one classroom. Please don't share the files.** |

All other Qs stay as in v3.

## ABOUT (about.html)
v3 text, plus this marked slot. **It must not render.**

`<!-- [OWNER] MAKER SLOT: h2 "Who we are" + one true sentence (first name, parent or teacher). Do not publish until the owner sends the facts. Never on home. -->`
