"""Startseite (Auswahl), Über mich, Kontakt, Ratgeber, Rechtliches, 404."""
from core import (ARROW, SITE, cta_band, crumbs_html, esc, faq_html, frame, related, write_page, business_schema, url, footer)

C = SITE["city"]


# ------------------------------------------------------------------ Landing
def landing():
    s = SITE
    regions = "".join(f"<li>{esc(r)}</li>" for r in s["radius"])
    faq = [
        ("Machst du beides am selben Tag?", "Ja. Viele Paare buchen mich als DJ und Videograf für dieselbe Hochzeit. Das spart Abstimmung, und der Film hört sich besser an, weil ich weiß, wann welche Musik läuft."),
        ("In welchem Gebiet bist du unterwegs?", f"Hauptsächlich {esc(C)} und NRW. Für Hochzeiten fahre ich auch deutschlandweit, dann mit angepasstem Reiseaufwand."),
        ("Wie schnell bekomme ich eine Antwort?", "Auf jede Anfrage antworte ich innerhalb von 24 Stunden, meistens früher. Mit Verfügbarkeit, Preisrahmen und den nächsten Schritten."),
    ]
    top = f"""<div class="landing">
  <div class="landing__bar">
    <a class="logo" href="/" aria-label="{esc(s['name'])}"><b>{s['mark']}</b><span>{esc(s['name'])}</span></a>
    <h1>DJ &amp; Videograf<br>aus {esc(C)} · NRW</h1>
  </div>
  <div class="split">
    <a class="pane pane--dj" href="/dj/" aria-label="Zum DJ-Bereich">
      <div class="vinyl" aria-hidden="true"></div>
      <div class="eq" data-eq="40" aria-hidden="true"></div>
      <span class="pane__no">01 — Hochzeit · Event · Party</span>
      <span class="pane__title" aria-hidden="true">DJ</span>
      <span class="pane__text">Live gemixt, passend zum Raum. Hochzeiten, Firmenevents und private Feiern.</span>
      <span class="pane__go">DJ-Bereich betreten {ARROW}</span>
    </a>
    <a class="pane pane--video" href="/video/" aria-label="Zum Videograf-Bereich">
      <div class="finder" aria-hidden="true"><i></i><i></i><i></i><i></i><span class="rec">REC</span><span class="tc" data-timecode>00:00:00:00</span><span class="cross"></span></div>
      <span class="pane__no">02 — Hochzeitsfilm · Imagefilm · Event</span>
      <span class="pane__title" aria-hidden="true">Film</span>
      <span class="pane__text">Bilder und Ton mit Gefühl für den Moment. Hochzeit, Unternehmen, Events.</span>
      <span class="pane__go">Video-Bereich betreten {ARROW}</span>
    </a>
  </div>
  <div class="landing__nav"><span>Wähle deinen Bereich</span><nav aria-label="Schnellzugriff"><a href="/ueber-mich/">Über mich</a><a href="/ratgeber/">Ratgeber</a><a href="/kontakt/">Kontakt</a></nav></div>
</div>
<div class="landing-intro">
<section class="section" aria-labelledby="intro-h">
  <div class="container">
    <div class="two-col two-col--wide-left">
      <div>
        <div class="eyebrow">Hallo</div>
        <h2 class="h-1 reveal" id="intro-h">Zwei Handwerke, <em>ein</em> Ansprechpartner</h2>
      </div>
      <div class="prose reveal" data-delay="1">
        <p>Ich bin {esc(s['name'])}, DJ und Videograf aus {esc(C)}. Ich stehe sonntags hinter der Kamera und samstags hinter dem Pult, manchmal beides am selben Tag.</p>
        <p>Auf dieser Seite findest du alles zu beiden Bereichen: was ich anbiete, wie ich arbeite, was es kostet und wie du anfragen kannst. Wähle oben deinen Bereich oder lies hier weiter.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="angebot-h">
  <div class="container two-col">
    <div class="reveal">
      <h2 class="h-2" id="angebot-h">DJ-Service</h2>
      <ul class="list-plus" style="margin-top:1.5rem">
        <li><a href="/dj/hochzeit/">Hochzeits-DJ in {esc(C)} und NRW</a></li>
        <li><a href="/dj/firmenevents/">DJ für Firmenfeiern und Events</a></li>
        <li><a href="/dj/private-partys/">DJ für Geburtstag und private Partys</a></li>
        <li><a href="/dj/musik-technik/">Musikstile, Technik, Hörproben</a></li>
        <li><a href="/dj/pakete/">Pakete und Preise</a></li>
      </ul>
    </div>
    <div class="reveal" data-delay="1">
      <h2 class="h-2">Videografie</h2>
      <ul class="list-plus" style="margin-top:1.5rem">
        <li><a href="/video/hochzeitsfilm/">Hochzeitsfilm: Highlight, Trailer, Dokumentation</a></li>
        <li><a href="/video/imagefilm/">Imagefilm und Unternehmensvideo</a></li>
        <li><a href="/video/eventvideo/">Eventvideo und Aftermovie</a></li>
        <li><a href="/video/portfolio/">Portfolio</a></li>
        <li><a href="/video/pakete/">Pakete und Preise</a></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="warum-h">
  <div class="container">
    <div class="split-head"><h2 class="h-1 reveal" id="warum-h">Warum <em>beides</em> aus einer Hand?</h2><p class="reveal" data-delay="1">Weil gute Hochzeits- und Eventdienstleister einen Rhythmus teilen. Das spart dir Koordination und macht das Ergebnis besser.</p></div>
    <ol class="process reveal">
      <li><h3>Ein Gespräch</h3><p>Du erklärst einmal, was du vorhast. Ich plane Musik und Film mit demselben Ablauf.</p></li>
      <li><h3>Besserer Ton</h3><p>Weil ich weiß, wann Reden, Musik und Tanz stattfinden, nehme ich Ton und Bild genau dann auf, wenn es zählt.</p></li>
      <li><h3>Weniger Chaos</h3><p>Ein Ansprechpartner statt drei E-Mail-Ketten. Auch am Tag selbst weiß ich, was die andere Hälfte meiner Arbeit braucht.</p></li>
      <li><h3>Kombi-Vorteil</h3><p>Wer beide Leistungen bucht, bekommt einen Preisvorteil. Details gibt es im Angebot.</p></li>
    </ol>
  </div>
</section>

<section class="section section--alt" aria-labelledby="gebiet-h">
  <div class="container two-col two-col--wide-left">
    <div><div class="eyebrow">Einsatzgebiet</div><h2 class="h-2 reveal" id="gebiet-h">Zuhause in {esc(C)}, <em>unterwegs</em> in NRW</h2>
      <ul class="regions reveal" style="margin-top:1.5rem">{regions}<li>und auf Anfrage deutschlandweit</li></ul></div>
    <div class="reveal" data-delay="1">{faq_html(faq)}</div>
  </div>
</section>
{cta_band("Datum <em>im Kopf?</em>", "Schreib mir Anlass, Datum und Ort. Innerhalb von 24 Stunden hast du meine Antwort.", "Jetzt anfragen", "/kontakt/#formular")}
</div>"""
    write_page("/", f"{s['name']} | DJ & Videograf aus {C} – Hochzeit, Event, Imagefilm",
               f"DJ und Videograf aus {C}: Hochzeits-DJ, Event-DJ, Hochzeitsfilm, Imagefilm und Eventvideo in NRW. Beides aus einer Hand. Jetzt Termin anfragen.",
               top, world="neutral", header_html="", priority="1.0", changefreq="weekly", body_class="is-landing",
               schema=[business_schema(), {"@context": "https://schema.org", "@type": "WebSite", "@id": url("/#website"), "url": url("/"),
                                           "name": f"{s['name']} – {s['claim']}", "inLanguage": "de-DE", "publisher": {"@id": url("/#business")}}],
               faq=faq)


