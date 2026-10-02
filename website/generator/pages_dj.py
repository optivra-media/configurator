"""DJ-Bereich: Startseite, Leistungsseiten, Musik & Technik, Pakete."""
from core import (ARROW, SITE, cta_band, crumbs_html, esc, faq_html, frame, related, service_schema, write_page, business_schema)
from service_page import service_page

C = SITE["city"]
MIXES = [  # url = Embed-URL (SoundCloud/Mixcloud-Widget). Leer lassen => "Hörprobe anfragen".
    {"tag": "Warm-up · 118 BPM", "title": "Sundowner Selection", "sub": "Disco, Nu-Disco, Deep House. Für Sektempfang und Dinner.", "url": "", "seed": 3},
    {"tag": "Wedding · 100–128 BPM", "title": "Dancefloor Wedding Set", "sub": "Von Motown bis Dua Lipa. Alle Generationen auf der Fläche.", "url": "", "seed": 7},
    {"tag": "Club · 122–128 BPM", "title": "After Midnight", "sub": "House, Tech-House und ein bisschen Chaos zur späten Stunde.", "url": "", "seed": 11},
]
GENRES = ["House", "Disco & Funk", "Hip-Hop", "R&B", "Pop & Charts", "80er", "90er", "2000er", "Latin & Afrobeats",
          "Schlager (ja, wirklich)", "Oldies & Swing", "Techno", "Deutschrap", "Rock-Klassiker"]


def mix_cards():
    out = []
    for m in MIXES:
        if m["url"]:
            action = (f'<button class="mix__play" data-embed="{esc(m["url"])}" data-title="{esc(m["title"])}">'
                      f'<i><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 3.5v17l14-8.5z"/></svg></i>Mix abspielen</button>')
        else:
            action = ('<a class="mix__play" href="/kontakt/?anfrage=dj-hochzeit#formular"><i>'
                      '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 3.5v17l14-8.5z"/></svg></i>Hörprobe anfragen</a>')
        out.append(f"""<article class="mix reveal">
  <div class="mix__top"><span>{esc(m['tag'])}</span><span>Mix</span></div>
  <div class="wave" data-seed="{m['seed']}" aria-hidden="true"></div>
  <div><h3>{esc(m['title'])}</h3><p class="muted" style="margin:.4rem 0 0">{esc(m['sub'])}</p></div>
  {action}
</article>""")
    return '<div class="mixes">' + "".join(out) + "</div>"


def build():
    home()
    hochzeit()
    firmen()
    privat()
    technik()
    pakete()


