// Draws original black-and-white sample worksheet faces onto canvases.
const INK="#1d1d1f", PAPER="#fdfbf6";
function base(c,w,h,title,sub,level){
  c.fillStyle=PAPER;c.fillRect(0,0,w,h);
  // paper fibre noise
  fibres(c,w,h,1);
  const u=w/100;
  c.strokeStyle=INK;c.fillStyle=INK;c.lineWidth=u*0.28;
  c.font=`500 ${u*2.6}px Inter, Arial, sans-serif`;
  c.fillText("Name ______________________",u*7,u*8);c.fillText("Date __________",u*68,u*8);
  c.fillStyle="#247F78";c.font=`700 ${u*2.2}px Inter, Arial`;c.fillText(level.toUpperCase(),u*7,u*15.5);
  c.fillStyle=INK;c.font=`600 ${u*6}px Fraunces, Georgia, serif`;c.fillText(title,u*7,u*23);
  c.font=`400 ${u*2.7}px Inter, Arial`;c.fillStyle="#444";c.fillText(sub,u*7,u*28.5);
  c.fillStyle=INK;
  // footer
  c.strokeStyle="#bbb";c.lineWidth=u*0.15;c.beginPath();c.moveTo(u*7,h-u*9);c.lineTo(w-u*7,h-u*9);c.stroke();
  c.fillStyle="#777";c.font=`500 ${u*2}px Inter, Arial`;
  c.fillText("Proud Little Learners",u*7,h-u*5);
  c.textAlign="right";c.fillText("SAMPLE LAYOUT · NOT THE FINAL WORKSHEET",w-u*7,h-u*5);c.textAlign="left";
  c.strokeStyle=INK;c.fillStyle=INK;c.lineWidth=u*0.35;
  return u;
}
const box=(c,x,y,s,u)=>{c.lineWidth=u*.35;c.beginPath();c.roundRect(x,y,s,s,u*1.2);c.stroke();};
const dot=(c,x,y,r,fill)=>{c.beginPath();c.arc(x,y,r,0,7);fill?c.fill():c.stroke();};
const txt=(c,s,x,y,sz,u,w=600)=>{c.font=`${w} ${u*sz}px Inter, Arial`;c.fillText(s,x,y);};
function tenFrame(c,x,y,cell,n,u,m=0){c.lineWidth=u*.3;
  for(let i=0;i<10;i++){const cx=x+(i%5)*cell,cy=y+Math.floor(i/5)*cell;c.strokeRect(cx,cy,cell,cell);
    if(i<n)dot(c,cx+cell/2,cy+cell/2,cell*.32,true);else if(i<n+m)dot(c,cx+cell/2,cy+cell/2,cell*.32,false);}}
function bond(c,x,y,r,a,b,t,u){c.lineWidth=u*.3;
  c.beginPath();c.moveTo(x,y);c.lineTo(x-r*1.6,y+r*2.4);c.moveTo(x,y);c.lineTo(x+r*1.6,y+r*2.4);c.stroke();
  [[x,y,t],[x-r*1.6,y+r*2.4,a],[x+r*1.6,y+r*2.4,b]].forEach(([px,py,v])=>{c.fillStyle=PAPER;dot(c,px,py,r,true);c.fillStyle=INK;dot(c,px,py,r);
    if(v!==null){c.textAlign="center";txt(c,String(v),px,py+r*.38,r/u*1.05,u);c.textAlign="left";}});}
function fibres(c,w,h,k){
  const n=Math.floor(w*h/70);
  for(let i=0;i<n;i++){c.fillStyle=`rgba(120,108,85,${Math.random()*0.04*k})`;c.fillRect(Math.random()*w,Math.random()*h,1.4,1.4);}
  c.lineCap="round";const f=Math.floor(w*h/2600);
  for(let i=0;i<f;i++){const x=Math.random()*w,y=Math.random()*h,a=Math.random()*6.28,l=(4+Math.random()*14)*w/1024;
    c.strokeStyle=`rgba(${Math.random()<.5?"150,135,110":"255,255,255"},${(0.05+Math.random()*0.08)*k})`;c.lineWidth=(0.6+Math.random()*0.8)*w/1024;
    c.beginPath();c.moveTo(x,y);c.quadraticCurveTo(x+Math.cos(a+.6)*l*.5,y+Math.sin(a+.6)*l*.5,x+Math.cos(a)*l,y+Math.sin(a)*l);c.stroke();}
}
export function paperBump(W=512){const H=Math.round(W*1.294),cv=document.createElement("canvas");cv.width=W;cv.height=H;const c=cv.getContext("2d");
  c.fillStyle="#808080";c.fillRect(0,0,W,H);fibres(c,W,H,4);
  for(let i=0;i<W*H/6;i++){const v=110+Math.random()*40|0;c.fillStyle=`rgba(${v},${v},${v},.25)`;c.fillRect(Math.random()*W,Math.random()*H,1,1);}return cv;}