# ------------------------------------------------------------------ Über mich
def about():
    body = f"""{crumbs_html([("Start", "/"), ("Über mich", "/ueber-mich/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Über mich</div>
    <h1 class="h-1 page-hero--wide">Ein Typ, zwei Handwerke, <em>ein</em> Gespür</h1>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container two-col two-col--wide-left">
    <div class="prose reveal">
      <p class="lede" style="max-width:none">Ob am Mischpult oder hinter der Kamera: Meine Arbeit besteht zu 90 Prozent aus Zuhören. Wer feiert da eigentlich? Was soll hängen bleiben? Was darf auf keinen Fall passieren?</p>
      <p>Ich bin {esc(SITE['name'])}, DJ und Videograf aus {esc(C)}. Beides begann als Leidenschaft und wurde zum Beruf, weil ich merkte, dass ich bei Events am liebsten genau dort stehe, wo etwas passiert, ohne selbst im Mittelpunkt zu stehen.</p>
      <h2>Wie ich arbeite</h2>
      <p>Mir ist Ehrlichkeit wichtiger als Verkaufssprache. Wenn dein Budget für ein Paket nicht reicht, sage ich dir, was sich lohnt. Wenn ich nicht der Richtige für dein Event bin, nenne ich dir jemanden, der besser passt. Auf diese Weise sind die meisten Empfehlungen entstanden.</p>
      <h2>Was dir wichtig sein darf</h2>
      <ul>
        <li><strong>Pünktlichkeit.</strong> Aufbau immer vor Ankunft der Gäste, keine Stress-Termine.</li>
        <li><strong>Backup.</strong> Doppeltes Equipment, gesicherte Daten, Ersatzplan.</li>
        <li><strong>Diskretion.</strong> Was bei deiner Feier passiert, bleibt dort, außer du teilst es.</li>
        <li><strong>Klare Preise.</strong> Angebot schriftlich, ohne versteckte Kosten.</li>
      </ul>
    </div>
    <div class="reveal portrait" data-delay="1">{frame(tone=3, tag="Portrait", tc="MIKA R.", ar="4/5", alt="Portrait", img="portrait")}</div>
  </div>
</section>
<section class="section section--alt" aria-labelledby="warum-h">
  <div class="container">
    <div class="split-head"><h2 class="h-2 reveal" id="warum-h">Warum <em>DJ und</em> Videograf?</h2><p class="reveal" data-delay="1">Beides lebt von Timing. Ein Schnitt sitzt wie ein Übergang zwischen zwei Songs: nicht zu früh, nicht zu spät.</p></div>
    <div class="notes reveal">
      <div class="note-line"><h3 class="h-3">Rhythmus</h3><p>Wer Musik auflegt, kennt Spannungsbögen. Wer Filme schneidet, baut sie. Beides profitiert voneinander.</p></div>
      <div class="note-line"><h3 class="h-3">Technik</h3><p>Ton, Licht, Strom, Sicherheit: Vieles gilt für Bühne und Dreh gleichermaßen. Das spart Fehler.</p></div>
      <div class="note-line"><h3 class="h-3">Menschen</h3><p>Egal ob Kamera oder Kopfhörer: Gute Ergebnisse entstehen, wenn Menschen sich wohlfühlen.</p></div>
    </div>
  </div>
</section>
{cta_band("Passen <em>wir</em> zusammen?", "Finde es in 20 Minuten heraus. Schreib mir, dann sprechen wir kurz am Telefon oder per Video.", "Kennenlernen anfragen", "/kontakt/#formular")}
"""
    write_page("/ueber-mich/", f"Über mich: DJ & Videograf aus {C}",
               f"Wer hinter Pult und Kamera steht: {SITE['name']}, DJ und Videograf aus {C}. Arbeitsweise, Haltung und warum beides aus einer Hand Sinn ergibt.",
               body, world="neutral", current="/ueber-mich/", crumbs=[("Start", "/"), ("Über mich", "/ueber-mich/")], priority="0.6")


