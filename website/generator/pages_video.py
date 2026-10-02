"""Video-Bereich: Startseite, Leistungsseiten, Portfolio, Pakete."""
from core import (ARROW, SITE, cta_band, crumbs_html, esc, faq_html, frame, write_page, service_schema, business_schema)
from service_page import service_page

C = SITE["city"]

# yt = YouTube-Video-ID (nur die ID!), vimeo = Vimeo-ID. Leer => "Film auf Anfrage".
WORKS = [
    dict(cat="hochzeit", title="Trauung im Park – Highlightfilm", meta="Hochzeit · 4:30", tone=3, cls="work--hero", yt="", vimeo="", img="work-1", ar="16/9"),
    dict(cat="imagefilm", title="Handwerk mit Haltung – Imagefilm", meta="Imagefilm · 2:10", tone=2, cls="", yt="", vimeo="", img="work-2", ar="10/11"),
    dict(cat="hochzeit", title="Getting Ready & First Look – Trailer", meta="Hochzeit · 1:45", tone=6, cls="work--wide", yt="", vimeo="", img="work-3", ar="16/9"),
    dict(cat="imagefilm", title="Manufaktur – Produktfilm", meta="Imagefilm · 1:20", tone=4, cls="work--wide", yt="", vimeo="", img="work-4", ar="16/9"),
    dict(cat="event", title="Sommerfest – Aftermovie", meta="Event · 1:30", tone=5, cls="", yt="", vimeo="", img="work-5", ar="4/3"),
    dict(cat="social", title="Recruiting-Reel – 9:16", meta="Social · 0:30", tone=1, cls="", yt="", vimeo="", img="work-6", ar="4/3"),
    dict(cat="event", title="Konferenz – Tagesrückblick", meta="Event · 2:00", tone=2, cls="", yt="", vimeo="", img="work-7", ar="4/3"),
    dict(cat="hochzeit", title="Freie Trauung am See", meta="Hochzeit · 5:10", tone=5, cls="work--wide", yt="", vimeo="", img="work-8", ar="16/9"),
    dict(cat="social", title="Behind the Scenes – Kurzclips", meta="Social · 0:45", tone=3, cls="work--wide", yt="", vimeo="", img="work-9", ar="16/9"),
]


def work_item(w, i):
    attrs = f'data-lightbox data-title="{esc(w["title"])}"'
    if w["yt"]:
        attrs += f' data-yt="{esc(w["yt"])}"'
    if w["vimeo"]:
        attrs += f' data-vimeo="{esc(w["vimeo"])}"'
    f = frame(tone=w["tone"], tag=w["meta"].split(" · ")[0], tc=f"CAM A · 00:0{i % 9}:1{i % 10}", ar=w["ar"], img=w["img"], alt=w["title"], cine=w["ar"] == "16/9", play="Ansehen", el="span")
    return f"""<button class="work reveal {w['cls']}" type="button" data-cat="{w['cat']}" {attrs} aria-label="Video öffnen: {esc(w['title'])}">
  {f}
  <span class="work__meta"><b>{esc(w['title'])}</b><span>{esc(w['meta'].split(' · ')[1])}</span></span>
</button>"""


def build():
    home()
    hochzeitsfilm()
    imagefilm()
    eventvideo()
    portfolio()
    pakete()


