# The public site does not offer a downloadable page. This script is not published as a worksheet.
raise SystemExit("No public worksheet file is generated.")
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
random.seed(5)
W,H=letter;c=canvas.Canvas("/tmp/packet-preview.pdf",pagesize=letter)
c.setTitle("Free Kindergarten Addition Within 5 Sample - Proud Little Learners")
def hdr(t,sub):
    c.setFont("Helvetica",12);c.drawString(54,H-50,"Name: ______________________   Date: ____________")
    c.setFont("Helvetica-Bold",22);c.drawString(54,H-90,t);c.setFont("Helvetica",12);c.drawString(54,H-110,sub)
def foot():
    c.setFont("Helvetica",9);c.drawString(54,30,"Proud Little Learners · Addition within 5 · Personal or classroom use");c.showPage()
pages=[[(1,1),(2,1),(1,3),(2,2),(3,2),(4,1)],[(0,3),(2,3),(1,4),(3,1),(5,0),(1,2)]]
ans=[]
for pi,probs in enumerate(pages):
    hdr("Add the Dots","Count both groups. Write how many in all. (Totals up to 5)")
    for i,(a,b) in enumerate(probs):
        y=H-170-i*95;x=70
        for j in range(a): c.circle(x+j*24,y,9)
        x2=x+max(a,1)*24+20;c.setFont("Helvetica-Bold",24);c.drawString(x2,y-8,"+")
        x3=x2+40
        for j in range(b): c.rect(x3+j*24-9,y-9,18,18)
        x4=x3+max(b,1)*24+20;c.drawString(x4,y-8,"=");c.rect(x4+36,y-22,46,44)
        c.setFont("Helvetica",16);c.drawString(x4+110,y-6,f"{a} + {b} = ____")
        ans.append(f"{a} + {b} = {a+b}")
    foot()
hdr("Number Sentences","Solve each one. Use your fingers or draw dots if you need help.")
probs=[(1,1),(2,2),(3,1),(0,4),(2,3),(1,4),(4,0),(3,2),(2,1),(1,2)]
for i,(a,b) in enumerate(probs):
    x=80+(i%2)*260;y=H-180-(i//2)*100
    c.setFont("Helvetica",30);c.drawString(x,y,f"{a} + {b} =");c.rect(x+130,y-12,50,46);ans.append(f"{a} + {b} = {a+b}")
foot()
hdr("Answer Key","For grown-ups")
c.setFont("Helvetica",14)
for i,a in enumerate(ans): c.drawString(70+(i//11)*250,H-160-(i%11)*30,f"{i+1}. {a}")
c.setFont("Helvetica",10);c.drawString(54,90,"Original practice informed by Common Core K.OA.A.1 and K.OA.A.2.")
foot();c.save()
