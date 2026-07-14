"""Static assets served by the dashboard, inlined as strings (no file machinery).

`APP_JS` is a ~60-line, dependency-free interactivity layer using htmx-style
attributes — enough of the model (GET/POST that swaps a target, load triggers,
interval polling) for a live job console and inline actions. It is intentionally a
drop-in stand-in for htmx: swap in the real ~14 KB `htmx.min.js` later (and rename
the `data-*` attributes to `hx-*`) if richer behavior is ever needed.

Attributes:
  data-get="/url" / data-post="/url"   fetch on click (or form submit)
  data-target="#sel" | "self"          where to put the response (default: self)
  data-swap="inner" | "outer"          how to swap (default: inner)
  data-trigger="load"                  fire once on load instead of on click
  data-poll="1500"                     refetch every N ms (GET); stops when the
                                       swapped-in markup no longer carries data-poll
"""

from __future__ import annotations

APP_JS = r"""
(function () {
  function doSwap(el, htmlText) {
    var sel = el.getAttribute('data-target');
    var target = (!sel || sel === 'self') ? el : document.querySelector(sel);
    if (!target) return;
    var swap = el.getAttribute('data-swap') || 'inner';
    if (swap === 'outer') { target.outerHTML = htmlText; }
    else { target.innerHTML = htmlText; }
    init(document);
  }
  function fetchInto(el, url, method, body) {
    var opts = { method: method || 'GET' };
    if (body != null) { opts.headers = { 'Content-Type': 'application/x-www-form-urlencoded' }; opts.body = body; }
    fetch(url, opts).then(function (r) { return r.text(); })
      .then(function (t) { doSwap(el, t); })
      .catch(function (e) { doSwap(el, '<p class="err">request failed: ' + e + '</p>'); });
  }
  function activate(el) {
    if (el.__hx) return; el.__hx = true;
    var get = el.getAttribute('data-get');
    var post = el.getAttribute('data-post');
    var trigger = el.getAttribute('data-trigger');
    var poll = el.getAttribute('data-poll');
    if (el.tagName === 'FORM' && post !== null) {
      el.addEventListener('submit', function (e) {
        e.preventDefault();
        var body = new URLSearchParams(new FormData(el)).toString();
        fetchInto(el, post, 'POST', body);
      });
      return;
    }
    if (post !== null) {
      el.addEventListener('click', function (e) { e.preventDefault(); fetchInto(el, post, 'POST'); });
    } else if (get !== null && !poll && trigger !== 'load') {
      el.addEventListener('click', function (e) { e.preventDefault(); fetchInto(el, get, 'GET'); });
    }
    if (trigger === 'load' && get !== null) { fetchInto(el, get, 'GET'); }
    if (poll && get !== null) {
      var ms = parseInt(poll, 10) || 2000;
      var timer = setInterval(function () {
        if (!document.body.contains(el)) { clearInterval(timer); return; }
        fetchInto(el, get, 'GET');
      }, ms);
    }
  }
  function init(root) {
    (root || document).querySelectorAll('[data-get],[data-post]').forEach(activate);
  }
  if (document.readyState !== 'loading') { init(document); }
  else { document.addEventListener('DOMContentLoaded', function () { init(document); }); }
  window.__uiInit = init;
})();
"""
