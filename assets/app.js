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
  const thumbs=[...g.querySelectorAll(".thumb")];
  if(!track)return;
  function go(i){track.scrollTo({left:i*track.clientWidth,behavior:"smooth"});}
  thumbs.forEach((b,i)=>b.addEventListener("click",()=>go(i)));
  track.addEventListener("scroll",()=>{
   const i=Math.round(track.scrollLeft/Math.max(track.clientWidth,1));
   thumbs.forEach((b,n)=>b.classList.toggle("on",n===i));
  },{passive:true});
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
 const picker=document.getElementById("pack-picker");
 if(picker){
  const qEl=document.getElementById("picker-q");
  const actions=document.getElementById("picker-actions");
  const result=document.getElementById("picker-result");
  const root=document.body.dataset.root||"";
  const steps=[
   {q:"Can your child count 5 things, like 5 pieces of cereal?",no:"beginner"},
   {q:"Can your child add 2 + 1 with a little help or none?",no:"beginner"},
   {q:"Is adding up to 10, like 4 + 3, easy for your child?",no:"intermediate",yes:"advanced"}
  ];
  const rec={
   beginner:{name:"Beginner: Adding within 5",why:"Your child will count two small groups and put them together."},
   intermediate:{name:"Intermediate: Adding within 10",why:"Your child will turn pictures into problems like 4 + 3."},
   advanced:{name:"Advanced: Story problems within 10",why:"Your child will solve short story problems you read out loud."}
  };
  let step=0;
  function show(){
   result.hidden=true;
   actions.hidden=false;
   qEl.textContent=steps[step].q;
   document.querySelectorAll("[data-pack]").forEach(el=>el.classList.remove("is-pick"));
  }
  function finish(key){
   const item=rec[key];
   actions.hidden=true;
   qEl.textContent="Start here:";
   result.hidden=false;
   result.innerHTML="<strong>"+item.name+"</strong>. "+item.why+' <a href="'+root+"products/k-addition-"+key+'.html">See this pack</a>. <button type="button" id="picker-reset">Start over</button>';
   document.querySelectorAll("[data-pack]").forEach(el=>el.classList.toggle("is-pick",el.dataset.pack===key));
   document.getElementById("picker-reset").addEventListener("click",()=>{step=0;show();});
  }
  actions.addEventListener("click",e=>{
   const b=e.target.closest("[data-answer]");if(!b)return;
   const cur=steps[step];
   if(b.dataset.answer==="no"){finish(cur.no);return;}
   if(cur.yes){finish(cur.yes);return;}
   step+=1;show();
  });
  show();
 }
 document.querySelectorAll('form[data-placeholder]').forEach(fm=>fm.addEventListener('submit',e=>{e.preventDefault();
  const m=fm.querySelector('.form-msg');m.hidden=false;}));
})();
