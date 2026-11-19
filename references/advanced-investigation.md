# Advanced investigation

Choose an experiment that distinguishes competing explanations. Use invasive instrumentation only in a disposable, authorized context, retain the original capture and repeat ordinary behavior afterward. These methods are conditional techniques, not a preinstalled toolchain or tested universal exporter.

| Uncertainty | Discriminating experiment | Evidence and limit |
| --- | --- | --- |
| Sticky layout or animated transform? | Sample rects and computed transforms while scrolling forward and backward | Correlate scroll position, document position and transform; one screenshot is insufficient |
| Time, scroll, pointer or media clock? | Hold all but one input constant, then vary it | Record causal response; correlated motion alone does not establish driver |
| Spring or authored tween? | Retarget mid-flight, reverse repeatedly, compare velocity continuity | Compare against source or fit competing models; a fitted curve remains inferred |
| Invisible interactive overlay? | Inspect hit testing, stacking, pointer events and event listeners at failing points | Trace the responsible element without removing unrelated layers |
| External CSS or runtime-generated styles? | Compare downloaded sheets, CSSOM, matched rules and DOM mutations | Preserve runtime state; computed CSS loses original authoring structure |
| Hidden lazy dependency? | Capture network before triggering the specific state | Record newly loaded chunks/assets; avoid crawling unrelated routes |
| A framework component boundary? | Supported runtime tree inspection plus handlers and import tracing | Production builds may conceal names; tree shape is not recovered source |
| Source map contains usable source? | Inspect declared map and source bodies in a confined output directory | Paths and position mappings alone do not supply missing files |
| CSS motion or JS timeline? | Compare exposed WAAPI animations against relevant source and supported runtime inspectors | Runtime libraries may expose no global handles; never assume one engine |
| Canvas/GPU object structure? | Inspect shipped assets/shaders and supported frame-debugger draw calls | Instrumented draw calls cannot reconstruct an absent editor project |
| Sprite, atlas or full image? | Inspect selected resource, texture coordinates, object position and clipping | Preserve atlas dimensions and UV/crop mapping; screenshots lose offscreen pixels |
| Font family or fallback run? | Inspect actual platform font data through supported debugger tools, font files and shaping behavior | Computed family lists show candidates, not necessarily the face used for every glyph |
| Screenshot-only layout? | OCR for text hypotheses, measured anchor geometry, candidate font comparison and constraint fitting | OCR and image segmentation are inferred; do not claim extracted CSS or exact fonts |
| Procedural noise or prerecorded media? | Repeat from a clean start with controlled time and seed when available | Different outputs can arise from seed, external state or nondeterminism |
| Offline archive incomplete? | Replay without network, inventory missing resources and identify fixture-backed APIs | Successful static replay does not prove original backend recovery |

Potential specialist tools include browser protocol clients, local AST parsers, source-map consumers, browser archive tools, image metadata utilities, fontTools, FFmpeg, frame debuggers, optical-flow tools and native format inspectors. Discover installed versions, consult primary docs and test on a fixture before claiming support. Avoid adding a new dependency when existing tooling answers the question.

For exported packages such as animation archives, validate the file signature, inventory entries, enforce a confined extraction root and size limits, and inspect manifests/dependencies. A renamed extension is not conversion. Preserve a byte-for-byte original and compare derived output.

Escalation ends when additional evidence cannot distinguish the hypotheses, required input is inaccessible, or the requested deliverable needs an absent authoring artifact. Report the gap and a useful next input instead of accumulating guesses. Keep expensive or risky experiments tied to a specific acceptance item.