export function blurShadow(S=256){const cv=document.createElement("canvas");cv.width=S;cv.height=Math.round(S*1.294);const c=cv.getContext("2d");
  c.filter=`blur(${S*0.07}px)`;c.fillStyle="rgba(20,35,45,1)";const m=S*0.2;c.fillRect(m,m*1.1,S-2*m,cv.height-2.2*m);return cv;}
export const KINDS={
  beginner:{level:"Level 1 · Beginner",title:"Add the Dots",sub:"Count both groups. Write how many in all. Totals within 5."},
  intermediate:{level:"Level 2 · Intermediate",title:"Ten-Frames & Counting On",sub:"Start at the bigger number and count on. Totals within 10."},
  advanced:{level:"Level 3 · Advanced",title:"Number Bonds & Make Ten",sub:"Find the missing part. Break numbers apart. Make ten."},
  bundle:{level:"Complete Bundle",title:"Kindergarten Addition",sub:"All three levels, one step at a time."},
};
export function drawSheet(kind,W=1024){
  const H=Math.round(W*1.294);const cv=document.createElement("canvas");cv.width=W;cv.height=H;const c=cv.getContext("2d");
  const k=KINDS[kind];const u=base(c,W,H,k.title,k.sub,k.level);
  if(kind==="beginner"){[[2,1],[1,3],[2,2],[3,2],[4,1]].forEach(([a,b],i)=>{const y=u*(40+i*17.5);let x=u*9;
    for(let j=0;j<a;j++)dot(c,x+j*u*5.2,y,u*1.9,true);x+=a*u*5.2+u*2;txt(c,"+",x,y+u*2,5,u,500);x+=u*7;
    for(let j=0;j<b;j++)dot(c,x+j*u*5.2,y,u*1.9,false);x+=b*u*5.2+u*2;txt(c,"=",x,y+u*2,5,u,500);box(c,x+u*7,y-u*5,u*10,u);
    c.fillStyle="#666";txt(c,`${a} + ${b} = ___`,u*72,y+u*1.5,3.2,u,500);c.fillStyle=INK;});}
  if(kind==="intermediate"){[[6,3],[7,2],[5,4]].forEach(([a,b],i)=>{const y=u*(36+i*22);tenFrame(c,u*9,y,u*6,a,u,b);
      txt(c,`${a} + ${b} =`,u*50,y+u*8.5,5,u);box(c,u*76,y+u*1.5,u*10,u);});
    const y=u*103;c.lineWidth=u*.3;c.beginPath();c.moveTo(u*9,y);c.lineTo(u*91,y);c.stroke();
    for(let i=0;i<=10;i++){const x=u*(9+i*8.2);c.beginPath();c.moveTo(x,y-u*1.5);c.lineTo(x,y+u*1.5);c.stroke();c.textAlign="center";txt(c,String(i),x,y+u*5,2.6,u,500);c.textAlign="left";}
    c.setLineDash([u,u]);for(let i=5;i<8;i++){const x=u*(9+i*8.2);c.beginPath();c.arc(x+u*4.1,y-u*1.5,u*4.1,Math.PI,0);c.stroke();}c.setLineDash([]);
    txt(c,"5 + 3: start at 5, count on 6, 7, 8",u*9,y+u*12,2.8,u,500);}
  if(kind==="advanced"){bond(c,u*24,u*40,u*5,4,null,7,u);bond(c,u*72,u*40,u*5,null,6,10,u);
    [["4 + __ = 7"],["__ + 3 = 8"],["6 + __ = 10"]].forEach(([s],i)=>txt(c,s,u*9+i*u*30,u*70,4.4,u));
    txt(c,"Make ten:",u*9,u*84,3.4,u,700);tenFrame(c,u*9,u*88,u*6,7,u);txt(c,"7 + ___ = 10",u*48,u*96,4.4,u);
    txt(c,"Sam has 6 blocks. He gets 4 more. How many now?",u*9,u*113,2.8,u,500);}
  if(kind==="bundle"){c.fillStyle="#243746";c.beginPath();c.roundRect(u*7,u*36,u*86,u*70,u*3);c.fill();
    c.fillStyle="#FAF8F3";["Beginner · within 5","Intermediate · within 10","Advanced · reasoning within 10"].forEach((s,i)=>{
      c.fillStyle=["#F4D77D","#F3BFA8","#7cc7bf"][i];dot(c,u*16,u*(52+i*18),u*3,true);c.fillStyle="#FAF8F3";txt(c,s,u*23,u*(53.5+i*18),3.6,u,600);});}
  return cv;
}