# ------------------------------------------------------------------ Kontakt
def contact():
    s = SITE
    opts = [("", "Bitte wählen"), ("dj-hochzeit", "Hochzeits-DJ"), ("video-hochzeit", "Hochzeitsfilm"), ("kombi", "DJ + Video (Kombi)"),
            ("dj-firma", "DJ für Firmenevent"), ("video-firma", "Imagefilm / Eventvideo"), ("dj-privat", "DJ für private Feier"), ("sonstiges", "Etwas anderes")]
    options = "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in opts)
    body = f"""{crumbs_html([("Start", "/"), ("Kontakt", "/kontakt/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Kontakt</div>
    <h1 class="h-1 page-hero--wide">Erzähl mir von deinem <em>Vorhaben</em></h1>
    <p class="lede">Je mehr ich weiß, desto genauer wird meine erste Antwort. Aber auch drei Zeilen reichen. Ich melde mich innerhalb von 24 Stunden.</p>
  </div>
</section>
<section class="section" style="padding-top:0" id="formular">
  <div class="container contact-grid">
    <form id="anfrage-form" class="form" action="/kontakt.php" method="post" novalidate>
      <div class="field"><label for="anlass">Worum geht es? <i>*</i></label>
        <select id="anlass" name="anlass" required>{options}</select><div class="err">Bitte wähle einen Anlass.</div></div>
      <div class="form-row form-row--2">
        <div class="field"><label for="name">Name <i>*</i></label><input id="name" name="name" type="text" autocomplete="name" required><div class="err">Bitte gib deinen Namen an.</div></div>
        <div class="field"><label for="email">E-Mail <i>*</i></label><input id="email" name="email" type="email" autocomplete="email" required><div class="err">Bitte gib eine gültige E-Mail-Adresse an.</div></div>
      </div>
      <div class="form-row form-row--2">
        <div class="field"><label for="datum">Datum</label><input id="datum" name="datum" type="date"></div>
        <div class="field"><label for="ort">Ort / Location</label><input id="ort" name="ort" type="text" autocomplete="off"></div>
      </div>
      <div class="form-row form-row--2">
        <div class="field"><label for="gaeste">Gästezahl (ca.)</label><input id="gaeste" name="gaeste" type="number" min="1" max="2000" inputmode="numeric"></div>
        <div class="field"><label for="tel">Telefon (optional)</label><input id="tel" name="tel" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="nachricht">Nachricht <i>*</i></label><textarea id="nachricht" name="nachricht" required placeholder="Was planst du? Was ist dir besonders wichtig?"></textarea><div class="err">Bitte schreib mir kurz, worum es geht.</div></div>
      <div class="hp" aria-hidden="true"><label>Nicht ausfüllen<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
      <input type="hidden" name="ts" value="">
      <label class="check"><input type="checkbox" name="datenschutz" required><span>Ich habe die <a href="/datenschutz/">Datenschutzerklärung</a> gelesen und bin damit einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verwendet werden.</span></label>
      <div class="form-status" role="status" aria-live="polite"></div>
      <div><button class="btn btn--primary" type="submit">Anfrage senden {ARROW}</button></div>
    </form>
    <aside class="contact-aside" aria-label="Direkter Kontakt">
      <dl>
        <div><dt>E-Mail</dt><dd><a href="mailto:{s['email']}">{s['email']}</a></dd></div>
        <div><dt>Telefon</dt><dd><a href="tel:{s['phone_href']}">{s['phone']}</a></dd></div>
        <div><dt>Antwortzeit</dt><dd>Innerhalb von 24 Stunden, auch am Wochenende</dd></div>
        <div><dt>Einsatzgebiet</dt><dd>{esc(C)}, {', '.join(esc(r) for r in s['radius'][1:5])} und auf Anfrage deutschlandweit</dd></div>
        <div><dt>Und danach?</dt><dd>Du bekommst eine Antwort mit Verfügbarkeit und Preisrahmen. Danach telefonieren wir kurz, ganz ohne Verpflichtung.</dd></div>
      </dl>
    </aside>
  </div>
</section>
"""
    write_page("/kontakt/", f"Kontakt & Anfrage: DJ und Videograf in {C}",
               f"Termin für Hochzeits-DJ, Hochzeitsfilm, Imagefilm oder Eventvideo anfragen. Antwort innerhalb von 24 Stunden. DJ und Videograf aus {C}.",
               body, world="neutral", current="/kontakt/", crumbs=[("Start", "/"), ("Kontakt", "/kontakt/")], priority="0.8",
               schema=[{"@context": "https://schema.org", "@type": "ContactPage", "url": url("/kontakt/"), "name": "Kontakt", "about": {"@id": url("/#business")}}])


