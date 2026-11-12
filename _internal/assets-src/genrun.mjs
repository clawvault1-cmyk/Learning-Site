import {chromium} from "playwright";import fs from "fs";
const b=await chromium.launch({executablePath:"/usr/bin/google-chrome"});const p=await b.newPage();
await p.goto("http://localhost:8080/_gen.html",{waitUntil:"networkidle"});const o=await p.evaluate(()=>window.gen());
for(const [k,v] of Object.entries(o))fs.writeFileSync(`/workspace/worksheets-site/assets/img/sheet-${k}.png`,Buffer.from(v.split(",")[1],"base64"));await b.close();
