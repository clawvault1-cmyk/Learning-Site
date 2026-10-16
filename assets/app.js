(function(){
 const S=window.SITE||{},C=window.CATALOG||[],R=document.body.dataset.root||"";
 document.querySelectorAll('.brand-name').forEach(e=>e.textContent=S.brand);
 document.querySelectorAll('.site-email').forEach(e=>{e.textContent=S.email;e.href='mailto:'+S.email});
 const t=document.querySelector('.nav-toggle'),n=document.querySelector('.nav-links');
 if(t)t.addEventListener('click',()=>{const o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});
 // checkout buttons: never fake a purchase
 document.querySelectorAll('[data-checkout]').forEach(b=>{
  if(S.checkoutUrl){b.href=S.checkoutUrl+(S.checkoutUrl.includes('?')?'&':'?')+'product='+b.dataset.checkout;b.textContent=b.dataset.label||'Buy now';}
  else{b.removeAttribute('href');b.classList.add('disabled');b.setAttribute('aria-disabled','true');b.textContent='Checkout coming soon';
   b.addEventListener('click',e=>{e.preventDefault();const m=b.parentElement.querySelector('.checkout-note');if(m)m.hidden=false;});}
 });
 // grade → subject → skill → pack. Nothing is preselected.
 const chooser=document.getElementById('chooser');
 if(chooser){
  const stage=document.getElementById('chooser-stage');
  const path=document.getElementById('chooser-path');
  const back=document.getElementById('chooser-back');
  const GRADES=["Pre-K","Kindergarten","1st Grade","2nd Grade"];
  const gradeNote={
   "Pre-K":"Early counting and letters are on the way.",
   "Kindergarten":"Addition packs are ready. Other skills are on the way.",
   "1st Grade":"Math and reading packs are on the way.",
   "2nd Grade":"Math and reading packs are on the way."
  };
  const skillNote={
   "Addition":"Putting groups together.",
   "Subtraction":"Taking some away.",
   "Counting & Number Recognition":"Counting objects and reading numbers.",
   "Counting & Early Math":"Counting and early number ideas.",
   "Addition & Subtraction":"Putting together and taking away.",
   "Place Value":"Tens and ones.",
   "CVC Words":"Simple words like cat, map, and sit.",
   "Sight Words":"Common words, connected to their sounds and spellings.",
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
   path.textContent=bits.length?bits.join(" · "):"Pick a grade to begin. Nothing is selected yet.";
   back.hidden=!state.grade;
   back.textContent=state.skill?"Change skill":state.subject?"Change subject":"Change grade";
   if(!state.grade){stage.innerHTML='<div class="choice-grid grades">'+GRADES.map(g=>'<button type="button" class="choice" data-grade="'+esc(g)+'"><strong>'+esc(g)+'</strong><span>'+esc(gradeNote[g])+'</span></button>').join('')+'</div>';return;}
   if(!state.subject){
    stage.innerHTML='<p class="chooser-lead">You chose <strong>'+esc(state.grade)+'</strong>. Math or reading?</p><div class="choice-grid subjects"><button type="button" class="choice" data-subject="Math"><strong>Math</strong><span>Numbers, counting, and operations.</span></button><button type="button" class="choice" data-subject="Reading"><strong>Reading</strong><span>Sounds, letters, and words.</span></button></div>';
    return;
   }
   if(!state.skill){
    const read=state.subject==="Reading"?'<p class="chooser-note">Reading packs are not ready yet. They will connect sounds and letters. Children blend those sounds to read and spell the patterns they have been taught. CVC words are simple words like cat, map, and sit. Sight words will connect sounds and spellings, including any part that does not follow the pattern. They are not only a list to memorize.</p>':'';
    const list=skills();
    stage.innerHTML=read+'<p class="chooser-lead"><strong>'+esc(state.grade)+' · '+esc(state.subject)+'</strong>. Choose a skill.</p><div class="choice-grid skills">'+list.map(sk=>'<button type="button" class="choice" data-skill="'+esc(sk)+'"><strong>'+esc(sk)+'</strong><span>'+esc(skillNote[sk]||"")+'</span></button>').join('')+'</div>';
    return;
   }
   const found=items();
   const av=found.filter(p=>p.status==="available");
   if(av.length){
    stage.innerHTML='<p class="chooser-lead"><strong>'+esc(state.grade)+' · '+esc(state.subject)+' · '+esc(state.skill)+'</strong> is ready to view.</p><ul class="f-list">'+av.map(p=>'<li><a href="'+R+p.url+'"><span><strong>'+esc(p.short||p.title)+'</strong><small>'+esc(p.summary)+'</small></span><span>$'+p.price.toFixed(2)+'</span></a></li>').join('')+'</ul>';
   }else{
    stage.innerHTML='<div class="soon-card"><span class="badge soon">Coming soon</span><h3>'+esc(state.grade)+' · '+esc(state.subject)+' · '+esc(state.skill)+'</h3><p>This pack is not ready yet. We will not ask you to buy it. You can print a free kindergarten addition sample while you wait.</p><a class="btn" href="'+R+'free-printables.html">Get the free sample</a></div>';
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
  if(window.__lenis)window.__lenis.scrollTo(el,{offset:-84,immediate:!!immediate});
  else el.scrollIntoView({behavior:immediate?'auto':'smooth',block:'start'});
 }
 document.querySelectorAll('a[href="#grades"],a[href="#sequence"],a[href="#packs"],a[href="#questions"],a[href$="index.html#grades"]').forEach(a=>{
  a.addEventListener('click',e=>{
   const href=a.getAttribute('href');
   const id=href.includes('#')?href.slice(href.indexOf('#')):'';
   const same=href.startsWith('#')||(onHome&&href.endsWith('#grades'));
   if(!same||!document.querySelector(id))return;
   e.preventDefault();e.stopImmediatePropagation();
   jumpTo(id,true);
  },true);
 });
 if(onHome&&/^#(grades|sequence|packs|questions)$/.test(location.hash)){
  let tries=0;const timer=setInterval(()=>{
   tries++;
   if(window.__lenis||document.documentElement.classList.contains('rm')||tries>25){
    jumpTo(location.hash,true);clearInterval(timer);
   }
  },200);
 }
 document.querySelectorAll('form[data-placeholder]').forEach(fm=>fm.addEventListener('submit',e=>{e.preventDefault();
  const m=fm.querySelector('.form-msg');m.hidden=false;}));
 // The grade chooser is the action. Don't cover its cards with the same button.
 const sticky=document.querySelector('.sticky-cta'),grades=document.getElementById('grades');
 if(sticky&&grades&&'IntersectionObserver' in window){
  new IntersectionObserver(([e])=>{sticky.classList.toggle('is-hidden',e.isIntersecting);},{threshold:0.2}).observe(grades);
 }
})();
