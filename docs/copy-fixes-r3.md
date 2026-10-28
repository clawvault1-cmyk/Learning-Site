# Copy fixes, round 3 (live site as of 11:39 PM ET)
Copy chief · Tue Oct 27, 2026 · apply 1:1 · source: /workspace/loops/round-3.md

How to read this: each fix is `page > section > element`, then the old text, then the new text. "DELETE" means remove the element. "ADD" means a new element in the spot named. Pack names stay exactly as they are.

## 1. Homepage > "Random worksheets vs. Our packs" (✗/✓ card)
Make it 4 rows. Each ✓ answers the ✗ on the same row.

| Row | Left (✗) old → new | Right (✓) old → new |
|---|---|---|
| 1 | Too easy → **Too easy** | 1. Adding within 5 → **Starts where your child is** |
| 2 | Too hard → **Too hard** | 2. Adding within 10 → **Tells you what to say when they're stuck** |
| 3 | Skips ahead → **Skips ahead** | 3. Story problems → **One small step at a time** |
| 4 | ADD → **You guess what's next** | ADD → **A tracker shows when to move on** |

- Left p "Too easy, then too hard." → DELETE
- Right p "One small step at a time." → DELETE (it's now row 3)
- The h3s stay: **Random worksheets** / **Our packs**

## 2. "Turn pictures into problems" (reads like "trouble")
| Where | Old | New |
|---|---|---|
| Homepage > Level 2 card > p | Turn pictures into problems like 4 + 3 = 7. | **Go from pictures to adding, like 4 + 3 = 7.** |
| Intermediate page > sub p | Your child turns pictures into problems like 4 + 3 = 7. | **Your child goes from pictures to adding, like 4 + 3 = 7.** |
| Intermediate page > meta description | …Your child turns pictures into problems like 4 + 3 = 7, with totals up to 10… | **Kindergarten math printables. Your child goes from pictures to adding, like 4 + 3 = 7, with totals up to 10. Parent guide and answer keys included. $3.99.** |
| Intermediate page > What your child will practice > p | Your child goes from counting pictures to writing the problem, like 4 + 3 = 7. | **Your child counts pictures, then writes the math, like 4 + 3 = 7.** (Leave the rest of the paragraph as it is.) |
| products.js > k-add-intermediate summary | (whatever it says now) | **Your child goes from pictures to adding, like 4 + 3 = 7.** |

"Story problem" means nothing to the dad persona, and the Level 3 name undersells what's in the pack. Here are the card and body lines (the name stays the same):
| Where | Old | New |
|---|---|---|
| Homepage > Level 3 card > p | Solve short story problems you read out loud. | **Make 10, find missing numbers, and solve short math stories you read aloud.** |
| Advanced page > sub p | Your child solves short story problems you read out loud. | **Your child makes 10, finds missing numbers, and solves short math stories you read aloud.** |
| products.js > k-add-advanced summary | (whatever it says now) | same as the Advanced sub p above |
| Beginner page > What your child will practice > last sentence | The last pages have a short story problem you read out loud. | **The last pages have a short math story you read aloud.** |

## 3. Color cover vs. black-and-white pages
| Where | Old | New |
|---|---|---|
| Homepage > What's in each pack > p.micro | Black-and-white PDF. Prints on regular paper. | **Color cover. Pages print in black and white to save ink.** |
| All 3 product pages > What's inside > li 5 | Black-and-white PDF for regular paper | **Color cover. Pages print in black and white to save ink.** |

## 4. Other wording flagged in round 3

### 4a. Weekly plan renewal line. This must be visible next to the button. It isn't fine print: the law requires it, and it's the reason a parent trusts the button.
| Where | Old | New |
|---|---|---|
| Homepage > weekly card > p.cancel-line | Cancel anytime | **Renews monthly until you cancel. Cancel online anytime.** |
| weekly.html > ADD p directly under a.btn.buy | (none) | **Renews monthly until you cancel. Cancel online anytime.** |
| weekly.html > ADD p right after that line | (none) | **Access ends when you cancel. New members can get a full refund within 7 days.** |
| weekly.html > `<details>` "Details" / "Renews monthly. Cancel anytime." | | DELETE the whole toggle |

### 4b. "This month's packets right away" (parents ask how many)
| Where | Old | New |
|---|---|---|
| Homepage > weekly card > p | A new packet every Monday. Get this month's packets right away. | **Start with this month's packets today. Then get a new one every Monday.** |
| weekly.html > lead p | A new printable math packet every Monday. Get this month's packets right away. | **Start with this month's packets today. Then get a new printable packet every Monday.** |

[OWNER] If the number is fixed (for example, every new member gets 4), use "**Start with 4 packets today. Then get a new one every Monday.**" in both places. The number is more convincing.

### 4c. Hero micro-line (add the two facts that beat free worksheets)
| Where | Old | New |
|---|---|---|
| Homepage > hero > p.micro | $3.99 a pack. Print it tonight. | **$3.99 for 18 pages. No screens. Print it tonight.** |

### 4d. Pack vs. weekly plan (could a parent pay twice for the same pages?)
| Where | Old | New |
|---|---|---|
| Homepage > Pick a starting level > p.lead | $3.99 each. Yours to keep. | **$3.99 each. Yours to keep. Not sure? Email us and we'll help you pick.** (mailto link on "Email us") |
| Homepage > weekly card > ADD p above the price | (none) | **Best if you want new pages every week, starting with counting.** |
| weekly.html > p | Want just one level? See the packs. | **Want to go deeper on adding? See the packs.** (link on "See the packs") |
| FAQ (homepage and faq.html) > ADD Q after "What's the difference…" | (none) | Q: **Are the weekly packets the same as the packs?** A: **No. Weekly packets are shorter and cover more topics, like counting, shapes, and taking away. Each pack goes deeper on adding, with 18 pages.** [OWNER: confirm this is true before publishing.] |

### 4e. Bring back the "10 minutes" strip (round 3, fix 2)
Homepage > ADD section between the ✗/✓ card and "Pick a starting level":
- h2: **What 10 minutes looks like**
- 1 h3 / p: **Print one page.** / **Pick the pack that fits your child.**
- 2 h3 / p: **Show it, then do it together.** / **Count cereal or buttons first. Then try the page.**
- 3 h3 / p: **Let your child try.** / **Stuck? The guide tells you what to say.**

### 4f. Closing call to action (round 3, fix 3)
Homepage > ADD section after Questions, before the footer:
- h2: **Give your child the head start they deserve.**
- p: **Kindergarten math builds step by step. A few minutes a day helps it stick.**
- a.btn: **Find my child's level** → `#packs`

### 4g. Pre-launch buttons that look live but do nothing (round 3, fix 4)
| Where | Old | New (until checkout opens) |
|---|---|---|
| Homepage > each of the 3 pack cards > a.btn.buy | Checkout opens soon (dead) | **See inside** → that pack's page |
| Homepage > weekly card > a.btn.buy | Checkout opens soon (dead) | **See the weekly plan** → weekly.html |
| Product pages and weekly.html > a.btn.buy | Checkout opens soon | Keep the text. Style it gray and inactive, with the existing note "Checkout opens soon. No payment is taken yet." |
| At launch | | Card buttons become **Buy now** / **Start the weekly plan** |

### 4h. Preview images (optional, if the watermark stays)
- Product page > under the gallery > ADD p: **Real pages from the pack.**

## For the owner only (not applied)
**Naming ideas.** The packs are NOT renamed. These are only for you to consider:
- Advanced: "Story problems within 10" undersells the pack, which also covers making 10 and missing numbers. Options: "Advanced: Making 10 and story problems", or "Advanced: Adding stories within 10".
- "Story problems" is teacher talk. "Math stories" is plainer for parents.
- Consider leading with the level: "Level 1: Adding within 5" and so on. Then the badge and the name say one thing instead of two.

**Facts I need from you before some lines can go live:**
- How many packets a new weekly member gets on day one (4b).
- Whether the weekly packets are different pages from the packs (4d FAQ).
- That the PDF cover really is in color (3).
- A first name and one true sentence for About.
- The Terms and Refund Policy pages still show "[OWNER: legal business name / state / address]" placeholders.