# ------------------------------------------------------------------ Home
def home():
    works = "".join(work_item(w, i) for i, w in enumerate(WORKS[:7]))
    body = f"""
<section class="hero hero--video">
  <div class="container">
    <div class="eyebrow">Videograf · {esc(C)} &amp; NRW</div>
    <h1 class="h-display h-display--m">Hochzeitsfilm, Imagefilm &amp; Eventvideo <em>aus {esc(C)}.</em></h1>
    <div class="hero__grid" style="margin-top:2rem">
      <p class="lede" style="margin:0">Ich filme so, dass du dich beim Anschauen daran erinnerst, wie es sich angefühlt hat. Nicht nur, wie es aussah. Leise Kamera, natürliches Licht, saubere Tonspur, ein Schnitt mit Rhythmus.</p>
      <div class="btn-row" style="margin:0"><a class="btn btn--primary" href="/kontakt/?anfrage=video-hochzeit#formular">Termin anfragen {ARROW}</a><a class="btn" href="/video/portfolio/">Portfolio</a></div>
    </div>
    <div class="showreel reveal">
      <button class="work" type="button" data-lightbox data-title="Showreel" style="display:block;width:100%" aria-label="Showreel ansehen">
        {frame(tone=6, tag="Showreel", tc="TC 00:00:04:12 · 25 FPS · 4K", ar="21/9", img="showreel", alt="Showreel-Standbild", cine=True, play="Showreel ansehen", el="span")}
      </button>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="leistungen-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="leistungen-h">Was ich <em>filme</em></h2>
      <p class="reveal" data-delay="1">Drei Schwerpunkte, bei denen ich weiß, worauf es ankommt. Dazu Social-Cuts und Drohnenaufnahmen nach Bedarf.</p>
    </div>
    <div class="svc-grid">
      <a class="svc reveal" href="/video/hochzeitsfilm/"><span class="svc__no">01</span><h3>Hochzeitsfilm</h3><p>Getting Ready, Trauung, Reden, Tanz. Ein Film, den ihr in zehn Jahren noch gerne anseht.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
      <a class="svc reveal" href="/video/imagefilm/"><span class="svc__no">02</span><h3>Imagefilm</h3><p>Dein Unternehmen, so erzählt, dass man dort arbeiten, kaufen oder bestellen möchte.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
      <a class="svc reveal" href="/video/eventvideo/"><span class="svc__no">03</span><h3>Eventvideo</h3><p>Aftermovie, Konferenz, Jubiläum. Auf Wunsch mit Same-Day-Edit, der noch am Abend läuft.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
    </div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="work-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="work-h">Ausgewählte <em>Arbeiten</em></h2>
      <p class="reveal" data-delay="1">Klick auf einen Film. Das Video lädt erst dann, vorher passiert keine Verbindung zu Drittanbietern.</p>
    </div>
    <div class="work-grid">{works}</div>
    <p style="margin-top:2.5rem"><a class="link-arrow" href="/video/portfolio/">Gesamtes Portfolio {ARROW}</a></p>
  </div>
</section>

<section class="section" aria-labelledby="ablauf-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="ablauf-h">Vom ersten Gespräch <em>zum Film</em></h2>
      <p class="reveal" data-delay="1">Klare Schritte, feste Termine, keine Überraschungen bei der Lieferung.</p>
    </div>
    <ol class="process reveal">
      <li><h3>Gespräch</h3><p>Du erzählst, was du vorhast. Ich stelle Fragen, schlage Formate vor und nenne dir einen Festpreis.</p></li>
      <li><h3>Konzept</h3><p>Bei Imagefilmen mit Storyboard und Drehplan, bei Hochzeiten mit einem Ablauf, der auch Fotograf:in und Location kennt.</p></li>
      <li><h3>Dreh</h3><p>Zurückhaltend, mit leichtem Setup. Ich bin da, aber nicht im Weg. Ton wird separat mit Funkmikrofonen aufgenommen.</p></li>
      <li><h3>Schnitt &amp; Lieferung</h3><p>Farbkorrektur, Sounddesign, zwei Korrekturschleifen. Lieferung als Download-Link und auf Wunsch auf USB.</p></li>
    </ol>
  </div>
</section>

<section class="section section--alt" aria-label="Technik und Fakten">
  <div class="container">
    <div class="facts reveal">
      <div class="fact"><b>4K</b><span>Aufnahme in 10-Bit-Farbe für saubere Farbkorrektur</span></div>
      <div class="fact"><b>2</b><span>Kameras parallel bei Trauung und Reden</span></div>
      <div class="fact"><b>6–8</b><span>Wochen bis zur Lieferung des Highlightfilms</span></div>
      <div class="fact"><b>3×</b><span>Datensicherung des Rohmaterials bis zur Abnahme</span></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="look-h">
  <div class="container two-col">
    <div class="reveal">{frame(tone=2, tag="Kamera", tc="ISO 800 · 1/50 · F2.0", ar="4/5", alt="Kamera und Gimbal im Einsatz", img="video-set", extra="portrait")}</div>
    <div>
      <div class="eyebrow">Der Look</div>
      <h2 class="h-2 reveal" id="look-h">Filmisch, aber <em>nicht</em> künstlich</h2>
      <div class="prose reveal" style="margin-top:1.5rem">
        <p>Mir ist ein ehrlicher Ton wichtiger als eine Instagram-Filter-Ästhetik. Ich drehe mit lichtstarken Festbrennweiten, vorzugsweise mit vorhandenem Licht. Bei Bedarf kommt eine kleine LED-Leuchte dazu, aber nie ein Scheinwerferpark.</p>
        <p>Ton ist die halbe Wirkung. Reden und Gelübde nehme ich deshalb immer separat mit Funkmikrofon auf, damit man jedes Wort versteht, auch wenn der Wind weht.</p>
        <ul><li>Gimbal und Slider für ruhige Bewegung</li><li>Drohnenaufnahmen im Rahmen der EU-Vorschriften, wenn es die Location erlaubt</li><li>Lizenzierte Musik, damit der Film auch online ohne Probleme geteilt werden kann</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container"><div class="eyebrow">Kombiniert buchen</div>
    <div class="two-col two-col--wide-left" style="align-items:center">
      <p class="lede reveal">Wer feiert, will die Musik nicht vergessen. Ich lege auch als DJ auf. Beides aus einer Hand ist entspannter und bringt den besten Ton in den Film.</p>
      <p class="reveal" data-delay="1"><a class="btn" href="/dj/">Zum DJ-Bereich {ARROW}</a></p>
    </div>
  </div>
</section>
"""
    faq = [
        ("Wie lange dauert es, bis ich meinen Film bekomme?", "Bei Hochzeiten liefere ich Trailer innerhalb von zwei Wochen und den Highlightfilm in der Regel nach sechs bis acht Wochen. Imagefilme dauern nach dem Dreh meist vier bis sechs Wochen."),
        ("Welche Aufträge nimmst du an?", "Hochzeiten, Imagefilme, Event- und Recruiting-Videos in " + C + " und NRW. Für weiter entfernte Aufträge kalkuliere ich Reisekosten fair mit ein."),
        ("Darf ich die Filme online teilen?", "Ja, ausdrücklich. Du bekommst die Nutzungsrechte für private Nutzung bzw. die vereinbarte gewerbliche Nutzung schriftlich."),
    ]
    write_page("/video/", f"Videograf {C}: Hochzeitsfilm, Imagefilm & Eventvideo | {SITE['name']}",
               f"Videograf aus {C}: Hochzeitsfilme, Imagefilme und Eventvideos in 4K mit Ton, der stimmt. Festpreis, klare Lieferzeit. Jetzt Termin anfragen.",
               body + f'<section class="section" aria-labelledby="faq-h"><div class="container two-col two-col--wide-left" style="align-items:start"><div><div class="eyebrow">FAQ</div><h2 class="h-2" id="faq-h">Kurz <em>beantwortet</em></h2></div><div class="reveal">{faq_html(faq)}</div></div></section>'
               + cta_band("Erzähl mir <em>von</em> deinem Projekt", "Datum, Ort, Anlass – das genügt für die erste Antwort. Innerhalb von 24 Stunden bekommst du eine ehrliche Einschätzung.", "Termin anfragen", "/kontakt/?anfrage=video-hochzeit#formular"),
               world="video", current="/video/", faq=faq, lightbox_on=True, priority="0.9",
               schema=[business_schema(), service_schema(f"Videograf {C}", "Hochzeitsfilm, Imagefilm und Eventvideo", "/video/", "Videografie")],
               crumbs=[("Start", "/"), ("Video", "/video/")])