# ------------------------------------------------------------------ Home
def home():
    marquee = "".join(f"<span>{esc(g)}</span>" for g in GENRES) * 2
    body = f"""
<section class="hero hero--dj">
  <div class="eq" data-eq="44" aria-hidden="true"></div>
  <div class="container">
    <div class="eyebrow">DJ · {esc(C)} &amp; NRW</div>
    <h1 class="h-display h-display--m">Hochzeits- &amp; Event-DJ <em>aus {esc(C)}.</em></h1>
    <p class="lede">Ich spiele keine Playlist ab, ich beobachte die Tanzfläche. Wer sich gerade traut, wer eine Pause braucht, wann die Großeltern mitmachen wollen. Dazu ein Sound, der in der Scheune genauso sitzt wie im Hotelballsaal.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="/kontakt/?anfrage=dj-hochzeit#formular">Termin anfragen {ARROW}</a>
      <a class="btn" href="/dj/musik-technik/#mixes">Mixe anhören</a>
    </div>
    <div class="hero__badge">
      <span><b>Live gemixt</b> · kein Autoplay</span><span><b>Eigene Technik</b> · inklusive Backup</span><span><b>Festpreis</b> · inkl. Aufbau</span>
    </div>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee__track">{marquee}</div></div>

<section class="section" aria-labelledby="leistungen-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="leistungen-h">Drei Anlässe, <em>ein</em> Prinzip</h2>
      <p class="reveal" data-delay="1">Der Abend gehört deinen Gästen, nicht meinem Geschmack. Deshalb frage ich erst, höre dann zu und lege danach auf.</p>
    </div>
    <div class="svc-grid">
      <a class="svc reveal" href="/dj/hochzeit/"><span class="svc__no">01</span><h3>Hochzeits-DJ</h3><p>Vom Sektempfang bis zur letzten Runde. Mit Moderation, wenn du sie willst, und ohne, wenn nicht.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
      <a class="svc reveal" href="/dj/firmenevents/"><span class="svc__no">02</span><h3>Firmenevents</h3><p>Sommerfest, Weihnachtsfeier, Jubiläum, Messeabend. Dezent beim Dinner, danach so laut wie gewünscht.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
      <a class="svc reveal" href="/dj/private-partys/"><span class="svc__no">03</span><h3>Private Partys</h3><p>Geburtstag, Polterabend, Abschlussfeier. Du nennst die Richtung, ich baue den Abend drumherum.</p><span class="svc__go">Mehr dazu {ARROW}</span></a>
    </div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="ablauf-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="ablauf-h">So kommt der Abend <em>zustande</em></h2>
      <p class="reveal" data-delay="1">Vier Schritte, keine Formularschlacht. Du weißt jederzeit, woran du bist.</p>
    </div>
    <ol class="process reveal">
      <li><h3>Anfrage</h3><p>Datum, Ort, Anlass, grobe Gästezahl. Innerhalb von 24 Stunden bekommst du Antwort mit Verfügbarkeit und Preis.</p></li>
      <li><h3>Kennenlernen</h3><p>Kurzes Telefonat oder Videocall, ca. 20 Minuten. Du erzählst, ich höre zu und sage ehrlich, ob ich der Richtige bin.</p></li>
      <li><h3>Musik-Briefing</h3><p>Wunschliste, No-Go-Liste, Ablaufplan mit Location und Dienstleistern. Alles in einem Dokument.</p></li>
      <li><h3>Dein Abend</h3><p>Aufbau und Soundcheck zwei Stunden vor Gästeankunft. Du feierst, ich kümmere mich um den Rest.</p></li>
    </ol>
  </div>
</section>

<section class="section" aria-label="Fakten">
  <div class="container">
    <div class="facts reveal">
      <div class="fact"><b>2 h</b><span>Aufbau &amp; Soundcheck vor der Ankunft der Gäste</span></div>
      <div class="fact"><b>24 h</b><span>bis du eine Antwort auf deine Anfrage hast</span></div>
      <div class="fact"><b>2×</b><span>Equipment: Controller, Laptop und Mikrofon doppelt am Start</span></div>
      <div class="fact"><b>1</b><span>Festpreis. Aufbau, Technik und Soundcheck sind drin.</span></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="mixes" aria-labelledby="mix-h">
  <div class="container">
    <div class="split-head">
      <h2 class="h-1 reveal" id="mix-h">Hör <em>rein.</em></h2>
      <p class="reveal" data-delay="1">Drei Sets, drei Stimmungen. Die Player laden erst nach deinem Klick, vorher wird keine Verbindung zu Drittanbietern aufgebaut.</p>
    </div>
    {mix_cards()}
  </div>
</section>

<section class="section" aria-labelledby="technik-h">
  <div class="container two-col">
    <div>
      <div class="eyebrow">Technik</div>
      <h2 class="h-2 reveal" id="technik-h">Klingt gut. Sieht <em>unaufgeregt</em> aus.</h2>
      <p class="reveal muted" style="margin-top:1.5rem;max-width:46ch">Aktive PA mit Subwoofer in der passenden Größe, drahtloses Mikrofon, dezentes Lichtset und ein schwarzes DJ-Pult, das nicht nach Disco-Keller aussieht. Alles läuft über gesichertes Stromgeräte-Equipment und wird vor Ort durchgemessen.</p>
      <p class="reveal"><a class="link-arrow" href="/dj/musik-technik/">Technik &amp; Musikstile im Detail {ARROW}</a></p>
    </div>
    <div class="reveal" data-delay="1">{frame(tone=4, tag="DJ-Setup", tc="BPM 124 · KEY 8A", ar="4/3", alt="Platzhalter für ein Foto des DJ-Setups", img="dj-setup")}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container"><div class="eyebrow">Kombiniert buchen</div>
    <div class="two-col two-col--wide-left" style="align-items:center">
      <p class="lede reveal">Du willst dein Fest nicht nur hören, sondern später auch sehen? Ich bin auch Videograf. Beides aus einer Hand spart Abstimmung, und der Film kennt den Ablauf der Musik.</p>
      <p class="reveal" data-delay="1"><a class="btn" href="/video/">Zum Videograf-Bereich {ARROW}</a></p>
    </div>
  </div>
</section>
"""
    faq = [
        ("Wie früh sollte ich meinen DJ buchen?", "Für Hochzeiten in der Hauptsaison (Mai bis September) empfehle ich 9 bis 12 Monate Vorlauf, für Freitage und Samstage eher mehr. Kurzfristige Anfragen beantworte ich trotzdem, oft klappt es noch."),
        ("Spielst du Musikwünsche meiner Gäste?", "Ja, wenn sie zur Stimmung passen. Du gibst mir vorab eine Wunschliste und eine No-Go-Liste. Spontane Wünsche am Abend entscheide ich nach Gefühl für die Fläche, und ehrlich gesagt hat die Fläche meistens recht."),
        ("Was passiert, wenn dein Equipment ausfällt?", "Controller, Laptop und Mikrofon habe ich doppelt dabei. Ein Wechsel dauert Sekunden und fällt den Gästen nicht auf."),
    ]
    write_page("/dj/", f"Hochzeits-DJ & Event-DJ in {C} | {SITE['name']}",
               f"Hochzeits-DJ und Event-DJ in {C} und NRW: live gemixt, mit eigener Technik, Festpreis und Antwort in 24 Stunden. Jetzt Termin anfragen.",
               body + f'<section class="section section--alt" aria-labelledby="faq-h"><div class="container two-col two-col--wide-left" style="align-items:start"><div><div class="eyebrow">FAQ</div><h2 class="h-2" id="faq-h">Kurz <em>beantwortet</em></h2></div><div class="reveal">{faq_html(faq)}</div></div></section>'
               + cta_band("Welches Datum <em>hast du</em> im Kopf?", "Schreib mir Datum, Ort und Anlass. Du bekommst innerhalb von 24 Stunden eine ehrliche Antwort.", "Termin anfragen", "/kontakt/?anfrage=dj-hochzeit#formular"),
               world="dj", current="/dj/", faq=faq, priority="0.9",
               schema=[business_schema(), service_schema(f"DJ-Service in {C}", "Hochzeits-DJ, Firmenevents und private Partys", "/dj/", "DJ")],
               crumbs=[("Start", "/"), ("DJ", "/dj/")])


