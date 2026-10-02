#!/usr/bin/env python3
"""Baut die komplette Website nach public_html/.  Aufruf:  python3 build.py"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "generator"))

import core  # noqa: E402
import pages_core  # noqa: E402
import pages_dj  # noqa: E402
import pages_video  # noqa: E402


def write(rel, content):
    path = os.path.join(core.OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    pages_core.build()
    pages_dj.build()
    pages_video.build()

    # sitemap.xml
    urls = []
    for path, prio, freq in sorted(core.PAGES, key=lambda p: (-float(p[1]), p[0])):
        urls.append(f"  <url><loc>{core.url(path)}</loc><lastmod>{core.TODAY}</lastmod>"
                    f"<changefreq>{freq}</changefreq><priority>{prio}</priority></url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")

    # robots.txt
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /kontakt.php\n\nSitemap: {core.url('/sitemap.xml')}\n")

    # Web-App-Manifest
    write("site.webmanifest", json.dumps({
        "name": f"{core.SITE['name']} – {core.SITE['claim']}", "short_name": core.SITE["mark"],
        "start_url": "/", "display": "browser", "background_color": "#0c0c0d", "theme_color": "#0c0c0d", "lang": "de",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2, ensure_ascii=False))

    # Favicon (SVG)
    write("favicon.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0c0c0d"/>
<rect x="8" y="8" width="48" height="48" fill="#c9f31d"/><text x="32" y="45" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="30" letter-spacing="-2" fill="#0c0c0d">{core.SITE['mark']}</text></svg>""")
    print(f"{len(core.PAGES)} Seiten in sitemap.xml, Ausgabe: {core.OUT}")


if __name__ == "__main__":
    main()
