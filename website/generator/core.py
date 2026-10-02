"""Gemeinsame Konfiguration, Layout und SEO-Helfer für den statischen Seitenbau."""
import hashlib
import html
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public_html")

# --------------------------------------------------------------------------
# ZENTRALE DATEN — hier einmal anpassen, dann `python3 build.py` ausführen.
# --------------------------------------------------------------------------
SITE = {
    "name": "Mika Reiner",
    "mark": "MR",
    "claim": "DJ & Videograf",
    "domain": "https://www.deine-domain.de",   # ohne Slash am Ende
    "email": "hallo@deine-domain.de",
    "phone": "+49 221 000 000 00",
    "phone_href": "+4922100000000",
    "city": "Köln",
    "region": "Nordrhein-Westfalen",
    "country": "DE",
    "zip": "50667",
    "street": "Musterstraße 1",
    "radius": ["Köln", "Düsseldorf", "Bonn", "Leverkusen", "Aachen", "Dortmund", "Essen", "Ruhrgebiet"],
    "instagram": "",     # z. B. https://www.instagram.com/deinname
    "youtube": "",       # Kanal-URL
    "soundcloud": "",    # Profil-URL
    "mixcloud": "",
    "geo": (50.9375, 6.9603),
    "published": "2026-10-02",
}
TODAY = date.today().isoformat()


def esc(s):
    return html.escape(str(s), quote=True)


def url(path):
    return SITE["domain"] + path


# --------------------------------------------------------------------------
# Kleine Bausteine
# --------------------------------------------------------------------------
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" aria-hidden="true"><path d="M3 12h17M14 5l7 7-7 7"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 3.5v17l14-8.5z"/></svg>'

IMG_DIR = os.path.join(OUT, "assets", "img")


def _find_img(name):
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(os.path.join(IMG_DIR, f"{name}.{ext}")):
            return f"/assets/img/{name}.{ext}"
    return None


def frame(tone=1, tag="", tc="", img=None, ar="16/9", alt="", cine=False, extra="", play=None, el="div"):
    """Medienfläche. Liegt unter assets/img/<img>.jpg|webp ein Foto, wird es automatisch genutzt."""
    src = _find_img(img) if img else None
    cls = "frame" + (" frame--cine" if cine else "") + (" frame--has-img" if src else "") + (f" {extra}" if extra else "")
    inner = f'<img src="{src}" alt="{esc(alt)}" loading="lazy" decoding="async">' if src else ""
    if cine:
        inner += '<span class="frame__bars"></span>'
    if tag:
        inner += f'<span class="frame__tag">{esc(tag)}</span>'
    if tc:
        inner += f'<span class="frame__tc">{esc(tc)}</span>'
    if play:
        inner += f'<span class="play" aria-hidden="true"><i>{PLAY}</i><span>{esc(play)}</span></span>'
    role = ' role="img" aria-label="%s"' % esc(alt) if (alt and not src) else ""
    return f'<{el} class="{cls}" data-tone="{tone}" style="--ar:{ar}"{role}>{inner}</{el}>'


def faq_html(items):
    out = ['<div class="faq">']
    for q, a in items:
        out.append(f"<details><summary>{esc(q)}</summary><div><p>{a}</p></div></details>")
    out.append("</div>")
    return "\n".join(out)


def faq_schema(items):
    import re
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in items
        ],
    }


def breadcrumb_schema(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)}
            for i, (n, p) in enumerate(crumbs)
        ],
    }


def crumbs_html(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            items.append(f'<li><a href="{p}">{esc(n)}</a></li>')
    return f'<nav class="crumbs container" aria-label="Brotkrumen"><ol>{"".join(items)}</ol></nav>'


def business_schema():
    same = [SITE[k] for k in ("instagram", "youtube", "soundcloud", "mixcloud") if SITE[k]]
    d = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": url("/#business"),
        "name": f"{SITE['name']} – {SITE['claim']}",
        "url": url("/"),
        "image": url("/assets/img/og-image.png"),
        "logo": url("/assets/img/icon-512.png"),
        "description": "Hochzeits-DJ, Event-DJ und Videograf für Hochzeitsfilme, Imagefilme und Eventvideos in Köln und NRW.",
        "email": SITE["email"],
        "telephone": SITE["phone"],
        "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": SITE["street"], "postalCode": SITE["zip"],
                    "addressLocality": SITE["city"], "addressRegion": SITE["region"], "addressCountry": SITE["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo"][0], "longitude": SITE["geo"][1]},
        "areaServed": [{"@type": "City", "name": c} for c in SITE["radius"]],
        "knowsAbout": ["Hochzeits-DJ", "Event-DJ", "Hochzeitsfilm", "Imagefilm", "Eventvideo"],
    }
    if same:
        d["sameAs"] = same
    return d