# ------------------------------------------------------------------ Hochzeit
def hochzeit():
    faq = [
        ("Was kostet ein Hochzeits-DJ in " + C + "?", "Meine Hochzeitspakete beginnen bei 1.190 €. Der Preis hängt von Spielzeit, Gästezahl, Anzahl der Beschallungsorte (z. B. Trauung im Garten, Feier im Saal) und Lichtwunsch ab. Alle Pakete findest du auf der <a href='/dj/pakete/'>Paketseite</a>."),
        ("Wie lange spielst du auf einer Hochzeit?", "Üblich sind sechs bis acht Stunden ab Sektempfang oder ab dem ersten Tanz. Bei längerer Planung gibt es Zusatzstunden zum festen Stundensatz, nichts wird am Abend neu verhandelt."),
        ("Kannst du auch die Trauung beschallen?", "Ja. Mit Funkmikrofonen für Redner:in und Brautpaar und einem kleinen Lautsprecherset, das unauffällig bleibt. Gerade bei freien Trauungen im Freien ist das oft das fehlende Puzzlestück."),
        ("Machst du Moderation?", "Auf Wunsch. Das reicht von „Das Buffet ist eröffnet“ bis zur Spielemoderation. Wer keine Ansagen möchte, bekommt Musik ohne Ansagen. Das besprechen wir vorher, nicht am Abend."),
        ("Brauchen wir eine Bühne oder besondere Voraussetzungen?", "Nein. Ich brauche etwa zwei mal zwei Meter Platz, zwei getrennte Steckdosen und trockene Bedingungen. Für Open-Air-Hochzeiten plane ich Wetterschutz mit ein."),
        ("Was ist mit unserem Eröffnungstanz?", "Gerne. Schick mir den Song früh, ich schneide ihn bei Bedarf auf die gewünschte Länge. Beim Soundcheck testen wir den Übergang noch einmal."),
    ]
    service_page(
        "dj", "/dj/hochzeit/", f"Hochzeits-DJ {C} & NRW: Musik, Technik, Moderation",
        f"Hochzeits-DJ in {C} und NRW: Beschallung von Trauung bis Tanzfläche, live gemixt, mit Musikbriefing, Backup-Technik und Festpreis. Jetzt Termin anfragen.",
        f"Hochzeits-DJ in <em>{C}</em> &amp; NRW", "Ein guter Hochzeits-DJ fällt nicht auf, bis er fehlt. Er sorgt dafür, dass Oma beim Sektempfang nicht gegen Bässe anschreien muss und trotzdem um 23 Uhr die Tanzfläche voll ist.",
        "DJ · Hochzeit", [("Start", "/"), ("DJ", "/dj/"), ("Hochzeit", "/dj/hochzeit/")],
        """<h2>Warum Hochzeiten anders sind als Partys</h2>
<p>Auf einer Hochzeit treffen vier Generationen, zwei Familien und zwei Freundeskreise aufeinander, die sich nicht kennen. Die Musik muss für alle funktionieren, ohne beliebig zu werden. Dafür hilft kein Genre-Rezept, sondern ein Gefühl dafür, wann ein Song auf der Tanzfläche gewinnt und wann er sie leert.</p>
<p>Deshalb arbeite ich vorab mit einem kurzen Musikbriefing: Welche Songs sind gesetzt, welche sind tabu, was lief auf eurer ersten gemeinsamen Autofahrt? Den Rest erledigt die Erfahrung am Abend. Ich lege live auf und reagiere auf das, was auf der Fläche passiert, statt eine fertige Liste abzuspulen.</p>
<h2>Was dich entspannt</h2>
<p>Ich kläre vorher Dinge, die später Stress machen: Wer gibt mir das Zeichen für den Eröffnungstanz? Wann ist der Anschnitt? Wie laut darf es nach 22 Uhr sein? Welche Reden stehen an? Alles landet in einem Ablaufplan, den ich auch mit Location, Fotograf:in und Trauredner:in abstimme.</p>""",
        ["Musikbriefing mit Wunsch- und No-Go-Liste", "Live-Mixing von Sektempfang bis zum letzten Song", "Aktive PA mit Subwoofer, passend zur Raumgröße", "Funkmikrofone für Reden und Trauung",
         "Dezentes Lichtset für die Tanzfläche", "Aufbau und Soundcheck, Abbau nach dem Ende", "Komplettes Ersatz-Equipment vor Ort", "Persönlicher Ablaufplan, abgestimmt mit Location &amp; Team"],
        "Im Preis enthalten",
        timeline=("Ein typischer <em>Hochzeitsabend</em>", "So sieht ein Ablauf häufig aus. Eure Hochzeit bekommt natürlich einen eigenen, aber die Struktur hilft bei der Planung.", [
            ("14:30", "Aufbau & Soundcheck", "Technik steht, bevor der erste Gast kommt. Ich teste Mikros an den Positionen, an denen später gesprochen wird."),
            ("16:00", "Trauung & Sektempfang", "Mikrofon für Trauung, danach unaufdringliche Hintergrundmusik. Gäste sollen reden, nicht rufen."),
            ("18:30", "Dinner", "Leise Lounge-Musik, Ansagen für Reden und Spiele nach Absprache. Lautstärke so, dass man am Tisch flüstern kann."),
            ("20:30", "Eröffnungstanz & Anschnitt", "Euer Song, Licht dimmen, kurze Ansage. Danach öffnet die Fläche."),
            ("21:00", "Tanzfläche", "Erst bekannte Titel für alle, dann Schritt für Schritt Tempo und Energie hoch."),
            ("00:00", "Mitternachtsmoment", "Pause für Snack, Überraschung oder Feuerwerk. Danach Round Two mit frischer Energie."),
            ("02:00", "Letzter Song", "Mit Ansage und Wunschsong des Brautpaars. Dann Licht an, Abbau, Heimweg."),
        ]),
        notes=("Gut zu <em>wissen</em>", [
            ("Anfahrt", "Im Umkreis von 40 km um " + C + " ist die Anfahrt im Preis enthalten. Darüber hinaus rechne ich eine faire Pauschale pro Kilometer, bei weiten Strecken mit Übernachtung."),
            ("Lautstärke &amp; Nachtruhe", "Ich messe vor Ort und spreche mit der Location ab, ab wann gedämpft wird. Wenn nötig, stelle ich auf leisere Titel um, ohne die Stimmung abzuwürgen."),
            ("GEMA", "Bei privaten Feiern im geschlossenen Kreis, zu denen Hochzeiten in der Regel zählen, fällt normalerweise keine GEMA-Gebühr an. Im Zweifel frag kurz bei der GEMA nach, ich helfe dir dabei."),
        ]),
        faq=faq,
        links=[("Hochzeitsfilm vom selben Tag", "/video/hochzeitsfilm/"), ("Pakete &amp; Preise", "/dj/pakete/"), ("Ratgeber: Hochzeits-DJ buchen", "/ratgeber/hochzeits-dj-buchen/")],
        cta=("Euer Datum <em>noch frei?</em>", "Schreib mir Datum und Location. Ich antworte innerhalb von 24 Stunden mit Verfügbarkeit und Preis.", "Hochzeit anfragen", "/kontakt/?anfrage=dj-hochzeit#formular"),
        banner=dict(tone=3, tag="Hochzeit", tc="REC 21:04:17", ar="21/8", alt="Tanzfläche bei einer Hochzeit mit warmem Licht", img="dj-hochzeit-banner"),
        service_name=f"Hochzeits-DJ {C}", service_kind="Hochzeits-DJ",
        primary=("Hochzeit anfragen", "/kontakt/?anfrage=dj-hochzeit#formular"), secondary=("Pakete ansehen", "/dj/pakete/"), priority="0.9")


