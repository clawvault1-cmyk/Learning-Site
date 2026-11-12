import {chromium} from "playwright";
const B="http://localhost:8080/index.html",O="/workspace/worksheets-site/shots/";
const browser=await chromium.launch({executablePath:"/usr/bin/google-chrome",args:["--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"]});
async function run(vp,mobile,points,prefix,video){
  const ctx=await browser.newContext({viewport:vp,deviceScaleFactor:mobile?2:1,isMobile:mobile,hasTouch:mobile,...(video?{recordVideo:{dir:"/tmp/vid",size:vp}}:{})});
  const p=await ctx.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));p.on("console",m=>{if(m.type()==="error")errs.push(m.text())});
  await p.goto(B,{waitUntil:"networkidle"});await p.waitForTimeout(2500);
  const range=await p.evaluate(()=>{const s=document.getElementById("story");const st=ScrollTrigger.getAll()[0];return st?{top:st.start,len:st.end-st.start}:{top:0,len:s.offsetHeight}});
  let n=1;
  for(const f of points){
    if(video){await p.evaluate(([y])=>window.__lenis?window.__lenis.scrollTo(y,{duration:2.2}):scrollTo(0,y),[range.top+range.len*f]);await p.waitForTimeout(2600);continue;}
    await p.evaluate(([y])=>{window.__lenis?window.__lenis.scrollTo(y,{immediate:true}):scrollTo(0,y)},[range.top+range.len*f]);
    await p.waitForTimeout(1800);
    await p.screenshot({path:`${O}${prefix}-${String(n++).padStart(2,"0")}.png`});
  }
  console.log(prefix,"errors:",errs.slice(0,5));await ctx.close();
}
const which=process.argv[2]||"all";
if(which==="all"||which==="desktop")await run({width:1440,height:900},false,[0,.15,.3,.45,.6,.75,.97,1.08],"v3-desktop");
if(which==="all"||which==="mobile")await run({width:390,height:844},true,[0,.3,.97],"v3-mobile");
if(which==="video")await run({width:1280,height:800},false,[.1,.25,.4,.55,.7,.85,.98],"v",true);
await browser.close();
