# Generates all HTML pages. Change BRAND here (and in assets/config.js), then: python3 build.py
import os
BRAND="StepWise Printables"
EMAIL="hello@example.com"
LINKS=dict(
 cc_math="https://www.thecorestandards.org/Math/Content/K/OA/",
 cc_ela="https://www.thecorestandards.org/ELA-Literacy/RF/K/",
 fl_math="https://www.fldoe.org/academics/standards/subject-areas/math-science/mathematics/",
 elof="https://headstart.gov/interactive-head-start-early-learning-outcomes-framework-ages-birth-five",
 dap="https://www.naeyc.org/resources/position-statements/dap/definition",
 wwc_math="https://ies.ed.gov/ncee/WWC/PracticeGuide/18",
 wwc_read="https://ies.ed.gov/ncee/wwc/PracticeGuide/21",
 ida="https://dyslexiaida.org/structured-literacy-effective-instruction-for-students-with-dyslexia-and-related-reading-difficulties/",
)
def sheet(kind="b",w=300,label="Sample layout illustration, not the final worksheet"):
    k={"b":"beginner","i":"intermediate","a":"advanced","n":"bundle"}[kind]
    src="sheet-%s%s.webp"%(k,"-sm" if w<=300 else "")
    return f'''<div class="sheet" style="max-width:{w}px"><img src="{{R}}assets/img/{src}" width="1100" height="1423" loading="lazy" decoding="async" alt="{label}: {k} level kindergarten addition"><div class="label">{label}</div></div>'''

