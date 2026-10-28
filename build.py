# Generates all HTML pages. Change BRAND here (and in assets/config.js), then: python3 build.py
import os
BRAND="Proud Little Learners"
EMAIL="hello@example.com"
LINKS=dict(
 cc_math="https://www.thecorestandards.org/Math/Content/K/OA/",
 cc_ela="https://www.thecorestandards.org/ELA-Literacy/RF/K/",
 elof="https://headstart.gov/interactive-head-start-early-learning-outcomes-framework-ages-birth-five",
 dap="https://www.naeyc.org/resources/position-statements/dap/definition",
 wwc_math="https://ies.ed.gov/ncee/WWC/PracticeGuide/18",
 wwc_read="https://ies.ed.gov/ncee/wwc/PracticeGuide/21",
 eric_zpd="https://files.eric.ed.gov/fulltext/ED446740.pdf",
 eric_scaffold="https://files.eric.ed.gov/fulltext/EJ1100363.pdf",
 ida="https://dyslexiaida.org/structured-literacy-effective-instruction-for-students-with-dyslexia-and-related-reading-difficulties/",
)
def page(fn,title,desc,body,sticky=False,head='',js='',cls='',sticky_href=None,sticky_label=None):
    depth=fn.count("/");R="../"*depth
    nav=[("Kindergarten Math","kindergarten-math.html"),("Weekly plan","weekly.html"),("Our Approach","our-educational-approach.html"),("Questions","faq.html")]
    navh="".join(f'<li><a href="{R}{h}">{t}</a></li>' for t,h in nav)
    body=body.replace("{R}",R).replace("{BRAND}",BRAND)
    head=head.replace("{R}",R).replace("{BRAND}",BRAND)
    if sticky:
        href=sticky_href or f"{R}weekly.html"
        label=sticky_label or "See the weekly plan"
        st=f'<div class="sticky-cta"><a class="btn" href="{href}">{label}</a></div>'
    else:
        st=""
    canon="https://proudlittlelearners.com/"+("" if fn=="index.html" else fn)
    canon_tags="" if 'rel="canonical"' in head else f'<link rel="canonical" href="{canon}"><meta property="og:url" content="{canon}">'
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {BRAND}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} | {BRAND}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">{canon_tags}
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="preload" href="{R}assets/fonts/fraunces-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{R}assets/fonts/inter-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}css/styles.css">
{head}<!-- Analytics placeholder: add GA4 / Meta Pixel snippet here once IDs exist -->
</head><body data-root="{R}" class="{cls}{' has-sticky' if sticky else ''}"><a class="skip" href="#main">Skip to content</a>
<header class="site"><nav class="wrap nav" aria-label="Main"><a class="logo" href="{R}index.html"><i aria-hidden="true">P</i><span class="brand-name">{BRAND}</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nl">Menu</button><ul class="nav-links" id="nl">{navh}<li><a class="btn" style="padding:10px 18px;min-height:44px;color:#fff" href="{R}index.html#grades">Choose a Grade</a></li></ul></nav></header>
<main id="main">{body}</main>
<footer class="site"><div class="wrap"><div class="grid g4">
<div><h4 class="brand-name">{BRAND}</h4><p>Printable worksheets for Pre-K to 2nd grade, with a next step you can see.</p></div>
<div><h4>Shop</h4><ul><li><a href="{R}index.html#grades">Choose a Grade</a></li><li><a href="{R}kindergarten-math.html">Kindergarten Math</a></li><li><a href="{R}weekly.html">Weekly plan</a></li><li><a href="{R}index.html#price">Pricing</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{R}our-educational-approach.html">Our Educational Approach</a></li><li><a href="{R}resources/index.html">Parent Resources</a></li><li><a href="{R}faq.html">Questions</a></li><li><a href="{R}about.html">About</a></li></ul></div>
<div><h4>Help</h4><ul><li><a href="{R}contact.html">Contact</a></li><li><a href="{R}privacy.html">Privacy Policy</a></li><li><a href="{R}terms.html">Terms of Use</a></li><li><a href="{R}refund-policy.html">Refund Policy</a></li></ul></div></div>
<p class="fine">© 2026 <span class="brand-name">{BRAND}</span>. For parents, caregivers, and teachers. We do not knowingly collect information from children.</p></div></footer>
{st}<script src="{R}assets/config.js"></script><script src="{R}assets/products.js"></script><script src="{R}assets/app.js"></script>{js}</body></html>'''
    os.makedirs(os.path.dirname(fn) or ".",exist_ok=True);open(fn,"w").write(html)

PATH='<ol class="path-steps" aria-label="Kindergarten addition path"><li class="{a}">Count groups</li><li class="{b}">Combine</li><li class="{c}">Pictures to equations</li><li class="{d}">Simple stories</li></ol>'
def steps(a="",b="",c="",d=""):
    return PATH.format(a=a,b=b,c=c,d=d)

# ---------- HOME (scrollytelling; scene and motion live in assets/js) ----------
home=open("assets/src/home-body.html").read()
page("index.html","Give Your Child a Strong Start","Small steps, with kindergarten addition pages in the right order. A new packet every week.",home,cls="home",
 head='<link rel="stylesheet" href="assets/vendor/lenis.css"><link rel="stylesheet" href="css/home.css">',
 js='<script type="module" src="assets/js/home.js"></script>')

# ---------- PRODUCTS ----------
prods=[
 dict(slug="beginner",lv="Beginner",nm="Addition Within 5",k="b",bc="badge",checkout="k-add-beginner",
  summary="Count and combine groups up to 5, write the number sentence, and try a short addition story.",
  practice="Your child counts two small groups, puts them together, and writes the total. A page might show 2 dots and 1 more dot, then the number sentence 2 + 1 = 3. The pack also includes a short addition story you can read aloud. Totals stay at 5 or below.",
  start="This is a good starting point if your child can count to 10, recognize the numbers 0–5, and count objects one by one.",
  progress="The pages move from counting each group, to combining the groups, to a number sentence, and then to a short addition story. Totals stay at 5 or below.",
  guidance="Stay nearby. Let your child count out loud. A prompt you can use: “Point to the two groups. How many in all?” If they pause, count one group together, then let them count the rest.",
  repeat="Stay with this pack if you are helping with most of the problems. Move to the Intermediate pack when adding up to 5, including the short story, feels easy.",
  standards="These pages practice goals from Common Core K.OA.A.1 (showing addition with objects and drawings) and K.OA.A.5 (adding within 5). Totals in this pack stay at 5 or below.",
  marks=("on","on","on","on")),
 dict(slug="intermediate",lv="Intermediate",nm="Addition Within 10",k="i",bc="badge peach",checkout="k-add-intermediate",
  summary="Pictures turn into number sentences with totals up to 10.",
  practice="Your child moves from pictures to number sentences such as 4 + 3 = __. Some pages use a ten-frame, which is a box with 10 spaces, so numbers up to 10 are easier to see. Totals stay at 10 or below.",
  start="A fit when adding up to 5 with pictures feels easy, and your child recognizes numbers 0–10.",
  progress="Pages go from a picture of the groups, to the number sentence, to counting on from the bigger number. A number line on some pages shows that count.",
  guidance="Point to the bigger number and count the rest together one time. Then let your child try the next problem. If the ten-frame is new, fill it with counters before using the pencil.",
  repeat="Stay here if the number sentences still feel like a guess. Move to the Advanced pack when adding up to 10 feels comfortable.",
  standards="These pages practice goals from Common Core K.OA.A.1 and K.OA.A.2: addition within 10 using objects, drawings, and equations.",
  marks=("","","on","")),
 dict(slug="advanced",lv="Advanced",nm="Reasoning Within 10",k="a",bc="badge teal",checkout="k-add-advanced",
  summary="Break numbers into parts, find a missing number, make 10, and solve short stories.",
  practice="Your child breaks a number into two parts, such as 7 as 4 and 3. They find a missing number, like 4 + __ = 7, and find the number that makes 10. Short stories ask what happens when groups are joined. You can read the stories out loud. Your child does not have to read them alone.",
  start="A fit when your child adds up to 10 with confidence. Plan to read the little stories yourself.",
  progress="This is the last step in the kindergarten addition path we have now: parts of a number, then a missing part, then a simple story. Subtraction packs are not ready yet.",
  guidance="Use objects to act out the story. Ask what is happening before you ask for the total. If a missing number is sticky, go back to two groups your child can see.",
  repeat="Stay with this pack if missing numbers still need a lot of help. When the pages feel comfortable, your child has finished the kindergarten addition levels available now. Subtraction is coming soon.",
  standards="These pages practice goals from Common Core K.OA.A.2 (stories within 10), K.OA.A.3 (breaking numbers up to 10 into pairs), and K.OA.A.4 (finding the number that makes 10). You can read the stories aloud.",
  marks=("","","on","on")),
]

def qa(p):
    return f'''<h3>What will my child practice?</h3><p>{p["practice"]}</p>
