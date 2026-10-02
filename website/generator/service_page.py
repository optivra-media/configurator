"""Generische Leistungsseite (DJ & Video nutzen dieselbe Struktur, aber eigene Inhalte)."""
from core import (ARROW, SITE, cta_band, crumbs_html, esc, faq_html, frame, related, service_schema, write_page)


def service_page(world, path, title, desc, h1, lede, kicker, crumbs, intro_html, included, included_title,
                 timeline=None, notes=None, faq=None, links=None, cta=None, banner=None, service_name=None,
                 service_kind=None, primary=None, secondary=None, priority="0.8"):
    p_label, p_href = primary
    s_label, s_href = secondary
    body = [crumbs_html(crumbs)]
    body.append(f"""<section class="page-hero">
  <div class="container">
    <div class="eyebrow">{esc(kicker)}</div>
    <h1 class="h-1 page-hero--wide">{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="{p_href}">{esc(p_label)} {ARROW}</a>
      <a class="btn" href="{s_href}">{esc(s_label)}</a>
    </div>
  </div>
</section>""")
    if banner:
        body.append(f'<div class="container banner reveal">{frame(**banner)}</div>')
    items = "".join(f"<li>{i}</li>" for i in included)
    body.append(f"""<section class="section">
  <div class="container two-col two-col--wide-left">
    <div class="prose reveal">{intro_html}</div>
    <aside class="reveal" data-delay="1" aria-label="{esc(included_title)}">
      <h2 class="h-3" style="margin-bottom:1.2rem">{esc(included_title)}</h2>
      <ul class="list-plus">{items}</ul>
    </aside>
  </div>
</section>""")
    if timeline:
        t_title, t_intro, t_items = timeline
        rows = "".join(f'<li><time>{t}</time><div><h3>{esc(h)}</h3><p>{d}</p></div></li>' for t, h, d in t_items)
        body.append(f"""<section class="section section--alt">
  <div class="container">
    <div class="split-head"><h2 class="h-2 reveal">{t_title}</h2><p class="reveal" data-delay="1">{t_intro}</p></div>
    <ol class="timeline reveal">{rows}</ol>
  </div>
</section>""")
    if notes:
        n_title, n_items = notes
        cells = "".join(f'<div class="note-line"><h3 class="h-3">{esc(h)}</h3><p>{d}</p></div>' for h, d in n_items)
        body.append(f"""<section class="section">
  <div class="container">
    <h2 class="h-2 reveal" style="margin-bottom:2.5rem">{n_title}</h2>
    <div class="notes reveal">{cells}</div>
  </div>
</section>""")
    if faq:
        body.append(f"""<section class="section section--alt" aria-labelledby="faq-h">
  <div class="container two-col two-col--wide-left" style="align-items:start">
    <div><div class="eyebrow">FAQ</div><h2 class="h-2" id="faq-h">Fragen, die fast <em>jeder</em> stellt</h2></div>
    <div class="reveal">{faq_html(faq)}</div>
  </div>
</section>""")
    if links:
        body.append(f"""<section class="section section--tight">
  <div class="container"><div class="eyebrow">Passt dazu</div>{related(links)}</div>
</section>""")
    if cta:
        body.append(cta_band(*cta))
    schema = [service_schema(service_name or title, desc, path, service_kind or title)]
    write_page(path, title, desc, "\n".join(body), world=world, schema=schema, crumbs=crumbs, faq=faq, priority=priority)
