(function(){
 const S=window.SITE||{},C=window.CATALOG||[],R=document.body.dataset.root||"";
 document.querySelectorAll('.brand-name').forEach(e=>e.textContent=S.brand);
 document.querySelectorAll('.status-line').forEach(e=>{if(S.availability)e.textContent=S.availability;});
 document.querySelectorAll('.site-email').forEach(e=>{e.textContent=S.email;e.href='mailto:'+S.email});
 document.querySelectorAll('.reply-time').forEach(e=>{if(S.replyTime)e.textContent=S.replyTime;});
 const t=document.querySelector('.nav-toggle'),n=document.querySelector('.nav-links');
 if(t&&n)t.addEventListener('click',()=>{const o=n.classList.toggle('open');t.setAttribute('aria-expanded',o);t.textContent=o?'Close':'Menu';document.body.classList.toggle('menu-open',o)});
 if(n)n.addEventListener('click',e=>{if(e.target.closest('a')){n.classList.remove('open');document.body.classList.remove('menu-open');if(t){t.setAttribute('aria-expanded','false');t.textContent='Menu';}}});
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
   el.classList.add("disabled");
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
   if(note){note.hidden=false;note.textContent="The sign-in link will appear here when the store account is connected. Email us and we will cancel for you.";}
  }
 });
 document.querySelectorAll("[data-email-cancel]").forEach(el=>{
  if(!S.email)return;
  el.href="mailto:"+S.email+"?subject="+encodeURIComponent("Cancel my Weekly Packet Plan");
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
 // grade → subject → skill → pack. Nothing is preselected.
 const chooser=document.getElementById('chooser');
 if(chooser){
  const stage=document.getElementById('chooser-stage');
  const path=document.getElementById('chooser-path');
  const back=document.getElementById('chooser-back');
  const GRADES=[{id:"Kindergarten",label:"Kindergarten"},{id:"Pre-K",label:"Preschool"},{id:"1st Grade",label:"1st Grade"},{id:"2nd Grade",label:"2nd Grade"}];
  const gradeNote={
   "Pre-K":"Coming soon.",
   "Kindergarten":"Math is ready now.",
   "1st Grade":"Coming soon.",
   "2nd Grade":"Coming soon."
  };
  const skillNote={
   "Addition":"Putting groups together.",
   "Subtraction":"Taking some away.",
   "Counting & Number Recognition":"Counting objects and reading numbers.",
   "Counting & Early Math":"Counting and early number ideas.",
   "Addition & Subtraction":"Putting together and taking away.",
   "Place Value":"Tens and ones.",
   "CVC Words":"Simple words like cat, map, and sit.",
   "Sight Words":"Words a reader recognizes automatically, instantly.",
   "Letter Recognition & Phonics":"Letter names and the sounds they stand for.",
   "Letter Recognition":"Letters and the sounds they stand for.",
   "Phonics & Spelling":"Sounds, letters, and spelling patterns.",
   "Reading Comprehension":"Understanding what a passage says."
  };
  const state={grade:"",subject:"",skill:""};
  const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  function items(){return C.filter(p=>p.grade===state.grade&&(!state.subject||p.subject===state.subject)&&(!state.skill||p.skill===state.skill));}
  function skills(){const seen=[];items().forEach(p=>{if(!seen.includes(p.skill))seen.push(p.skill);});return seen;}
  function render(){
   const bits=[state.grade,state.subject,state.skill].filter(Boolean);
   const label=v=>v==="Pre-K"?"Preschool":v;
   path.textContent=bits.length?bits.map(label).join(" · "):"Pick a grade to begin. Nothing is selected yet.";
   back.hidden=!state.grade;
   back.textContent=state.skill?"Change skill":state.subject?"Change subject":"Change grade";
   if(!state.grade){stage.innerHTML='<div class="choice-grid grades">'+GRADES.map(g=>'<button type="button" class="choice'+(g.id==="Kindergarten"?" choice-ready":"")+'" data-grade="'+esc(g.id)+'"><strong>'+esc(g.label)+'</strong><span>'+esc(gradeNote[g.id])+'</span></button>').join('')+'</div>';return;}
   if(!state.subject){
    const mathNote=state.grade==="Kindergarten"?"Ready now.":"Coming soon.";
    stage.innerHTML='<p class="chooser-lead">You chose <strong>'+esc(state.grade==="Pre-K"?"Preschool":state.grade)+'</strong>. Math or reading?</p><div class="choice-grid subjects"><button type="button" class="choice'+(state.grade==="Kindergarten"?" choice-ready":"")+'" data-subject="Math"><strong>Math</strong><span>'+esc(mathNote)+'</span></button><button type="button" class="choice" data-subject="Reading"><strong>Reading</strong><span>Coming soon.</span></button></div>';
    return;
   }
   if(!state.skill){
    const read=state.subject==="Reading"?'<p class="chooser-note">Reading packs are coming soon. CVC words are simple words like cat, map, and sit. A high-frequency word shows up often, like the or and. A sight word is one a reader knows right away. They are not the same.</p>':'';
    const list=skills();
    stage.innerHTML=read+'<p class="chooser-lead"><strong>'+esc(state.grade)+' · '+esc(state.subject)+'</strong>. Choose a skill.</p><div class="choice-grid skills">'+list.map(sk=>'<button type="button" class="choice" data-skill="'+esc(sk)+'"><strong>'+esc(sk)+'</strong><span>'+esc(skillNote[sk]||"")+'</span></button>').join('')+'</div>';
    return;
   }
   const found=items();
   const av=found.filter(p=>p.status==="available");
   if(av.length){
    stage.innerHTML='<p class="chooser-lead"><strong>'+esc(state.grade)+' · '+esc(state.subject)+' · '+esc(state.skill)+'</strong> is ready to view.</p><ul class="f-list">'+av.map(p=>'<li><a href="'+R+p.url+'"><span><strong>'+esc(p.short||p.title)+'</strong><small>'+esc(p.summary)+'</small></span><span>$'+p.price.toFixed(2)+'</span></a></li>').join('')+'</ul>';
   }else{
    const shown=state.grade==="Pre-K"?"Preschool":state.grade;
    stage.innerHTML='<div class="soon-card"><span class="badge soon">Coming soon</span><h3>'+esc(shown)+' · '+esc(state.subject)+' · '+esc(state.skill)+'</h3><p>Coming soon. The weekly plan is where new packets will show up.</p><a class="btn" href="'+R+'weekly.html">See the weekly plan</a></div>';
   }
  }
  stage.addEventListener('click',e=>{
   const b=e.target.closest('button');if(!b)return;
   if(b.dataset.grade){state.grade=b.dataset.grade;state.subject="";state.skill="";}
   if(b.dataset.subject){state.subject=b.dataset.subject;state.skill="";}
   if(b.dataset.skill){state.skill=b.dataset.skill;}
   render();
  });
  back.addEventListener('click',()=>{
   if(state.skill)state.skill="";
   else if(state.subject)state.subject="";
   else state.grade="";
   render();
  });
  render();
 }
 // Jump in-page goals without scrubbing the whole story. Manual scrolling still plays it.
 const onHome=/\/(?:index\.html)?$/.test(location.pathname);
 function jumpTo(id,immediate){
  const el=document.querySelector(id);if(!el)return;
  if(window.__lenis)window.__lenis.scrollTo(el,{offset:-104,immediate:!!immediate});
  else el.scrollIntoView({behavior:immediate?'auto':'smooth',block:'start'});
 }
 document.querySelectorAll('a[href*="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
   const href=a.getAttribute('href');
   if(!href||href.indexOf('#')<0)return;
   const id=href.slice(href.indexOf('#'));
   const same=href.startsWith('#')||(onHome&&/index\.html#/.test(href));
   if(!same||!document.querySelector(id))return;
   e.preventDefault();e.stopImmediatePropagation();
   jumpTo(id,true);
  },true);
 });
 if(onHome&&/^#(grades|price|pages|benefits|familiar|works|questions)$/.test(location.hash)){
  const ready=()=>window.__lenis||document.documentElement.classList.contains('rm')||document.documentElement.classList.contains('phone');
  if(ready())jumpTo(location.hash,true);
  else {let tries=0;const timer=setInterval(()=>{tries++;if(ready()||tries>25){jumpTo(location.hash,true);clearInterval(timer);}},200);}
 }
 document.querySelectorAll('form[data-placeholder]').forEach(fm=>fm.addEventListener('submit',e=>{e.preventDefault();
  const m=fm.querySelector('.form-msg');m.hidden=false;}));
 // The grade chooser is the action. Don't cover its cards with the same button.
 const sticky=document.querySelector('.sticky-cta'),grades=document.getElementById('grades');
 if(sticky&&grades&&'IntersectionObserver' in window){
  new IntersectionObserver(([e])=>{sticky.classList.toggle('is-hidden',e.isIntersecting);},{threshold:0.2}).observe(grades);
 }
 const buybar=document.getElementById('buybar'),packs=document.getElementById('packs');
 if(buybar&&packs&&'IntersectionObserver' in window){
  new IntersectionObserver(([e])=>{buybar.classList.toggle('is-hidden',e.isIntersecting);},{threshold:0.15}).observe(packs);
 }
})();
