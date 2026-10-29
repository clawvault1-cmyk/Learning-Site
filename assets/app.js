(function(){
 const S=window.SITE||{},C=window.CATALOG||[],R=document.body.dataset.root||"";
 document.querySelectorAll('.brand-name').forEach(e=>e.textContent=S.brand);
 document.querySelectorAll('.status-line').forEach(e=>{if(S.availability)e.textContent=S.availability;});
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
  const go=i=>track.scrollTo({left:i*step(),behavior:"smooth"});
  thumbs.forEach((b,i)=>b.addEventListener("click",()=>go(i)));
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
 function armBuy(el,raw){
  const href=payhipHref(raw),key=payhipKey(raw);
  if(href){
   el.href=href;
   el.classList.remove("disabled");
   el.removeAttribute("aria-disabled");
   el.textContent=el.dataset.label||"Buy now";
   el.addEventListener("click",()=>trackBuy(el,key));
  }else{
   el.removeAttribute("href");
   el.classList.remove("disabled");
   el.setAttribute("aria-disabled","true");
   el.textContent="Checkout opens soon";
   el.addEventListener("click",e=>e.preventDefault());
  }
 }
 const mainBuy=document.querySelector(".buybox .btn.buy"),bar=document.querySelector(".buybar");
 if(mainBuy&&bar)new IntersectionObserver(([e])=>{bar.hidden=e.isIntersecting;}).observe(mainBuy);
 const urls=S.checkoutUrls||{};
 document.querySelectorAll("[data-checkout].btn").forEach(el=>armBuy(el,urls[el.dataset.checkout]||""));
 document.querySelectorAll("[data-subscribe].btn").forEach(el=>armBuy(el,S.subscriptionUrl||""));
 document.querySelectorAll("[data-signin]").forEach(el=>{
  const url=String(S.storeSignInUrl||"").trim();
  const note=document.querySelector(".signin-note");
  if(/^https?:\/\//i.test(url)){
   el.href=url;
   el.classList.remove("disabled");
   el.removeAttribute("aria-disabled");
   if(note)note.hidden=true;
  }else{
   el.removeAttribute("href");
   el.classList.add("disabled");
   el.setAttribute("aria-disabled","true");
   el.addEventListener("click",e=>e.preventDefault());
   if(note){note.hidden=false;note.textContent="Email us and we'll cancel for you.";}
  }
 });
 document.querySelectorAll("[data-email-cancel]").forEach(el=>{
  if(!S.email)return;
  el.href="mailto:"+S.email+"?subject="+encodeURIComponent("Cancel my Weekly Kindergarten Math Plan");
 });
 if(S.metaPixelId&&/^\d{5,20}$/.test(String(S.metaPixelId))){
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
  const m=fm.querySelector('.form-msg');m.hidden=false;}));
})();
