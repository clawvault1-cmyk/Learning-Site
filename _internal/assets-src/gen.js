import {drawSheet} from "/workspace/worksheets-site/assets/src/textures.js";
window.gen=async()=>{await document.fonts.load("600 40px Fraunces");await document.fonts.load("500 20px Inter");await document.fonts.ready;
 const o={};for(const k of ["beginner","intermediate","advanced","bundle"])o[k]=drawSheet(k,1100).toDataURL("image/png");return o;};