# ------------------------------------------------------------------ Hochzeitsfilm
def hochzeitsfilm():
    faq = [
        ("Was kostet ein Hochzeitsfilm in " + C + "?", "Hochzeitsfilme beginnen bei 1.490 €. Der Preis richtet sich nach Drehzeit, Anzahl der Kameras, Filmformaten und Zusatzleistungen wie Drohne. Details auf der <a href='/video/pakete/'>Paketseite</a>."),
        ("Wie lange begleitest du uns?", "Von etwa vier Stunden (Trauung, Paarshooting, Empfang) bis zum ganzen Tag. Viele Paare wählen ab dem Getting Ready bis zum Anschnitt, ca. acht bis zehn Stunden."),
        ("Welche Filmformate gibt es?", "Der Highlightfilm (4 bis 6 Minuten) ist der Klassiker. Dazu ein Trailer fürs Teilen, optional ein Dokumentarfilm (20 bis 40 Minuten) mit Trauung und Reden ungekürzt."),
        ("Kannst du auch Drohne?", "Ja, wenn Location und Wetter es erlauben. Ich fliege nach den EU-Regeln und kläre die Erlaubnis vorher mit der Location ab."),
        ("Darf ich mir die Musik wünschen?", "Ja. Ich nutze lizenzierte Musik, damit der Film bei Instagram, YouTube oder auf der Hochzeitswebsite problemlos läuft. Du kannst Stimmung und Genre vorgeben. Euren Hochzeitssong binde ich gerne ein, wenn rechtlich möglich."),
        ("Stört die Kamera nicht die Stimmung?", "Ich arbeite leise und unauffällig, ohne Kameralicht ins Gesicht. Viele Gäste vergessen nach den ersten Minuten, dass ich da bin. Das ist die beste Voraussetzung für echte Momente."),
    ]
    service_page(
        "video", "/video/hochzeitsfilm/", f"Hochzeitsfilm {C}: Videograf für Trauung, Reden & Feier",
        f"Hochzeitsfilm in {C} und NRW: Highlightfilm, Trailer und Dokumentation in 4K, mit separatem Ton für Reden und Gelübde. Festpreis, klare Lieferzeit.",
        f"Hochzeitsfilm in <em>{C}</em> &amp; NRW", "Fotos zeigen, wie ihr aussaht. Ein Film zeigt, wie es klang, als sie Ja gesagt hat, wie Opa gelacht hat und welcher Tanz eure Gäste von den Stühlen geholt hat.",
        "Video · Hochzeitsfilm", [("Start", "/"), ("Video", "/video/"), ("Hochzeitsfilm", "/video/hochzeitsfilm/")],
        """<h2>Dokumentarisch statt gestellt</h2>
<p>Ich filme eure Hochzeit so, wie sie passiert. Wenige Regieanweisungen, keine zehnmal wiederholte Szene. Das Paarshooting plane ich mit dem Fotografen zusammen, damit ihr nicht doppelt posieren müsst.</p>
<p>Der fertige Film hat einen Spannungsbogen: leise Momente, laute Momente, zum Schluss eine Pointe. Dafür sichte und schneide ich das Material von Hand, nicht über Vorlagen. Das merkt man.</p>
<h2>Formate</h2>
<ul><li><strong>Trailer</strong> (1 bis 2 Minuten): schnell geteilt, innerhalb von zwei Wochen fertig</li><li><strong>Highlightfilm</strong> (4 bis 6 Minuten): der Film, den ihr euch immer wieder anseht</li><li><strong>Dokumentation</strong> (20 bis 40 Minuten): Trauung und Reden ungekürzt, mit sauberem Ton</li></ul>""",
        ["Begleitung vom Getting Ready bis zur Party (nach Paket)", "Zwei Kameras bei Trauung und Reden", "Separate Tonaufnahme mit Funkmikrofon", "Farbkorrektur und Sounddesign", "Lizenzierte Musik", "Zwei Korrekturschleifen", "Lieferung als Online-Galerie und auf USB-Stick", "Vorgespräch und Location-Check"],
        "Im Preis enthalten",
        timeline=("Der <em>Weg</em> zu eurem Film", "Von der ersten Nachricht bis zur Abnahme: So läuft die Zusammenarbeit.", [
            ("Woche −12", "Kennenlernen", "Videocall oder Treffen. Wir klären Stil, Tag, Dauer und Wünsche. Ihr bekommt ein verbindliches Angebot."),
            ("Woche −2", "Ablauf & Location-Check", "Ich stimme den Zeitplan mit Fotograf:in, DJ und Trauredner:in ab. Falls nötig, schaue ich mir die Location vorab an."),
            ("Tag X", "Dreh", "Unauffällig mit Gimbal, Zweitkamera und Funkton. Ich bin da, wenn es zählt, und gehe aus dem Weg, wenn es nicht passt."),
            ("+2 Wochen", "Trailer", "Eine erste Vorschau, damit ihr den Film schon teilen könnt."),
            ("+6 bis 8 Wochen", "Highlightfilm", "Fertiger Schnitt mit Farbkorrektur und Sounddesign. Zwei Korrekturschleifen sind inklusive."),
        ]),
        notes=("Gut zu <em>wissen</em>", [
            ("Zusammenarbeit mit Fotograf:in", "Ich arbeite mit vielen Fotografen zusammen und stimme Zeiten und Positionen ab, damit niemand im Bild des anderen steht."),
            ("Rechte & Datenschutz", "Gäste werden gefilmt. Ihr könnt vorab eine Info an eure Gäste geben (Textvorlage bekommt ihr von mir). Wer nicht gefilmt werden möchte, wird respektiert."),
            ("Sicherung", "Das Rohmaterial speichere ich dreifach, auch nach Lieferung des Films noch mindestens zwölf Monate."),
        ]),
        faq=faq,
        links=[("Hochzeits-DJ vom selben Anbieter", "/dj/hochzeit/"), ("Pakete &amp; Preise", "/video/pakete/"), ("Ratgeber: Was kostet ein Hochzeitsfilm?", "/ratgeber/hochzeitsfilm-kosten/")],
        cta=("Euer Datum <em>noch frei?</em>", "Schreib mir Datum und Location. Ich antworte innerhalb von 24 Stunden mit Verfügbarkeit und Preis.", "Hochzeitsfilm anfragen", "/kontakt/?anfrage=video-hochzeit#formular"),
        banner=dict(tone=6, tag="Hochzeitsfilm", tc="CAM A · 16:42:09", ar="21/8", alt="Standbild aus einem Hochzeitsfilm", img="video-hochzeit-banner", cine=True),
        service_name=f"Hochzeitsfilm {C}", service_kind="Hochzeitsvideografie",
        primary=("Hochzeitsfilm anfragen", "/kontakt/?anfrage=video-hochzeit#formular"), secondary=("Pakete ansehen", "/video/pakete/"), priority="0.9")


