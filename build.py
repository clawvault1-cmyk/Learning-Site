# Generates all HTML pages. Change BRAND here (and in assets/config.js), then: python3 build.py
import os
BRAND="StepWise Printables"
EMAIL="hello@example.com"
LINKS=dict(
 cc_math="https://www.thecorestandards.org/Math/Content/K/OA/",
 cc_ela="https://www.thecorestandards.org/ELA-Literacy/RF/K/",
 cc="https://www.thecorestandards.org/",
 elof="https://headstart.gov/school-readiness/article/head-start-early-learning-outcomes-framework",
 dap="https://www.naeyc.org/resources/position-statements/dap/definition",
 wwc="https://ies.ed.gov/ncee/wwc/",
 wwc_math="https://ies.ed.gov/ncee/wwc/PracticeGuide/18",
 wwc_read="https://ies.ed.gov/ncee/wwc/PracticeGuide/21",
 ida="https://dyslexiaida.org/structured-literacy/",
)
def sheet(kind="b",w=300,label="Sample layout illustration, not the final worksheet"):
    k={"b":"beginner","i":"intermediate","a":"advanced","n":"bundle"}[kind]
    src="sheet-%s%s.webp"%(k,"-sm" if w<=300 else "")
    return f'''<div class="sheet" style="max-width:{w}px"><img src="{{R}}assets/img/{src}" width="1100" height="1423" loading="lazy" decoding="async" alt="{label}: {k} level kindergarten addition"><div class="label">{label}</div></div>'''