<h3>Is this a suitable starting point?</h3><p>{p["start"]}</p>
<h3>How does practice progress?</h3><p>{p["progress"]}</p><p>The full kindergarten path is:</p>{steps(*p["marks"])}
<h3>What parent guidance is included?</h3><p>{p["guidance"]}</p>
<h3>When should we repeat a skill, and when should we move on?</h3><p>{p["repeat"]}</p>
<h3>What’s included?</h3>
<ul class="ticks"><li>Where to start</li><li>Pages in order</li><li>A parent prompt</li><li>An answer key</li><li>A progress tracker</li><li>Black-and-white PDF for US Letter paper</li></ul>
<p class="micro">Page count will be listed with the final file.</p>
<aside class="standards-note"><h3>Learning goals</h3><p>{p["standards"]} <a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Common Core kindergarten addition</a>.</p></aside>'''

for p in prods:
    others="".join(f'<a class="card link" href="k-addition-{o["slug"]}.html"><span class="{o["bc"]}">{o["lv"]}</span><h3>{o["nm"]}</h3><p>$3.99</p></a>' for o in prods if o["slug"]!=p["slug"])
    page(f"products/k-addition-{p['slug']}.html",f"Kindergarten Addition: {p['lv']}",f"{p['summary']} Printable kindergarten addition worksheets with parent guidance.",f'''