# ------------------------------------------------------------------ Imagefilm
def imagefilm():
    faq = [
        ("Was kostet ein Imagefilm?", "Imagefilme starten bei etwa 1.900 €. Ein Drehtag mit Konzept, Schnitt und zwei Social-Cuts liegt meist zwischen 2.500 und 4.500 €. Genauere Zahlen nenne ich nach einem kurzen Briefing."),
        ("Wie läuft ein Dreh bei uns im Betrieb ab?", "Wir klären Ablauf und Sicherheit vorab. Gedreht wird mit kleinem Team, ohne Betriebsstörung. Interviews finden an ruhigen Orten statt, Arbeitsabläufe werden im echten Tempo gezeigt."),
        ("Brauchen wir ein fertiges Drehbuch?", "Nein. Ich entwickle mit dir Idee, Botschaft und Storyboard. Dafür reicht ein 45-Minuten-Gespräch und ein paar Eckdaten zu deinen Kunden oder Bewerbern."),
        ("Bekommen wir den Film auch für Social Media?", "Ja. Auf Wunsch schneide ich zusätzliche Hochformat-Clips (9:16) mit Untertiteln für Instagram, TikTok und LinkedIn."),
        ("Wem gehören die Rechte?", "Du bekommst ein klar definiertes Nutzungsrecht, schriftlich im Angebot. Das Rohmaterial bleibt bei mir, kann aber gegen Aufpreis erworben werden."),
    ]
    service_page(
        "video", "/video/imagefilm/", f"Imagefilm {C}: Unternehmensvideo, Recruiting & Produktfilm",
        f"Imagefilm und Unternehmensvideo aus {C}: Konzept, Dreh, Schnitt und Social-Cuts aus einer Hand. Für Handwerk, Gastro, Praxis, Start-ups und Mittelstand.",
        f"Imagefilm &amp; <em>Unternehmensvideo</em>", "Ein guter Imagefilm erklärt nicht, was du alles kannst. Er zeigt, wie es sich anfühlt, mit dir zu arbeiten. Menschen vertrauen Gesichtern und Händen, nicht Slogans.",
        "Video · Imagefilm", [("Start", "/"), ("Video", "/video/"), ("Imagefilm", "/video/imagefilm/")],
        """<h2>Echt statt Stockfoto-Optik</h2>
<p>Kunden und Bewerber sehen in Sekunden, ob ein Video ehrlich ist. Deshalb zeige ich echte Menschen bei echter Arbeit, keine gestellten Lächel-Szenen. Dazu ein klarer roter Faden: Wer bist du, was macht dich besonders, was soll der Zuschauer tun?</p>
<h2>Wofür Unternehmen Videos nutzen</h2>
<ul><li>Startseite und Landingpages, die Vertrauen aufbauen</li><li>Recruiting: Bewerbende lernen Team und Kultur kennen</li><li>Produkt- und Dienstleistungserklärungen</li><li>Social-Media-Serien und Kurzclips</li><li>Messe und Präsentationen</li></ul>
<h2>Zielgruppen</h2>
<p>Handwerk, Gastronomie, Arztpraxen und Kliniken, Immobilien, Start-ups, Dienstleister und Mittelstand, vor allem in " + C + " und NRW.</p>""".replace('" + C + "', C),
        ["Briefing-Workshop (ca. 45 Minuten)", "Konzept, Storyboard und Drehplan", "Dreh in 4K mit Funkton für Interviews", "Schnitt, Farbkorrektur, Sounddesign", "Lizenzierte Musik, Untertitel", "Zwei Hochformat-Cutdowns für Social Media", "Zwei Korrekturschleifen"],
        "Typischer Umfang",
        timeline=("Vom Briefing <em>zum Film</em>", "Ein Imagefilm ist ein Projekt, kein Dreh. Dafür gibt es einen klaren Ablauf.", [
            ("Schritt 1", "Briefing", "Ziel, Zielgruppe, Botschaft, Budget, Einsatzorte. Ich stelle Fragen, die du vielleicht noch nicht beantwortet hast."),
            ("Schritt 2", "Konzept & Storyboard", "Idee, Interviewfragen, Drehorte und Shotlist. Du gibst frei, bevor die Kamera läuft."),
            ("Schritt 3", "Dreh", "Ein halber oder ganzer Tag. Interviews, Arbeitsszenen, Details und Außenaufnahmen."),
            ("Schritt 4", "Schnitt", "Erster Entwurf nach ca. zwei Wochen, danach zwei Korrekturschleifen."),
            ("Schritt 5", "Lieferung", "Alle Formate, Social-Cuts und Untertitel in einem Paket."),
        ]),
        faq=faq,
        links=[("Portfolio ansehen", "/video/portfolio/"), ("Pakete &amp; Preise", "/video/pakete/"), ("Eventvideo", "/video/eventvideo/")],
        cta=("Was soll <em>dein Film</em> bewirken?", "Beschreib mir kurz dein Vorhaben. Ich antworte mit Einschätzung, Ablauf und Preisrahmen.", "Imagefilm anfragen", "/kontakt/?anfrage=video-firma#formular"),
        banner=dict(tone=2, tag="Imagefilm", tc="CAM A · 10:14:22", ar="21/8", alt="Dreh eines Imagefilms im Unternehmen", img="video-imagefilm-banner", cine=True),
        service_name=f"Imagefilm {C}", service_kind="Unternehmensvideo",
        primary=("Imagefilm anfragen", "/kontakt/?anfrage=video-firma#formular"), secondary=("Pakete ansehen", "/video/pakete/"))


