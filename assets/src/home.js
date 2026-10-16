import {drawSheet} from "./textures.js";
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const html=document.documentElement;
const mobile=matchMedia("(max-width: 760px)").matches||matchMedia("(pointer: coarse)").matches&&innerWidth<900;
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
const glOK=(()=>{try{const c=document.createElement("canvas");return !!(c.getContext("webgl2")||c.getContext("webgl"));}catch(e){return false}})();
const thumb=(k,w=520)=>{const c=drawSheet(k,w);c.className="thumb";c.setAttribute("role","img");c.setAttribute("aria-label","Sample layout illustration of a "+k+" worksheet");return c;};

// magnetic buttons (fine pointers only)
if(matchMedia("(pointer:fine)").matches&&!reduce)$$(".mag").forEach(b=>{
  b.addEventListener("pointermove",e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.22}px,${(e.clientY-r.top-r.height/2)*.3}px)`;});
  b.addEventListener("pointerleave",()=>{b.style.transform="";});});

// reveal-on-scroll for normal sections
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}}),{rootMargin:"0px 0px -10% 0px"});
$$(".reveal").forEach(el=>io.observe(el));

Promise.all([document.fonts.load("600 40px Fraunces"),document.fonts.load("500 20px Inter")]).catch(()=>{}).then(()=>document.fonts.ready).then(start);
function start(){
  // poster fan (shown instantly, replaced by WebGL)
  const poster=$(".poster");["intermediate","beginner","advanced"].forEach(k=>poster.appendChild(thumb(k,mobile?360:560)));
  if(reduce||!glOK||!window.gsap){staticMode();return;}
  const kick=()=>import("./scene.js").then(m=>motion(m.initScene)).catch(e=>{console.error("motion failed",e&&e.stack||e);staticMode();});
  ("requestIdleCallback" in window)?requestIdleCallback(kick,{timeout:900}):setTimeout(kick,300);
}

function staticMode(){
  html.classList.add("rm");
  $$(".p-level").forEach(p=>{const d=document.createElement("div");while(p.firstChild)d.appendChild(p.firstChild);p.append(thumb(p.dataset.level,480),d);});
  $(".p-hero").after($(".poster"));const bt=$(".bigtype"),pj=$(".p-jump");if(bt&&pj)pj.before(bt);
  $$(".lineup .pack").forEach(p=>p.prepend(thumb(p.dataset.kind,420)));
}

function motion(initScene){
  const gsap=window.gsap,ST=window.ScrollTrigger;gsap.registerPlugin(ST);
  const lenis=new window.Lenis({lerp:.09,smoothWheel:true});window.__lenis=lenis;
  lenis.on("scroll",ST.update);gsap.ticker.add(t=>lenis.raf(t*1000));gsap.ticker.lagSmoothing(0);
  $$('a[href^="#"]').forEach(a=>a.addEventListener("click",e=>{const t=$(a.getAttribute("href"));if(t){e.preventDefault();lenis.scrollTo(t,{offset:-70});}}));

  const canvas=$("#gl"),S=initScene(canvas,{mobile});
  html.classList.add("gl");
  const sh=S.sheets.map(s=>s.st),hero=sh[0];
  const E=()=>S.extent();
  // progress ring
  const ring=$(".ring-fg"),L=2*Math.PI*26,lbl=$(".ring-label"),num=$(".ring-num");ring.style.strokeDasharray=L;
  const ch=[[0,"Intro"],[.16,"Beginner"],[.36,"Intermediate"],[.55,"Advanced"],[.68,"No jumps"],[.86,"The packs"]];
  let tlRef=null;const steps=$$(".levels-track li");
  function progress(p){const u=p*(tlRef?tlRef.duration():11.5),ai=u<4.1?0:u<6.1?1:2;steps.forEach((li,i)=>li.classList.toggle("on",i===ai));ring.style.strokeDashoffset=L*(1-p);let k=0;ch.forEach((c,i)=>{if(p>=c[0])k=i;});
    if(lbl.textContent!==ch[k][1]){lbl.textContent=ch[k][1];num.textContent=String(k+1).padStart(2,"0");}}
  // layout helpers (functions so they re-evaluate on resize)
  const fan=mobile
   ?[[0,-1.2,.25,-.12,0,0,.72],[-.34,-1.1,0,-.1,.12,.22,.62],[.34,-1.1,-.05,-.1,-.12,-.22,.62],[0,-1.02,-.3,0,0,.05,.58]]
   :[[1.02,-.08,.35,0,-.12,-.02,1.08],[.3,-.12,-.05,0,.22,.2,.98],[1.74,-.1,-.1,0,-.28,-.2,.98],[.66,.3,-.4,0,.12,.1,.9],[1.38,.32,-.45,0,-.1,-.1,.9]];
  sh.forEach((o,i)=>{const f=fan[i];Object.assign(o,{x:f[0],y:f[1],z:f[2],rx:f[3],ry:f[4],rz:f[5],s:f[6]});});
  const focus=mobile?{x:0,y:-.72,z:.3,s:.84}:{x:.92,y:-.02,z:.4,s:1.42};
  const center=mobile?{x:0,y:-.5,z:.1,s:.95}:{x:0,y:-.05,z:.2,s:1.12};
  // lineup slots: slot index -> sheet index
  const order=[3,1,0,2];
  const slot=j=>{const {hw,hh}=E();
    if(mobile){return {x:(j%2?1:-1)*hw*.47,y:j<2?.64:-.5,s:Math.min(.5,hw*.66)};}
    const sp=Math.min(hw*2/4.5,1.25);return {x:(j-1.5)*sp,y:-.02*hh,s:sp*.7/.85};};
  const tl=gsap.timeline({defaults:{ease:"power2.inOut"},scrollTrigger:{trigger:"#story",start:"top top",end:()=>"+="+innerHeight*(mobile?9:10.5),scrub:mobile?.6:1,
    pin:".stage",invalidateOnRefresh:true,onUpdate:st=>progress(st.progress),onToggle:st=>document.body.classList.toggle("story-on",st.isActive)}});document.body.classList.add("story-on");tlRef=tl;
  const panel=(sel,at,out)=>{tl.fromTo(sel,{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:.5,ease:"power2.out"},at);if(out!=null)tl.to(sel,{autoAlpha:0,y:-30,duration:.4,ease:"power2.in"},out);};
  // 1 → 2 hero out, others fall, hero to focus
  tl.to(".p-hero",{autoAlpha:0,y:-40,duration:.6},.9).to(".scroll-hint",{autoAlpha:0,duration:.3},.2);
  sh.slice(1).forEach((o,i)=>tl.to(o,{y:()=>-E().hh*2.1,x:o.x+(i%2?.4:-.4),rx:-.9,rz:(i%2?.6:-.6),duration:1.1,ease:"power2.in"},1+i*.05));
  tl.to(hero,{...focus,rx:0,ry:0,rz:0,duration:1.1},1).to(S,{float:.4,duration:1},1).to(S.cam,{z:4.6,duration:1.1},1);
  tl.fromTo(".levels-track",{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:.5},1.5).to(".levels-track",{autoAlpha:0,duration:.4},7.1);
  panel(".p-beginner",1.7,3.1);
  tl.to(hero,{ry:Math.PI,duration:1.1,ease:"power3.inOut"},3.1);tl.to(hero,{z:focus.z+.25,duration:.55,yoyo:true,repeat:1,ease:"sine.inOut"},3.1);
  panel(".p-intermediate",3.55,5.1);
  tl.to(hero,{ry:Math.PI*2,duration:1.1,ease:"power3.inOut"},5.1);tl.to(hero,{z:focus.z+.25,duration:.55,yoyo:true,repeat:1,ease:"sine.inOut"},5.1);
  panel(".p-advanced",5.55,7.1);
  // 3 big type
  tl.to(hero,{...center,ry:Math.PI*2-.25,rx:.06,duration:1},7.1).to(S.cam,{z:5.2,duration:1},7.1);
  tl.fromTo(".bigtype",{autoAlpha:0,scale:.55},{autoAlpha:1,scale:1,duration:1.4,ease:"power2.out"},7.2);
  panel(".p-jump",8.0,9.3);
  tl.to(".bigtype",{autoAlpha:0,scale:1.25,duration:.7,ease:"power2.in"},9.2);
  // 4 lineup
  order.forEach((si,j)=>{const o=sh[si];
    tl.fromTo(o,{y:si?()=>-E().hh*2.1:o.y},{x:()=>slot(j).x,y:()=>slot(j).y,z:0,s:()=>slot(j).s,rx:0,rz:0,ry:si===0?Math.PI*2:0,duration:1.2,ease:"power3.out",immediateRender:false},9.3+j*.08);});
  tl.to(S,{float:.25,duration:1},9.3);if(mobile)tl.to(".progress",{autoAlpha:0,duration:.3},9.3);
  tl.fromTo(".lineup",{autoAlpha:0},{autoAlpha:1,duration:.5},10.2);
  tl.to({},{duration:.8});
  // keep cards pinned under their sheets
  const packs=$$(".lineup .pack"),hdr=$("header.site");
  S.onFrame=()=>{if(+getComputedStyle($(".lineup")).opacity<.01)return;packs.forEach((p,j)=>{const q=S.project(order[j],-.55);p.style.transform=`translate(${q.x}px,${q.y+12}px) translateX(-50%)`;});};
  // hide canvas once story leaves view
  ST.create({trigger:"#after",start:"top 60%",onEnter:()=>{canvas.classList.add("off");S.pause(true);hdr.classList.add("solid")},onLeaveBack:()=>{canvas.classList.remove("off");S.pause(false);hdr.classList.remove("solid")}});
  requestAnimationFrame(()=>{canvas.classList.add("on");$(".poster").classList.add("gone");});
  progress(0);
}