def page(fn,title,desc,body,sticky=False,head='',js='',cls=''):
    depth=fn.count("/");R="../"*depth
    nav=[("Shop K Math","kindergarten-math.html"),("Free Printables","free-printables.html"),("Our Approach","our-educational-approach.html"),("Parent Resources","resources/index.html"),("FAQ","faq.html"),("About","about.html")]
    navh="".join(f'<li><a href="{R}{h}">{t}</a></li>' for t,h in nav)
    body=body.replace("{R}",R)
    st=f'<div class="sticky-cta"><a class="btn" href="{R}free-printables.html">Get the free addition sample</a></div>' if sticky else ""
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {BRAND}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} | {BRAND}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="preload" href="{R}assets/fonts/fraunces-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{R}assets/fonts/inter-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}css/styles.css">
{head}<!-- Analytics placeholder: add GA4 / Meta Pixel snippet here once IDs exist -->
</head><body data-root="{R}" class="{cls}{' has-sticky' if sticky else ''}"><a class="skip" href="#main">Skip to content</a>
<header class="site"><nav class="wrap nav" aria-label="Main"><a class="logo" href="{R}index.html"><i aria-hidden="true">S</i><span class="brand-name">{BRAND}</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nl">Menu</button><ul class="nav-links" id="nl">{navh}<li><a class="btn" style="padding:10px 18px;min-height:0;color:#fff" href="{R}free-printables.html">Free Sample</a></li></ul></nav></header>
<main id="main">{body}</main>
<footer class="site"><div class="wrap"><div class="grid g4">
<div><h4 class="brand-name">{BRAND}</h4><p>Printable worksheets for Pre-K to 2nd grade, organized one skill at a time.</p></div>
<div><h4>Shop</h4><ul><li><a href="{R}kindergarten-math.html">Kindergarten Math</a></li><li><a href="{R}products/k-addition-bundle.html">Addition Bundle</a></li><li><a href="{R}free-printables.html">Free Printables</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{R}our-educational-approach.html">Our Educational Approach</a></li><li><a href="{R}resources/index.html">Parent Resources</a></li><li><a href="{R}faq.html">FAQ</a></li><li><a href="{R}about.html">About</a></li></ul></div>
<div><h4>Help</h4><ul><li><a href="{R}contact.html">Contact</a></li><li><a href="{R}privacy.html">Privacy Policy</a></li><li><a href="{R}terms.html">Terms of Use</a></li><li><a href="{R}refund-policy.html">Refund Policy</a></li></ul></div></div>
<p class="fine">© 2026 <span class="brand-name">{BRAND}</span>. Our worksheets are informed by publicly available educational frameworks. We are not affiliated with, endorsed by, or certified by any school, government agency, or standards organization. For use by parents, caregivers, and teachers. We do not knowingly collect information from children.</p></div></footer>
{st}<script src="{R}assets/config.js"></script><script src="{R}assets/products.js"></script><script src="{R}assets/app.js"></script>{js}</body></html>'''
    os.makedirs(os.path.dirname(fn) or ".",exist_ok=True);open(fn,"w").write(html)

FINDER='''<div class="finder" id="finder"><span class="eyebrow" style="color:var(--yellow)">Worksheet finder</span><h2>Find the right level in three taps</h2>
<div class="f-row"><div><label for="f-grade">Grade</label><select id="f-grade"><option>Pre-K</option><option selected>Kindergarten</option><option>1st Grade</option><option>2nd Grade</option></select></div>
<div><label for="f-subject">Subject</label><select id="f-subject"><option selected>Math</option><option>Reading</option></select></div>
<div><label for="f-skill">Skill</label><select id="f-skill"></select></div></div><div id="f-result" aria-live="polite"></div></div>'''

LEVELS='''<div class="level-ladder">
<div><span class="badge">Level 1 · Beginner</span><h3>Addition within 5</h3><p>Uses pictures and objects. Your child counts two small groups and finds the total. Best for children who can count to 10 and recognize numbers 0–5.</p></div>
<div><span class="badge peach">Level 2 · Intermediate</span><h3>Addition within 10</h3><p>Moves from pictures to number sentences like 4 + 3 = __. Best for children who are comfortable adding within 5.</p></div>
<div><span class="badge teal">Level 3 · Advanced</span><h3>Reasoning within 10</h3><p>Simple word problems, breaking numbers apart, and finding the number that makes 10. Best for children who add within 10 confidently.</p></div></div>'''

# ---------- HOME (scrollytelling v2) ----------
home=open("assets/src/home-body.html").read().replace("{FINDER}",FINDER)
page("index.html","Printable Worksheets for Pre-K to 2nd Grade","Printable math and reading worksheets for Pre-K to 2nd grade, organized by skill and level. The right worksheet, the right skill, the right level.",home,sticky=True,cls="home",
 head='<link rel="stylesheet" href="assets/vendor/lenis.css"><link rel="stylesheet" href="css/home.css"><link rel="modulepreload" href="assets/js/home.js">',
 js='<script src="assets/vendor/gsap.min.js" defer></script><script src="assets/vendor/ScrollTrigger.min.js" defer></script><script src="assets/vendor/lenis.min.js" defer></script><script type="module" src="assets/js/home.js"></script>')
# ---------- CATEGORY ----------
prods=[("beginner","Beginner","Addition Within 5","b","Adding small groups of pictures and objects with totals up to 5.","Count to 10; recognize numbers 0–5; count objects one-to-one.","Totals from 0 to 5, shown with pictures and objects.","K.OA.A.1, K.OA.A.2 (within 5)","badge"),
       ("intermediate","Intermediate","Addition Within 10","i","Moving from pictures to number sentences with totals up to 10.","Add within 5 using pictures; recognize numbers 0–10.","Totals from 0 to 10; number sentences such as 4 + 3 = __.","K.OA.A.1, K.OA.A.2, K.OA.A.5","badge peach"),
       ("advanced","Advanced","Reasoning Within 10","a","Word problems, decomposing numbers, and making 10.","Add within 10 confidently; read simple number sentences (with adult help for word problems).","Within 10: word problems, breaking numbers apart, finding the number that makes 10.","K.OA.A.2, K.OA.A.3, K.OA.A.4","badge teal")]
cards="".join(f'''<div class="card">{sheet(k,240,"Sample layout illustration")}<p style="margin-top:14px"><span class="{bc}">{lv}</span></p><h3>{nm}</h3><p>{s}</p><p><strong>Before starting:</strong> {pre}</p><p class="price">$3.99</p><a class="btn" href="products/k-addition-{slug}.html">View {lv} pack</a></div>''' for slug,lv,nm,k,s,pre,rng,cc,bc in prods)
page("kindergarten-math.html","Kindergarten Math Worksheets","Kindergarten addition worksheets in three clear levels: within 5, within 10, and reasoning within 10.",f'''
<div class="wrap crumbs"><a href="index.html">Home</a> › Kindergarten Math</div>
<section class="tight"><div class="wrap"><span class="eyebrow">Kindergarten · Math</span><h1>Kindergarten Math Worksheets</h1><p class="lead">Start with addition, organized into three levels so your child practices exactly what they're ready for.</p></div></section>
<section class="tight white"><div class="wrap"><h2>Kindergarten Addition</h2>{LEVELS}<div class="grid g3" style="margin-top:28px">{cards}</div>
<div class="card" style="margin-top:28px;display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center"><div><span class="badge">Bundle</span><h3>Kindergarten Addition Complete Bundle</h3><p>All three levels in one download.</p></div><div><span class="price">$9.99</span> <a class="btn" href="products/k-addition-bundle.html">View bundle</a></div></div></div></section>
<section class="tight"><div class="wrap"><h2>More Kindergarten math skills</h2><div class="grid g3"><div class="card"><span class="badge soon">Coming soon</span><h3>Subtraction</h3><p>Taking away within 5 and 10.</p></div><div class="card"><span class="badge soon">Coming soon</span><h3>Counting & Number Recognition</h3><p>Counting objects and writing numbers 0–20.</p></div><div class="card"><span class="badge soon">Coming soon</span><h3>Place Value Foundations</h3><p>Teen numbers as ten and some ones.</p></div></div>
<p style="margin-top:20px"><a href="free-printables.html">Get the free sample and we'll tell you when new skills launch →</a></p></div></section>''')

