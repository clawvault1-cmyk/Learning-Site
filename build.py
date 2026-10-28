# Generates all HTML pages. Change BRAND here (and in assets/config.js), then: python3 build.py
import os, json
BRAND="Proud Little Learners"
EMAIL="hello@proudlittlelearners.com"
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
def page(fn,title,desc,body,sticky=False,head='',js='',cls='',sticky_href=None,sticky_label=None,og=None):
    depth=fn.count("/");R="../"*depth
    nav=[("Packs","index.html#packs"),("Weekly plan","weekly.html"),("Questions","faq.html")]
    navh="".join(f'<li><a href="{R}{h}">{t}</a></li>' for t,h in nav)
    body=body.replace("{R}",R).replace("{BRAND}",BRAND)
    head=head.replace("{R}",R).replace("{BRAND}",BRAND)
    st=""
    canon="https://proudlittlelearners.com/"+("" if fn=="index.html" else fn)
    canon_tags="" if 'rel="canonical"' in head else f'<link rel="canonical" href="{canon}"><meta property="og:url" content="{canon}">'
    shown=title if " | " in title else f"{title} | {BRAND}"
    if og:
        og_url,og_w,og_h=og
    else:
        og_url,og_w,og_h="https://proudlittlelearners.com/assets/img/og-share.png",1200,630
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{shown}</title><meta name="description" content="{desc}"><meta property="og:title" content="{shown}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{og_url}"><meta property="og:image:width" content="{og_w}"><meta property="og:image:height" content="{og_h}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{og_url}">{canon_tags}
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{R}assets/img/apple-touch-icon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Nunito:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}css/styles.css">
{head}<!-- Meta Pixel loads from app.js only when SITE.metaPixelId is set. -->
</head><body data-root="{R}" class="{cls}"><a class="skip" href="#main">Skip to content</a>
<header class="site"><nav class="wrap nav" aria-label="Main"><a class="logo" href="{R}index.html"><i aria-hidden="true">P</i><span class="brand-name">{BRAND}</span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nl" aria-label="Menu"><span></span><span></span><span></span></button><ul class="nav-links" id="nl">{navh}</ul></nav></header>
<main id="main">{body}</main>
<footer class="site"><div class="wrap">
<p class="brand-name">{BRAND}</p><p>Printable kindergarten math for parents.</p>
<div class="grid g4 foot">
<div><h4>Shop</h4><ul><li><a href="{R}index.html#packs">Packs</a></li><li><a href="{R}weekly.html">Weekly plan</a></li></ul></div>
<div><h4>Help</h4><ul><li><a href="{R}faq.html">Questions</a></li><li><a href="{R}contact.html">Contact</a></li><li><a href="{R}cancel.html">Cancel weekly plan</a></li></ul></div>
<div><h4>About</h4><ul><li><a href="{R}about.html">About us</a></li><li><a href="{R}our-educational-approach.html">How we teach</a></li><li><a href="{R}resources/index.html">Parent tips</a></li></ul></div>
<div><h4>Policies</h4><ul><li><a href="{R}privacy.html">Privacy</a></li><li><a href="{R}terms.html">Terms</a></li><li><a href="{R}refund-policy.html">Refunds</a></li></ul></div>
</div>
<p class="fine">© 2026 {BRAND}</p></div></footer>
{st}<script src="{R}assets/config.js"></script><script src="{R}assets/products.js"></script><script src="{R}assets/app.js"></script>{js}</body></html>'''
    os.makedirs(os.path.dirname(fn) or ".",exist_ok=True);open(fn,"w").write(html)

PATH='<ol class="path-steps" aria-label="Kindergarten addition path"><li class="{a}">Count groups</li><li class="{b}">Combine</li><li class="{c}">Pictures to equations</li><li class="{d}">Simple stories</li></ol>'
def steps(a="",b="",c="",d=""):
    return PATH.format(a=a,b=b,c=c,d=d)

# ---------- HOME (scrollytelling; scene and motion live in assets/js) ----------
home=open("assets/src/home-body.html").read()
page("index.html","Kindergarten Math Help for Parents | Proud Little Learners","Kindergarten math help without random worksheets. Short printable pages, easy to harder, with a guide for you. $3.99.",home,cls="home")

# ---------- PRODUCTS ----------
prods=[
 dict(slug="beginner",lv="Beginner",nm="Beginner: Adding within 5",k="b",bc="badge",checkout="k-add-beginner",
  summary="Count and combine groups up to 5, write the number sentence, and try a short addition story.",
  practice="Your child counts two small groups, puts them together, and writes the total. A page might show 2 dots and 1 more dot, then the number sentence 2 + 1 = 3. The pack also includes a short addition story you can read aloud. Totals stay at 5 or below.",
  start="This is a good starting point if your child can count to 10, recognize the numbers 0–5, and count objects one by one.",
  progress="The pages move from counting each group, to combining the groups, to a number sentence, and then to a short addition story. Totals stay at 5 or below.",
  guidance="Stay nearby. Let your child count out loud. A prompt you can use: “Point to the two groups. How many in all?” If they pause, count one group together, then let them count the rest.",
  repeat="Stay with this pack if you are helping with most of the problems. Move to the Intermediate pack when adding up to 5, including the short story, feels easy.",
  standards="These pages practice goals from Common Core K.OA.A.1 (showing addition with objects and drawings) and K.OA.A.5 (adding within 5). Totals in this pack stay at 5 or below.",
  marks=("on","on","on","on")),
 dict(slug="intermediate",lv="Intermediate",nm="Intermediate: Adding within 10",k="i",bc="badge peach",checkout="k-add-intermediate",
  summary="Pictures turn into number sentences with totals up to 10.",
  practice="Your child moves from pictures to number sentences such as 4 + 3 = __. Some pages use a ten-frame, which is a box with 10 spaces, so numbers up to 10 are easier to see. Totals stay at 10 or below.",
  start="A fit when adding up to 5 with pictures feels easy, and your child recognizes numbers 0–10.",
  progress="Pages go from a picture of the groups, to the number sentence, to counting on from the bigger number. A number line on some pages shows that count.",
  guidance="Point to the bigger number and count the rest together one time. Then let your child try the next problem. If the ten-frame is new, fill it with counters before using the pencil.",
  repeat="Stay here if the number sentences still feel like a guess. Move to the Advanced pack when adding up to 10 feels comfortable.",
  standards="These pages practice goals from Common Core K.OA.A.1 and K.OA.A.2: addition within 10 using objects, drawings, and equations.",
  marks=("","","on","")),
 dict(slug="advanced",lv="Advanced",nm="Advanced: Story problems within 10",k="a",bc="badge teal",checkout="k-add-advanced",
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
<p class="micro">{BY[p["checkout"]]["practicePages"]} practice pages, with a matching answer key for each one.</p>
<aside class="standards-note"><h3>Learning goals</h3><p>{p["standards"]} <a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">Common Core kindergarten addition</a>.</p></aside>'''