# ------------------------------------------------------------------ Firmen
def firmen():
    faq = [
        ("Kannst du mehrere Phasen eines Events abdecken?", "Ja. Typischer Ablauf: Empfang mit Lounge-Sound, Beschallung für Reden und Präsentationen, Dinner-Musik und danach Party. Ein Soundcheck, ein Ansprechpartner."),
        ("Stellst du eine Rechnung mit ausgewiesener Mehrwertsteuer?", "Selbstverständlich. Rechnung mit allen Pflichtangaben, Zahlung nach Veranstaltung auf Rechnung möglich."),
        ("Wer meldet die Veranstaltung bei der GEMA?", "Bei Firmenveranstaltungen ist in der Regel der Veranstalter für die GEMA-Anmeldung zuständig. Ich liefere dir auf Wunsch die Musikfolge. Bei Unsicherheiten fragt man am besten direkt bei der GEMA nach."),
        ("Wie läuft das mit Mikrofon und Präsentationstechnik?", "Ich bringe Funkmikrofone mit und kann den Ton von Laptop oder Beamer in die Anlage einspeisen. Technik-Ansprechpartner der Location kenne ich meist schon vom Briefing."),
        ("Wie groß dürfen Veranstaltungen sein?", "Mit meiner Standardanlage beschalle ich bis etwa 200 Personen. Für größere Events arbeite ich mit Technikpartnern und biete dir ein Gesamtangebot an."),
    ]
    service_page(
        "dj", "/dj/firmenevents/", f"DJ für Firmenevents in {C}: Sommerfest, Weihnachtsfeier, Jubiläum",
        f"Event-DJ für Firmenfeiern in {C} und NRW: Empfang, Dinner, Party. Mit Mikrofontechnik, Ablaufabstimmung und Rechnung auf Wunsch. Jetzt unverbindlich anfragen.",
        f"DJ für <em>Firmenevents</em> in {C}", "Ein Firmenfest hat ein Problem, das Hochzeiten nicht haben: Die Gäste kennen sich, müssen aber morgen wieder zusammenarbeiten. Die Musik soll Stimmung machen, nicht peinlich werden.",
        "DJ · Firmenevents", [("Start", "/"), ("DJ", "/dj/"), ("Firmenevents", "/dj/firmenevents/")],
        """<h2>Ein Abend, mehrere Gesichter</h2>
<p>Bei Firmenfeiern wechselt die Stimmung öfter als bei privaten Feiern: erst Begrüßung, dann Reden, dann Essen, dann Party. Ich plane diese Übergänge vorher mit dir oder deiner Agentur durch, damit die Technik nicht zum Thema wird.</p>
<p>Das Publikum ist gemischt, vom Azubi bis zur Geschäftsführung. Ich spiele Musik, die niemanden ausschließt und trotzdem Energie hat. Wer wirklich tanzen will, findet seinen Moment. Wer lieber am Stehtisch bleibt, hört trotzdem gute Musik.</p>
<h2>Formate, die ich häufig spiele</h2>
<ul><li>Sommerfest und Betriebsfeier</li><li>Weihnachtsfeier</li><li>Firmenjubiläum und Eröffnung</li><li>Messeabend und Kundenevent</li><li>Gala-Dinner mit Awards und anschließender Party</li></ul>""",
        ["Ablaufabstimmung mit dir, Agentur oder Location", "Dezente Musik beim Empfang und Dinner", "Funkmikrofone für Moderation und Reden", "Einspeisung für Laptop und Beamer-Ton", "Party-Set mit Anpassung an die Altersstruktur", "Rechnung mit ausgewiesener MwSt.", "Ansprechpartner für Technik und Sicherheit der Location"],
        "Das ist dabei",
        notes=("So <em>planen</em> wir", [
            ("Zeitplan zuerst", "Ich bekomme von dir den Ablauf des Abends. Daraus entstehen Musikflächen, Mikrofonmomente und Lautstärkephasen."),
            ("Stimmung nach Teilnehmenden", "Durchschnittsalter, Branche, Anteil internationaler Gäste: Das fließt in Auswahl und Moderation ein."),
            ("Technik passt zum Raum", "Von der Kantine bis zum Hotelsaal: Ich messe Raum und Nachhall und stelle Lautsprecher so, dass es klingt und nicht dröhnt."),
        ]),
        faq=faq,
        links=[("Eventvideo für dasselbe Fest", "/video/eventvideo/"), ("Pakete &amp; Preise", "/dj/pakete/"), ("Imagefilm fürs Unternehmen", "/video/imagefilm/")],
        cta=("Was <em>steht</em> an?", "Erzähl mir kurz von Anlass, Datum und Teilnehmerzahl. Du bekommst schnell ein Angebot, das zur Veranstaltung passt.", "Firmenevent anfragen", "/kontakt/?anfrage=dj-firma#formular"),
        banner=dict(tone=5, tag="Event", tc="REC 20:12:08", ar="21/8", alt="Firmenevent mit Lichtstimmung", img="dj-firma-banner"),
        service_name=f"Event-DJ Firmenfeier {C}", service_kind="Event-DJ",
        primary=("Firmenevent anfragen", "/kontakt/?anfrage=dj-firma#formular"), secondary=("Pakete ansehen", "/dj/pakete/"))