# ---------- PRODUCTS ----------
STD_NOTE='Standards listed are those the content is <em>informed by</em>. We do not claim official alignment certification. Read the standard text at <a href="'+LINKS["cc_math"]+'" target="_blank" rel="noopener">thecorestandards.org</a>.'
for slug,lv,nm,k,s,pre,rng,cc,bc in prods:
    others="".join(f'<a class="card link" href="k-addition-{o[0]}.html"><span class="{o[8]}">{o[1]}</span><h3>{o[2]}</h3><p>$3.99</p></a>' for o in prods if o[0]!=slug)
    page(f"products/k-addition-{slug}.html",f"Kindergarten Addition: {lv} ({nm.replace('Addition ','').replace('Reasoning ','Reasoning ')})",f"Printable kindergarten addition worksheets, {lv} level: {s}",f'''
<div class="wrap crumbs"><a href="{{R}}index.html">Home</a> › <a href="{{R}}kindergarten-math.html">Kindergarten Math</a> › {lv}</div>
<section class="tight"><div class="wrap prod-grid"><div>{sheet(k,460)}<p class="notice" style="margin-top:16px">The image above is a sample-layout illustration. Real page previews will be added when the final PDF is published.</p></div>
<div class="buybox"><span class="{bc}">Level · {lv}</span><h1 style="font-size:2rem;margin-top:10px">Kindergarten Addition: {lv}<br><small style="font-size:1.1rem;color:var(--muted)">{nm}</small></h1><p>{s}</p>
<p class="price">$3.99 <small style="font-size:.9rem;font-weight:600;color:var(--muted)">Instant PDF download · Pages: TBD</small></p>
<a class="btn" data-checkout="k-add-{slug}" data-label="Buy now: $3.99" href="#">Buy now: $3.99</a><p class="checkout-note notice" hidden>Checkout isn't live yet. No payment has been taken. <a href="{{R}}free-printables.html">Get the free sample</a> in the meantime.</p>
<ul class="ticks"><li>Print at home in black and white</li><li>Answer key included</li><li>One skill, one level</li></ul></div></div></section>
<section class="tight white"><div class="wrap"><h2>Is this the right level?</h2><table class="spec">
<tr><th>Learning objective</th><td>{s}</td></tr><tr><th>Your child should already be able to</th><td>{pre}</td></tr><tr><th>Difficulty range</th><td>{rng}</td></tr>
<tr><th>Informed by (Common Core, Kindergarten)</th><td>{cc}<br><small>{STD_NOTE}</small></td></tr><tr><th>Format</th><td>PDF, US Letter. Page count: TBD.</td></tr><tr><th>How to use</th><td>About 10 minutes per page, with an adult nearby. Stop while it's still fun.</td></tr></table></div></section>
<section class="tight"><div class="wrap"><h2>Other levels</h2><div class="grid g3">{others}<a class="card link" href="k-addition-bundle.html"><span class="badge">Bundle</span><h3>All three levels</h3><p>$9.99</p></a></div></div></section>''')