def page(fn,title,desc,body,sticky=False,head='',js='',cls='',sticky_href=None,sticky_label=None):
    depth=fn.count("/");R="../"*depth
    nav=[("Kindergarten Math","kindergarten-math.html"),("Free Sample","free-printables.html"),("Our Approach","our-educational-approach.html"),("Questions","faq.html")]
    navh="".join(f'<li><a href="{R}{h}">{t}</a></li>' for t,h in nav)
    body=body.replace("{R}",R)
    if sticky:
        href=sticky_href or f"{R}free-printables.html"
        label=sticky_label or "Get the free sample"
        st=f'<div class="sticky-cta"><a class="btn" href="{href}">{label}</a></div>'
    else:
        st=""
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {BRAND}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} | {BRAND}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="preload" href="{R}assets/fonts/fraunces-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{R}assets/fonts/inter-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}css/styles.css">
{head}<!-- Analytics placeholder: add GA4 / Meta Pixel snippet here once IDs exist -->
</head><body data-root="{R}" class="{cls}{' has-sticky' if sticky else ''}"><a class="skip" href="#main">Skip to content</a>
<header class="site"><nav class="wrap nav" aria-label="Main"><a class="logo" href="{R}index.html"><i aria-hidden="true">S</i><span class="brand-name">{BRAND}</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nl">Menu</button><ul class="nav-links" id="nl">{navh}<li><a class="btn" style="padding:10px 18px;min-height:0;color:#fff" href="{R}index.html#grades">Choose a Grade</a></li></ul></nav></header>
<main id="main">{body}</main>
<footer class="site"><div class="wrap"><div class="grid g4">
<div><h4 class="brand-name">{BRAND}</h4><p>Printable worksheets for Pre-K to 2nd grade. One skill at a time, with a clear next step.</p></div>
<div><h4>Shop</h4><ul><li><a href="{R}index.html#grades">Choose a Grade</a></li><li><a href="{R}kindergarten-math.html">Kindergarten Math</a></li><li><a href="{R}products/k-addition-bundle.html">Addition Bundle</a></li><li><a href="{R}free-printables.html">Free Sample</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{R}our-educational-approach.html">Our Educational Approach</a></li><li><a href="{R}resources/index.html">Parent Resources</a></li><li><a href="{R}faq.html">Questions</a></li><li><a href="{R}about.html">About</a></li></ul></div>
<div><h4>Help</h4><ul><li><a href="{R}contact.html">Contact</a></li><li><a href="{R}privacy.html">Privacy Policy</a></li><li><a href="{R}terms.html">Terms of Use</a></li><li><a href="{R}refund-policy.html">Refund Policy</a></li></ul></div></div>
<p class="fine">© 2026 <span class="brand-name">{BRAND}</span>. Our worksheets are informed by publicly available learning standards and research-informed teaching guides. We are not affiliated with, endorsed by, or certified by any school, government agency, or standards organization. For use by parents, caregivers, and teachers. We do not knowingly collect information from children.</p></div></footer>
{st}<script src="{R}assets/config.js"></script><script src="{R}assets/products.js"></script><script src="{R}assets/app.js"></script>{js}</body></html>'''
    os.makedirs(os.path.dirname(fn) or ".",exist_ok=True);open(fn,"w").write(html)

PATH='<ol class="path-steps" aria-label="Kindergarten addition path"><li class="{a}">Count groups</li><li class="{b}">Combine</li><li class="{c}">Pictures to equations</li><li class="{d}">Simple stories</li></ol>'
def steps(a="",b="",c="",d=""):
    return PATH.format(a=a,b=b,c=c,d=d)

# ---------- HOME (scrollytelling; scene and motion live in assets/js) ----------
home=open("assets/src/home-body.html").read()
page("index.html","Help Your Child Feel Ready for What Comes Next","Give your child practice that builds on what they already know. Start with a grade, then choose a skill they are ready to practice.",home,sticky=True,cls="home",
 sticky_href="#grades",sticky_label="Choose your child's grade",
 head='<link rel="stylesheet" href="assets/vendor/lenis.css"><link rel="stylesheet" href="css/home.css"><link rel="modulepreload" href="assets/js/home.js">',
 js='<script src="assets/vendor/gsap.min.js" defer></script><script src="assets/vendor/ScrollTrigger.min.js" defer></script><script src="assets/vendor/lenis.min.js" defer></script><script type="module" src="assets/js/home.js"></script>')

# ---------- PRODUCTS ----------
prods=[
 dict(slug="beginner",lv="Beginner",nm="Addition Within 5",k="b",bc="badge",checkout="k-add-beginner",
  summary="Count two small groups and write how many in all. Every total stays at 5 or below.",
  practice="Your child counts two small groups, puts them together, and writes the total. A page might show 2 dots and 1 more dot, then the number sentence 2 + 1 = 3. Totals stay at 5 or below.",
  start="This is a good starting point if your child can count to 10, recognize the numbers 0–5, and count objects one by one.",
  progress="The pages move in small steps: count each group, combine the groups, then match the picture to a number sentence. This pack does not jump ahead to stories.",
  guidance="Stay nearby. Let your child count out loud. If they skip, ask “How many are in this group?” before they write the total. Buttons, coins, or cereal pieces can stand in for the dots.",
  repeat="Stay with this pack if you are helping with most of the problems. Move to the Intermediate pack when adding up to 5 with pictures feels easy and your child can say the number sentence.",
  included="A printable PDF for US Letter paper, made to print in black and white, plus an answer key. The page count will be added when the final file is ready. The picture on this page is a sample layout, not the finished worksheet.",
  standards="Informed by Common Core K.OA.A.1, which asks children to show addition with objects and drawings, and K.OA.A.5, which is adding within 5. Florida’s B.E.S.T. kindergarten benchmarks also introduce addition with objects, drawings, and equations. This pack keeps the totals at 5 or below.",
  marks=("on","on","on","")),
 dict(slug="intermediate",lv="Intermediate",nm="Addition Within 10",k="i",bc="badge peach",checkout="k-add-intermediate",
  summary="Pictures turn into number sentences with totals up to 10.",
  practice="Your child moves from pictures to number sentences such as 4 + 3 = __. Some pages use a ten-frame, which is a box with 10 spaces, so numbers up to 10 are easier to see. Totals stay at 10 or below.",
  start="A fit when adding up to 5 with pictures feels easy, and your child recognizes numbers 0–10.",
  progress="Pages go from a picture of the groups, to the number sentence, to counting on from the bigger number. A number line on some pages shows that count. Stories come in the next pack, not this one.",
  guidance="Point to the bigger number and count the rest together one time. Then let your child try the next problem. If the ten-frame is new, fill it with counters before using the pencil.",
  repeat="Stay here if the number sentences still feel like a guess. Move to the Advanced pack when adding up to 10 feels comfortable.",
  included="A printable PDF for US Letter paper, made to print in black and white, plus an answer key. The page count will be added when the final file is ready. The picture on this page is a sample layout, not the finished worksheet.",
  standards="Informed by Common Core K.OA.A.1 and K.OA.A.2, which include addition within 10 using objects, drawings, and equations. Florida’s B.E.S.T. benchmarks for kindergarten also explore addition of numbers from 0 to 10 with objects, drawings, number lines, and equations.",
  marks=("","","on","")),
 dict(slug="advanced",lv="Advanced",nm="Reasoning Within 10",k="a",bc="badge teal",checkout="k-add-advanced",
  summary="Break numbers into parts, find a missing number, make 10, and solve short stories.",
  practice="Your child breaks a number into two parts, such as 7 as 4 and 3. They find a missing number, like 4 + __ = 7, and find the number that makes 10. Short stories ask what happens when groups are joined. You can read the stories out loud. Your child does not have to read them alone.",
  start="A fit when your child adds up to 10 with confidence. Plan to read the little stories yourself.",
  progress="This is the last step in the kindergarten addition path we have now: parts of a number, then a missing part, then a simple story. Subtraction packs are not ready yet.",
  guidance="Use objects to act out the story. Ask what is happening before you ask for the total. If a missing number is sticky, go back to two groups your child can see.",
  repeat="Stay with this pack if missing numbers still need a lot of help. When the pages feel comfortable, your child has finished the kindergarten addition path we offer today. The next new math skill will be listed as Coming Soon until it is real.",
  included="A printable PDF for US Letter paper, made to print in black and white, plus an answer key. The page count will be added when the final file is ready. The picture on this page is a sample layout, not the finished worksheet.",
  standards="Informed by Common Core K.OA.A.2 (word problems within 10), K.OA.A.3 (breaking numbers up to 10 into pairs), and K.OA.A.4 (finding the number that makes 10). Florida’s B.E.S.T. kindergarten benchmarks include making 10, finding pairs that make a sum, and solving real-world problems with objects, drawings, or equations. Children are not expected to read those problems by themselves.",
  marks=("","","on","on")),
]

def qa(p):
    return f'''<h3>What will my child practice?</h3><p>{p["practice"]}</p>
