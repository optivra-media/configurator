// Erzeugt OG-Bild (1200x630), Apple-Touch-Icon und PWA-Icons mit Chromium (Playwright).
// Aufruf: node tools/make-icons.mjs   (benötigt Playwright + Chromium)
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../public_html');
const fonts = path.join(root, 'assets/fonts');
const out = path.join(root, 'assets/img');
const name = process.env.SITE_NAME || 'Mika Reiner';
const mark = process.env.SITE_MARK || 'MR';
const face = `
@font-face{font-family:A;src:url(file://${fonts}/archivo-var.woff2);font-weight:100 900}
@font-face{font-family:S;src:url(file://${fonts}/instrument-serif-latin-400-italic.woff2);font-style:italic}`;

const og = `<html><style>${face}
*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;display:flex;font-family:A;overflow:hidden;background:#0c0c0d;color:#efeee9;position:relative}
.l{flex:1;padding:56px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.r{flex:1;background:#efeadf;color:#141414;padding:56px;display:flex;flex-direction:column;justify-content:space-between;position:relative}
.big{font-size:230px;font-weight:900;letter-spacing:-.07em;line-height:.8;text-transform:uppercase}
.tag{font:500 15px ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;opacity:.75}
.disc{position:absolute;width:560px;height:560px;border-radius:50%;right:-180px;top:-120px;background:repeating-radial-gradient(circle,rgba(255,255,255,.14) 0 1px,transparent 1px 7px),radial-gradient(circle,#c9f31d 0 9%,#15150f 9.4%);-webkit-mask-image:radial-gradient(circle,#000 0 55%,transparent 72%)}
.brk i{position:absolute;width:34px;height:34px;border:3px solid #141414;opacity:.55}
.brk i:nth-child(1){left:40px;top:40px;border-right:0;border-bottom:0}.brk i:nth-child(2){right:40px;top:40px;border-left:0;border-bottom:0}
.brk i:nth-child(3){left:40px;bottom:40px;border-right:0;border-top:0}.brk i:nth-child(4){right:40px;bottom:40px;border-left:0;border-top:0}
.rec{font:500 15px ui-monospace,monospace;letter-spacing:.14em;display:flex;gap:10px;align-items:center}.rec:before{content:"";width:12px;height:12px;border-radius:50%;background:#ff4a2b}
.ft{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:22px 56px;background:#c9f31d;color:#0c0c0d;font-weight:800;font-size:26px;letter-spacing:-.02em;z-index:3}
.ft em{font-family:S;font-weight:400;font-size:30px}
</style><body>
<div class="l"><div class="disc"></div><span class="tag">01 — Hochzeit · Event · Party</span><div class="big">DJ</div></div>
<div class="r"><div class="brk"><i></i><i></i><i></i><i></i></div><span class="rec">REC</span><div class="big">Film</div></div>
<div class="ft"><span>${name}</span><span><em>DJ &amp; Videograf</em> aus Köln</span></div></body></html>`;

const icon = (size, radius) => `<html><style>${face}*{margin:0}body{width:${size}px;height:${size}px;background:#0c0c0d;display:grid;place-items:center}
.b{width:${size * .76}px;height:${size * .76}px;background:#c9f31d;display:grid;place-items:center;border-radius:${radius}px;color:#0c0c0d;font:900 ${size * .4}px A;letter-spacing:-.06em;padding-top:${size * .02}px}</style>
<body><div class="b">${mark}</div></body></html>`;

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
async function shot(html, w, h, file) {
  const p = await browser.newPage({ viewport: { width: w, height: h } });
  await p.setContent(html, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(out, file) });
  await p.close();
}
fs.mkdirSync(out, { recursive: true });
await shot(og, 1200, 630, 'og-image.png');
await shot(icon(512, 0), 512, 512, 'icon-512.png');
await shot(icon(192, 0), 192, 192, 'icon-192.png');
await shot(icon(180, 0), 180, 180, path.join('..', '..', 'apple-touch-icon.png'));
await shot(icon(48, 0), 48, 48, path.join('..', '..', 'favicon.png'));
await browser.close();
// favicon.ico = PNG im ICO-Container (von allen modernen Browsern akzeptiert)
const png = fs.readFileSync(path.join(root, 'favicon.png'));
const hdr = Buffer.alloc(22);
hdr.writeUInt16LE(0, 0); hdr.writeUInt16LE(1, 2); hdr.writeUInt16LE(1, 4);
hdr[6] = 48; hdr[7] = 48; hdr.writeUInt16LE(1, 10); hdr.writeUInt16LE(32, 12);
hdr.writeUInt32LE(png.length, 14); hdr.writeUInt32LE(22, 18);
fs.writeFileSync(path.join(root, 'favicon.ico'), Buffer.concat([hdr, png]));
fs.unlinkSync(path.join(root, 'favicon.png'));
console.log('Icons erzeugt.');