# ------------------------------------------------------------------ Privat
def privat():
    faq = [
        ("Ab wie vielen Stunden buchst du private Partys?", "Mindestbuchung sind vier Stunden inklusive Auf- und Abbau. Kürzere Einsätze lohnen sich wegen der Technik selten, die Preisunterschiede sind klein."),
        ("Kommst du auch in Privatwohnungen oder Gärten?", "Ja, nach Besichtigung oder Fotos. Ich brauche Strom, ein trockenes Plätzchen und eine ehrliche Einschätzung zur Nachbarschaft. Eine Anlage für 50 Leute klingt anders als eine für 150."),
        ("Können wir selbst Playlists mitbringen?", "Klar. Ich nutze sie als Gerüst und mische sie live, wenn du magst. Ein reiner Playlist-Betrieb ist günstiger, aber dann bin ich eher Techniker als DJ. Sag mir, was du brauchst."),
        ("Was ist mit der Lautstärke?", "Ich arbeite mit Pegelbegrenzung, wenn die Nachbarn nicht mitfeiern. Besser vorher reden, dann nachts nicht diskutieren."),
    ]
    service_page(
        "dj", "/dj/private-partys/", f"DJ für Geburtstag & Party in {C}: Anlage, Licht, Musik",
        f"DJ für Geburtstage, Polterabende und private Partys in {C} und Umgebung. Mit Anlage, Licht und Wunschmusik. Transparente Preise, schnelle Antwort.",
        f"DJ für <em>Geburtstag</em> &amp; Party", "Die Party ist gut, wenn niemand ans Handy denkt, weil die Musik passt. Das klappt nicht mit einer Spotify-Playlist und zufälligem Skippen, sondern mit jemandem, der die Fläche liest.",
        "DJ · Private Partys", [("Start", "/"), ("DJ", "/dj/"), ("Private Partys", "/dj/private-partys/")],
        """<h2>Von 30 bis 100 Gäste</h2>
<p>Private Feiern haben den Vorteil, dass es keinen Konsens-Kompromiss braucht. Du kennst deine Leute, ich frage genau nach: Wer feiert, wie alt sind die Gäste, wann soll es voll werden? Daraus entsteht ein Abend, der zu euch passt und nicht zu irgendeinem Durchschnitt.</p>
<h2>Anlässe</h2>
<ul><li>Runde Geburtstage (30, 40, 50 und alles dazwischen)</li><li>Polterabend und Junggesellenabschied</li><li>Abschlussfeiern und Abi-Partys</li><li>Gartenfeste, Hofpartys, Scheunenabende</li><li>Silvester und Jahresabschluss im Freundeskreis</li></ul>
<h2>Was du vorbereiten musst</h2>
<p>Wenig. Eine Fläche, Strom, Gästezahl, Altersmix und ein paar Songs, die gesetzt sind. Den Rest klären wir im Gespräch.</p>""",
        ["Musikwunsch- und No-Go-Liste vorab", "Anlage passend zu Raum oder Garten", "Funkmikrofon für Reden und Glückwünsche", "Lichtset für Dämmerung und Tanzfläche", "Auf- und Abbau, Soundcheck", "Optionales Pegel-Limit für Wohngebiet"],
        "Das bekommst du",
        faq=faq,
        links=[("Fotos und Film vom Fest", "/video/eventvideo/"), ("Pakete &amp; Preise", "/dj/pakete/"), ("Musik &amp; Technik", "/dj/musik-technik/")],
        cta=("Wann wird <em>gefeiert?</em>", "Datum, Ort, grobe Gästezahl: mehr brauche ich für die erste Antwort nicht.", "Party anfragen", "/kontakt/?anfrage=dj-privat#formular"),
        service_name=f"DJ für private Feiern {C}", service_kind="DJ",
        primary=("Party anfragen", "/kontakt/?anfrage=dj-privat#formular"), secondary=("Pakete ansehen", "/dj/pakete/"))


