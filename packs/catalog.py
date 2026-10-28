"""Problem lists for the three addition packs and the first eight weekly packets.

Operands live here. Answer phrases are drawn later and checked by parsing,
not by trusting a stored total.
"""

NUMW = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def plural(noun, n):
    return noun if n == 1 else noun + "s"


def add_story(a, b, name, obj, variant=0):
    q = plural(obj, 2)
    if a == 0:
        verb = "arrives" if b == 1 else "arrive"
        return f"No {q} are there yet. Then {NUMW[b]} {plural(obj, b)} {verb}. How many {q} now?"
    if b == 0:
        return f"{name} has {NUMW[a]} {plural(obj, a)}. No more are added. How many {q} does {name} have?"
    if variant % 2 == 0:
        return f"{name} has {NUMW[a]} {plural(obj, a)}. {name} gets {NUMW[b]} more. How many {q} now?"
    opener = f"There is one {obj}." if a == 1 else f"There are {NUMW[a]} {plural(obj, a)}."
    verb = "comes" if b == 1 else "come"
    return f"{opener} {NUMW[b].capitalize()} more {plural(obj, b)} {verb}. How many {q} in all?"


def sub_story(a, b, name, obj):
    q = plural(obj, 2)
    return f"{name} has {NUMW[a]} {plural(obj, a)}. {name} gives {NUMW[b]} away. How many {q} are left?"


def A(a, b):
    return {"kind": "add", "a": a, "b": b}


def C(n, shape="circle"):
    return {"kind": "count", "n": n, "shape": shape}


def TWO(a, b):
    return {"kind": "two", "a": a, "b": b}


def ST(a, b, name, obj, variant=0):
    item = A(a, b)
    item["text"] = add_story(a, b, name, obj, variant)
    return item


def SUB(a, b):
    return {"kind": "sub", "a": a, "b": b}


def SST(a, b, name, obj):
    item = SUB(a, b)
    item["text"] = sub_story(a, b, name, obj)
    return item


def PART(total, a, b):
    if a + b != total:
        raise ValueError(f"partners {a}+{b} != {total}")
    return {"kind": "partners", "total": total, "a": a, "b": b}


def MISS(total, known):
    if not 0 <= known <= total:
        raise ValueError("bad missing part")
    return {"kind": "missing", "total": total, "known": known}


def M10(a):
    if not 0 <= a <= 10:
        raise ValueError(a)
    return {"kind": "make10", "a": a, "b": 10 - a}


def pg(title, instruction, layout, problems, tracker, track="add", step_back=False, weights=None):
    if not 4 <= len(problems) <= 8:
        raise ValueError(f"{title} has {len(problems)} problems")
    spec = {
        "title": title,
        "instruction": instruction,
        "layout": layout,
        "problems": problems,
        "tracker": tracker,
        "track": track,
        "step_back": step_back,
    }
    if weights:
        spec["weights"] = weights
    return spec


LICENSE = (
    "Personal, homeschool, and single-classroom use. You may print copies for the children you teach. "
    "Do not resell this file or redistribute it."
)
PLAIN = "These are practice pages. They are not a test, and they are not a promise of a particular result."


def _guide(*pairs):
    blocks = list(pairs)
    blocks.append(("h", "License"))
    blocks.append(("license", LICENSE))
    blocks.append(("p", PLAIN))
    return blocks