PACKS=json.load(open("assets/packs.json"))
FILE=json.load(open("packs/packs.json"))
BY={item["id"]:item for item in FILE["packs"]}
def preview_kind(path):
    for key,label in (("cover","Cover"),("guide","Parent guide"),("tracker","Progress tracker"),("practice","Practice page")):
        if key in path: return label
    return "Page"
def pick_previews(paths):
    pngs=[p for p in paths if p.endswith(".png")]
    def hits(key): return [p for p in pngs if key in p]
    chosen=hits("cover")[:1]+hits("practice")[:3]+hits("guide")[:1]+hits("tracker")[:1]
    return chosen or pngs[:1]
COVER_WIDTHS=(640,960,1600)
PAGE_WIDTHS=(480,800,1200)
CARD_SIZES="(min-width:1024px) 360px, 92vw"
GALLERY_SIZES="(min-width:1024px) 640px, 92vw"
def art_srcset(slug, stem, widths):
    return ", ".join(f"{{R}}assets/img/packs/{slug}/{stem}-{w}.webp {w}w" for w in widths)
COVER_SIZES="(min-width:1024px) 560px, 80vw"
def art_img(slug, stem, widths, w, h, alt, sizes, lazy=False, large=False):
    default=widths[-1] if large else (widths[1] if len(widths)>2 else widths[-1])
    lazy_attr=' loading="lazy" decoding="async"' if lazy else ' decoding="async"'
    return (f'<img src="{{R}}assets/img/packs/{slug}/{stem}-{default}.webp" srcset="{art_srcset(slug, stem, widths)}" sizes="{sizes}" alt="{alt}" width="{w}" height="{h}"{lazy_attr}>')