def service_schema(name, description, path, kind):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": kind,
        "description": description,
        "url": url(path),
        "provider": {"@id": url("/#business")},
        "areaServed": [{"@type": "City", "name": c} for c in SITE["radius"][:4]],
    }


# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------
NAV = {
    "dj": [("Hochzeit", "/dj/hochzeit/"), ("Firmenevents", "/dj/firmenevents/"), ("Private Partys", "/dj/private-partys/"),
           ("Musik & Technik", "/dj/musik-technik/"), ("Pakete", "/dj/pakete/"), ("Über mich", "/ueber-mich/")],
    "video": [("Hochzeitsfilm", "/video/hochzeitsfilm/"), ("Imagefilm", "/video/imagefilm/"), ("Eventvideo", "/video/eventvideo/"),
              ("Portfolio", "/video/portfolio/"), ("Pakete", "/video/pakete/"), ("Über mich", "/ueber-mich/")],
    "neutral": [("DJ", "/dj/"), ("Videograf", "/video/"), ("Ratgeber", "/ratgeber/"), ("Über mich", "/ueber-mich/")],
}
HOME = {"dj": "/dj/", "video": "/video/", "neutral": "/"}


def header(world, current):
    links = NAV[world]

    def li(n, p):
        cur = ' aria-current="page"' if p == current else ""
        return f'<li><a href="{p}"{cur}>{esc(n)}</a></li>'

    nav_items = "".join(li(n, p) for n, p in links)
    drawer_items = "".join(
        f'<li><a href="{p}"{" aria-current=page" if p == current else ""}>{esc(n)}{ARROW}</a></li>' for n, p in links)
    sw_dj = ' aria-current="true"' if world == "dj" else ""
    sw_vid = ' aria-current="true"' if world == "video" else ""
    switch = f'<div class="switch" role="group" aria-label="Bereich wechseln"><a href="/dj/"{sw_dj}>DJ</a><a href="/video/"{sw_vid}>Video</a></div>'
    anfrage = {"dj": "dj-hochzeit", "video": "video-hochzeit", "neutral": ""}[world]
    cta = f"/kontakt/?anfrage={anfrage}#formular" if anfrage else "/kontakt/#formular"
    return f"""<a class="skip" href="#main">Zum Inhalt springen</a>
<header class="site-header">
  <div class="container">
    <a class="logo" href="/" aria-label="{esc(SITE['name'])} – zur Startseite"><b>{SITE['mark']}</b><span>{esc(SITE['claim'])}</span></a>
    <nav class="nav" aria-label="Hauptnavigation"><ul>{nav_items}</ul></nav>
    {switch}
    <a class="btn btn--primary btn--sm header-cta" href="{cta}">Anfragen {ARROW}</a>
    <button class="burger" aria-expanded="false" aria-controls="drawer" aria-label="Menü öffnen"><span></span></button>
  </div>
</header>
<div class="drawer" id="drawer">
  <nav aria-label="Mobile Navigation"><ul>{drawer_items}</ul></nav>
  {switch}
  <a class="btn btn--primary" href="{cta}">Termin anfragen {ARROW}</a>
</div>"""


def footer():
    s = SITE
    soc = []
    if s["instagram"]:
        soc.append(f'<li><a href="{esc(s["instagram"])}" rel="me noopener" target="_blank">Instagram</a></li>')
    if s["youtube"]:
        soc.append(f'<li><a href="{esc(s["youtube"])}" rel="me noopener" target="_blank">YouTube</a></li>')
    if s["soundcloud"]:
        soc.append(f'<li><a href="{esc(s["soundcloud"])}" rel="me noopener" target="_blank">SoundCloud</a></li>')
    soc_html = "".join(soc)
    region = " · ".join(s["radius"][:5])
    return f"""<footer class="site-footer">
  <div class="container">
    <p class="footer__big" aria-hidden="true">Lass uns <em>reden.</em></p>
    <div class="footer__grid">
      <div class="footer__brand">
        <h2>{esc(s['name'])}</h2>
        <p>{esc(s['claim'])} aus {esc(s['city'])}. Unterwegs in {esc(region)} und auf Anfrage deutschlandweit.</p>
        <p><a href="mailto:{s['email']}">{s['email']}</a><br><a href="tel:{s['phone_href']}">{s['phone']}</a></p>
      </div>
      <div><h2>DJ</h2><ul>
        <li><a href="/dj/hochzeit/">Hochzeits-DJ</a></li><li><a href="/dj/firmenevents/">Firmenevents</a></li>
        <li><a href="/dj/private-partys/">Private Partys</a></li><li><a href="/dj/musik-technik/">Musik &amp; Technik</a></li>
        <li><a href="/dj/pakete/">Pakete &amp; Preise</a></li></ul></div>
      <div><h2>Video</h2><ul>
        <li><a href="/video/hochzeitsfilm/">Hochzeitsfilm</a></li><li><a href="/video/imagefilm/">Imagefilm</a></li>
        <li><a href="/video/eventvideo/">Eventvideo</a></li><li><a href="/video/portfolio/">Portfolio</a></li>
        <li><a href="/video/pakete/">Pakete &amp; Preise</a></li></ul></div>
      <div><h2>Mehr</h2><ul>
        <li><a href="/ueber-mich/">Über mich</a></li><li><a href="/ratgeber/">Ratgeber</a></li>
        <li><a href="/kontakt/">Kontakt</a></li>{soc_html}</ul></div>
    </div>
    <div class="footer__bottom">
      <span>© {date.today().year} {esc(s['name'])}</span>
      <ul><li><a href="/impressum/">Impressum</a></li><li><a href="/datenschutz/">Datenschutz</a></li></ul>
    </div>
  </div>
</footer>"""


