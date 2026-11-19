# Evidence contract

Keep one directory per artifact. A small component may need only the brief, source, two captures and a report. Add files when they supply evidence.

```text
reference/<artifact>/
  brief.md                 source, scope, output, acceptance and exceptions
  manifest.json            artifact paths, SHA-256, URLs, capture dates, terms
  raw/                     delivered HTML, CSS, JS, maps, assets, media
  observations/            DOM/style snapshots, state and motion observations
  captures/                screenshots, recordings, frame timestamps
  comparisons/             expected/actual pairs, diff maps and measurements
  report.md                verified, failed and unverified acceptance items
```

For each resource record original URL or local origin, acquisition method, UTC date, content hash, content type, and license or reuse status when known. Hash bytes, not filenames. Mark unavailable source explicitly. A hash proves which bytes were used, not who created them or whether they are reusable.

For each observation record state, action, viewport in CSS pixels, device pixel ratio, browser/version, OS, zoom, locale, theme, reduced motion, scroll position, font readiness, asset readiness and capture clock. For video add stream index, time base, presentation timestamp and variable-frame-rate status. For GPU work record hardware/backend and seed when controllable.

The state ledger maps input to logical state, visual transition, endpoint, interruption and evidence. Include reverse scrolling, repeated input, release/cancel, focus and responsive changes when the component exposes them. Separate `recovered`, `observed`, `inferred` and `unavailable`; add confidence and the next discriminating experiment to inferences.

Raw HARs, DOM, props, recordings and URLs can expose private data or credentials. Keep a private raw copy only when needed. Prepare a separately reviewed sanitized export for sharing, removing authorization, cookies, signed URL parameters and personal payloads. Do not claim a generic redaction pass catches every secret.

The Zephyr handoff adds preserved behavior, allowed changes, asset provenance, unresolved assumptions and the strongest verified representative flow. Zephyr writes a new adaptation brief and keeps this baseline intact.