def slide_gallery(slug, name, attrs, interiors=True, extra_pages=None):
    specs=[("cover", name, "cover-4x3", COVER_WIDTHS, 1600, 1200, COVER_SIZES, f"assets/img/packs/{slug}/cover-1x1-600.webp", True)]
    if interiors:
        specs.append(("page", "Parent guide", "guide", PAGE_WIDTHS, 1200, 1553, GALLERY_SIZES, f"assets/img/packs/{slug}/guide-480.webp", False))
        for n in range(1,6):
            specs.append(("page", "Practice page", f"interior-{n:02d}", PAGE_WIDTHS, 1200, 1553, GALLERY_SIZES, f"assets/img/packs/{slug}/interior-{n:02d}-480.webp", False))
        specs.append(("page", "Progress tracker", "tracker", PAGE_WIDTHS, 1200, 1553, GALLERY_SIZES, f"assets/img/packs/{slug}/tracker-480.webp", False))
    extras=list(extra_pages or [])
    n=len(specs)+len(extras)
    slides=[]; thumbs=[]; dots=[]
    i=0
    def emit(kind, img, thumb):
        slides.append(f'<div class="slide {kind}">{img}</div>')
        thumbs.append(f'<button type="button" class="thumb{" on" if i==0 else ""}" data-i="{i}"><img src="{{R}}{thumb}" alt=""></button>')
        dots.append(f'<button type="button" class="dot{" on" if i==0 else ""}" data-i="{i}" aria-label="Page {i+1}"></button>')
    for kind, alt, stem, widths, w, h, sizes, thumb, large in specs:
        emit(kind, art_img(slug, stem, widths, w, h, alt, sizes, lazy=0<i<n-2, large=large), thumb)
        i+=1
    for src, alt in extras:
        loading=' loading="lazy"' if 0<i<n-2 else ''
        emit("page", f'<img src="{{R}}{src}" alt="{alt}" width="1200" height="1553" decoding="async"{loading}>', src)
        i+=1
    thumb_row=f'<div class="thumbs">{"".join(thumbs)}</div>' if n>1 else ""
    nav=f'<div class="gal-nav"><div class="dots">{"".join(dots)}</div><p class="gal-count">1 / {n}</p></div>' if n>1 else ""
    return f'<div class="gallery" {attrs}><div class="gallery-main"><div class="slides">{"".join(slides)}</div></div>{nav}{thumb_row}</div>'
def og_for(slug):
    path=f"assets/img/packs/{slug}/cover-4x3-1600.webp"
    return (f"https://proudlittlelearners.com/{path}", 1600, 1200, path)
def support_sentence(src):
    s=src["supportingPages"]
    bits=[f'{src["answerPages"]} answer-key pages']
    if s.get("guide"):
        n=s["guide"]
        bits.append("a parent guide" if n==1 else f"a {n}-page parent guide")
    if s.get("parentNote"): bits.append("a parent note")
    if s.get("cover"): bits.append("a cover")
    if s.get("tracker"): bits.append("a tracker")
    if s.get("certificate"): bits.append("a certificate")
    return ", ".join(bits)