def beginner():
    practice = [
        pg("Count the group", "Count the circles. Write how many.", "count",
           [C(3), C(1), C(4), C(2), C(5), C(2)], "Count one group", track="count"),
        pg("Count the group again", "Count the squares. Write how many.", "count",
           [C(2, "square"), C(5, "square"), C(1, "square"), C(3, "square"), C(4, "square"), C(1, "square")],
           "Count one group", track="count"),
        pg("Two groups", "Count each group. Write both numbers. Do not add yet.", "two",
           [TWO(1, 2), TWO(2, 1), TWO(3, 1), TWO(1, 1), TWO(2, 2), TWO(4, 1)],
           "Count two groups", track="count"),
        pg("A group can be empty", "An empty bowl means nothing is there. Write 0 for that group.", "two",
           [TWO(0, 3), TWO(3, 0), TWO(2, 3), TWO(1, 4), TWO(5, 0), TWO(0, 1)],
           "Count two groups, with 0", track="count"),
        pg("How many in all?", "Count both groups. Write how many in all.", "picture_total",
           [A(1, 1), A(2, 1), A(1, 2), A(2, 0), A(0, 1), A(1, 0)], "Totals up to 3"),
        pg("Put the groups together", "Count both groups. Write the total.", "picture_total",
           [A(2, 2), A(3, 1), A(1, 3), A(4, 0), A(0, 4), A(3, 0)], "Totals up to 4"),
        pg("Totals up to 5", "Count every object. Write the total.", "picture_total",
           [A(4, 1), A(1, 4), A(3, 2), A(2, 3), A(5, 0), A(0, 5)], "Totals up to 5"),
        pg("Mixed groups", "The groups look different. Count them all and write the total.", "picture_total",
           [A(3, 2), A(2, 1), A(4, 1), A(1, 1), A(2, 2), A(0, 3)], "Mixed totals"),
        pg("A number sentence", "The pictures match the sentence. Write the total.", "picture_sentence",
           [A(1, 1), A(2, 1), A(1, 2), A(3, 1), A(2, 2), A(4, 0)], "Number sentence", step_back=True),
        pg("Sentences up to 5", "Count the pictures. Finish the number sentence.", "picture_sentence",
           [A(3, 2), A(4, 1), A(2, 3), A(5, 0), A(1, 4), A(0, 5)], "Number sentence"),
        pg("Count on", "Filled dots are the first number. Count the empty circles for the second number.", "count_on",
           [A(2, 2), A(3, 1), A(4, 1), A(2, 3), A(1, 3), A(3, 2)], "Count on"),
        pg("Just the sentence", "Write the total. Draw dots if you want to.", "sentence",
           [A(1, 1), A(2, 3), A(0, 4), A(3, 2), A(5, 0), A(1, 4), A(2, 2), A(4, 1)], "Number sentences"),
        pg("Write the whole sentence", "Count each group. Write both numbers and the total.", "build",
           [A(1, 2), A(2, 2), A(3, 1), A(4, 1), A(2, 3), A(1, 4)], "Write the sentence"),
        pg("A tiny story", "A grown-up reads. Draw the story. Write how many in all.", "story_total",
           [ST(1, 1, "Mia", "cracker"), ST(2, 1, "Sam", "block", 1), ST(1, 2, "Jo", "cup"), ST(0, 2, "Ana", "hat", 1)],
           "Read-aloud story", track="story", step_back=True),
        pg("Story and sentence", "A grown-up reads. Write the number sentence.", "story_sentence",
           [ST(2, 2, "Leo", "ball"), ST(3, 1, "Ivy", "book", 1), ST(4, 0, "Ben", "spoon"), ST(1, 3, "Cal", "grape", 1)],
           "Read-aloud story", track="story"),
        pg("Stories up to 5", "A grown-up reads. Draw, then write the sentence.", "story_sentence",
           [ST(2, 3, "Mia", "star"), ST(4, 1, "Sam", "bird", 1), ST(5, 0, "Jo", "car"), ST(3, 2, "Ana", "block", 1)],
           "Read-aloud story", track="story"),
        pg("One more story page", "A grown-up reads. Your child writes the sentence.", "story_sentence",
           [ST(1, 4, "Leo", "cup"), ST(2, 2, "Ivy", "hat", 1), ST(0, 4, "Ben", "ball"), ST(3, 1, "Cal", "book", 1)],
           "Read-aloud story", track="story"),
        pg("Show what you know", "Write each total. You can use counters if you want.", "sentence",
           [A(1, 0), A(2, 1), A(0, 3), A(2, 2), A(4, 1), A(3, 2), A(1, 4), A(5, 0)], "Sentence review"),
    ]
    guide = _guide(
        ("h", "How to use this pack"),
        ("p", "Print one practice page at a time. Plan on about 10 minutes. Stop while your child is still willing to sit. One page is a full day. Do the pages in order, from practice page 1 through practice page 18. Each practice page has an answer key at the back of this file, with the same page number. You can leave the keys on a screen instead of printing them."),
        ("h", "I do, we do, you do"),
        ("p", "Problem 1 on each practice page is marked I do. Solve it out loud while your child watches. Problem 2 is marked We do. Solve it together. Your child does the rest. If the rest falls apart, stay on we do for one more problem. That is a useful step, not a failed page."),
        ("h", "Counters, then pictures, then numbers"),
        ("p", "Practice pages 1 and 2 ask your child to count one group. Practice pages 3 and 4 ask for two groups, still without adding. An empty bowl on practice page 4 means 0. If the printed pictures are hard to track, set cereal or coins on top of them and count those. Practice pages 5 to 8 ask for the total. Practice pages 9 to 13 connect the pictures to a number sentence. The totals step back on practice page 9 because the sentence is new. Practice pages 14 to 17 are tiny stories for you to read aloud. Your child does not have to read the story. Practice page 18 reviews the sentences."),
        ("break", ""),
        ("h", "What to say if your child gets stuck"),
        ("p", "On practice pages 1 to 4, say Touch each object as you count. On practice pages 5 to 8, say Count this group. Count the other group. Now count every object. On practice pages 9 to 13, point to the plus sign and say Plus means we put the groups together. On practice pages 14 to 17, ask What happened in the story before you ask How many now. If practice page 18 is shaky, go back to practice page 10 for another day."),
        ("h", "When to move to the next pack"),
        ("p", "Stay with this pack if you are helping with most of the problems on practice pages 12 to 18. Move to Adding within 10 when practice pages 16, 17, and 18 are correct with only a little help, including the stories. If practice page 1 is hard, spend a few days counting real objects up to 5, then start this pack again."),
        ("h", "What you need"),
        ("p", "A printer, US Letter paper, and a pencil. Counters such as cereal or coins are optional. The pages are made to print in black and white."),
    )
    return {
        "id": "k-add-beginner",
        "name": "Adding within 5",
        "level_line": "Beginner pack",
        "limit": 5,
        "blurb": "Count two groups, put them together, and write the total. Then write the number sentence, and listen to a tiny story.",
        "prereq": "Counts objects to 5.",
        "prereq_cover": "Start here if your child can count objects up to 5.",
        "skills": [
            "Counting one group up to 5",
            "Counting two groups, including an empty group as 0",
            "Combining two groups and writing the total",
            "Writing a number sentence within 5",
            "Solving a short read-aloud addition story within 5",
        ],
        "practice": practice,
        "guide_title": "Parent guide",
        "guide": guide,
        "guide_pages": 2,
        "certificate": True,
        "entry_add": 3,
        "entry_story": 3,
        "preview_practice": [3, 7, 15],
    }


