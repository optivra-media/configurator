/* NB — DJ & Video · Interaktionen (Vanilla JS, keine Abhängigkeiten) */
(function () {
  'use strict';
  var doc = document;
  doc.documentElement.classList.add('js');
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };

  /* Header: Rahmen sobald gescrollt */
  var header = $('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Mobiles Menü */
  var burger = $('.burger'), drawer = $('#drawer');
  if (burger && drawer) {
    var setNav = function (open) {
      burger.setAttribute('aria-expanded', open);
      burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
      drawer.classList.toggle('is-open', open);
      doc.body.classList.toggle('nav-open', open);
    };
    burger.addEventListener('click', function () { setNav(burger.getAttribute('aria-expanded') !== 'true'); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });
    $$('a', drawer).forEach(function (a) { a.addEventListener('click', function () { setNav(false); }); });
    window.matchMedia('(min-width:1020px)').addEventListener('change', function (m) { if (m.matches) setNav(false); });
  }

  /* Reveal beim Scrollen */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else { reveals.forEach(function (el) { el.classList.add('is-in'); }); }

  /* Laufender Timecode (Startseite / Video-Hero) */
  $$('[data-timecode]').forEach(function (el) {
    var start = Date.now(), pad = function (n) { return (n < 10 ? '0' : '') + n; };
    var tick = function () {
      var t = Date.now() - start, f = Math.floor((t % 1000) / 41.667), s = Math.floor(t / 1000);
      el.textContent = '00:' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60) + ':' + pad(f);
    };
    tick(); setInterval(tick, 80);
  });

  /* Equalizer-Balken erzeugen (keine 40 leeren <i> im HTML nötig) */
  $$('[data-eq]').forEach(function (box) {
    var n = parseInt(box.getAttribute('data-eq'), 10) || 32;
    for (var i = 0; i < n; i++) {
      var b = doc.createElement('i');
      b.style.setProperty('--s', (0.25 + Math.abs(Math.sin(i * 1.7) * 0.75)).toFixed(2));
      b.style.setProperty('--d', (-(i * 0.17) % 1.4).toFixed(2) + 's');
      box.appendChild(b);
    }
  });

  /* Wellenform-Darstellung der Mix-Karten */
  $$('.wave').forEach(function (w) {
    var seed = parseInt(w.getAttribute('data-seed'), 10) || 1;
    for (var i = 0; i < 48; i++) {
      var h = 18 + Math.abs(Math.sin((i + seed) * 0.7) * Math.cos((i * seed) * 0.13)) * 82;
      var b = doc.createElement('i'); b.style.setProperty('--h', h.toFixed(0) + '%'); w.appendChild(b);
    }
  });

  /* Embed erst nach Klick laden (DSGVO: keine Verbindung zu Drittanbietern beim Seitenaufruf) */
  $$('[data-embed]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var url = btn.getAttribute('data-embed');
      if (!url) { window.location.href = '/kontakt/?anfrage=dj-hochzeit#formular'; return; }
      var f = doc.createElement('iframe');
      f.src = url; f.loading = 'lazy'; f.allow = 'autoplay'; f.title = btn.getAttribute('data-title') || 'Audio-Player';
      btn.closest('.mix').replaceChild(f, btn);
    });
  });

  /* Portfolio-Filter */
  var chips = $$('[data-filter]');
  if (chips.length) {
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var f = chip.getAttribute('data-filter');
        chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
        $$('.work').forEach(function (w) { w.hidden = !(f === 'alle' || w.getAttribute('data-cat') === f); });
      });
    });
  }

  /* Lightbox (YouTube-nocookie / Vimeo erst bei Klick) */
  var lb = $('#lightbox');
  if (lb) {
    var stage = $('.lightbox__stage', lb), cap = $('.lightbox__title', lb), note = $('.lightbox__note', lb), last;
    var open = function (trigger) {
      last = trigger;
      var yt = trigger.getAttribute('data-yt'), vm = trigger.getAttribute('data-vimeo');
      var title = trigger.getAttribute('data-title') || 'Video';
      stage.innerHTML = '';
      if (yt || vm) {
        var f = doc.createElement('iframe');
        f.src = yt ? 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(yt) + '?autoplay=1&rel=0'
                   : 'https://player.vimeo.com/video/' + encodeURIComponent(vm) + '?autoplay=1&dnt=1';
        f.allow = 'autoplay; fullscreen; picture-in-picture'; f.allowFullscreen = true; f.title = title;
        stage.appendChild(f); note.textContent = '';
      } else {
        var src = $('.frame', trigger);
        if (src) { var c = src.cloneNode(true); var pb = $('.play', c); if (pb) pb.remove(); stage.appendChild(c); }
        note.textContent = 'Vollständiger Film auf Anfrage – schreib mir kurz.';
      }
      cap.textContent = title;
      lb.classList.add('is-open'); doc.body.style.overflow = 'hidden';
      $('.lightbox__close', lb).focus();
    };
    var close = function () {
      lb.classList.remove('is-open'); stage.innerHTML = ''; doc.body.style.overflow = '';
      if (last) last.focus();
    };
    $$('[data-lightbox]').forEach(function (t) { t.addEventListener('click', function (e) { e.preventDefault(); open(t); }); });
    $('.lightbox__close', lb).addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    doc.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') { e.preventDefault(); $('.lightbox__close', lb).focus(); }
    });
  }

  /* Kontaktformular */
  var form = $('#anfrage-form');
  if (form) {
    var status = $('.form-status', form), btn = $('button[type=submit]', form);
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('anfrage'), sel = $('select[name=anlass]', form);
    if (pre && sel) { $$('option', sel).forEach(function (o) { if (o.value === pre) sel.value = pre; }); }
    var ts = $('input[name=ts]', form); if (ts) ts.value = Math.floor(Date.now() / 1000);

    var validate = function () {
      var ok = true;
      $$('.field', form).forEach(function (f) {
        var i = $('input,select,textarea', f); if (!i) return;
        var bad = i.required && !i.value.trim();
        if (i.type === 'email' && i.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(i.value)) bad = true;
        f.classList.toggle('has-error', bad); i.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad) ok = false;
      });
      var dp = $('input[name=datenschutz]', form);
      if (dp && !dp.checked) { ok = false; dp.focus(); }
      return ok;
    };
    var show = function (cls, msg) { status.className = 'form-status ' + cls; status.textContent = msg; status.setAttribute('tabindex', '-1'); status.focus(); };

    form.addEventListener('submit', function (e) {
      if (!validate()) { e.preventDefault(); var first = $('.has-error input,.has-error select,.has-error textarea', form); if (first) first.focus(); return; }
      if (!window.fetch) return; // Fallback: normaler POST
      e.preventDefault();
      btn.disabled = true; var label = btn.textContent; btn.textContent = 'Wird gesendet …';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && res.j.ok) { form.reset(); show('is-ok', res.j.message || 'Danke dir! Deine Anfrage ist angekommen. Ich melde mich innerhalb von 24 Stunden.'); }
          else { show('is-err', (res.j && res.j.message) || 'Das hat leider nicht geklappt. Bitte schreib mir direkt per E-Mail.'); }
        })
        .catch(function () { show('is-err', 'Keine Verbindung. Bitte versuch es erneut oder schreib mir direkt per E-Mail.'); })
        .then(function () { btn.disabled = false; btn.textContent = label; });
    });
    if (params.get('gesendet') === '1') show('is-ok', 'Danke dir! Deine Anfrage ist angekommen. Ich melde mich innerhalb von 24 Stunden.');
    if (params.get('fehler') === '1') show('is-err', 'Das hat leider nicht geklappt. Bitte prüfe deine Angaben oder schreib mir direkt per E-Mail.');
  }
})();