COPY={
 "beginner":dict(name="Beginner: Adding within 5",
  title="Beginner: Adding within 5 | Proud Little Learners",
  desc="Kindergarten math printables: count two groups, then put them together. Totals up to 5. Guide and answer keys. $3.99.",
  ask="Can your child count 5 toys?",
  test="Start here if your child can count 5 toys.",
  sub="Count two groups, then put them together, like 2 + 1 = 3.",
  detail="18 pages · adding up to 5",
  quote='"Count this group. Count the other group. Now count every object."',
  says='When the plus sign shows up: "Plus means we put the groups together."',
  move="When pages 16, 17, and 18 are right with only a little help."),
 "intermediate":dict(name="Intermediate: Adding within 10",
  title="Intermediate: Adding within 10 | Proud Little Learners",
  desc="Kindergarten math printables: go from pictures to adding, like 4 + 3 = 7. Totals up to 10. Guide and answer keys. $3.99.",
  ask="Can your child add 2 toys and 3 toys?",
  test="Start here if your child can add 2 toys and 3 toys.",
  sub="Go from pictures to adding, like 4 + 3 = 7.",
  detail="18 pages · adding up to 10",
  quote='"Fill the top row first. A full top row is 5. Now count the rest."',
  says="The guide shows this on a box with 10 spaces. Fill it with cereal first.",
  move="When your child can add up to 10 with only a little help, including page 18."),
 "advanced":dict(name="Advanced: Story problems within 10",
  title="Advanced: Story problems within 10 | Proud Little Learners",
  desc="Kindergarten math printables: making 10, missing numbers, and short stories you read aloud. Guide and answer keys. $3.99.",
  ask="Can your child add 4 toys and 5 toys?",
  test="Start here if your child can add 4 toys and 5 toys.",
  sub='Make 10, find missing numbers, and solve short stories you read aloud, like "3 ducks swim. 2 more come. How many now?"',
  detail="18 pages · making 10 and math stories",
  quote='"What happened?" Then ask, "How many?"',
  says="Act the story out with cereal or coins. Your child doesn't need to read.",
  move="When these pages feel easy, your child has finished all three packs."),
}
def product_page(p):
    c=COPY[p["slug"]]
    d=PACKS[p["slug"]]
    gallery=slide_gallery(p["slug"], c["name"], f'data-pixel-view data-content-name="{c["name"]}" data-checkout="{d["checkout"]}"')
    og_url,og_w,og_h,og_path=og_for(p["slug"])
    others="".join(f'<a class="level-card" href="k-addition-{o["slug"]}.html"><span class="mock">{art_img(o["slug"], "interior-01", PAGE_WIDTHS, 1200, 1553, "", "(min-width:768px) 240px, 42vw", lazy=True)}</span><p class="test">{COPY[o["slug"]]["ask"]}</p><h3>{COPY[o["slug"]]["name"]}</h3><p class="price">$3.99</p></a>' for o in prods if o["slug"]!=p["slug"])
    ld=json.dumps({"@context":"https://schema.org","@type":"Product","name":c["name"],"description":c["sub"],"image":og_url,"brand":{"@type":"Brand","name":BRAND},"offers":{"@type":"Offer","price":"3.99","priceCurrency":"USD","url":"https://proudlittlelearners.com/products/k-addition-"+p["slug"]+".html"}},ensure_ascii=False)
    buy=f'<a class="btn buy" aria-disabled="true" data-checkout="{d["checkout"]}" data-content-name="{c["name"]}" data-value="3.99" data-label="Buy now">Checkout opens soon</a>'
    page(f"products/k-addition-{p['slug']}.html", c["title"], c["desc"], f'''
<div class="wrap crumbs"><a href="{{R}}index.html#packs">Packs</a></div>
<section class="product-top"><div class="wrap prod-top">
{gallery}
<div class="buybox"><h1>{c["name"]}</h1><p class="test">{c["test"]}</p><p>{c["sub"]}</p>
<p class="price price-lg">$3.99</p>
{buy}
</div></div></section>
<section class="sec"><div class="wrap"><h2>What's inside</h2>
<div class="inside-grid">
<div class="inside-tile"><img src="{{R}}assets/img/packs/{p["slug"]}/interior-01-480.webp" alt="" width="480" height="621">18 practice pages, easy to harder</div>
<div class="inside-tile"><img src="{{R}}assets/img/packs/{p["slug"]}/interior-02-480.webp" alt="" width="480" height="621">An answer key for every page</div>
<div class="inside-tile"><img src="{{R}}assets/img/packs/{p["slug"]}/guide-480.webp" alt="" width="480" height="621">A 2-page parent guide</div>
<div class="inside-tile"><img src="{{R}}assets/img/packs/{p["slug"]}/tracker-480.webp" alt="" width="480" height="621">A tracker and a certificate</div>
</div>
<div class="inside-notes">
<p>Color cover. Black-and-white pages save ink.</p>
<p>You'll need a pencil and some cereal or toys.</p>
<p>Instant download. Print for your family or one classroom.</p>
</div>
<details class="details"><summary>What you say</summary><blockquote>{c["quote"]}</blockquote><p>{c["says"]}</p></details>
<details class="details"><summary>When to move up</summary><p>{c["move"]}</p></details>
</div></section>
<section class="sec"><div class="wrap"><h2>Other packs</h2><div class="level-grid">{others}</div>
</div></section>
<div class="buybar" hidden><span class="buybar-price">$3.99</span>{buy}</div>
<script type="application/ld+json">{ld}</script>''', og=(og_url, og_w, og_h), cls="product")
for p in prods:
    product_page(p)