page("products/k-addition-bundle.html","Kindergarten Addition Complete Bundle","All three kindergarten addition levels in one printable PDF bundle.",f'''
<div class="wrap crumbs"><a href="{{R}}index.html">Home</a> › <a href="{{R}}kindergarten-math.html">Kindergarten Math</a> › Bundle</div>
<section class="tight"><div class="wrap prod-grid"><div>{sheet("n",460)}<div class="grid g3" style="margin-top:16px">{sheet("b",200,"Sample layout")}{sheet("i",200,"Sample layout")}{sheet("a",200,"Sample layout")}</div></div>
<div class="buybox"><span class="badge">Complete bundle</span><h1 style="font-size:2rem;margin-top:10px">Kindergarten Addition Complete Bundle</h1><p>All three levels, from adding pictures within 5 to reasoning within 10, so your child can move up one step at a time.</p>
<p class="price">$9.99 <small style="font-size:.9rem;font-weight:600;color:var(--muted)">vs. $11.97 separately · Pages: TBD</small></p>
<a class="btn" data-checkout="k-add-bundle" data-label="Buy the bundle: $9.99" href="#">Buy the bundle: $9.99</a><p class="checkout-note notice" hidden>Checkout isn't live yet. No payment has been taken.</p>
<p class="notice" style="margin-top:16px">Previews are sample-layout illustrations. The price is an introductory test price.</p></div></div></section>
<section class="tight white"><div class="wrap"><h2>What's included</h2><div class="grid g3">{"".join(f'<a class="card link" href="k-addition-{p[0]}.html"><span class="{p[8]}">{p[1]}</span><h3>{p[2]}</h3><p>{p[4]}</p><p><small>Informed by: {p[7]}</small></p></a>' for p in prods)}</div></div></section>''')

# ---------- FREE (ad landing) ----------
page("free-printables.html","Free Kindergarten Addition Printables","Free printable kindergarten addition practice (within 5). Download the PDF instantly. No account needed.",f'''
<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">Free download · Kindergarten math</span><h1>Free Kindergarten Addition Practice (Within 5)</h1>
<p class="lead">Simple, focused pages: count the dots, add two small groups, write the total. Every problem stays within 5, with no surprise jumps.</p>
<ul class="ticks"><li>Original practice pages + answer key</li><li>Prints cleanly in black and white</li><li>About 10 minutes a page</li></ul>
<div class="btn-row"><a class="btn" href="downloads/free-k-addition-within-5-sample.pdf" download>Download the free PDF</a></div><p style="font-size:.9rem;color:var(--muted)">Instant download. No email required.</p></div>
<div class="stack">{sheet("b",340,"Sample layout illustration (see the PDF for the real pages)")}</div></div></section>
<section class="tight white"><div class="wrap grid g2"><div><h2>Is this the right level?</h2><p><strong>Good fit if your child can:</strong> count to 10, recognize numbers 0–5, and count objects one by one.</p><p><strong>Ready for more?</strong> Try the <a href="products/k-addition-intermediate.html">Intermediate (within 10)</a> pack.</p><p><small>Informed by Common Core K.OA.A.1 and K.OA.A.2. Not endorsed by any organization.</small></p></div>
<div class="card"><h3>Want new free printables?</h3><p>Join our email list for tips on choosing the right level and new free pages. For parents and teachers (18+).</p>
<form data-placeholder><label for="em">Email</label><input id="em" type="email" required placeholder="you@example.com"><button class="btn" style="margin-top:10px;width:100%">Join the list</button><p class="form-msg notice" hidden>Thanks! Our email list isn't connected yet, so nothing was saved. Your download above works right now.</p></form></div></div></section>
<section><div class="wrap"><div class="cta-band"><h2>Liked the sample?</h2><p>The Beginner pack continues addition within 5, then the next two levels build up to reasoning within 10.</p><a class="btn" href="kindergarten-math.html">See all three levels</a></div></div></section>''',sticky=False)