<div class="wrap crumbs"><a href="{{R}}index.html">Home</a> › <a href="{{R}}kindergarten-math.html">Kindergarten Math</a> › {p["lv"]}</div>
<section class="tight"><div class="wrap"><div class="buybox" style="max-width:640px"><span class="{p["bc"]}">Level · {p["lv"]}</span><h1 style="font-size:2rem;margin-top:10px">Kindergarten Addition: {p["lv"]}<br><small style="font-size:1.1rem;color:var(--muted)">{p["nm"]}</small></h1><p>{p["summary"]}</p>
<p class="price">$3.99 <small style="font-size:.9rem;font-weight:600;color:var(--muted)">Instant PDF · Page count comes with the final file</small></p>
<button type="button" class="btn buy" data-checkout="{p["checkout"]}" data-label="Buy now: $3.99">Buy now: $3.99</button>
<ul class="ticks"><li>Print at home in black and white</li><li>Answer key included</li><li>Parent prompt and progress tracker</li></ul>
<p><a href="{{R}}index.html#pages">A look inside</a></p></div></div></section>
<section class="tight white"><div class="wrap prose"><h2>Questions parents ask</h2>{qa(p)}</div></section>
<section class="tight"><div class="wrap"><h2>Other levels</h2><div class="grid g3">{others}<a class="card link" href="{{R}}weekly.html"><span class="badge">Weekly</span><h3>A fresh packet every week</h3><p>$3.99/mo</p></a></div></div></section>''')

RENEW="$3.99 a month, renews automatically each month until you cancel. Cancel anytime online in a couple of clicks."
SUB_BTN=f'''<button type="button" class="btn buy" data-subscribe="weekly" data-label="Start weekly · $3.99/mo">Start weekly · $3.99/mo</button>
<p class="renew-note">{RENEW}</p>
<p class="pay-note">Checkout isn’t open yet. No payment is taken.</p>'''

page("weekly.html",f"{BRAND} Weekly","A new math or reading packet every week for $3.99 a month. Preschool through 2nd grade. Cancel anytime.",f'''
<section class="tight"><div class="wrap" style="max-width:720px"><span class="eyebrow">Weekly plan</span>
<h1>A fresh packet every week, so you always know what to do next.</h1>
<p class="lead"><span class="brand-name">{BRAND}</span> Weekly is $3.99 a month. A new math or reading packet every week. Preschool through 2nd grade. Pick your child's grade. Cancel anytime.</p>
<p class="price">$3.99<span class="per">/mo</span></p>
{SUB_BTN}
<ul class="ticks"><li>One new printable packet each week</li><li>Math or reading, for the grade you pick</li><li>Print at home in black and white</li><li>Answer key, a short tip, and a progress tracker</li></ul>
<p>Kindergarten addition is ready to buy one level at a time. Other grades are on the way, and the weekly plan is where new packets will show up. <a href="index.html#grades">Pick your child's grade</a>.</p>
<p><a href="terms.html">Terms</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="index.html#grades">Pick your child's grade</a></p>
</div></section>''')

page("products/k-addition-bundle.html","Weekly plan","The old three-level page now points to the weekly plan.",'''
<section class="tight"><div class="wrap prose"><h1>This page moved</h1>
<p>A new packet every week is $3.99 a month. <a href="{R}weekly.html">See the weekly plan</a>.</p></div></section>
<script>location.replace("{R}weekly.html");</script>''',
head='<meta http-equiv="refresh" content="0;url={R}weekly.html"><link rel="canonical" href="https://proudlittlelearners.com/weekly.html"><meta property="og:url" content="https://proudlittlelearners.com/weekly.html">')

# ---------- CATEGORY ----------
cards="".join(f'''<div class="card"><p><span class="{p["bc"]}">{p["lv"]}</span></p><h3>{p["nm"]}</h3><p>{p["summary"]}</p><p><strong>A good time to start:</strong> {p["start"]}</p><p class="price">$3.99</p><a class="btn" href="products/k-addition-{p["slug"]}.html">View {p["lv"]} pack</a></div>''' for p in prods)
page("kindergarten-math.html","Kindergarten Math Worksheets","Kindergarten addition is available now, in three levels. Other kindergarten skills are coming soon.",f'''
<div class="wrap crumbs"><a href="index.html">Home</a> › Kindergarten Math</div>
<section class="tight"><div class="wrap"><span class="eyebrow">Available now · Kindergarten · Math</span><h1>Kindergarten addition</h1>
<p class="lead">Start with the level that matches what your child can already do. You will know how to help, and what to practice next.</p>
<p><a href="index.html#grades">Choose a different grade</a></p></div></section>
<section class="tight white"><div class="wrap"><h2>Your child’s next steps, already organized.</h2>
<ol class="step-path"><li>Combine small groups</li><li>Add within 10</li><li>Explore number relationships</li></ol>
<div class="grid g3" style="margin-top:28px">{cards}</div>
<div class="card" style="margin-top:28px;display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center"><div><span class="badge">Weekly plan</span><h3>A fresh packet every week</h3><p><span class="brand-name">{BRAND}</span> Weekly is $3.99 a month. A new math or reading packet every week, for the grade you pick.</p></div><div><span class="price">$3.99<span class="per">/mo</span></span> <a class="btn buy" href="weekly.html">See the weekly plan</a></div></div></div></section>
<section class="tight"><div class="wrap"><h2>Coming soon</h2>
<div class="grid g3"><div class="card"><span class="badge soon">Coming soon</span><h3>Subtraction</h3><p>Taking some away, after addition feels comfortable.</p></div>
<div class="card"><span class="badge soon">Coming soon</span><h3>Counting and numbers</h3><p>Counting objects and reading numbers.</p></div>
<div class="card"><span class="badge soon">Coming soon</span><h3>Reading</h3><p>Sounds and letters, simple words like cat, map, and sit, plus high-frequency words and words a child learns to recognize right away. <a href="our-educational-approach.html#reading">See how reading practice will work</a>.</p></div></div>
<p style="margin-top:20px"><a href="weekly.html">See the weekly plan</a></p></div></section>''')

# Old address. Sends visitors to the weekly plan.
page("free-printables.html","Weekly plan","The weekly plan is a new packet every week.",'''
<section class="tight"><div class="wrap prose"><h1>This page moved</h1>
<p><a href="{R}weekly.html">See the weekly plan</a>.</p></div></section>
<script>location.replace("{R}weekly.html");</script>''',
head='<meta http-equiv="refresh" content="0;url={R}weekly.html"><link rel="canonical" href="https://proudlittlelearners.com/weekly.html"><meta property="og:url" content="https://proudlittlelearners.com/weekly.html">')

# ---------- APPROACH ----------
def row(name,how,links):
    return f'<tr><th>{name}</th><td>{how}<p>{links}</p></td></tr>'
page("our-educational-approach.html","Our Educational Approach","How learning standards and research-informed teaching practices shape the worksheets.",f'''
<section class="tight"><div class="wrap prose"><span class="eyebrow">Our educational approach</span>
<h1>Designed around established learning standards and research-informed teaching practices.</h1>
<p class="lead">You can help your child. We use established learning standards to choose the skills, and research-informed teaching practices to organize the practice.</p>
<ul class="ticks"><li><strong>Common Core learning standards.</strong> The learning goals practiced.</li><li><strong>IES guidance.</strong> Building skills progressively, and connecting objects, pictures, and equations.</li><li><strong>Structured literacy.</strong> Explicitly connecting sounds, letters, reading, and spelling.</li><li><strong>NAEYC.</strong> Adapting practice to the child, and hands-on learning.</li></ul>
</div></section>
<section class="tight" id="ideas"><div class="wrap prose">
<h2>Learning ideas behind the design</h2>
<p>These research-informed ideas shape how the pages are organized.</p>
<ul class="ideas">
<li><b>Zone of proximal development</b><span>New work should sit just past what a child can do alone, where a little help makes it possible.</span> <a href="{LINKS["eric_zpd"]}" target="_blank" rel="noopener">Scaffolding and the zone of proximal development (ERIC)</a></li>
<li><b>Scaffolding</b><span>An adult helps with the hard part, then takes that help away as the child can do more. Wood, Bruner, and Ross described this in 1976.</span> <a href="{LINKS["eric_scaffold"]}" target="_blank" rel="noopener">Scaffolding and the zone of proximal development, revisited (ERIC)</a></li>
<li><b>A progression from objects to symbols</b><span>Teach number ideas in order. Begin with objects and informal marks, then connect them to number symbols.</span> <a href="{LINKS["wwc_math"]}" target="_blank" rel="noopener">IES practice guide: Teaching Math to Young Children</a></li>
<li><b>Progress monitoring</b><span>Watch what a child can do, then choose a next step that is not too easy and not too hard.</span> <a href="{LINKS["wwc_math"]}" target="_blank" rel="noopener">IES practice guide: Teaching Math to Young Children</a></li>
<li><b>Developmentally appropriate practice</b><span>Build on what this child can already do, in a way that fits that child.</span> <a href="{LINKS["dap"]}" target="_blank" rel="noopener">NAEYC: defining developmentally appropriate practice</a></li>
</ul>
</div></section>
<section class="tight white"><div class="wrap prose">
<h2>Where each idea shows up</h2>
<table class="sources"><thead><tr><th>Foundation</th><th>How it informs the materials</th></tr></thead><tbody>
{row("Common Core learning standards","These standards name the learning goals. Kindergarten addition includes putting groups together with objects, drawings, and number sentences, with totals up to 10, breaking numbers into parts, and finding what makes 10. The packs practice those goals. You can read the stories aloud.",
f'<a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Common Core, kindergarten addition</a>')}
{row("Institute of Education Sciences / What Works Clearinghouse","<em>Teaching Math to Young Children</em> recommends building number skills progressively and linking what children see to the symbols they write. <em>Foundational Skills to Support Reading</em> recommends connecting sounds in speech to letters, then reading and spelling the patterns that were taught. Pack levels follow that order. Reading packs are coming soon.",
f'<a href="{LINKS["wwc_math"]}" target="_blank" rel="noopener">Teaching Math to Young Children</a><br><a href="{LINKS["wwc_read"]}" target="_blank" rel="noopener">Foundational reading skills, grades K–3</a>')}
{row("NAEYC developmentally appropriate practice","NAEYC describes practice that fits the child and includes hands-on learning. Each pack says where to start. You can stay with a page or move on, based on what you see.",
f'<a href="{LINKS["dap"]}" target="_blank" rel="noopener">NAEYC: defining developmentally appropriate practice</a>')}
{row("Structured literacy","The International Dyslexia Association describes teaching that explicitly connects sounds, letters, reading, and spelling, from easier patterns to harder ones. Coming reading pages will follow that connection.",
f'<a href="{LINKS["ida"]}" target="_blank" rel="noopener">Structured Literacy overview from the International Dyslexia Association</a>')}
{row("Head Start Early Learning Outcomes Framework","This framework describes learning from birth to age 5, including early counting and language. It is a guide for what young children are ready to explore, not a test. Pre-K pages, when they are ready, will stay in that range.",
f'<a href="{LINKS["elof"]}" target="_blank" rel="noopener">Interactive Head Start Early Learning Outcomes Framework</a>')}
</tbody></table>
</div></section>
<section class="tight" id="reading"><div class="wrap prose">
<h2>How reading practice will work</h2>
<p>Reading packs are coming soon. Kindergarten reading goals are published with the <a href="{LINKS["cc_ela"]}" target="_blank" rel="noopener">Common Core kindergarten reading standards</a>.</p>
<h3>Sounds, letters, reading, and spelling</h3>
<p>A child learns that a letter stands for a sound. The letter m stands for the sound at the beginning of map. They blend sounds to read a word, and they spell the pattern they just learned.</p>
<h3>CVC words, in plain English</h3>
<p>CVC words are simple words like cat, map, and sit. You can hear three sounds: a consonant, a short vowel, and another consonant. A longer explanation is in our <a href="resources/cvc-words-explained-for-parents.html">parent guide to CVC words</a>.</p>
<h3>High-frequency words and sight words</h3>
<p>A high-frequency word is a word that occurs often in text, such as the, and, or said.</p>
<p>A sight word is a word a reader recognizes automatically, instantly. A high-frequency word can become a sight word once your child knows it right away. They are not the same thing.</p>
<p>Practice will connect the sounds and the spelling, including any part that does not follow the usual pattern. Recognizing the word instantly comes from that connection.</p>
</div></section>''')

# ---------- SIMPLE PAGES ----------
def prose(fn,title,desc,inner): page(fn,title,desc,f'<section class="tight"><div class="wrap prose"><h1>{title}</h1>{inner}</div></section>')
prose("about.html","About Us","Created for families across the United States, our printable learning packs make it easier to support early math and reading at home—with manageable steps and clear parent guidance.",f'''<p class="lead">We make printable worksheets for parents, caregivers, homeschool families, and teachers of children in Pre-K through 2nd grade.</p>
<p>Created for families across the United States, our printable learning packs make it easier to support early math and reading at home—with manageable steps and clear parent guidance.</p>
<p>You want to help. A pack tells you where to start, how to help, and what to practice next.</p>
<h2>What you can count on</h2><ul class="ticks"><li>Each pack says what your child will practice, and what they should already be able to do.</li><li>Packs that are ready are marked Available now. Others are marked Coming soon.</li><li>A parent prompt, an answer key, and a progress tracker come with each pack.</li></ul>
<h2>Where we are now</h2><p>Kindergarten addition levels are ready to buy one at a time. <span class="brand-name">{BRAND}</span> Weekly is $3.99 a month for a new packet every week. Other grades, subtraction, and reading are on the way. <a href="contact.html">Tell us what you need.</a></p>
''')
faqs=[
("What if a page is too hard?","Stop that page and step back, or show the same idea with objects or pictures. That temporary help is called scaffolding. Take it away when the work feels easier."),
("How much help should I give?","Show one example, try the next one together, then let your child try. That is scaffolding: help first, then fade the help. You do not need to give every answer."),
("When should we move forward?","Move on when this step feels comfortable with little help, not after one easy page. The IES early-math guide says a child should be comfortable with an earlier step before a harder one."),
("Why an organized pack instead of a loose page?","A loose page can jump to a skill your child is not ready for. A pack keeps one progression, with a prompt, an answer key, and a tracker."),
("How do I choose a grade?","Use Choose a Grade on the homepage. Pick the grade, then Math or Reading, then a skill. Kindergarten addition is available now. Every other path says Coming soon and points to the weekly plan."),
("What format are the worksheets?","PDF files for US Letter paper, designed for black-and-white home printing."),
("How do I get files after purchase?","You get a PDF to print at home after you pay."),
("How many pages are in each pack?","Page counts will be listed when each final PDF is ready."),
("Is there a weekly plan?","Yes. The weekly plan is $3.99 a month. You get a new math or reading packet every week for the grade you pick, from Preschool through 2nd grade. $3.99 a month, renews automatically each month until you cancel. Cancel anytime online in a couple of clicks. Checkout is not open yet, so no payment is taken. The Terms explain billing and what happens after you cancel."),
("What learning standards and teaching methods inform the worksheets?","Our worksheets are informed by established learning standards and research-informed teaching practices. Kindergarten addition packs practice selected Common Core math goals, using clear examples, visual models, and a gradual sequence. Our educational approach page explains the sources and how they inform the materials. Start with your child’s grade, then choose the skills they are ready to practice."),
("Can I share the files?","You may print them for your own children or your own classroom. Please don't redistribute or resell the files. See our Terms."),
("Do you offer refunds?","Yes, in certain situations. See our Refund Policy."),
("Do you collect information from children?","No. This site is for adults. We do not knowingly collect personal information from children.")]
prose("faq.html","Questions Parents Ask","Plain answers about difficulty, help at home, moving forward, downloads, and policies.",'<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)+'</div><p><a href="terms.html">Terms</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="contact.html">Contact</a> · <a href="index.html#grades">Choose a grade</a></p>')
prose("contact.html","Contact Us","Questions about a worksheet, a download, or a skill you want us to make.",f'''<p class="lead">Questions about a level, a download, or a skill you would like us to make? We would like to hear from you.</p><p>Email: <a class="site-email" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><small>For parents, caregivers, and teachers only.</small></p>''')
DRAFT='<p class="notice">Draft placeholder. Have this reviewed by a qualified professional before launch.</p>'
prose("privacy.html","Privacy Policy","Privacy policy.",DRAFT+'''<p>Last updated: TBD</p><h2>What we collect</h2><p>If you join our email list or contact us, we collect your email address and anything you choose to send. When checkout launches, payments will be processed by a third-party provider. We won't store your card details.</p>
<h2>Children</h2><p>Our site is meant for adults. We do not knowingly collect personal information from children under 13. If you think a child has given us information, contact us and we'll delete it.</p>
<h2>Analytics</h2><p>We may use basic analytics and advertising pixels to understand site traffic. Details will be listed here before they're enabled.</p><h2>Your choices</h2><p>You can unsubscribe from emails at any time and ask us to delete your data.</p>''')
prose("terms.html","Terms of Use","Terms of use and license.",DRAFT+'''<p>Last updated: TBD</p><h2>License</h2><p>When you buy or download a worksheet, you get a personal license to print it for your own children, homeschool, or single classroom.</p><h2>Not permitted</h2><p>Reselling, redistributing, uploading to shared sites, or claiming the content as your own.</p>
<h2>Educational information</h2><p>These are practice materials. We make no guarantee of specific academic results. These sources have not endorsed these products.</p>
<h2>Weekly plan</h2>
<p><span class="brand-name">{BRAND}</span> Weekly is $3.99 a month. The plan is a new printable math or reading packet each week, for a grade you pick, from Preschool through 2nd grade.</p>
<p><strong>Billing.</strong> $3.99 is charged once each month. Billing starts only when checkout is open. Until then, no payment is taken.</p>
<p><strong>Auto-renew.</strong> The plan renews automatically each month until you cancel. We will not start a new charge after you cancel.</p>
<p><strong>How to cancel.</strong> You can cancel anytime online in a couple of clicks. When billing is open, the email that comes with each charge will include a cancel link. There is no app, and there is no separate account page.</p>
<p><strong>After you cancel.</strong> The next month is not charged. Packets you already downloaded stay yours to print for your own children, homeschool, or single classroom, under the license above. New packets stop. Canceling does not by itself refund a month you already paid. See the Refund Policy.</p>''')
prose("refund-policy.html","Refund Policy","Refund policy for digital downloads and the weekly plan.",DRAFT+'''<p>Last updated: TBD</p><p>Because our products are digital downloads, sales are generally final. If a file is broken, won't download, or doesn't match its description, contact us within 14 days and we'll fix it or refund you.</p>
<h2>Weekly plan</h2>
<p><span class="brand-name">{BRAND}</span> Weekly is $3.99 a month and renews automatically until you cancel. You can cancel anytime online in a couple of clicks. Canceling stops the next monthly charge. It does not refund a month that was already paid, unless a packet from that month is broken, will not download, or does not match its description. Contact us within 14 days of that packet and we will fix it or refund that charge.</p>
<p>Packets you already downloaded stay yours to print under the license in the Terms. New packets stop after you cancel. There is no app.</p>''')
print("built")
