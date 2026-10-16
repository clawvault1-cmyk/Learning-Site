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
 // finder
 const f=document.getElementById('finder');
 if(f){const g=f.querySelector('#f-grade'),s=f.querySelector('#f-subject'),k=f.querySelector('#f-skill'),out=f.querySelector('#f-result');
  const uniq=a=>[...new Set(a)];
  function fill(){const sk=uniq(C.filter(p=>p.grade===g.value&&p.subject===s.value).map(p=>p.skill));
   k.innerHTML=sk.length?sk.map(x=>`<option>${x}</option>`).join(''):'<option value="">More skills coming soon</option>';show();}
  function show(){const m=C.filter(p=>p.grade===g.value&&p.subject===s.value&&p.skill===k.value);
   const av=m.filter(p=>p.status==='available');
   if(av.length){out.innerHTML='<p class="f-ok">Available now:</p><ul class="f-list">'+av.map(p=>`<li><a href="${R+p.url}"><strong>${p.title.split(': ').pop()}</strong> <span>$${p.price.toFixed(2)}</span></a></li>`).join('')+'</ul>';}
   else{out.innerHTML=`<p class="f-soon"><span class="badge soon">Coming soon</span> ${g.value} ${s.value}${k.value?' · '+k.value:''} is in development. <a href="${R}free-printables.html">Get the free sample</a> and we'll tell you when new levels launch.</p>`;}}
  g.onchange=fill;s.onchange=fill;k.onchange=show;fill();}
 // free form (no backend yet)
 document.querySelectorAll('form[data-placeholder]').forEach(fm=>fm.addEventListener('submit',e=>{e.preventDefault();
  const m=fm.querySelector('.form-msg');m.hidden=false;}));
})();