# ------------------------------------------------------------------ Eventvideo
def eventvideo():
    faq = [
        ("Was ist ein Same-Day-Edit?", "Ein kurzer Clip (1 bis 2 Minuten), der noch während des Events fertiggestellt und vor den Gästen gezeigt wird. Das sorgt für einen Gänsehautmoment und ist ein Highlight bei Hochzeiten, Jubiläen und Galas."),
        ("Was kostet ein Eventvideo?", "Ein Aftermovie für ein vierstündiges Event kostet in der Regel zwischen 900 und 1.800 €. Mehrkamera-Mitschnitte und Same-Day-Edit werden einzeln kalkuliert."),
        ("Kannst du ein Event live streamen?", "Für Konferenzen und Reden gibt es Livestream-Setups mit Mehrkamera und Ton. Das kalkuliere ich als Zusatzmodul."),
        ("Ist eine Kombination mit DJ möglich?", "Ja. Ich kenne den Ablauf der Musik und plane Aufnahmen für die Höhepunkte des Abends. Du sparst dir einen zweiten Ansprechpartner."),
    ]
    service_page(
        "video", "/video/eventvideo/", f"Eventvideo & Aftermovie in {C}: Firmenfeier, Konferenz, Party",
        f"Eventvideo und Aftermovie in {C}: Firmenfeiern, Konferenzen, Jubiläen und Partys. Mit Same-Day-Edit, Mehrkamera und sauberem Ton. Jetzt anfragen.",
        f"Eventvideo &amp; <em>Aftermovie</em>", "Events sind schnell vorbei. Ein guter Aftermovie hält die Stimmung fest, zeigt Gäste und Programm und macht die nächste Veranstaltung leichter zu verkaufen.",
        "Video · Eventvideo", [("Start", "/"), ("Video", "/video/"), ("Eventvideo", "/video/eventvideo/")],
        """<h2>Wenn die Zeit knapp ist</h2>
<p>Bei Events habe ich keine zweite Chance. Deshalb plane ich vorab, wann welche Programmpunkte anstehen, wo ich stehen muss und welche Momente nicht verpasst werden dürfen. Der Ablauf kommt von dir oder der Agentur, ich ergänze mit Kameraposition und Tonplan.</p>
<h2>Formate</h2>
<ul><li><strong>Aftermovie</strong> (1 bis 2 Minuten): Stimmung, Gäste, Highlights</li><li><strong>Same-Day-Edit</strong>: noch am Abend gezeigt</li><li><strong>Mitschnitt</strong>: Reden, Keynotes oder Panels mit mehreren Kameras</li><li><strong>Social-Clips</strong>: Hochformat für Reels und Stories</li></ul>
<h2>Einsatzbereiche</h2>
<p>Firmenfeiern, Konferenzen, Jubiläen, Konzerte, Vereinsfeste, Galas, Messeauftritte, private Partys.</p>""",
        ["Ablauf- und Kameraplanung vorab", "Mehrkamera-Setup optional", "Tonmitschnitt von Reden und Panels", "Aftermovie in 4K inklusive Musik-Lizenz", "Optional: Same-Day-Edit", "Hochformat-Clips für Social Media", "Lieferung per Download-Link"],
        "Das ist dabei",
        faq=faq,
        links=[("DJ für dasselbe Event", "/dj/firmenevents/"), ("Portfolio ansehen", "/video/portfolio/"), ("Pakete &amp; Preise", "/video/pakete/")],
        cta=("Welches Event <em>steht an?</em>", "Datum, Ort, Anlass, grobe Dauer: Danach bekommst du eine Einschätzung und einen Festpreis.", "Eventvideo anfragen", "/kontakt/?anfrage=video-firma#formular"),
        banner=dict(tone=5, tag="Event", tc="CAM B · 21:33:51", ar="21/8", alt="Standbild aus einem Eventvideo", img="video-event-banner", cine=True),
        service_name=f"Eventvideo {C}", service_kind="Eventvideografie",
        primary=("Eventvideo anfragen", "/kontakt/?anfrage=video-firma#formular"), secondary=("Pakete ansehen", "/video/pakete/"))


