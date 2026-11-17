(function(){
 const S=window.SITE||{},C=window.CATALOG||[],R=document.body.dataset.root||"";
 const reduce=window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
 document.querySelectorAll('.brand-name').forEach(e=>e.textContent=S.brand);
 document.querySelectorAll('.site-email').forEach(e=>{e.textContent=S.email;e.href='mailto:'+S.email});
 document.querySelectorAll('.reply-time').forEach(e=>{if(S.replyTime)e.textContent=S.replyTime;});
 const t=document.querySelector('.nav-toggle'),n=document.querySelector('.nav-links');
 if(t&&n)t.addEventListener('click',()=>{const o=n.classList.toggle('open');t.setAttribute('aria-expanded',o);document.body.classList.toggle('menu-open',o)});
 if(n)n.addEventListener('click',e=>{if(e.target.closest('a')){n.classList.remove('open');document.body.classList.remove('menu-open');if(t)t.setAttribute('aria-expanded','false');}});
 document.querySelectorAll(".gallery").forEach(g=>{
  const track=g.querySelector(".slides");
  if(!track)return;
  const slides=[...track.children],thumbs=[...g.querySelectorAll(".thumb")],dots=[...g.querySelectorAll(".dot")],count=g.querySelector(".gal-count");
  const step=()=>{const w=slides[0]?slides[0].getBoundingClientRect().width:track.clientWidth;const gap=parseFloat(getComputedStyle(track).columnGap)||parseFloat(getComputedStyle(track).gap)||0;return Math.max(w+gap,1);};
  const mark=i=>{thumbs.forEach((b,n)=>b.classList.toggle("on",n===i));dots.forEach((b,n)=>b.classList.toggle("on",n===i));if(count)count.textContent=(i+1)+" / "+slides.length;};
  const go=i=>track.scrollTo({left:i*step(),behavior:reduce?"auto":"smooth"});
  thumbs.forEach((b,i)=>{if(!b.getAttribute("aria-label"))b.setAttribute("aria-label","Show image "+(i+1));b.addEventListener("click",()=>go(i));});
  dots.forEach((b,i)=>b.addEventListener("click",()=>go(i)));
  track.addEventListener("scroll",()=>mark(Math.round(track.scrollLeft/step())),{passive:true});
 });
 function payhipKey(raw){
  const v=String(raw||"").trim();
  if(!v)return "";
  if(/^https?:\/\//i.test(v)){
   try{
    const u=new URL(v);
    const q=u.searchParams.get("link");
    if(q)return q;
    const parts=u.pathname.split("/").filter(Boolean);
    if((parts[0]==="b"||parts[0]==="buy")&&parts[1])return parts[1];
   }catch(e){}
   return "";
  }
  return v;
 }
 function payhipHref(raw){
  const key=payhipKey(raw);
  return key?"https://payhip.com/buy?link="+encodeURIComponent(key):"";
 }
 function trackBuy(el,key){
  if(typeof fbq!=="function"||!key)return;
  fbq("trackCustom","BuyClick",{content_name:el.dataset.contentName||"",content_ids:[key],value:3.99,currency:"USD"});
 }
 const urls=S.checkoutUrls||{};
 const checkoutLive=Object.keys(urls).some(k=>payhipHref(urls[k]));
 const weeklyLive=!!payhipHref(S.subscriptionUrl||"");
 const anyLive=checkoutLive||weeklyLive;
 if(Array.isArray(C)){
  C.forEach(item=>{
   item.status=payhipHref(urls[item.id]||"")?"available":"coming-soon";
  });
 }
 document.querySelectorAll("[data-when-live]").forEach(el=>{el.hidden=!anyLive;});
 document.querySelectorAll("[data-when-soon]").forEach(el=>{el.hidden=anyLive;});
 const pixelOn=!!(S.metaPixelId&&/^\d{5,20}$/.test(String(S.metaPixelId)));
 document.querySelectorAll("[data-pixel-policy]").forEach(el=>{el.hidden=!pixelOn;});
 document.querySelectorAll("[data-pixel-off]").forEach(el=>{el.hidden=pixelOn;});
 function ensureStatus(el){
  let line=el.parentElement && el.parentElement.querySelector(":scope > .status-line");
  if(!line){
   line=document.createElement("p");
   line.className="status-line";
   el.insertAdjacentElement("afterend",line);
  }
  return line;
 }
 function armBuy(el,raw){
  const href=payhipHref(raw),key=payhipKey(raw);
  const line=ensureStatus(el);
  if(href){
   el.href=href;
   el.classList.remove("disabled");
   el.removeAttribute("aria-disabled");
   el.textContent=el.dataset.label||"Buy now";
   el.addEventListener("click",()=>trackBuy(el,key));
   if(line)line.hidden=true;
  }else{
   el.removeAttribute("href");
   el.classList.add("disabled");
   el.setAttribute("aria-disabled","true");
   el.textContent="Checkout opens soon";
   el.addEventListener("click",e=>e.preventDefault());
   if(line){
    line.hidden=false;
    line.textContent=S.availability||"Checkout opens soon. No payment is taken yet.";
   }
  }
 }
 const mainBuy=document.querySelector(".buybox .btn.buy"),bar=document.querySelector(".buybar");
 if(mainBuy&&bar)new IntersectionObserver(([e])=>{bar.hidden=e.isIntersecting;}).observe(mainBuy);
 document.querySelectorAll("[data-checkout].btn").forEach(el=>armBuy(el,urls[el.dataset.checkout]||""));
 document.querySelectorAll("[data-subscribe].btn").forEach(el=>armBuy(el,S.subscriptionUrl||""));
 document.querySelectorAll(".status-line").forEach(el=>{
  if(!el.textContent.trim()){
   if(!anyLive && S.availability) el.textContent=S.availability;
   else if(anyLive) el.hidden=true;
  }
 });
 document.querySelectorAll("[data-notify]").forEach(el=>{
  if(!S.email){el.hidden=true;return;}
  if(anyLive){el.hidden=true;return;}
  const subject=el.dataset.notifySubject||"Tell me when checkout opens";
  el.hidden=false;
  const a=el.querySelector("a")||el;
  if(a.tagName==="A") a.href="mailto:"+S.email+"?subject="+encodeURIComponent(subject);
 });
 document.querySelectorAll("[data-signin]").forEach(el=>{
  const url=String(S.storeSignInUrl||"").trim();
  const note=document.querySelector(".signin-note");
  const steps=document.querySelector("[data-signin-steps]");
  if(/^https?:\/\//i.test(url)){
   el.hidden=false;
   el.href=url;
   el.classList.remove("disabled");
   el.removeAttribute("aria-disabled");
   if(note)note.hidden=true;
   if(steps)steps.hidden=false;
  }else{
   el.hidden=true;
   el.removeAttribute("href");
   el.classList.add("disabled");
   el.setAttribute("aria-disabled","true");
   el.addEventListener("click",e=>e.preventDefault());
   if(note){note.hidden=false;note.textContent="Email us and we'll cancel for you.";}
   if(steps)steps.hidden=true;
  }
 });
 document.querySelectorAll("[data-email-cancel]").forEach(el=>{
  if(!S.email)return;
  el.href="mailto:"+S.email+"?subject="+encodeURIComponent("Cancel my Weekly Kindergarten Math Plan");
 });
 document.querySelectorAll("script[type='application/ld+json']").forEach(tag=>{
  try{
   const data=JSON.parse(tag.textContent);
   const offer=data && data.offers;
   if(!offer)return;
   const pageCheckout=document.querySelector("[data-checkout], [data-subscribe]");
   let live=false;
   if(pageCheckout && pageCheckout.hasAttribute("data-subscribe")) live=weeklyLive;
   else if(pageCheckout) live=!!payhipHref(urls[pageCheckout.dataset.checkout]||"");
   offer.availability=live?"https://schema.org/InStock":"https://schema.org/PreOrder";
   offer.priceCurrency=offer.priceCurrency||"USD";
   tag.textContent=JSON.stringify(data);
  }catch(e){}
 });
 if(pixelOn){
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
  fbq("init",String(S.metaPixelId));
  fbq("track","PageView");
  const view=document.querySelector("[data-pixel-view]");
  if(view){
   const raw=view.dataset.subscribe?S.subscriptionUrl:(urls[view.dataset.checkout]||"");
   const key=payhipKey(raw);
   const payload={content_name:view.dataset.contentName||view.dataset.subscribe||"",value:3.99,currency:"USD"};
   if(key)payload.content_ids=[key];
   fbq("track","ViewContent",payload);
  }
 }
 document.querySelectorAll('form[data-placeholder]').forEach(fm=>fm.addEventListener('submit',e=>{e.preventDefault();
  const m=fm.querySelector('.form-msg');if(m)m.hidden=false;}));
})();
