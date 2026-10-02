# DJ & Videograf – Website

Statische, SEO-optimierte Website (HTML/CSS/JS, kein Framework, keine externen Dienste) mit PHP-Kontaktformular.
Läuft auf jedem Hostinger-Webhosting (Apache/LiteSpeed + PHP), kein Node/Datenbank nötig.

## Aufbau
```
public_html/    <- das wird zu Hostinger hochgeladen (fertig gebaut)
generator/      <- Seiteninhalte + Layout (Python)
build.py        <- python3 build.py  erzeugt alle HTML-Seiten, sitemap.xml, robots.txt
tools/          <- Icon-/OG-Bild-Generator (Playwright), nur für Entwicklung
```
Seiten: Auswahl-Startseite (DJ | Video), DJ (Hochzeit, Firmenevents, Private Partys, Musik & Technik, Pakete),
Video (Hochzeitsfilm, Imagefilm, Eventvideo, Portfolio, Pakete), Über mich, Kontakt, Ratgeber (3 Artikel),
Impressum, Datenschutz, 404.

## 1. Platzhalter ersetzen (Pflicht)
1. `generator/core.py` → Block `SITE`: Name, Domain, E-Mail, Telefon, Adresse, Stadt, Social-Links.
2. `public_html/kontakt.php` → `$TO`, `$FROM`, `$SITE` (Absender sollte eine Adresse deiner Domain sein).
3. `public_html/.htaccess` → www-Weiterleitung mit deiner Domain aktivieren (auskommentiert).
4. Texte, Preise, Equipment-Angaben und Orte in `generator/pages_*.py` an die Realität anpassen
   (Preise und Leistungsversprechen sind Beispielwerte).
5. Impressum/Datenschutz in `generator/pages_core.py` ausfüllen und rechtlich prüfen lassen.
6. `python3 build.py` ausführen. Optional: `node tools/make-icons.mjs` für OG-Bild/Icons mit deinem Namen
   (Env `SITE_NAME`, `SITE_MARK`; benötigt Playwright).

## 2. Eigene Fotos & Videos
- Fotos in `public_html/assets/img/` ablegen, Dateiname = Slot (`.webp` oder `.jpg`), danach `python3 build.py`:
  `portrait`, `showreel`, `dj-setup`, `video-set`, `work-1` … `work-9`, `dj-hochzeit-banner`, `dj-firma-banner`,
  `video-hochzeit-banner`, `video-imagefilm-banner`, `video-event-banner`.
  Empfohlen: WebP, ca. 250 KB, 1600 px breit. Ohne Foto erscheint eine gestaltete Farbfläche.
- YouTube/Vimeo: in `generator/pages_video.py` (`WORKS`) die Video-ID bei `yt=` bzw. `vimeo=` eintragen.
- Mixe: in `generator/pages_dj.py` (`MIXES`) die Embed-URL (SoundCloud/Mixcloud-Widget) bei `url=` eintragen.
- Alle Embeds laden erst nach Klick (DSGVO). Ohne Tracking/Cookies ist kein Cookie-Banner nötig.

## 3. Auf Hostinger veröffentlichen
1. hPanel → Websites → Dateien → Dateimanager → `public_html` öffnen (Standard-Platzhalter löschen).
2. **Inhalt** von `public_html/` hochladen (inkl. `.htaccess`; „Versteckte Dateien anzeigen“ aktivieren) oder als ZIP hochladen und entpacken.
3. SSL aktivieren (hPanel → Sicherheit → SSL), danach greift die HTTPS-Weiterleitung aus `.htaccess`.
4. E-Mail-Postfach für die Absenderadresse anlegen und das Formular testen.
5. `https://deine-domain.de/sitemap.xml` in der Google Search Console einreichen; Google-Unternehmensprofil anlegen.

## SEO-Stand
Eindeutige Title/Description je Seite, Canonical, Open Graph/Twitter Card, JSON-LD (LocalBusiness, Service, FAQPage,
BreadcrumbList, Article, WebSite), semantische Überschriften, sitemap.xml, robots.txt, saubere URLs, gzip + Caching,
selbst gehostete WOFF2-Schriften, keine Render-Blocker-Skripte, `lang="de"`, mobile-first.