def intermediate():
    practice = [
        pg("Pictures to a sentence", "Count the pictures. Finish the number sentence.", "picture_sentence",
           [A(2, 3), A(4, 1), A(1, 3), A(5, 0), A(2, 2), A(3, 2)], "Sentences within 5"),
        pg("Totals of 6", "One new total today: 6. Count, then finish the sentence.", "picture_sentence",
           [A(1, 5), A(4, 1), A(2, 4), A(3, 3), A(6, 0), A(3, 2)], "Totals up to 6"),
        pg("Totals of 7", "The new total is 7. Count both groups.", "picture_sentence",
           [A(1, 6), A(3, 4), A(5, 2), A(7, 0), A(2, 4), A(4, 3)], "Totals up to 7"),
        pg("Totals of 8", "The new total is 8. Finish each sentence.", "picture_sentence",
           [A(2, 6), A(4, 4), A(5, 3), A(1, 7), A(8, 0), A(3, 4)], "Totals up to 8"),
        pg("A ten-frame", "A full top row is 5. Write how many dots you see.", "ten_count",
           [C(2), C(4), C(3), C(5), C(1), C(5)], "Count on a ten-frame", track="count"),
        pg("Five and some more", "A full top row is 5. Count the dots in the bottom row too.", "ten_count",
           [C(5), C(6), C(6), C(7), C(7), C(8)], "Ten-frame to 8", track="count"),
        pg("Add on a ten-frame", "Filled dots are the first number. Empty circles are the second.", "ten_add",
           [A(3, 2), A(4, 1), A(2, 4), A(5, 2), A(6, 1)], "Ten-frame totals to 7"),
        pg("Ten-frame to 8", "Finish the sentence. The frame holds every dot.", "ten_add",
           [A(4, 4), A(5, 3), A(6, 1), A(7, 1), A(3, 5)], "Ten-frame totals to 8"),
        pg("Ten-frame to 9", "The new total is 9. Count the filled dots and the empty circles.", "ten_add",
           [A(5, 4), A(6, 3), A(7, 2), A(8, 1), A(4, 5)], "Ten-frame totals to 9"),
        pg("Fill toward 10", "The new total is 10. A full frame is 10.", "ten_add",
           [A(5, 5), A(6, 4), A(7, 3), A(8, 2), A(9, 1)], "Ten-frame totals to 10"),
        pg("A number line", "Start on the first number. Jump once for each in the second number. Do not count the start.", "nline",
           [A(3, 2), A(4, 1), A(2, 2), A(1, 4), A(6, 0)], "Number line to 6", step_back=True),
        pg("Jumps to 7", "Jump on the line. Write where you land.", "nline",
           [A(2, 5), A(4, 3), A(3, 4), A(6, 1), A(5, 2)], "Number line to 7"),
        pg("Jumps to 8", "One jump for each in the second number.", "nline",
           [A(3, 5), A(4, 4), A(6, 2), A(5, 3), A(2, 6)], "Number line to 8"),
        pg("Jumps to 9", "The new landing is 9. Write the total.", "nline",
           [A(4, 5), A(6, 3), A(7, 2), A(8, 1), A(3, 6)], "Number line to 9"),
        pg("Pictures up to 10", "No frame this time. Count the pictures and finish the sentence.", "picture_sentence",
           [A(1, 8), A(4, 6), A(3, 6), A(5, 5), A(2, 7)], "Pictures up to 10"),
        pg("Sentences up to 10", "Write the total. Draw dots if you want.", "sentence",
           [A(4, 3), A(6, 2), A(5, 4), A(3, 7), A(8, 2), A(4, 6)], "Sentences up to 10"),
        pg("Mix the tools", "A ten-frame, a number line, pictures, and sentences.", "inter_mixed",
           [
               {**A(4, 4), "paint": "ten_add"},
               {**A(3, 5), "paint": "nline"},
               {**A(6, 3), "paint": "picture_sentence"},
               {**A(7, 2), "paint": "sentence"},
               {**A(5, 5), "paint": "sentence"},
           ], "Mixed tools", weights=[1.15, 1.35, 1.15, 0.9, 0.9]),
        pg("Show what you know", "Write each total. The last two land on 10.", "sentence",
           [A(2, 3), A(4, 2), A(3, 4), A(5, 3), A(2, 7), A(9, 0), A(6, 4), A(8, 2)], "Sentence review"),
    ]
    guide = _guide(
        ("h", "How to use this pack"),
        ("p", "About 10 minutes a day is enough. Print one page, work in order, and stop while your child is still willing. Practice pages run from 1 to 18. The answer key for each page is at the back. Start this pack only if adding within 5 already feels comfortable."),
        ("h", "I do, we do, you do"),
        ("p", "Problem 1 is marked I do. Do it out loud. Problem 2 is marked We do. Do it together. Your child does the rest. If the rest is too hard, do another problem together before you move on."),
        ("h", "Pictures, the ten-frame, then the number line"),
        ("p", "Practice pages 1 to 4 turn pictures into number sentences. The totals grow one step at a time, from 5 up to 8. Practice pages 5 and 6 introduce the ten-frame, a grid with 10 spaces. A full top row is 5. Practice pages 7 to 10 add on the ten-frame, with totals 7, then 8, then 9, then 10. Practice pages 11 to 14 use a number line. The jumps start small on purpose, even though the ten-frame pages already reached 10. Practice page 15 goes back to loose pictures. Practice pages 16 and 18 are number sentences. Practice page 17 mixes the tools."),
        ("break", ""),
        ("h", "What to say if your child gets stuck"),
        ("p", "On the ten-frame, say Fill the top row first. A full top row is 5. Now count the rest. On the number line, say Put your finger on the first number. Jump one space for each in the second number. Do not count the space you start on. If a sentence is a guess, go back to practice page 4 or the ten-frame on practice page 10."),
        ("h", "When to move to the next pack"),
        ("p", "Stay here if the sentences on practice pages 16 to 18 still feel like guesses. Move to Story problems within 10 when your child can add totals up to 10 with only a little help, including practice page 18. If this pack feels too big, go back to Adding within 5 and finish those stories first."),
        ("h", "What you need"),
        ("p", "A printer, US Letter paper, and a pencil. Counters such as cereal or coins are optional. You can set counters in the ten-frame before your child writes."),
    )
    return {
        "id": "k-add-intermediate",
        "name": "Adding within 10",
        "level_line": "Intermediate pack",
        "limit": 10,
        "blurb": "Turn pictures into number sentences with totals up to 10. Practice on a ten-frame and on a number line.",
        "prereq": "Comfortable adding within 5.",
        "prereq_cover": "Start here if your child is comfortable adding within 5.",
        "skills": [
            "Writing number sentences from pictures, totals growing from 5 to 10",
            "Counting dots on a ten-frame",
            "Adding two groups on a ten-frame within 10",
            "Adding on a number line within 10",
        ],
        "practice": practice,
        "guide_title": "Parent guide",
        "guide": guide,
        "guide_pages": 2,
        "certificate": True,
        "entry_add": 5,
        "preview_practice": [4, 10, 12],
    }