def lightbox():
    return """<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Videoansicht">
  <button class="lightbox__close" aria-label="Schließen">×</button>
  <div class="lightbox__inner">
    <div class="lightbox__stage"></div>
    <div class="lightbox__cap"><span class="lightbox__title"></span><span class="lightbox__note"></span></div>
  </div>
</div>"""


def cta_band(headline, text, label, href, em="?"):
    return f"""<section class="cta-band" aria-labelledby="cta-h">
  <div class="container">
    <div><h2 class="h-1" id="cta-h">{headline}</h2><p>{text}</p></div>
    <a class="btn" href="{href}">{esc(label)} {ARROW}</a>
  </div>
</section>"""


def related(links):
    return '<nav class="related" aria-label="Weiterführende Seiten">' + "".join(
        f'<a href="{p}"><span>{esc(n)}</span>{ARROW.replace("<svg", "<svg width=22 height=22")}</a>' for n, p in links) + "</nav>"


# --------------------------------------------------------------------------
# Seitenrahmen
# --------------------------------------------------------------------------
PAGES = []  # (path, priority, changefreq) für sitemap.xml
_css_ver = None


def _asset_ver():
    global _css_ver
    if _css_ver is None:
        h = hashlib.md5()
        for f in ("css/style.css", "js/main.js"):
            with open(os.path.join(OUT, "assets", f), "rb") as fh:
                h.update(fh.read())
        _css_ver = h.hexdigest()[:8]
    return _css_ver


THEME = {"dj": "#0c0c0d", "video": "#efeadf", "neutral": "#0c0c0d"}


def write_page(path, title, description, body, world="neutral", current=None, schema=None, crumbs=None,
               og_type="website", index=True, priority="0.7", changefreq="monthly", extra_head="", header_html=None,
               footer_html=None, lightbox_on=False, body_class="", faq=None, sitemap=True):
    """Schreibt public_html/<path>/index.html (path z. B. '/dj/hochzeit/')."""
    full_title = title if SITE["name"] in title else f"{title} | {SITE['name']}"
    canonical = url(path)
    graph = list(schema or [])
    if crumbs:
        graph.append(breadcrumb_schema(crumbs))
    if faq:
        graph.append(faq_schema(faq))
    ld = "".join(f'<script type="application/ld+json">{json.dumps(g, ensure_ascii=False, separators=(",", ":"))}</script>\n' for g in graph)
    robots = "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1" if index else "noindex,follow"
    v = _asset_ver()
    og_img = url("/assets/img/og-image.png")
    head = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{THEME[world]}">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="{esc(SITE['name'])} – {esc(SITE['claim'])}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full_title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_img}">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css?v={v}">
{extra_head}{ld}</head>"""
    hdr = header_html if header_html is not None else header(world, current or path)
    ftr = footer_html if footer_html is not None else footer()
    lb = lightbox() if lightbox_on else ""
    page = f"""{head}
<body class="world-{world} {body_class}">
{hdr}
<main id="main">
{body}
</main>
{ftr}
{lb}
<script src="/assets/js/main.js?v={v}" defer></script>
</body>
</html>
"""
    if path.endswith(".html"):
        target = os.path.join(OUT, path.lstrip("/"))
    elif path == "/":
        target = os.path.join(OUT, "index.html")
    else:
        target = os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(page)
    if sitemap and index:
        PAGES.append((path, priority, changefreq))
