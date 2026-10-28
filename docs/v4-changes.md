# v4 changes (vs v3 live)

## Home: changed strings (old → new)
| Spot | v3 (old) | v4 (new) |
|---|---|---|
| #kids line | Hates worksheets? Start with cereal or toys, and stop while it's still fun. | **Hates worksheets? Each pack has cut-and-paste and a dice game. One page, about 10 minutes, then stop.** |
| ✓ li 1 | 18 pages, from easy to harder | **Pages in order, from easy to harder** |
| #say label | From the Beginner guide, pages 5–8: | **Beginner guide, practice pages 5 to 8. You say:** |
| #say quote | "Count this group. Count the other group. Now count every object." | **"Count this group. Count the other group. Now count every picture."** |
| #say follow-up | Still stuck? Set cereal on the pictures and count those. | **Then wait while your child counts.** |
| #say method (new) | — | **Every page is "I do, we do, you do," a method many teachers use: you show one, do one together, then your child tries.** |
| #packs lead | Try these with real toys. Pick the last one your child gets right. | **Try these with real toys. Start with the hardest one your child can do.** |
| Card 1 facts | $3.99 · 18 pages · adding up to 5 | **$3.99 · 18 practice pages · adding up to 5** |
| Card 2 facts | $3.99 · 18 pages · adding up to 10 | **$3.99 · 20 practice pages · adding up to 10** |
| Card 3 facts | $3.99 · 18 pages · making 10 and math stories | **$3.99 · 18 practice pages · making 10 and math stories** |
| Not-ready line (new) | — | **Can't count 5 toys yet? Count apples or blocks up to 5 for a few days first.** |
| Pack value (new) | — | **Each pack: the full 2-page guide, answer keys, a tracker, and a certificate. Yours to keep and reprint.** |
| Email line | Not sure? Email us. We'll help you pick. | DELETE |
| #plans p | A new packet every Monday: counting, shapes, adding, and more. | **A new packet every Monday, with a 1-page parent note.** |
| Q1 answer | Yes. Every page has an answer key, and the guide is 2 short pages in plain words. | **Yes. Every page has an answer key.** |

**Homepage words:** 274 → **323**. Only one "what to say" claim, $3.99 once per card, no "deserve", no "proven".

## Why the v3 lines had to go (final-PDF check)
- **"every object":** the final guide says "every picture". fix-2-copy.md said to keep "object" from catalog.py, but the final PDF overrides it.
- **"Set cereal on the pictures and count those":** not in the final Beginner guide. The final guide only says "Counters such as cereal are optional."
- **"Start with cereal or toys":** the final guide starts on the page. Real apples or blocks are only the not-ready path, so I replaced the line with true facts (cut-and-paste, dice game, about 10 minutes).
- **"Pick the last one your child gets right":** the tester called it fuzzy. It's now "the hardest one your child can do", plus the not-ready path from the Beginner guide.

## Fact fixes per product page
**Beginner: Adding within 5 (41 PDF pages: 18 practice + 18 keys)**
1. The quote now reads "…Now count every picture." (was "object"), labeled **On practice pages 5 to 8, you say:**
2. Added the story-page quote (pages 15–17): "What happened in the story? How many now?"
3. Deleted "Plus means we put the groups together." (not in the final guide)
4. Move-up rule changed from "pages 16, 17, and 18" to the guide's version: **story pages 15 to 17 and practice page 18 right with only a little help. Still helping with most? Stay.**
5. Added the not-ready line: count real apples or blocks up to 5 for a few days, then start again.
6. Supplies: pencil, crayons, scissors, glue or tape; dice optional (was "a pencil and some cereal or toys").

**Intermediate: Adding within 10 (45 PDF pages: 20 practice + 20 keys)**
1. **18 → 20 practice pages** on the home card, inside list, and meta.
2. Readiness now follows the guide's "only if adding within 5 already feels comfortable."
3. Quote stays "Fill the top row first. A full top row is 5. Now count the rest." with the correct label **practice pages 5 to 10**.
4. Added the number-line quote (pages 12–15).
5. Deleted "box with 10 spaces… fill it with cereal first."
6. Move-up rule changed to **add up to 10 with only a little help, including the mini-book on practice page 20** (was "including page 18"), plus "Too big? Go back to Adding within 5 and finish those stories first."

**Advanced: Story problems within 10 (41 PDF pages: 18 practice + 18 keys)**
1. Readiness changed to **can add up to 10 with pictures to count**, plus "You read the stories out loud. Still guessing in Adding within 10? Finish that pack first."
2. Quotes are now the make-10 line (pages 11–12) and the story line (pages 14–17), copied exactly.
3. Deleted "What happened? / How many?" (paraphrased) and "Act the story out with cereal or coins."
4. "When to move up" → **When it's finished**: practice pages 16, 17, and 18 feel easy with only a little help; the last of the three addition packs.

**Sitewide:** license line now matches the PDF: "family, homeschool, or one classroom."

## Pack vs weekly (only true contrasts)
- **The weekly packet really does include** answer keys and a tracker (week 1 PDF: cover, 1-page note, 7 practice pages, tracker, 7 keys = 17 pages). So the copy never says weekly lacks those.
- **Pack-only:** the full 2-page guide, the certificate, and keeping the files after you cancel the plan.

## For the owner
- **Pricing (unchanged):** a pack is $3.99 for 18–20 practice pages, kept for good. The weekly plan is $3.99/month for about 30 a month. The new pack-value line helps, but that's still the owner's call.
- **Which PDFs go to Payhip:** the site now matches the final build (Intermediate = 20 practice pages, "every picture"). An older build must not be uploaded.
- **"A method many teachers use":** this is true of "I do, we do, you do" (gradual release). There's no "proven" or research claim. The owner can cut the phrase if they want it even plainer.
- **Maker line:** a slot is marked in about.html only, as an HTML comment, so it's invisible. It needs a real first name and one sentence.
- **Weekly length:** the week 1 PDF says "Week 1 of 16". The site lists only the first 8 weeks, which is fine. Confirm the plan runs 16 weeks.
- **Still open:** how many packets arrive on day 1, the Terms and Privacy placeholders, and the "Beginner" naming idea.
