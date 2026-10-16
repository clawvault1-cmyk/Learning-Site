import {WebGLRenderer,Scene,PerspectiveCamera,PlaneGeometry,Mesh,MeshStandardMaterial,ShadowMaterial,Group,CanvasTexture,
 HemisphereLight,DirectionalLight,PointLight,SRGBColorSpace,NeutralToneMapping,RepeatWrapping,Vector3,FrontSide,BackSide,DoubleSide,MeshBasicMaterial} from "three";
import {drawSheet,paperBump,blurShadow} from "./textures.js";

export function initScene(canvas,{mobile}){
  const dpr=Math.min(window.devicePixelRatio||1,mobile?1.5:2);
  const r=new WebGLRenderer({canvas,antialias:!mobile||dpr<1.5,alpha:true,powerPreference:"high-performance"});
  r.setPixelRatio(dpr);r.outputColorSpace=SRGBColorSpace;r.toneMapping=NeutralToneMapping;r.toneMappingExposure=1.18;
  
  const scene=new Scene(),cam=new PerspectiveCamera(35,1,0.1,50);cam.position.set(0,0,5.2);
  scene.add(new HemisphereLight(0xfffaf0,0x9fb0bd,1.55));
  const key=new DirectionalLight(0xfffaf2,2.1);key.position.set(1.4,2.2,6);scene.add(key);
  const teal=new PointLight(0x247f78,3.2,9,1.6);teal.position.set(-3,-1.4,2.4);scene.add(teal);
  const peach=new PointLight(0xf6c9a8,2.2,9,1.6);peach.position.set(3,1.8,2.2);scene.add(peach);


  const W=0.85,H=1.1,seg=mobile?[14,18]:[24,32];
  function curled(){const g=new PlaneGeometry(W,H,...seg),p=g.attributes.position;
    for(let i=0;i<p.count;i++){const x=p.getX(i)/W*2,y=p.getY(i)/H*2;
      let z=0.035*x*x - 0.02*y*y + 0.06*Math.pow(Math.max(0,(x+y)/2),3)+0.012*Math.sin(y*2.4);p.setZ(i,z);}
    g.computeVertexNormals();return g;}
  const geo=curled(),tw=mobile?768:1280;
  const tex=k=>{const t=new CanvasTexture(drawSheet(k,tw));t.colorSpace=SRGBColorSpace;t.anisotropy=r.capabilities.getMaxAnisotropy();return t;};
  const T={beginner:tex("beginner"),intermediate:tex("intermediate"),advanced:tex("advanced"),bundle:tex("bundle")};
  const blank=(()=>{const c=document.createElement("canvas");c.width=c.height=64;const x=c.getContext("2d");x.fillStyle="#f6f2ea";x.fillRect(0,0,64,64);const t=new CanvasTexture(c);t.colorSpace=SRGBColorSpace;return t;})();
  const backOf=t=>{const b=t.clone();b.wrapS=RepeatWrapping;b.repeat.x=-1;b.needsUpdate=true;return b;};
  const bump=new CanvasTexture(paperBump(mobile?384:640));
  const mat=(map,side)=>new MeshStandardMaterial({map,side,roughness:0.86,metalness:0,color:0xffffff,bumpMap:bump,bumpScale:mobile?0.6:0.9});
  const edgeMat=new MeshStandardMaterial({color:0xe2dacb,roughness:.95,side:DoubleSide});
  const shTex=new CanvasTexture(blurShadow(256)),shGeo=new PlaneGeometry(W*1.45,H*1.4);
  // sheet 0 = hero (front Beginner→Advanced, back Intermediate)
  const defs=[["beginner","int"],["intermediate"],["bundle"],["beginner"],["advanced"]].slice(0,mobile?4:5);
  const sheets=defs.map(([k,back])=>{const g=new Group();
    const f=new Mesh(geo,mat(T[k],FrontSide)),b=new Mesh(geo,mat(back?backOf(T.intermediate):blank,BackSide));
    const e=new Mesh(geo,edgeMat);e.position.z=-0.007;e.scale.set(1.007,1.006,1);b.position.z=-0.013;
    g.add(f,e,b);scene.add(g);
    const shm=new Mesh(shGeo,new MeshBasicMaterial({map:shTex,transparent:true,opacity:.3,depthWrite:false}));shm.renderOrder=-1;scene.add(shm);
    return {g,f,b,shm,st:{x:0,y:0,z:0,rx:0,ry:0,rz:0,s:1}};});
  const hero=sheets[0],heroFrontAdv=T.advanced,heroFrontBeg=T.beginner;
  const camSt={z:5.2,x:0,y:0},mouse={x:0,y:0,tx:0,ty:0};
  addEventListener("pointermove",e=>{mouse.tx=(e.clientX/innerWidth-.5);mouse.ty=(e.clientY/innerHeight-.5);},{passive:true});
  let w=1,h=1;
  function resize(){w=canvas.clientWidth||innerWidth;h=canvas.clientHeight||innerHeight;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix();}
  resize();addEventListener("resize",resize);
  const v=new Vector3();let t0=performance.now(),running=true;
  function frame(now){if(!running)return;requestAnimationFrame(frame);const t=(now-t0)/1000;
    mouse.x+=(mouse.tx-mouse.x)*.05;mouse.y+=(mouse.ty-mouse.y)*.05;
    cam.position.set(camSt.x+mouse.x*.25,camSt.y-mouse.y*.18,camSt.z);cam.lookAt(camSt.x*.6,camSt.y*.6,0);
    sheets.forEach((s,i)=>{const o=s.st,fl=api.float;
      s.g.position.set(o.x,o.y+Math.sin(t*.8+i*1.7)*.025*fl,o.z);
      s.g.rotation.set(o.rx+Math.sin(t*.6+i)*.03*fl,o.ry+Math.cos(t*.5+i*2)*.04*fl,o.rz);s.g.scale.setScalar(o.s);
      const d=Math.max(.05,o.z+.75),sm=s.shm;sm.position.set(s.g.position.x+d*.07,s.g.position.y-d*.11,-0.75+i*.001);sm.rotation.z=o.rz;
      sm.scale.set(o.s*(1+d*.12)*Math.max(.12,Math.abs(Math.cos(s.g.rotation.y))),o.s*(1+d*.12)*Math.max(.3,Math.abs(Math.cos(s.g.rotation.x))),1);
      sm.material.opacity=.36/(1+d*1.1);});
    // swap hero front face while it is hidden (edge-on or back showing)
    const want=hero.st.ry>Math.PI?heroFrontAdv:heroFrontBeg;
    if(hero.f.material.map!==want){hero.f.material.map=want;hero.f.material.needsUpdate=true;}
    r.render(scene,cam);api.onFrame&&api.onFrame();}
  requestAnimationFrame(frame);
  const api={sheets,cam:camSt,float:1,onFrame:null,mobile,
    // visible half-extents at z=0 for layout maths
    extent(){const hh=Math.tan(cam.fov*Math.PI/360)*camSt.z;return {hw:hh*cam.aspect,hh};},
    project(i,dy){const s=sheets[i];v.set(s.g.position.x,s.g.position.y+dy*s.g.scale.y,s.g.position.z).project(cam);return {x:(v.x+1)/2*w,y:(1-v.y)/2*h};},
    pause(p){if(p&&running){running=false;}else if(!p&&!running){running=true;requestAnimationFrame(frame);}}};
  return api;
}