# ------------------------------------------------------------------ Musik & Technik
def technik():
    genre_chips = "".join(f'<li class="chip">{esc(g)}</li>' for g in GENRES)
    body = f"""{crumbs_html([("Start", "/"), ("DJ", "/dj/"), ("Musik &amp; Technik", "/dj/musik-technik/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">DJ · Musik &amp; Technik</div>
    <h1 class="h-1 page-hero--wide">Sound, der zum Raum <em>passt</em></h1>
    <p class="lede">Gute Musik ist die halbe Miete. Die andere Hälfte ist Technik, die man nicht bemerkt: sauber eingemessen, kein Brummen, kein Dröhnen im Saal.</p>
  </div>
</section>

<section class="section" aria-labelledby="musik-h">
  <div class="container two-col two-col--wide-left">
    <div class="prose reveal">
      <h2 id="musik-h">Musikstile</h2>
      <p>Ich spiele alles, was auf einer Tanzfläche funktioniert, und weiß, wann etwas nicht funktioniert. Auf Hochzeiten mische ich meistens Pop, Disco, Funk, Klassiker und Hits aus allen Jahrzehnten. Auf Firmenfeiern ist es oft ein Mix aus Charts und House. Bei privaten Partys richte ich mich nach dir: Techno, Hip-Hop, Latin, was auch immer.</p>
      <p>Wichtiger als das Genre ist der Übergang. Ein Titel muss den vorherigen aufnehmen, nicht ersetzen. Genau da trennt sich Auflegen von Abspielen.</p>
      <h2>Wunschliste und No-Go-Liste</h2>
      <p>Vor jedem Event bekommst du ein kurzes Dokument zum Ausfüllen. Pflichtsongs, Wunschsongs, Dinge, die auf keinen Fall laufen dürfen (Ex-Lieblingssong, Ballermann-Hits, was auch immer). Das ist der wichtigste Teil der Vorbereitung.</p>
    </div>
    <div class="reveal" data-delay="1"><div class="eyebrow">Spektrum</div><ul class="chips">{genre_chips}</ul></div>
  </div>
</section>

<section class="section section--alt" id="mixes" aria-labelledby="mix-h">
  <div class="container">
    <div class="split-head"><h2 class="h-2 reveal" id="mix-h">Mixe &amp; <em>Hörproben</em></h2><p class="reveal" data-delay="1">Die Player laden erst nach deinem Klick. Vorher findet keine Datenübertragung an Drittanbieter statt.</p></div>
    {mix_cards()}
  </div>
</section>

<section class="section" aria-labelledby="tech-h">
  <div class="container">
    <div class="split-head"><h2 class="h-2 reveal" id="tech-h">Equipment, das <em>mitdenkt</em></h2><p class="reveal" data-delay="1">Alles ist auf Mobilität und Zuverlässigkeit ausgelegt. Keine Show-Technik, die du nicht brauchst, aber alles, was für einen sauberen Abend nötig ist.</p></div>
    <div class="notes reveal">
      <div class="note-line"><h3 class="h-3">Beschallung</h3><p>Aktive PA-Systeme mit Subwoofer, wahlweise für Räume bis 80, 150 oder 250 Personen. Separate Monitorbox am DJ-Pult, damit ich auch bei gedämpftem Saal sauber arbeiten kann.</p></div>
      <div class="note-line"><h3 class="h-3">Zuspielung &amp; Backup</h3><p>Zwei komplette Wiedergabewege (Controller plus Laptop). Musik liegt lokal, nicht im Stream, damit schlechtes WLAN nie zum Problem wird.</p></div>
      <div class="note-line"><h3 class="h-3">Mikrofone</h3><p>Drahtlose Handmikrofone und Headsets für Reden, Trauungen und Moderation. Sprachverständlichkeit hat Vorrang.</p></div>
      <div class="note-line"><h3 class="h-3">Licht</h3><p>Dezentes LED-Set für Tanzfläche und Hintergrund. Kein Stroboskop-Overkill, aber Atmosphäre, die auf Fotos und Film gut wirkt.</p></div>
      <div class="note-line"><h3 class="h-3">Stromversorgung</h3><p>Eigene Verteilung mit Fehlerstromschutz. Für Open-Air plane ich Wetterschutz und Aggregat nach Absprache ein.</p></div>
      <div class="note-line"><h3 class="h-3">Aufbau</h3><p>Rund zwei mal zwei Meter Platz, zwei getrennte Stromkreise bei großen Setups, Aufbauzeit ca. 90 Minuten plus Soundcheck.</p></div>
    </div>
  </div>
</section>
{cta_band("Du brauchst <em>genaue</em> Daten?", "Schick mir die Location, ich schicke dir einen Technikvorschlag mit Lautsprecherpositionen und Strombedarf.", "Technik besprechen", "/kontakt/?anfrage=dj-hochzeit#formular")}
"""
    write_page("/dj/musik-technik/", "DJ-Musik & Technik: Musikstile, Equipment, Mixe",
               f"Musikstile, DJ-Technik und Hörproben: Was ich als Hochzeits- und Event-DJ aus {C} spiele und mit welchem Equipment ich arbeite.",
               body, world="dj", current="/dj/musik-technik/",
               crumbs=[("Start", "/"), ("DJ", "/dj/"), ("Musik & Technik", "/dj/musik-technik/")])