<h3>Is this a suitable starting point?</h3><p>{p["start"]}</p>
<h3>How does practice progress?</h3><p>{p["progress"]}</p><p>The full kindergarten path is:</p>{steps(*p["marks"])}
<h3>What parent guidance is included?</h3><p>{p["guidance"]}</p>
<h3>When should we repeat a skill, and when should we move on?</h3><p>{p["repeat"]}</p>
<h3>What’s included?</h3><p>{p["included"]}</p><p>{p["standards"]} We are not endorsed by the groups that publish those standards. Read them here: <a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Common Core kindergarten addition</a> and <a href="{LINKS["fl_math"]}" target="_blank" rel="noopener">Florida B.E.S.T. mathematics</a>.</p>'''

for p in prods:
    others="".join(f'<a class="card link" href="k-addition-{o["slug"]}.html"><span class="{o["bc"]}">{o["lv"]}</span><h3>{o["nm"]}</h3><p>$3.99</p></a>' for o in prods if o["slug"]!=p["slug"])
    page(f"products/k-addition-{p['slug']}.html",f"Kindergarten Addition: {p['lv']}",f"{p['summary']} Printable kindergarten addition worksheets with parent guidance.",f'''
<div class="wrap crumbs"><a href="{{R}}index.html">Home</a> › <a href="{{R}}kindergarten-math.html">Kindergarten Math</a> › {p["lv"]}</div>
<section class="tight"><div class="wrap prod-grid"><div>{sheet(p["k"],460)}<p class="notice" style="margin-top:16px">The image above is a sample layout. It is not the final worksheet. Real page previews will be added when the PDF is finished.</p></div>
<div class="buybox"><span class="{p["bc"]}">Level · {p["lv"]}</span><h1 style="font-size:2rem;margin-top:10px">Kindergarten Addition: {p["lv"]}<br><small style="font-size:1.1rem;color:var(--muted)">{p["nm"]}</small></h1><p>{p["summary"]}</p>
<p class="price">$3.99 <small style="font-size:.9rem;font-weight:600;color:var(--muted)">Instant PDF · Page count comes with the final file</small></p>
<a class="btn" data-checkout="{p["checkout"]}" data-label="Buy now: $3.99" href="#">Buy now: $3.99</a><p class="checkout-note notice" hidden>Checkout isn't live yet. No payment has been taken. <a href="{{R}}free-printables.html">Get the free sample</a> in the meantime.</p>
<ul class="ticks"><li>Print at home in black and white</li><li>Answer key included</li><li>One skill, one level</li></ul></div></div></section>
<section class="tight white"><div class="wrap prose"><h2>Questions parents ask</h2>{qa(p)}</div></section>
<section class="tight"><div class="wrap"><h2>Other levels</h2><div class="grid g3">{others}<a class="card link" href="k-addition-bundle.html"><span class="badge">Bundle</span><h3>All three levels</h3><p>$9.99</p></a></div></div></section>''')

page("products/k-addition-bundle.html","Kindergarten Addition Complete Bundle","All three kindergarten addition levels in order, for $9.99 instead of $11.97.",f'''
<div class="wrap crumbs"><a href="{{R}}index.html">Home</a> › <a href="{{R}}kindergarten-math.html">Kindergarten Math</a> › Bundle</div>
<section class="tight"><div class="wrap prod-grid"><div>{sheet("n",460)}<div class="grid g3" style="margin-top:16px">{sheet("b",200,"Sample layout")}{sheet("i",200,"Sample layout")}{sheet("a",200,"Sample layout")}</div></div>
<div class="buybox"><span class="badge">Complete bundle</span><h1 style="font-size:2rem;margin-top:10px">Kindergarten Addition Complete Bundle</h1>
<p>The next stages are already organized. You get every kindergarten addition pack we currently sell, and you pay less than buying them one by one.</p>
<p class="price">$9.99 <small style="font-size:.9rem;font-weight:600;color:var(--muted)">The three packs are $3.99 each, or $11.97. Page count comes with the final files.</small></p>
<a class="btn" data-checkout="k-add-bundle" data-label="Buy the bundle: $9.99" href="#">Buy the bundle: $9.99</a><p class="checkout-note notice" hidden>Checkout isn't live yet. No payment has been taken.</p>
<p class="notice" style="margin-top:16px">Pictures are sample layouts, not the final pages. Checkout is not open, so nothing is charged.</p></div></div></section>
<section class="tight white"><div class="wrap prose"><h2>Questions parents ask</h2>
<h3>What will my child practice?</h3><p>The full kindergarten addition path: count and combine groups up to 5, move to number sentences up to 10, then break numbers into parts, make 10, and solve short stories you can read aloud.</p>
<h3>Is this a suitable starting point?</h3><p>Choose the bundle if you want the next stage ready when this one feels easy, or if you are not sure yet which level fits. A child who already adds up to 5 with ease can start in the middle of the set. You can also begin with the free sample.</p>
<h3>How does practice progress?</h3><p>The packs stay in order. Nothing jumps from 1 + 2 to a much harder skill.</p>{steps("on","on","on","on")}
<h3>What parent guidance is included?</h3><p>Each level includes a short note on how to help. You do not need to finish a pack in one sitting. Use the note for the level you are on today.</p>
<h3>When should we repeat a skill, and when should we move on?</h3><p>Stay with a level while you are still helping with most problems. Move to the next level in the bundle when the current one feels comfortable and your child can tell you what they did.</p>
<h3>What’s included?</h3><p>All three packs: Beginner ($3.99), Intermediate ($3.99), and Advanced ($3.99). The bundle price is $9.99. Each pack is a black-and-white PDF for US Letter paper, with an answer key. Page counts will be added when the final files are ready.</p>
<p>The set is informed by Common Core kindergarten addition standards and Florida’s B.E.S.T. kindergarten math benchmarks. We are not endorsed by either organization. <a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Read the Common Core kindergarten addition standards</a> and <a href="{LINKS["fl_math"]}" target="_blank" rel="noopener">Florida’s B.E.S.T. mathematics page</a>.</p>
</div></section>
<section class="tight"><div class="wrap"><h2>Inside the bundle</h2><div class="grid g3">{"".join(f'<a class="card link" href="k-addition-{p["slug"]}.html"><span class="{p["bc"]}">{p["lv"]}</span><h3>{p["nm"]}</h3><p>{p["summary"]}</p></a>' for p in prods)}</div></div></section>''')

# ---------- CATEGORY ----------
cards="".join(f'''<div class="card">{sheet(p["k"],240,"Sample layout illustration")}<p style="margin-top:14px"><span class="{p["bc"]}">{p["lv"]}</span></p><h3>{p["nm"]}</h3><p>{p["summary"]}</p><p><strong>A good time to start:</strong> {p["start"]}</p><p class="price">$3.99</p><a class="btn" href="products/k-addition-{p["slug"]}.html">View {p["lv"]} pack</a></div>''' for p in prods)
page("kindergarten-math.html","Kindergarten Math Worksheets","Kindergarten addition worksheets in three levels: within 5, within 10, and reasoning within 10. Other kindergarten skills are not for sale yet.",f'''
<div class="wrap crumbs"><a href="index.html">Home</a> › Kindergarten Math</div>
<section class="tight"><div class="wrap"><span class="eyebrow">Kindergarten · Math</span><h1>Kindergarten addition, one step at a time</h1>
<p class="lead">These are the kindergarten math packs we actually have. Start with the level that matches what your child can already do. Other skills are marked Coming Soon. They are not products yet.</p>
<p><a href="index.html#grades">Choose a different grade</a></p></div></section>
<section class="tight white"><div class="wrap"><h2>The path</h2><p>Count groups, combine them, turn pictures into equations, then try simple stories.</p>{steps("on","on","on","on")}
<div class="grid g3" style="margin-top:28px">{cards}</div>
<div class="card" style="margin-top:28px;display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center"><div><span class="badge">Bundle</span><h3>All three levels, in order</h3><p>$9.99 instead of $11.97. The next stage is included, so you are not hunting for it later.</p></div><div><span class="price">$9.99</span> <a class="btn" href="products/k-addition-bundle.html">View bundle</a></div></div></div></section>
<section class="tight"><div class="wrap"><h2>More kindergarten skills</h2><p>These are not for sale. When you choose them from the grade list, you will see Coming Soon and a free sample.</p>
<div class="grid g3"><div class="card"><span class="badge soon">Coming soon</span><h3>Subtraction</h3><p>Taking some away, after addition feels comfortable.</p></div>
<div class="card"><span class="badge soon">Coming soon</span><h3>Counting and numbers</h3><p>Counting objects and reading numbers.</p></div>
<div class="card"><span class="badge soon">Coming soon</span><h3>Reading</h3><p>Sounds and letters, simple words like cat, map, and sit, and sight words connected to their spellings. <a href="our-educational-approach.html#reading">See how reading practice will work</a>.</p></div></div>
<p style="margin-top:20px"><a href="free-printables.html">Get the free addition sample</a> while those skills are still being made.</p></div></section>''')

# ---------- FREE ----------
page("free-printables.html","Free Kindergarten Addition Sample","A free printable kindergarten addition page for totals within 5. Instant PDF. No account needed.",f'''
<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">Free download · Kindergarten addition</span><h1>Try one page before you choose a pack</h1>
<p class="lead">Count the dots, add two small groups, and write the total. Every problem stays within 5. There is no surprise jump.</p>
<ul class="ticks"><li>A real practice page, plus an answer key</li><li>Prints in black and white</li><li>Short enough for one sitting</li></ul>
<div class="btn-row"><a class="btn" href="downloads/free-k-addition-within-5-sample.pdf" download>Download the free PDF</a></div>
<p style="font-size:.9rem;color:var(--muted)">The file downloads now. No email required.</p></div>
<div class="stack">{sheet("b",340,"Sample layout illustration (see the PDF for the real pages)")}</div></div></section>
<section class="tight white"><div class="wrap grid g2"><div><h2>Is this a suitable starting point?</h2>
<p><strong>A good fit if your child can</strong> count to 10, recognize numbers 0–5, and count objects one by one.</p>
<p><strong>If the page is too hard,</strong> use counters and count together. If it feels easy, look at the <a href="products/k-addition-intermediate.html">Intermediate pack (within 10)</a>.</p>
<p><small>Informed by Common Core K.OA.A.1 and K.OA.A.5. Not endorsed by any organization.</small></p></div>
<div class="card"><h3>Want a note when new pages are ready?</h3><p>The email list is for parents and teachers (18+). It is not connected yet, so joining does not save your address or charge you.</p>
<form data-placeholder><label for="em">Email</label><input id="em" type="email" required placeholder="you@example.com"><button class="btn" style="margin-top:10px;width:100%">Join the list</button><p class="form-msg notice" hidden>Thanks. The list is not connected yet, so nothing was saved and nothing was charged. Your download above works right now.</p></form></div></div></section>
<section><div class="wrap"><div class="cta-band"><h2>Want the full starting level?</h2><p>The Beginner pack continues addition within 5. The next two levels move toward stories, still within 10.</p><a class="btn" href="kindergarten-math.html">See the three levels</a></div></div></section>''')

# ---------- APPROACH ----------
def row(name,how,links):
    return f'<tr><th>{name}</th><td>{how}<p>{links}</p></td></tr>'
page("our-educational-approach.html","Our Educational Approach","How learning standards and research-informed teaching guides shape the worksheets, in plain language.",f'''
<section class="tight"><div class="wrap prose"><span class="eyebrow">Our educational approach</span>
<h1>Where the practice ideas come from</h1>
<p class="lead">We look at learning standards and research-informed teaching guides. Then we turn them into short pages you can print. The guides shape the order of practice. They do not score your child.</p>
<p class="notice"><strong>A clear line:</strong> We are not affiliated with, endorsed by, or certified by any school, district, state, or the organizations below. These worksheets are not scientifically proven. No school partnership is claimed. “Informed by” means we read the public sources and used them to choose skills and sequence.</p>
<h2>What that means at the kitchen table</h2>
<ul class="ticks"><li>Start from a skill your child can already do.</li><li>Teach the next idea with objects, then a picture, then symbols.</li><li>Keep each pack on one skill so the next page is not a surprise.</li></ul>
</div></section>
<section class="tight white"><div class="wrap prose">
<h2>Foundations we use</h2>
<p>The left column names the source. The right column says how it shapes the materials.</p>
<table class="sources"><thead><tr><th>Foundation</th><th>How it informs the materials</th></tr></thead><tbody>
{row("Common Core and Florida B.E.S.T.","These are learning standards. They describe what kindergarten math includes. Both treat addition as putting groups together, with objects, drawings, and number sentences, and with totals up to 10. Common Core also asks children to break numbers into parts, find what makes 10, and add within 5 with ease. Florida’s B.E.S.T. benchmarks ask for those same kinds of steps, including short real-world problems an adult can read aloud. Our kindergarten addition packs stay inside those ideas. We name the standards we read. We do not claim a state or a school approved the pages.",
f'<a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Common Core, kindergarten addition</a><br><a href="{LINKS["fl_math"]}" target="_blank" rel="noopener">Florida B.E.S.T. Standards for Mathematics</a>')}
{row("Institute of Education Sciences / What Works Clearinghouse","The U.S. Department of Education reviews research and publishes practice guides. <em>Teaching Math to Young Children</em> recommends teaching number ideas in a planned order and building on what a child already knows. <em>Foundational Skills to Support Reading for Understanding in Kindergarten Through 3rd Grade</em> recommends linking sounds in speech to letters, teaching children to blend those sounds, and practicing the spelling patterns they have been taught, including common words. We use that order for levels. Reading packs are not for sale yet. When they are, they will follow this sound-to-letter path.",
f'<a href="{LINKS["wwc_math"]}" target="_blank" rel="noopener">Teaching Math to Young Children</a><br><a href="{LINKS["wwc_read"]}" target="_blank" rel="noopener">Foundational reading skills, grades K–3</a>')}
{row("NAEYC developmentally appropriate practice","The National Association for the Education of Young Children describes teaching that fits the child in front of you. It builds on what that child can already do, keeps learning engaging, and fits the child’s age, strengths, and background. It is not a race through a checklist. We keep pages short, say what to try first, and tell you when to stay with a skill.",
f'<a href="{LINKS["dap"]}" target="_blank" rel="noopener">NAEYC: defining developmentally appropriate practice</a>')}
{row("Structured literacy","The International Dyslexia Association describes structured literacy as teaching sounds, letters, and spelling patterns directly, in order, from easier patterns to harder ones. Children are not left to guess the pattern from a mixed pile of words. Future reading pages will teach one pattern, then offer practice with that pattern. This is an approach we are using. It is not a claim that these pages treat dyslexia, and no clinic has reviewed them.",
f'<a href="{LINKS["ida"]}" target="_blank" rel="noopener">Structured Literacy overview from the International Dyslexia Association</a>')}
{row("Head Start Early Learning Outcomes Framework","This federal framework describes how children grow from birth to age 5, including early math and language. Head Start says the framework is not a test, and it should not be used to decide that a child has failed or is not ready for kindergarten. Pre-K pages, when they are ready, will stay in that early range: counting, sounds, and letters, in small steps. We will not use the framework as a scorecard.",
f'<a href="{LINKS["elof"]}" target="_blank" rel="noopener">Interactive Head Start Early Learning Outcomes Framework</a>')}
</tbody></table>
</div></section>
<section class="tight" id="reading"><div class="wrap prose">
<h2>How reading practice will work</h2>
<p>Reading packs are not for sale yet. Here is the plan, in everyday words. Kindergarten reading standards for foundational skills are published with the <a href="{LINKS["cc_ela"]}" target="_blank" rel="noopener">Common Core kindergarten reading standards</a>.</p>
<h3>Sounds and letters go together</h3>
<p>A child learns that a letter stands for a sound. The letter m stands for the sound at the beginning of map. Seeing the letter and saying the sound are practiced together, not as two unrelated lists.</p>
<h3>Blend and spell</h3>
<p>Blending means pushing sounds together to read a word. Spelling means pulling a word apart and writing the letters. Children practice the pattern they were just taught. They are not handed a mix of patterns on the same page.</p>
<h3>CVC words, in plain English</h3>
<p>CVC words are simple words like cat, map, and sit. You can hear three sounds: a consonant, a short vowel, and another consonant. In cat, you can hear the sounds at the start, in the middle, and at the end. There is no silent letter in these starter words. A longer explanation is in our <a href="resources/cvc-words-explained-for-parents.html">parent guide to CVC words</a>.</p>
<h3>Sight words</h3>
<p>A sight word is a word children see often, such as the, said, or was. Some of these words follow a pattern the child has learned. Others have a part that does not. Practice will still connect the sounds and the spelling, and it will point out the irregular part. A sight word is not only a card to memorize with no link to the letters.</p>
<p class="notice">Nothing on this page is an endorsement. The sources are linked so you can read them yourself.</p>
</div></section>''')

# ---------- SIMPLE PAGES ----------
def prose(fn,title,desc,inner): page(fn,title,desc,f'<section class="tight"><div class="wrap prose"><h1>{title}</h1>{inner}</div></section>')
prose("about.html","About Us","StepWise Printables makes printable worksheets for Pre-K through 2nd grade, one skill at a time.",f'''<p class="lead">We make printable worksheets for parents, caregivers, homeschool families, and teachers of children in Pre-K through 2nd grade.</p>
<p>Many free worksheets mix easy and hard problems on the same page. A child who is practicing 1 + 2 may turn the page and find something much harder. We would rather give you a clear starting point and a manageable next step.</p>
<h2>What we promise</h2><ul class="ticks"><li>Each pack says what your child will practice, and what they should already be able to do.</li><li>Prices and “coming soon” labels stay honest. We do not list products we cannot sell.</li><li>Our pages are informed by public standards and research-informed guides. Those groups have not endorsed us.</li></ul>
<h2>Where we are now</h2><p>Kindergarten addition is available. Other grades, subtraction, and reading will be added when the pages are actually ready. <a href="contact.html">Tell us what you need.</a></p>''')
faqs=[
("What if a page is too hard?","Stop that page. Go back to an easier one, or show the same idea with counters. A hard page means the earlier step still needs practice."),
("How much help should I give?","Stay nearby. Let your child try. If they are stuck, show one example with objects, then hand the pencil back. You do not need to give every answer."),
("When should we move forward?","Move forward when the current pages feel comfortable and your child can tell you what they did. If you are helping with almost every problem, stay a little longer."),
("Why an organized pack instead of free worksheets?","Free pages are often mixed together, so the next page may jump in difficulty. A pack stays on one skill and shows the next step. You can still start with the free addition sample."),
("How do I choose a grade?","Use Choose a Grade on the homepage. Pick the grade, then Math or Reading, then a skill. Only Kindergarten Addition has packs today. Every other path says Coming Soon and links to the free sample."),
("What format are the worksheets?","PDF files for US Letter paper, designed for black-and-white home printing."),
("How do I get files after purchase?","Checkout is not live yet. No payment is taken. When checkout opens, a download link will follow payment."),
("How many pages are in each pack?","The page count will be listed when each final PDF is ready. We are not guessing a number."),
("Are the worksheets aligned to Common Core or Florida B.E.S.T.?","Kindergarten addition pages are informed by those standards, and we link the original text. We do not claim official alignment, certification, or endorsement."),
("Can I share the files?","You may print them for your own children or your own classroom. Please don't redistribute or resell the files. See our Terms."),
("Do you offer refunds?","Yes, in certain situations. See our Refund Policy."),
("Do you collect information from children?","No. This site is for adults. We do not knowingly collect personal information from children.")]
prose("faq.html","Questions Parents Ask","Plain answers about difficulty, help at home, moving forward, downloads, and policies.",'<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)+'</div><p><a href="terms.html">Terms</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="contact.html">Contact</a> · <a href="index.html#grades">Choose a grade</a></p>')
prose("contact.html","Contact Us","Questions about a worksheet, a download, or a skill you want us to make.",f'''<p class="lead">Questions about a level, a download, or a skill you would like us to make? We would like to hear from you.</p><p>Email: <a class="site-email" href="mailto:{EMAIL}">{EMAIL}</a></p>
<form data-placeholder class="card"><label for="n">Your name</label><input id="n" required><label for="e" style="margin-top:10px;display:block">Email</label><input id="e" type="email" required><label for="m" style="margin-top:10px;display:block">Message</label><textarea id="m" rows="5" required></textarea><button class="btn" style="margin-top:12px">Send message</button><p class="form-msg notice" hidden>This form is not connected yet, so your message was not sent and nothing was charged. Please email us directly.</p></form>
<p><small>For parents, caregivers, and teachers only. Please don't have children submit this form.</small></p>''')
DRAFT='<p class="notice">Draft placeholder. Have this reviewed by a qualified professional before launch.</p>'
prose("privacy.html","Privacy Policy","Privacy policy.",DRAFT+'''<p>Last updated: TBD</p><h2>What we collect</h2><p>If you join our email list or contact us, we collect your email address and anything you choose to send. When checkout launches, payments will be processed by a third-party provider. We won't store your card details.</p>
<h2>Children</h2><p>Our site is meant for adults. We do not knowingly collect personal information from children under 13. If you think a child has given us information, contact us and we'll delete it.</p>
<h2>Analytics</h2><p>We may use basic analytics and advertising pixels to understand site traffic. Details will be listed here before they're enabled.</p><h2>Your choices</h2><p>You can unsubscribe from emails at any time and ask us to delete your data.</p>''')
prose("terms.html","Terms of Use","Terms of use and license.",DRAFT+'''<p>Last updated: TBD</p><h2>License</h2><p>When you buy or download a worksheet, you get a personal license to print it for your own children, homeschool, or single classroom.</p><h2>Not permitted</h2><p>Reselling, redistributing, uploading to shared sites, or claiming the content as your own.</p>
<h2>Educational information</h2><p>Our worksheets are practice materials informed by public learning standards and research-informed guides. They are not endorsed by any school or government organization, and we make no guarantee of specific academic results.</p>''')
prose("refund-policy.html","Refund Policy","Refund policy for digital downloads.",DRAFT+'''<p>Last updated: TBD</p><p>Because our products are digital downloads, sales are generally final. If a file is broken, won't download, or doesn't match its description, contact us within 14 days and we'll fix it or refund you.</p>''')
print("built")