# ---------- APPROACH ----------
def src(t,h,txt,uses): return f'<div class="card"><h3>{t}</h3><p>{txt}</p><p><strong>How we use it:</strong> {uses}</p><p><a href="{h}" target="_blank" rel="noopener">Official source ↗</a></p></div>'
page("our-educational-approach.html","Our Educational Approach","How we organize worksheets using the Common Core, Head Start ELOF, NAEYC, What Works Clearinghouse, and structured literacy principles.",f'''
<section class="tight"><div class="wrap prose"><span class="eyebrow">Our educational approach</span><h1>Built on public frameworks, explained in plain language</h1>
<p class="lead">We organize every worksheet around one skill, one level, and a clear learning goal. To decide what those skills and levels should be, we draw on recognized, publicly available education frameworks.</p>
<p class="notice"><strong>Please note:</strong> We are not affiliated with, endorsed by, approved by, or certified by any of the organizations below. Our worksheets are <em>informed by</em> their published work. We don't claim our worksheets are scientifically proven to improve academic outcomes.</p></div></section>
<section class="tight white"><div class="wrap grid g2">
{src("Common Core State Standards",LINKS["cc"],"A set of K–12 expectations for what students should learn in math and English Language Arts at each grade. For Kindergarten math, the standards describe adding and subtracting within 10 using objects, drawings, and equations.","We use them to sequence K–2 skills and list relevant codes (for example, K.OA.A.1–K.OA.A.5) only where we've checked the standard text. See <a href='"+LINKS["cc_math"]+"' target='_blank' rel='noopener'>Kindergarten Operations & Algebraic Thinking</a> and <a href='"+LINKS["cc_ela"]+"' target='_blank' rel='noopener'>Kindergarten Reading: Foundational Skills</a>.")}
{src("Head Start Early Learning Outcomes Framework (ELOF)",LINKS["elof"],"A federal framework describing skills children typically develop from birth to age 5, including early math and literacy.","We use it to shape Pre-K worksheets so they fit what young children are developmentally ready for.")}
{src("NAEYC: Developmentally Appropriate Practice",LINKS["dap"],"The National Association for the Education of Young Children describes developmentally appropriate practice: teaching that meets children where they are and supports each next step.","We keep pages short and uncluttered, and we build each level on the last one.")}
{src("What Works Clearinghouse (U.S. Department of Education, IES)",LINKS["wwc"],"Reviews education research and publishes practice guides, including <a href='"+LINKS["wwc_math"]+"' target='_blank' rel='noopener'>Teaching Math to Young Children</a> and <a href='"+LINKS["wwc_read"]+"' target='_blank' rel='noopener'>Foundational Skills to Support Reading for Understanding in K–3</a>.","We use the guides' recommendations, such as developmental progressions in early math, to organize our levels.")}
{src("Structured Literacy & the Science of Reading",LINKS["ida"],"Structured literacy teaches reading explicitly and in order: sounds, letters, decoding, spelling, then fluency. It's based on research into how children learn to read.","Our upcoming reading worksheets follow a planned phonics sequence instead of mixing skills at random.")}
<div class="card"><h3>What every worksheet includes</h3><ul class="ticks"><li>A clear learning objective</li><li>The skills your child needs first</li><li>A defined difficulty range</li><li>Standards it's informed by (verified codes only)</li></ul></div></div></section>''')