# ------------------------------------------------------------------ Ratgeber
POSTS = [
    dict(slug="hochzeits-dj-buchen", title="Hochzeits-DJ buchen: 9 Fragen, die du vor der Zusage stellen solltest",
         short="Hochzeits-DJ buchen: 9 Fragen vor der Zusage", date="2026-10-02", read="5 Min.",
         desc="Worauf es bei der Wahl des Hochzeits-DJs ankommt: Fragen zu Musik, Technik, Backup, Preis und Ablauf. Mit Checkliste fürs Kennenlerngespräch.",
         teaser="Von Backup-Technik bis zur No-Go-Liste: Diese Fragen trennen gute von mittelmäßigen DJs.",
         body="""<p>Der DJ entscheidet mit, ob eure Hochzeit nach 22 Uhr eine volle Tanzfläche hat oder ein leeres Parkett. Gleichzeitig ist es einer der Dienstleister, bei denen man am wenigsten vergleichen kann. Mit diesen neun Fragen bekommst du schnell ein Bild.</p>
<h2>1. Spielst du live oder lässt du eine Playlist laufen?</h2>
<p>Beides ist legitim, aber der Preis sollte dazu passen. Ein DJ, der live mischt, reagiert auf die Fläche. Eine Playlist kann das nicht.</p>
<h2>2. Was passiert, wenn das Equipment ausfällt?</h2>
<p>Die richtige Antwort beginnt mit „Ich habe doppelt dabei“. Ein DJ ohne Plan B ist ein Risiko, das du nicht eingehen musst.</p>
<h2>3. Wie läuft das Vorgespräch ab?</h2>
<p>Gute DJs fragen vorher viel: Gästestruktur, Lieblingsmusik, Tabus, Ablauf. Wer nur nach Datum und Preis fragt, will nur den Termin.</p>
<h2>4. Gibt es eine Wunsch- und No-Go-Liste?</h2>
<p>Das ist eine der wichtigsten Unterlagen. Wer sie nicht anbietet, schaut vermutlich nicht genau hin.</p>
<h2>5. Wie sieht der Ablauf mit Location und anderen Dienstleistern aus?</h2>
<p>Ein erfahrener DJ stimmt Zeiten mit Location, Fotograf:in und Trauredner:in ab, damit Reden, Anschnitt und Eröffnungstanz funktionieren.</p>
<h2>6. Ist die Anfahrt im Preis inklusive?</h2>
<p>Klärt das schriftlich. Genauso wie Aufbau, Soundcheck und Abbau.</p>
<h2>7. Kannst du die Trauung beschallen?</h2>
<p>Wenn ihr eine freie Trauung plant, braucht ihr oft Mikrofone und Lautsprecher am Trauort. Das sollte im Paket stecken oder optional buchbar sein.</p>
<h2>8. Wie lange spielst du, und was kostet eine zusätzliche Stunde?</h2>
<p>Hochzeiten gehen selten wie geplant zu Ende. Kennt ihr den Stundensatz vorher, gibt es keine Diskussion um 1 Uhr nachts.</p>
<h2>9. Was steht im Vertrag?</h2>
<p>Preis, Leistungsumfang, Anzahlung, Storno-Regeln, Ersatz bei Krankheit. Wer das nicht schriftlich anbietet, bietet es vermutlich nicht an.</p>
<div class="callout"><p><strong>Tipp:</strong> Hört euch einen Mix an, der zu eurem Geschmack passt, aber vertraut vor allem darauf, wie sich das Gespräch anfühlt. Mit dem DJ verbringt ihr einen der wichtigsten Abende eures Lebens.</p></div>""",
         links=[("Hochzeits-DJ in " + C, "/dj/hochzeit/"), ("DJ-Pakete & Preise", "/dj/pakete/")]),
    dict(slug="hochzeitsfilm-kosten", title="Hochzeitsfilm: Was er kostet und wovon der Preis abhängt",
         short="Hochzeitsfilm: Was er kostet", date="2026-10-02", read="4 Min.",
         desc="Was kostet ein Hochzeitsfilm? Preisfaktoren wie Drehzeit, Kameras, Drohne und Schnitt erklärt, mit Tipps, wie ihr Angebote vergleicht.",
         teaser="Drehzeit, Schnittaufwand, Zweitkamera: Das steckt hinter dem Preis eines Hochzeitsfilms.",
         body="""<p>Ein Hochzeitsfilm kostet je nach Umfang zwischen etwa 1.200 und 3.500 Euro, in manchen Fällen mehr. Dahinter stecken meist deutlich mehr Stunden, als man auf den ersten Blick denkt: Ein Drehtag von zehn Stunden bedeutet oft 40 bis 60 Stunden Nachbearbeitung.</p>
<h2>Die wichtigsten Preisfaktoren</h2>
<ul><li><strong>Drehzeit:</strong> vier Stunden (Trauung bis Empfang) kosten weniger als ein ganzer Tag.</li><li><strong>Anzahl der Kameras:</strong> Eine zweite Kamera bei Trauung und Reden verbessert Ton und Bildauswahl spürbar.</li><li><strong>Formate:</strong> Trailer, Highlightfilm und Dokumentation haben unterschiedlichen Schnittaufwand.</li><li><strong>Drohne:</strong> Luftaufnahmen brauchen Planung, Genehmigung und Zeit.</li><li><strong>Lieferung:</strong> USB-Stick, Kopien für Familie, Rohmaterial.</li></ul>
<h2>Woran ihr gute Angebote erkennt</h2>
<p>Ein seriöses Angebot nennt Drehstunden, Formate, Lieferzeit, Anzahl der Korrekturschleifen, Nutzungsrechte und Musiklizenz. Fehlt etwas davon, fragt nach.</p>
<h2>Wo sich sparen lässt</h2>
<p>Statt eines ganzen Tages könnt ihr bei Trauung, Reden und Eröffnungstanz filmen lassen. Auch auf Dokumentation und Drohne lässt sich verzichten. Nicht sparen solltet ihr beim Ton: Gelübde und Reden sind der emotionalste Teil.</p>
<h2>Gute Frage zum Schluss</h2>
<p>„Dürfen wir ein vollständiges Beispiel sehen?“ Ein Trailer zeigt, was gut aussieht. Ein kompletter Hochzeitsfilm zeigt, wie erzählt wird.</p>""",
         links=[("Hochzeitsfilm in " + C, "/video/hochzeitsfilm/"), ("Video-Pakete & Preise", "/video/pakete/")]),
    dict(slug="musikwuensche-hochzeit", title="Musikwünsche für die Hochzeit: Playlist, No-Go-Liste und Eröffnungstanz",
         short="Musikwünsche für die Hochzeit", date="2026-10-02", read="4 Min.",
         desc="So bereitet ihr die Musik für eure Hochzeit vor: Wunschliste, No-Go-Liste, Eröffnungstanz und Gästewünsche. Mit Tipps vom DJ.",
         teaser="Weniger ist mehr: So bereitet ihr Musikwünsche vor, ohne dem DJ die Hände zu binden.",
         body="""<p>Die meisten Paare machen zwei Fehler: Sie schicken dem DJ eine 300-Titel-Playlist oder gar nichts. Beides ist schwierig. Mit ein bisschen Struktur klappt es besser.</p>
<h2>Die Wunschliste: 15 bis 25 Songs</h2>
<p>Wählt Titel, die ihr unbedingt hören wollt. Ein DJ kann um diese Songs herum aufbauen. Mehr Titel schränken ihn ein.</p>
<h2>Die No-Go-Liste</h2>
<p>Genauso wichtig: Was soll nie laufen? Der Song, der eine Ex-Beziehung erinnert, Schlager, die niemand hören will, Partyhits, die zu oft gespielt werden. Eine kurze Liste hilft mehr als eine lange.</p>
<h2>Der Eröffnungstanz</h2>
<p>Schickt den Titel früh, damit der DJ ihn schneiden kann. Viele Songs sind zu lang oder haben ein ruhiges Intro. Bei Bedarf wird der Übergang zur Party geplant.</p>
<h2>Musik für Trauung und Empfang</h2>
<p>Überlegt, was beim Einzug, bei der Unterschrift und beim Auszug laufen soll. Ein Livestream-Lied oder ein Klassiker mit Bedeutung wirkt stärker als ein Standardstück.</p>
<h2>Gästewünsche am Abend</h2>
<p>Sagt dem DJ, ob Gäste Wünsche äußern dürfen. Viele DJs entscheiden dann nach Gefühl, was passt. Das ist meist die beste Lösung.</p>
<h2>Das Wichtigste</h2>
<p>Vertraut dem DJ bei Auswahl und Reihenfolge. Gebt Leitplanken, aber keine Regieanweisungen. Die Fläche entscheidet.</p>""",
         links=[("Hochzeits-DJ in " + C, "/dj/hochzeit/"), ("Musik & Technik", "/dj/musik-technik/")]),
]