# ------------------------------------------------------------------ Portfolio
def portfolio():
    items = "".join(work_item(w, i) for i, w in enumerate(WORKS))
    body = f"""{crumbs_html([("Start", "/"), ("Video", "/video/"), ("Portfolio", "/video/portfolio/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Video · Portfolio</div>
    <h1 class="h-1 page-hero--wide">Arbeiten, die <em>für sich</em> sprechen</h1>
    <p class="lede">Hochzeiten, Unternehmen, Events. Wähle eine Kategorie und starte einen Film. Das Video lädt erst nach deinem Klick.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">
    <div class="chips work-filter" role="group" aria-label="Filter">
      <button class="chip" type="button" data-filter="alle" aria-pressed="true">Alle</button>
      <button class="chip" type="button" data-filter="hochzeit" aria-pressed="false">Hochzeit</button>
      <button class="chip" type="button" data-filter="imagefilm" aria-pressed="false">Imagefilm</button>
      <button class="chip" type="button" data-filter="event" aria-pressed="false">Event</button>
      <button class="chip" type="button" data-filter="social" aria-pressed="false">Social</button>
    </div>
    <div class="work-grid">{items}</div>
  </div>
</section>
{cta_band("Gefällt dir <em>der Stil?</em>", "Dann lass uns über dein Projekt sprechen. Ich antworte innerhalb von 24 Stunden.", "Projekt anfragen", "/kontakt/?anfrage=video-hochzeit#formular")}
"""
    write_page("/video/portfolio/", f"Videograf Portfolio {C}: Hochzeitsfilme, Imagefilme, Events",
               f"Portfolio des Videografen aus {C}: Hochzeitsfilme, Imagefilme, Eventvideos und Social-Clips. Jetzt Beispiele ansehen und Projekt anfragen.",
               body, world="video", current="/video/portfolio/", lightbox_on=True,
               crumbs=[("Start", "/"), ("Video", "/video/"), ("Portfolio", "/video/portfolio/")])


