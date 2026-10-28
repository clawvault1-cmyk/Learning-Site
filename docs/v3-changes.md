# v3 changes (vs v2 and the old live site)

## Hero
| | Old live | v2 | **v3** |
|---|---|---|---|
| h1 | Help your kindergartner with math, step by step. | Not sure how to help with kindergarten math? | **Kindergarten math help, without random worksheets.** (6 words. It ends the pain, using the parents' own "random worksheets") |
| Sub | Printable pages in the right order, with a short guide that tells you what to say. About 10 minutes a day. (21) | Print pages in the right order. A short guide tells you what to say. 10 minutes a day. (18) | **Short pages, easy to harder, with a guide for you. About 10 minutes a day.** (15. It drops the unexplained "right order" and keeps the "what to say" claim for the ✓ list) |
| Button | Find my child's level | same | **Find my child's level**. It's true now: it lands on the "Which one fits?" toy test |
| Next line | — | — | **Hates worksheets? Start with cereal or toys, and stop while it's still fun.** |

## What each of the 7 asks became
1. **Show the guide.** New section #say, right under the ✓ list:
   - Label: "From the Beginner guide, pages 5–8:"
   - Quote: "Count this group. Count the other group. Now count every object."
   - Follow-up: "Still stuck? Set cereal on the pictures and count those."
   - All three are copied from the real guide text (packs/catalog.py). I didn't use the product page's "Point to the two groups. How many in all?" because that wording isn't in the PDF guide.
   - The "what to say" claim now appears **once** on the homepage (✓ li 2), down from 6.
2. **Why pay vs free.** The h2 is "Why not free worksheets?" and every ✓ is a checkable fact:
   - 18 pages, from easy to harder
   - The words to say when your child gets stuck
   - An answer key for every page
   - A tracker and a clear "move up" rule (the rule is printed on each product page, e.g. "When pages 16, 17, and 18 are right with only a little help.")
   - Print tonight
3. **Level picking.** "Which one fits? Try these with real toys. Pick the last one your child gets right."
   - Can your child count 5 toys? → Beginner
   - Can your child add 2 toys and 3 toys? → Intermediate
   - Can your child add 4 toys and 5 toys? → Advanced
   - Each test leads its card. The names are unchanged.
4. **Worksheet-hater line.** It's directly under the hero (#kids), and it replaces the 3-step #how strip.
5. **Hero.** 6 words + 15 words + button: 25 words above the fold.
6. **Repetition removed.**
   - "$3.99" appears once per card (4 on the page, down from 8).
   - The pain list appears once (the ✗ side). The pain bullets and "Our packs fix that" are gone.
   - #inside is merged into the ✓ list.
7. **Fact line on cards.** "$3.99 · 18 pages · adding up to 5", "… adding up to 10", "… making 10 and math stories". The page count was checked: packs.json/check-report.json give practicePages 18 and totalPages 41 (the rest are 18 answer keys, a 2-page guide, a tracker, a certificate, and a cover). "18 pages" means practice pages; the product page's inside list says "18 practice pages".

## Other big changes
- **Product pages:**
  - Each leads with the toy test.
  - "What you say" quotes that pack's real guide.
  - "When to move up" uses the guide's own rule.
  - Practice paragraphs, the Common Core line, and the "Level N" badges are deleted.
- **Closing:** "Print one page tonight." + button. No "deserve" and no first-grade promise.
- **Weekly:**
  - "a short parent guide" → "a 1-page parent note". The weekly build really ships "A one-page note for the grown-up", not a guide.
  - The 4 required terms stay in 2 lines under the button.
- **FAQ:** the level answer now uses the toy test.

## Homepage word count
| Section | Old live | v2 | v3 |
|---|---|---|---|
| hero | 42 | 30 | 25 |
| #kids (replaces #how) | 47 | 26 | 13 |
| #problem ("Why not free worksheets?") | 101 | 33 | 50 |
| #say (new) | — | — | 27 |
| #packs ("Which one fits?") | 105 | 68 | 89 |
| #inside | 48 | 21 | 0 (merged) |
| #plans | 56 | 19 | 19 |
| #questions | 173 | 65 | 43 |
| #start | 29 | 20 | 8 |
| **Total** | **601** | **282** | **274** |

## Flags for the owner (no copy change made)
- **Pricing concern (test-1, budget skeptic):**
  - A pack is $3.99 for 18 practice pages, kept forever.
  - The weekly plan is $3.99/month for this month's packets plus 7–8 new practice pages every Monday (about 30 a month).
  - Side by side, the pack looks like the worse deal. I didn't change prices. The copy positions the plan as a little of everything every week and the packs as going deeper on adding. The owner should decide price or positioning.
- **Beginner start point changed to match the pack:** packs.json says the prerequisite is "Counts objects to 5." The old site said "can count to 10." v3 uses 5.
- **Advanced test:** "add 4 toys and 5 toys" matches the prerequisite "Adds within 10 with pictures."
- **Product-page quote mismatch:** the live line "Point to the two groups. How many in all?" isn't in the Beginner PDF guide. v3 swaps it for the real guide words. If the owner prefers that line, add it to the guide first.
- **Still open:**
  - How many packets come on day 1 ("this month's packets" is kept from the live site and unverified)
  - The About name and sentence
  - The Terms placeholders
  - Naming: "Beginner" reads like a label on the child (test-1, the dad persona). A possible rename is "Adding up to 5 / Adding up to 10 / Making 10 and math stories". This is flagged only, not applied.