def advanced():
    practice = [
        pg("Partners of 5", "The two groups make 5. Write both parts.", "partners",
           [PART(5, 1, 4), PART(5, 2, 3), PART(5, 3, 2), PART(5, 4, 1), PART(5, 5, 0), PART(5, 0, 5)],
           "Partners of 5", track="partners"),
        pg("The missing part of 5", "Filled dots are the part you know. Count the empty circles for the other part.", "missing_pic",
           [MISS(5, 1), MISS(5, 2), MISS(5, 4), MISS(5, 0), MISS(5, 3), MISS(5, 5)],
           "Missing part of 5", track="partners"),
        pg("Partners of 6", "These groups make 6. Write both parts.", "partners",
           [PART(6, 1, 5), PART(6, 2, 4), PART(6, 3, 3), PART(6, 4, 2), PART(6, 5, 1), PART(6, 6, 0)],
           "Partners of 6", track="partners"),
        pg("The missing part of 6", "Write the part that is still empty.", "missing_pic",
           [MISS(6, 1), MISS(6, 4), MISS(6, 2), MISS(6, 5), MISS(6, 3), MISS(6, 0)],
           "Missing part of 6", track="partners"),
        pg("Partners of 7", "Write the two parts that make 7.", "partners",
           [PART(7, 1, 6), PART(7, 2, 5), PART(7, 3, 4), PART(7, 4, 3), PART(7, 5, 2), PART(7, 6, 1)],
           "Partners of 7", track="partners"),
        pg("Partners of 8", "Write both parts. The total is 8.", "partners",
           [PART(8, 2, 6), PART(8, 3, 5), PART(8, 4, 4), PART(8, 5, 3), PART(8, 1, 7), PART(8, 8, 0)],
           "Partners of 8", track="partners"),
        pg("Partners of 9", "Write both parts. The total is 9.", "partners",
           [PART(9, 1, 8), PART(9, 2, 7), PART(9, 3, 6), PART(9, 4, 5), PART(9, 9, 0)],
           "Partners of 9", track="partners"),
        pg("Partners of 10", "Write both parts. The total is 10.", "partners",
           [PART(10, 1, 9), PART(10, 2, 8), PART(10, 3, 7), PART(10, 4, 6), PART(10, 5, 5)],
           "Partners of 10", track="partners"),
        pg("A missing part", "Draw the missing objects if you need them. Write the missing part.", "missing_draw",
           [MISS(6, 4), MISS(7, 2), MISS(8, 3), MISS(6, 1), MISS(7, 5), MISS(8, 6)],
           "Missing part to 8", track="partners"),
        pg("Missing parts up to 10", "Build the total with counters if it helps. Cover the part you know.", "missing_draw",
           [MISS(9, 4), MISS(9, 2), MISS(10, 3), MISS(10, 7), MISS(9, 6), MISS(10, 1)],
           "Missing part to 10", track="partners"),
        pg("Make 10 on a frame", "Count the empty spaces. That is how many more make 10.", "make10_frame",
           [M10(4), M10(5), M10(6), M10(7), M10(8), M10(9)], "Make 10 on a frame", track="make10"),
        pg("More ways to make 10", "The empty spaces are the missing part.", "make10_frame",
           [M10(2), M10(3), M10(6), M10(7), M10(8), M10(9)], "Make 10 again", track="make10"),
        pg("Make 10 without the frame", "How many more to make 10? Draw dots in the little box if you want.", "make10_draw",
           [M10(0), M10(1), M10(4), M10(5), M10(8), M10(10)], "Make 10 by drawing", track="make10"),
        pg("A short story", "A grown-up reads. Draw the story and write the sentence. Totals stay small today.", "story_sentence",
           [ST(2, 2, "Mia", "cracker"), ST(3, 1, "Sam", "block", 1), ST(1, 3, "Jo", "cup"), ST(2, 3, "Ana", "hat", 1)],
           "Story within 5", track="story", step_back=True),
        pg("Stories to 7", "A grown-up reads. The totals are a little bigger.", "story_sentence",
           [ST(4, 2, "Leo", "ball"), ST(3, 4, "Ivy", "book", 1), ST(5, 2, "Ben", "spoon"), ST(6, 1, "Cal", "grape", 1)],
           "Story within 7", track="story"),
        pg("Stories to 9", "A grown-up reads. Draw, then write the sentence.", "story_sentence",
           [ST(4, 4, "Mia", "star"), ST(5, 3, "Sam", "bird", 1), ST(6, 3, "Jo", "car"), ST(4, 5, "Ana", "block", 1)],
           "Story within 9", track="story"),
        pg("Explain with a drawing", "Draw a picture of the sentence. Then write the total.", "explain",
           [A(6, 4), A(5, 3), A(7, 2), A(4, 5)], "Explain with a drawing", track="explain"),
        pg("Partners, 10, and a story", "Two missing parts, two make-10 problems, then two stories a grown-up reads.", "adv_mixed",
           [
               {**MISS(8, 5), "paint": "missing_draw"},
               {**MISS(10, 4), "paint": "missing_draw"},
               {**M10(7), "paint": "make10_draw"},
               {**M10(3), "paint": "make10_draw"},
               {**ST(2, 5, "Leo", "cup"), "paint": "story_sentence"},
               {**ST(4, 6, "Ivy", "hat", 1), "paint": "story_sentence"},
           ], "Mixed review", track="mix", weights=[0.68, 0.68, 0.68, 0.68, 1.64, 1.64]),
    ]
    guide = _guide(
        ("h", "How to use this pack"),
        ("p", "About 10 minutes a day. One page is enough. Go in order from practice page 1 to practice page 18. Answer keys are at the back. Start this pack if your child can add within 10 when pictures are there to count. You will read the stories out loud."),
        ("h", "I do, we do, you do"),
        ("p", "Do problem 1, marked I do, out loud. Do problem 2, marked We do, together. Let your child try the rest. If the rest comes apart, go back to doing one together."),
        ("h", "Partners, make 10, then stories"),
        ("p", "Practice pages 1 and 2 break 5 into two parts. The numbers are small on purpose, because partners is the new idea. Practice pages 3 to 8 grow the total one step at a time, from 6 up to 10. Practice pages 9 and 10 ask for a missing part. Your child can draw the missing objects. Practice pages 11 to 13 are make 10. The ten-frame on practice pages 11 and 12 shows the empty spaces. Practice pages 14 to 16 are short stories you read aloud. The stories start with small totals again. Practice page 17 asks your child to explain a sentence by drawing. Practice page 18 mixes partners, make 10, and a story."),
        ("break", ""),
        ("h", "What to say if your child gets stuck"),
        ("p", "Act the problem out with cereal or coins. Ask What are the two parts before you ask for a total. For a missing number, build the whole total with counters, cover the part you already know, and count what is still showing. For a story, ask What happened before How many. If make 10 is sticky, go back to practice page 11, where the empty spaces are easy to see."),
        ("h", "When this pack is finished"),
        ("p", "Stay here if missing numbers still need a lot of help. When practice pages 16, 17, and 18 feel comfortable with only a little help, this pack is finished. This set does not go on to a harder addition pack. These pages do not teach subtraction."),
        ("h", "What you need"),
        ("p", "A printer, US Letter paper, and a pencil. Counters such as cereal or coins are optional."),
    )
    return {
        "id": "k-add-advanced",
        "name": "Story problems within 10",
        "level_line": "Advanced pack",
        "limit": 10,
        "blurb": "Break numbers into parts, make 10, and solve short stories you read aloud. Explain an answer by drawing.",
        "prereq": "Adds within 10 with pictures.",
        "prereq_cover": "Start here if your child adds within 10 with pictures.",
        "skills": [
            "Finding number partners for totals from 5 to 10",
            "Finding a missing part",
            "Making 10 on a ten-frame and without one",
            "Solving short read-aloud story problems within 10",
            "Explaining an addition sentence with a drawing",
        ],
        "practice": practice,
        "guide_title": "Parent guide",
        "guide": guide,
        "guide_pages": 2,
        "certificate": True,
        "entry_story": 5,
        "preview_practice": [1, 11, 15],
    }