WEEKS=[
"Counting to 5","Counting to 10","More and fewer","Adding within 5",
"Story problems within 5","Adding within 10","Taking away within 5","Shapes and patterns"]
wgallery=slide_gallery("weekly", "Weekly Kindergarten Math Plan", 'data-pixel-view data-content-name="Weekly Kindergarten Math Plan" data-subscribe="weekly"', interiors=False, extra_pages=[
 ("packs/weekly/week-01/preview-practice-01.webp","Practice page"),
 ("packs/weekly/week-02/preview-practice-05.webp","Practice page"),
 ("packs/weekly/week-03/preview-practice-01.webp","Practice page"),
 ("packs/weekly/week-01/preview-practice-05.webp","Practice page"),
])
wog_url,wog_w,wog_h,_=og_for("weekly")
weeklist="".join(f"<li>{w}</li>" for w in WEEKS)
wbuy='<a class="btn buy" aria-disabled="true" data-subscribe="weekly" data-content-name="Weekly Kindergarten Math Plan" data-value="3.99" data-label="Start the weekly plan">Checkout opens soon</a>'
page("weekly.html","Weekly Kindergarten Math Plan | Proud Little Learners","A new printable kindergarten math packet every Monday. $3.99/month.",f'''
<div class="wrap crumbs"><a href="{{R}}index.html#packs">Packs</a></div>
<section class="product-top"><div class="wrap prod-top">
{wgallery}
<div class="buybox"><span class="badge">Weekly plan</span><h1>Weekly Kindergarten Math Plan</h1>
<p>A new packet every Monday: counting, shapes, adding, and more. Get this month's packets today.</p>
<p class="price price-lg">$3.99/month</p>
{wbuy}
<p class="cancel-line">Renews monthly until you cancel. Cancel online anytime.</p>
<p class="cancel-line">Access ends when you cancel. New members: full refund within 7 days.</p>
</div></div></section>
<section class="sec"><div class="wrap"><h2>In each packet</h2>
<p>7 or 8 practice pages, answer keys, a 1-page parent note, and a tracker.</p>
<details class="details"><summary>The first 8 weeks</summary>
<ol class="week-grid">{weeklist}</ol></details>
<p>Want to focus on adding? <a href="{{R}}index.html#packs">See the packs.</a></p>
</div></section>
<div class="buybar" hidden><span class="buybar-price">$3.99/month</span>{wbuy}</div>''', og=(wog_url, wog_w, wog_h), cls="product")

moved='''
<section class="tight"><div class="wrap prose"><h1>This page moved</h1>
<p><a href="{R}index.html#packs">See the kindergarten math packs.</a></p></div></section>
<script>location.replace("{R}index.html#packs");</script>'''
page("products/k-addition-bundle.html","Page moved | Proud Little Learners","This page has moved.",moved,
head='<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={R}index.html#packs">')
page("free-printables.html","Page moved | Proud Little Learners","This page has moved.",moved,
head='<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={R}index.html#packs">')

cards=""
for slug in ("beginner","intermediate","advanced"):
    c=COPY[slug]
    shot=art_img(slug, "interior-01", PAGE_WIDTHS, 1200, 1553, "", "(min-width:1024px) 360px, 120px")
    cards+=f'<article class="pack-card lv-{slug}"><a class="mock" href="products/k-addition-{slug}.html">{shot}</a><div class="card-copy"><h3>{c["ask"]}</h3><p class="pack-name"><a href="products/k-addition-{slug}.html">{c["name"]}</a></p><p class="price">$3.99</p><span class="meta">{c["detail"]}</span></div><div class="card-actions"><a class="btn" href="products/k-addition-{slug}.html">See inside</a></div></article>'