def ratgeber():
    cards = "".join(f"""<a class="post reveal" href="/ratgeber/{p['slug']}/"><time datetime="{p['date']}">{p['read']} Lesezeit</time><h3>{esc(p['short'])}</h3><p>{esc(p['teaser'])}</p><span class="link-arrow">Lesen {ARROW}</span></a>""" for p in POSTS)
    body = f"""{crumbs_html([("Start", "/"), ("Ratgeber", "/ratgeber/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Ratgeber</div>
    <h1 class="h-1 page-hero--wide">Wissen für deine <em>Planung</em></h1>
    <p class="lede">Ehrliche Antworten auf Fragen, die sich fast jedes Paar und jeder Veranstalter stellt.</p>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="container"><div class="posts">{cards}</div></div></section>
"""
    write_page("/ratgeber/", f"Ratgeber: Hochzeits-DJ, Hochzeitsfilm & Eventplanung",
               "Praktische Tipps für Hochzeit und Events: DJ buchen, Hochzeitsfilm Kosten, Musikwünsche vorbereiten. Ratgeber vom DJ und Videografen aus Köln.",
               body, world="neutral", current="/ratgeber/", crumbs=[("Start", "/"), ("Ratgeber", "/ratgeber/")], priority="0.7")
    for p in POSTS:
        path = f"/ratgeber/{p['slug']}/"
        rel = related(p["links"])
        art = f"""{crumbs_html([("Start", "/"), ("Ratgeber", "/ratgeber/"), (p['short'], path)])}
<article class="section" style="padding-top:2rem">
  <div class="container">
    <header style="margin-bottom:3rem"><div class="eyebrow">{p['read']} Lesezeit · <time datetime="{p['date']}">{p['date'][8:]}.{p['date'][5:7]}.{p['date'][:4]}</time></div>
    <h1 class="h-2" style="max-width:22ch">{esc(p['title'])}</h1></header>
    <div class="prose">{p['body']}</div>
    <div style="margin-top:4rem;max-width:70ch"><div class="eyebrow">Weiterlesen</div>{rel}</div>
  </div>
</article>
{cta_band("Du planst <em>gerade?</em>", "Schreib mir Anlass und Datum. Ich beantworte offene Fragen und gebe dir ein klares Angebot.", "Kontakt aufnehmen", "/kontakt/#formular")}"""
        article_schema = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["desc"],
                          "datePublished": p["date"], "dateModified": p["date"], "inLanguage": "de-DE", "mainEntityOfPage": url(path),
                          "author": {"@type": "Person", "name": SITE["name"]}, "publisher": {"@id": url("/#business")},
                          "image": url("/assets/img/og-image.png")}
        write_page(path, p["title"], p["desc"], art, world="neutral", current="/ratgeber/", og_type="article", priority="0.6",
                   schema=[article_schema], crumbs=[("Start", "/"), ("Ratgeber", "/ratgeber/"), (p["short"], path)])