def _note(pages_line, map_line, stuck, move):
    return _guide(
        ("h", "How this week goes"),
        ("p", pages_line),
        ("h", "I do, we do, you do"),
        ("p", "Problem 1 is marked I do. Do it out loud. Problem 2 is marked We do. Do it together. Your child does the rest. If the rest falls apart, do one more problem together."),
        ("h", "What is on each page"),
        ("p", map_line),
        ("h", "If your child gets stuck"),
        ("p", stuck),
        ("h", "When to go to next week"),
        ("p", move),
        ("h", "What you need"),
        ("p", "A printer, US Letter paper, and a pencil. Counters such as cereal or coins are optional."),
    )


def _week(num, name, blurb, prereq, prereq_cover, skills, practice, note, preview, limit):
    return {
        "id": f"week-{num:02d}",
        "week": num,
        "name": name,
        "kicker": f"Week {num} of 8",
        "level_line": "",
        "limit": limit,
        "blurb": blurb,
        "prereq": prereq,
        "prereq_cover": prereq_cover,
        "skills": skills,
        "practice": practice,
        "guide_title": "This week's note",
        "guide": note,
        "guide_pages": 1,
        "certificate": False,
        "weekly": True,
        "preview_practice": preview,
    }


def weekly():
    w1 = [
        pg("Count the buttons", "Count the buttons. Write how many.", "count",
           [C(1), C(2), C(3), C(4), C(5), C(3)], "Count to 5", track="count"),
        pg("Buttons in a different order", "Count each group. Write the number.", "count",
           [C(2), C(4), C(1), C(5), C(3), C(2)], "Count mixed groups", track="count"),
        pg("Squares to count", "Count the squares. An empty bowl means 0.", "count",
           [C(5, "square"), C(0, "square"), C(3, "square"), C(4, "square"), C(1, "square"), C(2, "square")],
           "Count, including 0", track="count"),
        pg("Draw that many", "Read the number. Draw that many dots in the big box.", "draw_dots",
           [{"kind": "dots", "n": n} for n in (2, 4, 1, 3, 5, 2)], "Draw the number", track="count"),
        pg("What comes next?", "Write the number that comes next. Each step is one more.", "sequence",
           [
               {"kind": "missing_num", "seq": [1, 2, 3, 4], "blank": 3},
               {"kind": "missing_num", "seq": [0, 1, 2, 3], "blank": 3},
               {"kind": "missing_num", "seq": [2, 3, 4, 5], "blank": 3},
               {"kind": "missing_num", "seq": [1, 2, 3, 4, 5], "blank": 4},
               {"kind": "missing_num", "seq": [0, 1, 2], "blank": 2},
               {"kind": "missing_num", "seq": [3, 4, 5], "blank": 2},
           ], "The next number", track="sequence"),
        pg("Two groups, not adding", "Count each group. Write both numbers. Do not add.", "two",
           [TWO(1, 2), TWO(2, 2), TWO(3, 1), TWO(1, 4), TWO(0, 3), TWO(2, 1)], "Count two groups", track="count"),
        pg("Count once more", "Count each group and write how many.", "count",
           [C(4), C(1), C(5), C(2), C(3), C(0)], "Count review", track="count"),
    ]
    w2 = [
        pg("Five and six", "Count the circles. You will see 6, which is one more than 5.", "count",
           [C(5), C(6), C(5), C(6), C(4), C(6)], "Count to 6", track="count"),
        pg("Six and seven", "The new count is 7. Touch each circle.", "count",
           [C(7), C(6), C(7), C(5), C(6), C(7)], "Count to 7", track="count"),
        pg("Seven and eight", "The new count is 8.", "count",
           [C(8), C(7), C(8), C(6), C(8), C(7)], "Count to 8", track="count"),
        pg("Eight and nine", "The new count is 9.", "count",
           [C(9), C(8), C(9), C(7), C(8), C(9)], "Count to 9", track="count"),
        pg("Nine and ten", "The new count is 10. A group of 10 is two rows of 5.", "count",
           [C(10), C(9), C(10), C(8), C(9), C(10)], "Count to 10", track="count"),
        pg("The ten-frame", "A full top row is 5. A full frame is 10. Write how many dots.", "ten_count",
           [C(5), C(6), C(7), C(8), C(9), C(10)], "Ten-frame counts", track="count"),
        pg("What comes next?", "Write the number that comes next.", "sequence",
           [
               {"kind": "missing_num", "seq": [4, 5, 6, 7], "blank": 3},
               {"kind": "missing_num", "seq": [6, 7, 8, 9], "blank": 3},
               {"kind": "missing_num", "seq": [7, 8, 9, 10], "blank": 3},
               {"kind": "missing_num", "seq": [3, 4, 5, 6], "blank": 3},
               {"kind": "missing_num", "seq": [8, 9, 10], "blank": 2},
               {"kind": "missing_num", "seq": [5, 6, 7, 8], "blank": 3},
           ], "Next number to 10", track="sequence"),
    ]
    w3 = [
        pg("Which has more?", "Circle the group that has more. A grown-up can point and say more.", "more",
           [{"kind": "more", "a": a, "b": b} for a, b in ((1, 3), (4, 2), (2, 5), (3, 1), (5, 3), (1, 4))],
           "More, within 5", track="compare"),
        pg("More, by just one", "Circle the group that has more. These pairs are close.", "more",
           [{"kind": "more", "a": a, "b": b} for a, b in ((2, 3), (4, 3), (1, 2), (5, 4), (3, 2), (4, 5))],
           "More, one apart", track="compare"),
        pg("Which has fewer?", "Circle the group that has fewer.", "fewer",
           [{"kind": "fewer", "a": a, "b": b} for a, b in ((1, 4), (5, 2), (3, 5), (4, 1), (2, 4), (5, 3))],
           "Fewer, within 5", track="compare"),
        pg("Fewer, by just one", "Circle the group that has fewer.", "fewer",
           [{"kind": "fewer", "a": a, "b": b} for a, b in ((3, 2), (4, 5), (2, 1), (5, 4), (3, 4), (1, 2))],
           "Fewer, one apart", track="compare"),
        pg("Same or not", "Circle same or not the same. A grown-up reads the words.", "same",
           [{"kind": "same", "a": a, "b": b} for a, b in ((0, 0), (2, 2), (3, 1), (4, 4), (5, 2), (1, 1))],
           "Same amount", track="compare"),
        pg("More, up to 10", "Circle the group that has more. These groups are bigger.", "more",
           [{"kind": "more", "a": a, "b": b} for a, b in ((4, 7), (8, 5), (3, 6), (9, 6), (7, 10), (2, 5))],
           "More, within 10", track="compare"),
        pg("Which number is more?", "Circle the number that is more. If they match, circle both.", "numerals",
           [{"kind": "numerals", "a": a, "b": b} for a, b in ((3, 7), (9, 4), (8, 8), (6, 8), (10, 7), (5, 5))],
           "Compare numbers", track="compare"),
    ]
    w4 = [
        pg("Two snack groups", "Count each group. Write both numbers. Do not add yet.", "two",
           [TWO(1, 1), TWO(2, 1), TWO(1, 2), TWO(2, 0), TWO(3, 1), TWO(1, 3)], "Count both snacks", track="count"),
        pg("Put the snacks together", "Count both groups. Write how many in all.", "picture_total",
           [A(1, 1), A(2, 1), A(1, 2), A(0, 2), A(2, 0), A(1, 0)], "Totals up to 3"),
        pg("Totals of 4", "The new totals reach 4.", "picture_total",
           [A(2, 2), A(3, 1), A(1, 3), A(4, 0), A(0, 3), A(2, 1)], "Totals up to 4"),
        pg("Totals of 5", "The new totals reach 5.", "picture_total",
           [A(4, 1), A(2, 3), A(3, 2), A(5, 0), A(1, 4), A(0, 5)], "Totals up to 5"),
        pg("A snack sentence", "The sentence is new, so the totals step back. Write the total.", "picture_sentence",
           [A(1, 2), A(2, 2), A(3, 1), A(0, 4), A(2, 1), A(4, 0)], "Sentences to 4", step_back=True),
        pg("Sentences to 5", "Finish the number sentence.", "picture_sentence",
           [A(3, 2), A(4, 1), A(2, 3), A(1, 4), A(5, 0), A(3, 1)], "Sentences to 5"),
        pg("Sentences on your own", "Write the total. Draw dots if you want.", "sentence",
           [A(1, 1), A(2, 2), A(0, 3), A(4, 1), A(3, 2), A(1, 3), A(5, 0), A(2, 1)], "Sentence review"),
    ]
    w5 = [
        pg("Picture sentences", "Count the pictures. Finish the sentence.", "picture_sentence",
           [A(2, 2), A(3, 1), A(1, 4), A(2, 3), A(0, 4), A(4, 1)], "Picture sentences"),
        pg("Count on", "Filled dots are the first number. Empty circles are the second.", "count_on",
           [A(3, 2), A(4, 1), A(2, 2), A(1, 3), A(5, 0), A(2, 3)], "Count on"),
        pg("Sentences", "Write the total.", "sentence",
           [A(1, 2), A(3, 2), A(0, 5), A(4, 0), A(2, 1), A(1, 3), A(3, 1), A(2, 2)], "Sentences"),
        pg("Build the sentence", "Write both numbers and the total.", "build",
           [A(2, 1), A(3, 2), A(1, 1), A(4, 1), A(0, 3), A(2, 3)], "Build the sentence"),
        pg("Listen to a story", "A grown-up reads. Draw the story. Write how many in all.", "story_total",
           [ST(1, 1, "Mia", "grape"), ST(2, 1, "Sam", "cracker", 1), ST(0, 2, "Jo", "block"), ST(1, 2, "Ana", "cup", 1)],
           "Story, write the total", track="story", step_back=True),
        pg("Story sentences", "A grown-up reads. Write the number sentence.", "story_sentence",
           [ST(2, 2, "Leo", "hat"), ST(3, 1, "Ivy", "star", 1), ST(4, 0, "Ben", "book"), ST(1, 3, "Cal", "spoon", 1)],
           "Story sentence", track="story"),
        pg("Stories to 5", "A grown-up reads. Your child writes the sentence.", "story_sentence",
           [ST(3, 1, "Mia", "ball"), ST(2, 3, "Sam", "car", 1), ST(5, 0, "Jo", "bird"), ST(1, 4, "Ana", "block", 1)],
           "Story to 5", track="story"),
    ]
    w6 = [
        pg("Warm up within 5", "Finish the sentence. These totals stay at 5.", "picture_sentence",
           [A(2, 3), A(4, 1), A(3, 2), A(1, 4), A(5, 0), A(2, 2)], "Review within 5"),
        pg("A total of 6", "The new total is 6.", "picture_sentence",
           [A(1, 5), A(3, 3), A(4, 2), A(6, 0), A(2, 4), A(5, 1)], "Totals of 6"),
        pg("A total of 7", "The new total is 7.", "picture_sentence",
           [A(2, 5), A(4, 3), A(6, 1), A(3, 4), A(7, 0), A(1, 6)], "Totals of 7"),
        pg("A total of 8", "The new total is 8.", "picture_sentence",
           [A(4, 4), A(3, 5), A(6, 2), A(5, 3), A(8, 0), A(2, 6)], "Totals of 8"),
        pg("Learn the ten-frame", "A full top row is 5. Write how many dots.", "ten_count",
           [C(4), C(5), C(6), C(7), C(8), C(5)], "Ten-frame counts", track="count"),
        pg("Add on the frame to 8", "Filled dots, then empty circles. Finish the sentence.", "ten_add",
           [A(3, 4), A(5, 2), A(6, 2), A(4, 4), A(2, 5)], "Frame totals to 8"),
        pg("Frame totals of 9", "The new total is 9.", "ten_add",
           [A(4, 5), A(6, 3), A(7, 2), A(5, 4), A(8, 1)], "Frame totals to 9"),
        pg("Sentences to 10", "The new total is 10. Write the total. Draw dots if you want.", "sentence",
           [A(3, 4), A(5, 3), A(2, 7), A(4, 5), A(6, 4), A(3, 7), A(8, 2), A(5, 5)], "Sentences to 10"),
    ]
    w7 = [
        pg("Some were taken", "Crossed objects were taken away. Count the filled ones that are left.", "sub_shown",
           [SUB(2, 1), SUB(3, 1), SUB(3, 2), SUB(1, 0), SUB(2, 0), SUB(3, 0)], "Take away from 3", track="sub"),
        pg("Take away from 4", "Count what is left. The crossed ones are gone.", "sub_shown",
           [SUB(4, 1), SUB(4, 0), SUB(3, 1), SUB(4, 2), SUB(2, 1), SUB(4, 1)], "Take away from 4", track="sub"),
        pg("Take away from 5", "Count the filled circles.", "sub_shown",
           [SUB(5, 1), SUB(5, 2), SUB(4, 2), SUB(5, 0), SUB(3, 2), SUB(5, 3)], "Take away from 5", track="sub"),
        pg("You cross them out", "Cross out the number in the problem. Write how many are left. Totals step back because you make the marks.", "sub_cross",
           [SUB(3, 1), SUB(4, 1), SUB(2, 2), SUB(4, 2), SUB(3, 0), SUB(1, 1)], "Cross out, within 4", track="sub", step_back=True),
        pg("Cross out from 5", "Cross out that many. Write how many are left.", "sub_cross",
           [SUB(5, 1), SUB(5, 2), SUB(4, 3), SUB(5, 3), SUB(5, 4), SUB(3, 3)], "Cross out from 5", track="sub"),
        pg("A take-away sentence", "The crossed circles are gone. Finish the sentence.", "sub_sentence",
           [SUB(4, 1), SUB(5, 2), SUB(3, 1), SUB(5, 0), SUB(2, 2), SUB(4, 3)], "Sentences within 5", track="sub"),
        pg("Take-away stories", "A grown-up reads. Write the sentence for what is left.", "sub_story",
           [SST(3, 1, "Mia", "grape"), SST(5, 2, "Sam", "cracker"), SST(4, 1, "Jo", "block"), SST(5, 1, "Ana", "cup")],
           "Take-away story", track="sub"),
    ]
    shapes = ("triangle", "square", "circle", "rectangle")
    w8 = [
        pg("How many corners?", "Write how many corners. A circle is round, so it has 0 corners.", "corners",
           [{"kind": "corners", "shape": s} for s in ("triangle", "square", "circle", "rectangle", "triangle", "square")],
           "Count corners", track="shape"),
        pg("How many sides?", "Write how many straight sides.", "sides",
           [{"kind": "sides", "shape": s} for s in ("triangle", "square", "rectangle", "triangle", "rectangle", "square")],
           "Count sides", track="shape"),
        pg("How many triangles?", "Count only the triangles in each box.", "shape_count",
           [
               {"kind": "shape_count", "target": "triangle", "shapes": row}
               for row in (
                   ["triangle", "circle", "square", "triangle"],
                   ["circle", "circle", "square", "rectangle"],
                   ["triangle", "triangle", "triangle", "circle"],
                   ["square", "triangle", "rectangle", "circle"],
                   ["triangle", "square", "triangle", "square"],
                   ["rectangle", "circle", "triangle", "triangle"],
               )
           ], "Count the triangles", track="shape"),
        pg("How many circles?", "Count only the circles in each box.", "shape_count",
           [
               {"kind": "shape_count", "target": "circle", "shapes": row}
               for row in (
                   ["circle", "square", "circle", "triangle"],
                   ["triangle", "square", "rectangle", "triangle"],
                   ["circle", "circle", "circle", "square"],
                   ["square", "circle", "rectangle", "triangle"],
                   ["circle", "triangle", "circle", "rectangle"],
                   ["square", "rectangle", "square", "circle"],
               )
           ], "Count the circles", track="shape"),
        pg("A pattern of two", "The two shapes take turns. Draw the next two.", "pattern",
           [
               {"kind": "pattern", "rule": ["circle", "square"], "repeats": 3, "ask": 2},
               {"kind": "pattern", "rule": ["square", "triangle"], "repeats": 3, "ask": 2},
               {"kind": "pattern", "rule": ["triangle", "circle"], "repeats": 3, "ask": 2},
               {"kind": "pattern", "rule": ["rectangle", "circle"], "repeats": 3, "ask": 2},
           ], "AB patterns", track="pattern"),
        pg("A pattern with a pair", "Look for the shape that repeats twice. Draw the next two.", "pattern",
           [
               {"kind": "pattern", "rule": ["circle", "square", "square"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["triangle", "circle", "circle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["square", "triangle", "triangle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["rectangle", "square", "square"], "repeats": 2, "ask": 2},
           ], "ABB patterns", track="pattern"),
        pg("A pattern of three", "Three shapes repeat. Draw the next two.", "pattern",
           [
               {"kind": "pattern", "rule": ["circle", "square", "triangle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["triangle", "rectangle", "circle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["square", "triangle", "rectangle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["circle", "triangle", "square"], "repeats": 2, "ask": 2},
           ], "ABC patterns", track="pattern"),
        pg("Patterns on your own", "Find the part that repeats. Draw the next two shapes.", "pattern",
           [
               {"kind": "pattern", "rule": ["square", "circle"], "repeats": 3, "ask": 2},
               {"kind": "pattern", "rule": ["triangle", "rectangle"], "repeats": 3, "ask": 2},
               {"kind": "pattern", "rule": ["circle", "triangle", "triangle"], "repeats": 2, "ask": 2},
               {"kind": "pattern", "rule": ["rectangle", "circle", "square"], "repeats": 2, "ask": 2},
           ], "Pattern review", track="pattern"),
    ]
    # shapes tuple kept so a typo in a shape name is easier to spot in review
    assert set(shapes) == {"triangle", "square", "circle", "rectangle"}
    weeks = [
        _week(1, "Counting to 5", "Count buttons up to 5, draw a number, and say what comes next.",
              "Can point to objects one at a time.",
              "Start here if your child can point to objects one at a time.",
              ["Counting groups up to 5", "Writing a number for a group", "Drawing a given number of dots", "Saying the next number up to 5"],
              w1,
              _note("This week is counting, not adding. About 10 minutes a day. One page is enough. Do practice pages 1 to 7 in order. The answer key for each page is at the back.",
                    "Practice pages 1 to 3: count a group and write how many. Practice page 3 includes an empty bowl, which is 0. Practice page 4: read the numeral and draw that many dots. Practice page 5: write the number that comes next. Practice page 6: count two groups, but do not add them. Practice page 7 is a short counting review.",
                    "Say Touch each button as you count. If practice page 1 is hard, count real buttons or cereal together, then come back to the page.",
                    "Next week is counting to 10. Move on when your child can count groups up to 5 with only a little help, including practice page 7."),
              [1, 5], 5),
        _week(2, "Counting to 10", "Count groups from 5 up to 10, then count the same numbers on a ten-frame.",
              "Counts objects to 5.",
              "Start here if your child can count objects up to 5.",
              ["Counting groups from 6 through 10", "Counting dots on a ten-frame", "Saying the next number up to 10"],
              w2,
              _note("About 10 minutes a day. The counts grow by one each page, from 6 up to 10. Do practice pages 1 to 7 in order.",
                    "Practice pages 1 to 5 count loose circles, one new number at a time. Practice page 6 puts those counts on a ten-frame. A full top row is 5, and a full frame is 10. Practice page 7 asks what number comes next, up to 10.",
                    "If 8, 9, or 10 falls apart, cover the bottom row and count the top row of 5 first, then the extras. Go back one page rather than skipping ahead.",
                    "Next week is comparing. Move on when counting to 10, including the ten-frame on practice page 6, needs only a little help."),
              [5, 6], 10),
        _week(3, "More and fewer", "Circle the group with more, the group with fewer, or the numbers that match.",
              "Counts objects to 10.",
              "Start here if your child can count objects up to 10.",
              ["Comparing two groups as more or fewer", "Deciding whether two groups are the same amount", "Comparing numerals up to 10"],
              w3,
              _note("About 10 minutes a day. This week uses the counts from the last two weeks. No adding yet.",
                    "Practice pages 1 and 2: circle the group with more, first an easy gap, then a gap of one, all within 5. Practice pages 3 and 4 do the same for fewer. Practice page 5 asks whether the groups are the same. A grown-up reads the words same and not the same. Practice page 6 compares bigger groups, up to 10. Practice page 7 compares numerals. Circle both numbers if they match.",
                    "Have your child line the objects up with a finger, one to one. The row with extras is more. The row that runs out is fewer.",
                    "Next week is adding within 5. Move on when practice pages 6 and 7 are solid with only a little help."),
              [1, 6], 10),
        _week(4, "Adding within 5", "Put two snack groups together and write totals up to 5.",
              "Counts objects to 5.",
              "Start here if your child can count objects up to 5.",
              ["Counting two groups without adding", "Combining groups to totals of 3, then 4, then 5", "Finishing a number sentence within 5"],
              w4,
              _note("About 10 minutes a day. Totals stay at 5 or below and grow one step at a time.",
                    "Practice page 1 counts two groups and stops there. Practice pages 2 to 4 write the total, first to 3, then 4, then 5. Practice page 5 introduces the number sentence, so the totals step back. Practice page 6 brings the sentence up to 5. Practice page 7 is sentences without pictures.",
                    "Say Count this group. Count the other group. Now count every snack. If the plus sign is new, say Plus means the groups go together.",
                    "Next week keeps totals within 5 and adds stories. Move on when practice page 7 is correct with only a little help."),
              [2, 6], 5),
        _week(5, "Stories within 5", "Number sentences within 5, then tiny stories a grown-up reads aloud.",
              "Can combine two groups within 5.",
              "Start here if your child can combine two groups with totals up to 5.",
              ["Finishing number sentences within 5", "Writing a full number sentence from pictures", "Solving a read-aloud addition story within 5"],
              w5,
              _note("About 10 minutes a day. Your child does not have to read the stories. You do.",
                    "Practice pages 1 to 4 are sentences: with pictures, by counting on, as plain sentences, then writing every number. Practice pages 5 to 7 are stories. Practice page 5 asks only for the total. Practice pages 6 and 7 ask for the whole sentence. Totals on the first story page are small because the story is new.",
                    "Ask What happened in the story before How many now. If a sentence is a guess, go back to practice page 1 and match each group to a number.",
                    "Next week is adding within 10. Move on when the stories on practice pages 6 and 7 need only a little help."),
              [4, 6], 5),
        _week(6, "Adding within 10", "Grow totals from 5 to 10, with pictures and a ten-frame.",
              "Comfortable adding within 5.",
              "Start here if your child is comfortable adding within 5.",
              ["Writing number sentences with totals from 6 to 10", "Adding on a ten-frame", "Seeing 10 as one more than the totals already practiced"],
              w6,
              _note("About 10 minutes a day. A new total arrives only after the one before it feels workable.",
                    "Practice page 1 reviews totals within 5. Practice pages 2, 3, and 4 introduce 6, then 7, then 8, with pictures. Practice page 5 is the ten-frame. A full top row is 5. Practice pages 6 and 7 add on the frame, to 8 and then to 9. Practice page 8 is the first page with a total of 10, written as a sentence.",
                    "On the frame, say Top row first. That row holds 5. If practice page 8 is a guess, return to practice page 7 and add one counter to a total of 9.",
                    "Next week is taking away within 5. Move on when sentences to 10, including practice page 8, need only a little help."),
              [5, 8], 10),
        _week(7, "Subtracting within 5", "Take some away and count what is left. Totals start at 5 or below.",
              "Counts objects to 5 and can add within 5.",
              "Start here if your child can count to 5 and add within 5.",
              ["Counting what is left when some objects are crossed out", "Crossing out a given number within 5", "Writing a subtraction sentence within 5", "Solving a short read-aloud take-away story"],
              w7,
              _note("About 10 minutes a day. Nothing on these pages starts above 5, and you never take away more than you have.",
                    "Practice pages 1 to 3 show the take-away already crossed out. The starting number grows from 3 to 4 to 5. Practice pages 4 and 5 ask your child to make the crosses. Practice page 4 steps back to smaller numbers because the marking is new. Practice page 6 writes a sentence. Practice page 7 is a story you read aloud.",
                    "Say These were here. These went away. Count the ones still filled in. Match counters to the circles and physically take the counters away if the crosses are confusing.",
                    "Next week leaves addition and subtraction for shapes and patterns. Stay on this week if the stories on practice page 7 still need a lot of help."),
              [3, 7], 5),
        _week(8, "Shapes and patterns", "Count corners and sides, then extend a simple repeating pattern.",
              "Counts objects to 10.",
              "Start here if your child can count objects up to 10.",
              ["Counting corners, including 0 for a circle", "Counting sides of triangles, squares, and rectangles", "Counting how many of a named shape", "Extending AB, ABB, and ABC patterns"],
              w8,
              _note("About 10 minutes a day. Shapes come first. Patterns use those shapes, and they start with the simplest repeat.",
                    "Practice page 1 counts corners. A circle has 0. Practice page 2 counts straight sides. Practice pages 3 and 4 count only the triangles, then only the circles. Practice page 5 is a two-shape pattern: one, then the other, over and over. Practice page 6 repeats a shape in a pair. Practice page 7 repeats three shapes. Practice page 8 mixes those patterns.",
                    "For a pattern, cover the row and reveal one repeat at a time. Say the shape names together, then ask your child to keep the chant going into the empty boxes.",
                    "This is the last packet in this set of eight. When practice page 8 needs only a little help, your child has finished this eight-week run."),
              [1, 5], 10),
    ]
    return weeks


def all_products():
    return [beginner(), intermediate(), advanced()], weekly()