# ---------- SIMPLE PAGES ----------
def prose(fn,title,desc,inner): page(fn,title,desc,f'<section class="tight"><div class="wrap prose"><h1>{title}</h1>{inner}</div></section>')
prose("about.html","About Us","About our printable worksheet shop.",f'''<p class="lead">We make printable worksheets for parents, caregivers, homeschool families, and teachers of children in Pre-K through 2nd grade.</p>
<p>We started with one frustration: free worksheets online often jump between difficulty levels without warning. A child practicing 1 + 2 shouldn't suddenly face 17 − 6.</p><p>So we're building a library where every worksheet targets one skill at one clearly defined level, and each level leads to the next.</p>
<h2>What we promise</h2><ul class="ticks"><li>Clear learning objectives and prerequisites on every product</li><li>Honest descriptions and previews</li><li>No inflated claims. Our work is informed by public frameworks, and we're not endorsed by them.</li></ul>
<h2>Where we are now</h2><p>We're launching with Kindergarten Addition. Subtraction, reading, Pre-K, and 1st–2nd grade will follow, prioritized by what parents ask for. <a href="contact.html">Tell us what you need.</a></p>''')
faqs=[("How do I choose the right level?","Each product lists the skills your child should already know. If those feel easy, move up a level. The free sample is a good starting check."),
("What format are the worksheets?","PDF files sized for US Letter paper. They're designed for black-and-white home printing."),
("How do I get my files after purchase?","Checkout isn't live yet. Once it launches, you'll receive a download link right after payment."),
("How many pages are in each pack?","Page counts will be confirmed when each pack is finalized. They're listed as TBD for now."),
("Are the worksheets aligned to Common Core?","Our Kindergarten math content is informed by specific Common Core standards, which we list by code on each product page. We don't claim official certification or endorsement."),
("Can I share the files?","You may print them for your own children or your own classroom. Please don't redistribute or resell the files. See our Terms."),
("Do you offer refunds?","Yes, in certain situations. See our Refund Policy."),
("Do you collect information from children?","No. Our site is for adults. We don't knowingly collect personal information from children.")]
prose("faq.html","Frequently Asked Questions","Answers about levels, downloads, printing, and policies.",'<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)+'</div><p><a href="terms.html">Terms</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="contact.html">Contact</a></p>')
prose("contact.html","Contact Us","Get in touch with questions about worksheets or downloads.",f'''<p class="lead">Questions about a level, a download, or a skill you'd like us to make? We'd love to hear from you.</p><p>Email: <a class="site-email" href="mailto:{EMAIL}">{EMAIL}</a></p>
<form data-placeholder class="card"><label for="n">Your name</label><input id="n" required><label for="e" style="margin-top:10px;display:block">Email</label><input id="e" type="email" required><label for="m" style="margin-top:10px;display:block">Message</label><textarea id="m" rows="5" required></textarea><button class="btn" style="margin-top:12px">Send message</button><p class="form-msg notice" hidden>This form isn't connected yet, so your message wasn't sent. Please email us directly.</p></form>
<p><small>For parents, caregivers, and teachers only. Please don't have children submit this form.</small></p>''')
DRAFT='<p class="notice">Draft placeholder. Have this reviewed by a qualified professional before launch.</p>'
prose("privacy.html","Privacy Policy","Privacy policy.",DRAFT+'''<p>Last updated: TBD</p><h2>What we collect</h2><p>If you join our email list or contact us, we collect your email address and anything you choose to send. When checkout launches, payments will be processed by a third-party provider. We won't store your card details.</p>
<h2>Children</h2><p>Our site is meant for adults. We do not knowingly collect personal information from children under 13. If you think a child has given us information, contact us and we'll delete it.</p>
<h2>Analytics</h2><p>We may use basic analytics and advertising pixels to understand site traffic. Details will be listed here before they're enabled.</p><h2>Your choices</h2><p>You can unsubscribe from emails at any time and ask us to delete your data.</p>''')
prose("terms.html","Terms of Use","Terms of use and license.",DRAFT+'''<p>Last updated: TBD</p><h2>License</h2><p>When you buy or download a worksheet, you get a personal license to print it for your own children, homeschool, or single classroom.</p><h2>Not permitted</h2><p>Reselling, redistributing, uploading to shared sites, or claiming the content as your own.</p>
<h2>Educational information</h2><p>Our worksheets are practice materials informed by public frameworks. They are not endorsed by any school or government organization, and we make no guarantee of specific academic results.</p>''')
prose("refund-policy.html","Refund Policy","Refund policy for digital downloads.",DRAFT+'''<p>Last updated: TBD</p><p>Because our products are digital downloads, sales are generally final. If a file is broken, won't download, or doesn't match its description, contact us within 14 days and we'll fix it or refund you.</p>''')
print("built")