# ------------------------------------------------------------------ Rechtliches
def legal():
    s = SITE
    imp = f"""{crumbs_html([("Start", "/"), ("Impressum", "/impressum/")])}
<section class="section" style="padding-top:2rem"><div class="container">
<h1 class="h-1" style="margin-bottom:2.5rem">Impressum</h1>
<div class="prose prose--legal">
<div class="callout"><p><strong>Hinweis zur Einrichtung:</strong> Bitte ersetze alle Platzhalter (Name, Anschrift, Steuer-ID usw.) durch deine echten Angaben und lasse die Texte im Zweifel rechtlich prüfen. Diese Vorlage ersetzt keine Rechtsberatung.</p></div>
<h2>Angaben gemäß § 5 DDG</h2>
<p>{esc(s['name'])}<br>{esc(s['street'])}<br>{esc(s['zip'])} {esc(s['city'])}</p>
<h2>Kontakt</h2>
<p>Telefon: {s['phone']}<br>E-Mail: <a href="mailto:{s['email']}">{s['email']}</a></p>
<h2>Umsatzsteuer</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a UStG: DE000000000<br><em>(oder: Kleinunternehmer gemäß § 19 UStG, keine Ausweisung der Umsatzsteuer)</em></p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>{esc(s['name'])}, Anschrift wie oben</p>
<h2>Streitschlichtung</h2>
<p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte und Links</h2>
<p>Als Diensteanbieter bin ich für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Für Inhalte externer Links übernehme ich keine Haftung; für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.</p>
<h2>Urheberrecht</h2>
<p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet. Vervielfältigung, Bearbeitung und Verbreitung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung.</p>
</div></div></section>"""
    write_page("/impressum/", "Impressum", f"Impressum von {s['name']}, DJ und Videograf aus {s['city']}.", imp, world="neutral",
               crumbs=[("Start", "/"), ("Impressum", "/impressum/")], index=False, sitemap=False)

    dsg = f"""{crumbs_html([("Start", "/"), ("Datenschutz", "/datenschutz/")])}
<section class="section" style="padding-top:2rem"><div class="container">
<h1 class="h-1" style="margin-bottom:2.5rem">Datenschutz&shy;erklärung</h1>
<div class="prose prose--legal">
<div class="callout"><p><strong>Hinweis zur Einrichtung:</strong> Diese Vorlage beschreibt die technische Ausstattung dieser Website (kein Tracking, keine Cookies, selbst gehostete Schriften, Videos erst nach Klick). Ergänze deine Angaben und prüfe den Text rechtlich, bevor du die Seite veröffentlichst. Diese Vorlage ersetzt keine Rechtsberatung.</p></div>
<h2>1. Verantwortlicher</h2>
<p>{esc(s['name'])}, {esc(s['street'])}, {esc(s['zip'])} {esc(s['city'])}<br>E-Mail: <a href="mailto:{s['email']}">{s['email']}</a></p>
<h2>2. Hosting</h2>
<p>Diese Website wird bei Hostinger International Ltd. bzw. der jeweils vertraglich vereinbarten Hostinger-Gesellschaft gehostet. Beim Aufruf der Seite erhebt der Webserver automatisch technische Daten in sogenannten Server-Logfiles (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser, Betriebssystem). Die Verarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einem sicheren und stabilen Betrieb). Mit dem Hosting-Anbieter besteht ein Vertrag zur Auftragsverarbeitung.</p>
<h2>3. Cookies und Tracking</h2>
<p>Diese Website verwendet keine Cookies zu Analyse- oder Marketingzwecken und setzt keine Tracking-Tools ein. Es wird lediglich im Browser lokal gespeichert, was für die Darstellung nötig ist.</p>
<h2>4. Schriftarten</h2>
<p>Die verwendeten Schriftarten werden lokal vom eigenen Server ausgeliefert. Es findet keine Verbindung zu Google-Servern statt.</p>
<h2>5. Kontaktformular und E-Mail</h2>
<p>Wenn du das Kontaktformular nutzt oder mir schreibst, verarbeite ich deine Angaben (Name, E-Mail, Anlass, Datum, Ort, Nachricht, ggf. Telefonnummer) zur Bearbeitung deiner Anfrage und für Anschlussfragen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (vorvertragliche Maßnahmen) bzw. lit. f DSGVO. Die Daten werden gelöscht, sobald sie für den Zweck nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungsfristen entgegenstehen.</p>
<h2>6. Eingebettete Inhalte (Videos, Audio)</h2>
<p>Videos (YouTube im erweiterten Datenschutzmodus bzw. Vimeo mit „Do Not Track“) und Audio-Player (z. B. SoundCloud, Mixcloud) werden erst nach deinem Klick geladen. Erst dann wird eine Verbindung zum jeweiligen Anbieter hergestellt und deine IP-Adresse übermittelt. Rechtsgrundlage ist deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
<h2>7. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Datenschutzaufsichtsbehörde. Für Nordrhein-Westfalen ist das die Landesbeauftragte für Datenschutz und Informationsfreiheit NRW.</p>
<h2>8. Aktualität</h2>
<p>Stand: {TODAY_DE()}. Ich passe diese Erklärung an, wenn sich die Website oder die Rechtslage ändert.</p>
</div></div></section>"""
    write_page("/datenschutz/", "Datenschutzerklärung", f"Datenschutzerklärung von {s['name']}.", dsg, world="neutral",
               crumbs=[("Start", "/"), ("Datenschutz", "/datenschutz/")], index=False, sitemap=False)


def TODAY_DE():
    from datetime import date
    d = date.today()
    return f"{d.day:02d}.{d.month:02d}.{d.year}"


# ------------------------------------------------------------------ 404
def notfound():
    body = f"""<section class="notfound"><div class="container">
  <div class="eyebrow">Fehler 404</div>
  <h1 class="h-display h-display--m">Diese Seite <em>fehlt.</em></h1>
  <p class="lede" style="margin-top:2rem">Der Link ist veraltet oder falsch getippt. Von hier aus kommst du weiter:</p>
  <div class="btn-row"><a class="btn btn--primary" href="/">Zur Startseite {ARROW}</a><a class="btn" href="/dj/">DJ</a><a class="btn" href="/video/">Video</a><a class="btn" href="/kontakt/">Kontakt</a></div>
</div></section>"""
    write_page("/404.html", "Seite nicht gefunden", "Diese Seite existiert nicht.", body, world="neutral", index=False, sitemap=False)


def build():
    landing()
    about()
    contact()
    ratgeber()
    legal()
    notfound()