wshot='<img src="packs/weekly/week-01/preview-practice-01.webp" alt="Weekly Kindergarten Math Plan" width="1200" height="1553" loading="lazy" decoding="async">'
page("kindergarten-math.html","Kindergarten Math Packs | Proud Little Learners","Three printable kindergarten math packs, $3.99 each: Adding within 5, Adding within 10, and Story problems within 10.",f'''
<section class="tight"><div class="wrap"><h1>Which one fits?</h1>
<p class="lead">Try these with real toys. Pick the last one your child gets right.</p>
<div class="pack-grid">{cards}</div>
<article class="plan-card weekly-extra"><a class="mock" href="weekly.html">{wshot}</a><div class="card-copy"><span class="badge">Weekly plan</span><h3>Weekly Kindergarten Math Plan</h3><p>A new packet every Monday: counting, shapes, adding, and more.</p><p class="price">$3.99/month</p></div><div class="card-actions"><a class="btn" href="weekly.html">See the weekly plan</a></div></article>
</div></section>''')

def prose(fn,title,desc,inner,h1=None):
    page(fn,title,desc,f'<section class="tight"><div class="wrap prose"><h1>{h1 or title}</h1>{inner}</div></section>')

prose("about.html","About Us | Proud Little Learners","Printable kindergarten math for parents who want to help at home.",'''
<p class="lead">We make kindergarten math pages for parents who want to help but don't know where to start.</p>
<p>Questions? Email <a href="mailto:hello@proudlittlelearners.com">hello@proudlittlelearners.com</a>.</p>''',"About us")