# ------------------------------------------------------------------ Pakete
def pakete():
    faq = [
        ("Wie läuft die Buchung ab?", "Nach unserem Gespräch bekommst du ein schriftliches Angebot. Mit Unterschrift und 30 % Anzahlung ist dein Termin reserviert. Der Rest ist nach der Abnahme fällig."),
        ("Was gehört zur Lieferung?", "Der fertige Film als Download (MP4, 4K und Full-HD), auf Wunsch zusätzlich auf USB-Stick. Social-Cuts und Trailer je nach Paket."),
        ("Was, wenn das Wetter schlecht ist?", "Dann filme ich trotzdem. Regen kann sogar für starke Bilder sorgen. Bei Drohnenflügen entscheide ich nach Sicherheitslage, nicht nach Wunsch."),
        ("Kann ich DJ und Video kombinieren?", "Ja, das ist möglich und spart Aufwand. Im Kombi-Paket erhältst du einen Preisvorteil. Dafür einfach im <a href='/kontakt/?anfrage=kombi#formular'>Formular</a> „Kombi“ auswählen."),
    ]
    tiers = [
        ("Moment", "1.490", "Trauung, Empfang und Paarshooting", ["Bis zu 4 Stunden Dreh", "Highlightfilm 3 bis 4 Min.", "Funkton für Trauung", "Lizenzierte Musik", "Online-Lieferung"], False),
        ("Tag", "2.190", "Vom Getting Ready bis zum Anschnitt", ["Bis zu 8 Stunden Dreh", "Highlightfilm 4 bis 6 Min. + Trailer", "Zweite Kamera bei Trauung &amp; Reden", "Drohnenaufnahmen, wenn erlaubt", "USB-Stick inklusive"], True),
        ("Ganz", "2.990", "Ganzer Tag plus Dokumentation", ["Bis zu 12 Stunden Dreh", "Highlightfilm, Trailer, Dokumentation", "Same-Day-Edit für die Feier", "Zwei Kameras durchgehend", "Rohmaterial-Archiv 12 Monate"], False),
    ]
    cards = ""
    for name, price, who, feats, hot in tiers:
        flag = '<span class="tier__flag">Beliebt</span>' if hot else ""
        cls = "tier tier--hot reveal" if hot else "tier reveal"
        btn_cls = "btn btn--primary" if hot else "btn"
        li = "".join(f"<li>{f}</li>" for f in feats)
        cards += f"""<article class="{cls}">{flag}<h3>{name}</h3><div class="tier__price"><small>ab</small>{price} €</div><p class="tier__for muted">{who}</p><ul>{li}</ul><a class="{btn_cls}" href="/kontakt/?anfrage=video-hochzeit#formular">{name} anfragen {ARROW}</a></article>"""
    biz = [("Imagefilm (Basis)", "ab 1.900 €", "1 Drehtag, Konzept, Schnitt, 2 Social-Cuts"), ("Imagefilm (Plus)", "ab 3.400 €", "Mehrere Drehorte, Interviews, Recruiting-Fokus"),
           ("Eventvideo / Aftermovie", "ab 900 €", "Bis 4 Stunden, 1 bis 2 Minuten Film"), ("Same-Day-Edit", "ab 600 €", "Zusatzmodul, Clip noch am Abend"),
           ("Social-Clips (3 Stück)", "ab 450 €", "Hochformat 9:16, mit Untertiteln"), ("Drohnenaufnahmen", "ab 250 €", "Je Location, nach EU-Regeln")]
    biz_html = '<div class="addons">' + "".join(f'<div class="addon"><div><b>{a}</b><br><span>{d}</span></div><em>{p}</em></div>' for a, p, d in biz) + "</div>"
    body = f"""{crumbs_html([("Start", "/"), ("Video", "/video/"), ("Pakete", "/video/pakete/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Video · Pakete &amp; Preise</div>
    <h1 class="h-1 page-hero--wide">Pakete für <em>Hochzeit</em> &amp; Business</h1>
    <p class="lede">Hochzeitsfilme gibt es als Pakete. Business-Projekte kalkuliere ich nach Briefing. In beiden Fällen bekommst du einen Festpreis, bevor du dich festlegst.</p>
  </div>
</section>
<section class="section" aria-label="Hochzeitspakete">
  <div class="container"><div class="tiers">{cards}</div>
    <p class="muted" style="margin-top:1.5rem;font-size:.9rem">Alle Preise inkl. gesetzlicher MwSt. Richtwerte für Veranstaltungen im Raum {esc(C)}; das verbindliche Angebot erhältst du nach unserem Gespräch.</p>
  </div>
</section>
<section class="section section--alt" aria-labelledby="biz-h">
  <div class="container"><div class="split-head"><h2 class="h-2 reveal" id="biz-h">Business &amp; <em>Events</em></h2><p class="reveal" data-delay="1">Richtwerte für typische Projekte. Dein Angebot hängt von Umfang und Anforderungen ab.</p></div><div class="reveal">{biz_html}</div></div>
</section>
<section class="section" aria-labelledby="faq-h">
  <div class="container two-col two-col--wide-left" style="align-items:start"><div><div class="eyebrow">FAQ</div><h2 class="h-2" id="faq-h">Rund um <em>Buchung</em></h2></div><div class="reveal">{faq_html(faq)}</div></div>
</section>
{cta_band("Welches Paket <em>passt?</em>", "Sag mir, was du planst. Ich empfehle, was nötig ist, nicht das teuerste Paket.", "Angebot anfragen", "/kontakt/?anfrage=video-hochzeit#formular")}
"""
    write_page("/video/pakete/", f"Videograf Preise: Hochzeitsfilm ab 1.490 € in {C}",
               f"Preise und Pakete für Hochzeitsfilm, Imagefilm und Eventvideo in {C}: transparente Richtwerte, Festpreis nach Gespräch, Antwort in 24 Stunden.",
               body, world="video", current="/video/pakete/", faq=faq, priority="0.8",
               crumbs=[("Start", "/"), ("Video", "/video/"), ("Pakete", "/video/pakete/")])
