import { chromium } from 'playwright';
const [,, outDir, ...paths] = process.argv;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const errors = [];
for (const [label, vp] of [['d', { width: 1440, height: 900 }], ['m', { width: 390, height: 844 }]]) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1 });
  for (const p of paths) {
    const pg = await ctx.newPage();
    pg.on('console', m => { if (m.type() === 'error') errors.push(`${p} ${label}: ${m.text()}`); });
    pg.on('pageerror', e => errors.push(`${p} ${label}: ${e.message}`));
    pg.on('requestfailed', r => errors.push(`${p} ${label}: failed ${r.url()}`));
    await pg.goto('http://127.0.0.1:8099' + p, { waitUntil: 'networkidle' });
    await pg.addStyleTag({ content: '.reveal{opacity:1!important;transform:none!important}' });
    const name = (p === '/' ? 'home' : p.replace(/\//g, '_').replace(/^_|_$/g, '')) + '-' + label;
    await pg.screenshot({ path: `${outDir}/${name}.png`, fullPage: true });
    const ov = await pg.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    if (ov) errors.push(`${p} ${label}: horizontaler Overflow`);
    await pg.close();
  }
  await ctx.close();
}
await b.close();
console.log(errors.length ? errors.join('\n') : 'keine Fehler');