faqs=[
("Which pack should we start with?","Beginner: Adding within 5, if your child can count 5 toys. Not sure? Try the three toy tests on the home page."),
("I'm not a teacher. Can I do this?","Yes. Every page has an answer key, and the guide is 2 short pages in plain words."),
("What if a page is too hard?","Go back a page, or count real things like cereal. Try again tomorrow."),
("When do we move up?","When the last 3 pages are right with only a little help. The guide says which pages."),
("My child doesn't like worksheets. Will this help?","The pages are short, and you start with real things. Stop while it's still fun."),
("Is it on a screen?","No. You print it, and your child uses a pencil."),
("How do I get my files?","You get a download link right after you pay, and by email."),
("How does the weekly plan work?","$3.99/month. This month's packets today, then a new one every Monday. Cancel anytime. Access ends when you cancel."),
("Are weekly packets the same as the packs?","No. They're shorter and cover more, like counting and shapes. Packs go deeper on adding."),
("How do I cancel?",'Sign in and <a href="cancel.html">cancel</a>, or email us.'),
("Can I get a refund?",'If a file has a problem, we\'ll fix it or refund you. New weekly members can get <a href="refund-policy.html">a full refund within 7 days</a>.'),
("Can I share the files?","Print them for your family or one classroom. Please don't share the files."),
]
prose("faq.html","Questions | Proud Little Learners","Answers about packs, the weekly plan, downloads, and refunds.",'<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)+"</div>","Questions")

prose("contact.html","Contact | Proud Little Learners","Email us with a question about a pack, a download, or the weekly plan.",'''
<p class="lead">Questions about a pack, a download, or the weekly plan? Email us.</p>
<p><a class="site-email" href="mailto:hello@proudlittlelearners.com">hello@proudlittlelearners.com</a></p>
<p>We reply within 1 business day.</p>''',"Contact us")

prose("cancel.html","Cancel the Weekly Kindergarten Math Plan | Proud Little Learners","Cancel the weekly plan online or by email.",'''
<p class="lead">When you cancel, billing stops and access ends. Download any packets you want to keep first.</p>
<ol class="plain-steps" aria-label="How to cancel"><li>Sign in</li><li>Go to Subscriptions</li><li>Click Cancel</li></ol>
<div class="cancel-actions"><a class="btn buy" data-signin>Sign in to cancel</a>
<a class="btn alt" data-email-cancel href="mailto:hello@proudlittlelearners.com?subject=Cancel%20my%20Weekly%20Kindergarten%20Math%20Plan">Email us to cancel</a></div>
<p class="signin-note" hidden></p>
<p>Send the email address you signed up with. We'll cancel within 1 business day and email you when it's done.</p>''',"Cancel the weekly plan")

prose("our-educational-approach.html","How We Teach | Proud Little Learners","The simple ideas behind our kindergarten math packs: real things, then pictures, then numbers.",f'''
<p class="lead">Our packs use a few simple ideas that teachers use every day.</p>
<h2>Real things, then pictures, then numbers</h2>
<p>Your child counts cereal or toys first. Then dots on the page. Then numbers, like 2 + 1 = 3.</p>
<h2>I show you, we do it together, you try</h2>
<p>You show one problem. You do the next one together. Then your child tries alone. The guide tells you what to say at each step.</p>
<h2>One small step at a time</h2>
<p>Each page is just a little harder than the last. A child should feel sure of one step before the next.</p>
<h2>Where these ideas come from</h2>
<ul>
<li><a href="{LINKS["wwc_math"]}" target="_blank" rel="noopener">Teaching Math to Young Children, a free guide from the U.S. Department of Education's research office (IES)</a></li>
<li><a href="{LINKS["cc_math"]}" target="_blank" rel="noopener">The Common Core kindergarten math standards</a></li>
</ul>''',"How we teach")

def legal(fn,title,desc,h1):
    prose(fn,title,desc,open("assets/legal/"+fn.replace(".html",".body.html")).read(),h1)
legal("privacy.html","Privacy Policy | Proud Little Learners","What we collect, why, and who we share it with. We don't sell your information.","Privacy Policy")
legal("terms.html","Terms | Proud Little Learners","Terms for buying and using our printable packs and the weekly plan.","Terms")
legal("refund-policy.html","Refund Policy | Proud Little Learners","How refunds work for packs and the weekly plan.","Refund Policy")

page("resources/index.html","Parent Tips | Proud Little Learners","Short, plain guides for helping your kindergartner with math at home.",'''
<section class="tight"><div class="wrap prose"><h1>Parent tips</h1>
<p>Short guides for helping your child with math at home.</p>
<ul class="ticks">
<li><a href="how-to-know-if-your-kindergartener-is-ready-for-addition.html"><strong>Is My Child Ready to Add?</strong></a> Simple signs your kindergartner is ready, and what to do if they need more time.</li>
<li><a href="addition-within-5-vs-addition-within-10.html"><strong>Adding Within 5 vs. Within 10</strong></a> What these mean, and when to move up.</li>
<li><a href="how-to-choose-the-right-worksheet-difficulty.html"><strong>How to Pick the Right Worksheet Level</strong></a> How to find pages that aren't too easy or too hard.</li>
<li><a href="how-to-help-your-child-practice-without-frustration.html"><strong>How to Keep Practice From Turning Into a Fight</strong></a> Ways to keep practice short and calm.</li>
</ul>
<h2>Want the next page ready for you?</h2>
<p>Get a new kindergarten math packet every Monday.</p>
<p><a class="btn" href="{R}weekly.html">See the weekly plan</a> <a class="btn alt" href="{R}index.html#packs">See the packs</a></p>
</div></section>''')

import re
def check_built():
    your=re.compile(r"\[(?:Your\b|A few\b)")
    general=re.compile(r"\[[A-Z][A-Za-z'’][^\]]{0,80}\]")
    legal={"privacy.html","terms.html","refund-policy.html"}
    bad=[]
    for dirpath, dirnames, filenames in os.walk("."):
        dirnames[:] = [d for d in dirnames if d not in (".git","node_modules")]
        if "/assets/" in dirpath.replace("\\","/") or dirpath.endswith("assets"): continue
        for fn in filenames:
            if not fn.endswith(".html"): continue
            path=os.path.join(dirpath, fn)
            text=open(path, encoding="utf-8").read()
            for m in your.finditer(text):
                bad.append(f"{path}: {m.group(0)}")
            if fn not in legal:
                for m in general.finditer(text):
                    bad.append(f"{path}: {m.group(0)}")
    home=open("index.html", encoding="utf-8").read()
    if re.search(r"gsap|lenis|ScrollTrigger|assets/js/home|id=\"story\"|id=\"gl\"", home):
        bad.append("index.html still includes the scroll animation")
    if "Fraunces" in home or "three" in home and "three.min" in home:
        bad.append("index.html still loads a removed library")
    if bad:
        print("BUILD CHECK FAILED")
        print("\n".join(bad[:40]))
        raise SystemExit(1)
check_built()
print("built")