# ------------------------------------------------------------------ Pakete
def pakete():
    faq = [
        ("Wie läuft die Buchung ab?", "Nach der Anfrage und einem kurzen Gespräch bekommst du ein verbindliches Angebot. Mit der Unterschrift und einer Anzahlung von 30 % ist dein Termin reserviert. Der Rest wird nach dem Event fällig."),
        ("Sind die Preise Festpreise?", "Ja. Aufbau, Soundcheck, Technik und Anfahrt im Umkreis sind enthalten. Was extra kostet, steht im Angebot, nicht am Abend."),
        ("Was passiert, wenn ich krank werde oder du?", "Fällt der Termin wegen Krankheit auf meiner Seite aus, organisiere ich qualifizierten Ersatz aus meinem DJ-Netzwerk. Steht eine Verschiebung an, gilt die Zusage für das neue Datum, sofern ich frei bin."),
        ("Kann ich DJ und Videograf kombinieren?", "Ja, das ist sogar sinnvoll. Im Kombi-Paket sparst du Koordination und es gibt einen Preisvorteil. Details im <a href='/kontakt/?anfrage=kombi#formular'>Kontaktformular</a>."),
    ]
    tiers = [
        ("Essential", "790", "Kleine Feiern bis ca. 80 Gäste", ["Bis zu 5 Stunden Spielzeit", "Anlage bis 80 Gäste", "Funkmikrofon", "Musikbriefing", "Auf- und Abbau inklusive"], False),
        ("Komplett", "1.190", "Hochzeiten und Firmenfeiern bis 150 Gäste", ["Bis zu 8 Stunden Spielzeit", "Anlage bis 150 Gäste", "Beschallung Trauung / Empfang", "Moderation nach Wunsch", "Lichtset & Backup-Technik", "Ablaufplan-Abstimmung"], True),
        ("Premium", "1.690", "Große Feiern, mehrere Orte, Wunschprogramm", ["Bis zu 10 Stunden Spielzeit", "Anlage bis 250 Gäste", "Zweite Beschallungszone", "Erweiterte Lichtshow", "Persönliche Songberatung für Schlüsselmomente", "Open End nach Absprache"], False),
    ]
    cards = ""
    for name, price, who, feats, hot in tiers:
        flag = '<span class="tier__flag">Beliebt</span>' if hot else ""
        cls = "tier tier--hot reveal" if hot else "tier reveal"
        btn_cls = "btn btn--primary" if hot else "btn"
        li = "".join(f"<li>{f}</li>" for f in feats)
        cards += f"""<article class="{cls}">{flag}<h3>{name}</h3><div class="tier__price"><small>ab</small>{price} €</div><p class="tier__for muted">{who}</p><ul>{li}</ul><a class="{btn_cls}" href="/kontakt/?anfrage=dj-hochzeit#formular">{name} anfragen {ARROW}</a></article>"""
    addons = [("Zusätzliche Stunde", "bis 90 € · jede weitere Spielstunde"), ("Beschallung Trauung", "ab 190 € · Funkmikrofone und Lautsprecher am zweiten Ort"), ("Nebel &amp; Lichtshow", "ab 150 € · Extra-Look für die Tanzfläche"),
              ("Fahrtkosten", "0,60 €/km · ab 40 km Entfernung"), ("Übernachtung", "nach Aufwand · bei Anreise über 100 km"), ("Kombi mit Video", "ab 200 € Vorteil · Hochzeitsfilm und DJ aus einer Hand")]
    add_html = '<div class="addons">' + "".join(f'<div class="addon"><div><b>{a}</b><br><span>{d.split(" · ")[1]}</span></div><em>{d.split(" · ")[0]}</em></div>' for a, d in addons) + "</div>"
    body = f"""{crumbs_html([("Start", "/"), ("DJ", "/dj/"), ("Pakete", "/dj/pakete/")])}
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">DJ · Pakete &amp; Preise</div>
    <h1 class="h-1 page-hero--wide">Pakete ohne <em>Kleingedrucktes</em></h1>
    <p class="lede">Drei Pakete als Orientierung. Dein Angebot passe ich an Ort, Dauer und Gästezahl an. Das Ergebnis ist ein Festpreis, den du schriftlich bekommst.</p>
  </div>
</section>
<section class="section" aria-label="Pakete">
  <div class="container"><div class="tiers">{cards}</div>
    <p class="muted" style="margin-top:1.5rem;font-size:.9rem">Alle Preise inkl. gesetzlicher MwSt. Richtwerte für Veranstaltungen im Raum {esc(C)}; das verbindliche Angebot erhältst du nach unserem Gespräch.</p>
  </div>
</section>
<section class="section section--alt" aria-labelledby="add-h">
  <div class="container"><div class="split-head"><h2 class="h-2 reveal" id="add-h">Optionen &amp; <em>Extras</em></h2><p class="reveal" data-delay="1">Nichts davon musst du buchen. Aber vielleicht fehlt dir bei der Planung genau eines davon.</p></div><div class="reveal">{add_html}</div></div>
</section>
<section class="section" aria-labelledby="faq-h">
  <div class="container two-col two-col--wide-left" style="align-items:start"><div><div class="eyebrow">FAQ</div><h2 class="h-2" id="faq-h">Rund um <em>Buchung</em></h2></div><div class="reveal">{faq_html(faq)}</div></div>
</section>
{cta_band("Welches Paket <em>passt?</em>", "Sag mir kurz, was du planst. Ich empfehle dir, was wirklich nötig ist, nicht das teuerste Paket.", "Angebot anfragen", "/kontakt/?anfrage=dj-hochzeit#formular")}
"""
    write_page("/dj/pakete/", f"DJ-Pakete & Preise für Hochzeit und Event in {C}",
               f"Transparente Preise für Hochzeits-DJ und Event-DJ in {C}: drei Pakete ab 790 €, Zusatzoptionen und Festpreis-Angebot innerhalb von 24 Stunden.",
               body, world="dj", current="/dj/pakete/", faq=faq, priority="0.8",
               crumbs=[("Start", "/"), ("DJ", "/dj/"), ("Pakete", "/dj/pakete/")])
