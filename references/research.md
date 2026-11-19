# Research basis

Researched 2026-11-20 against primary documentation and protocol definitions. These findings are documentation-backed. The verification report separately records experiments. Mutable docs require installed-version checks.

| Source | Finding used |
| --- | --- |
| [CDP browser protocol](https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json) | DOMSnapshot, matched CSS rules, response bodies and animation pause/seek support deeper capture; feature coverage varies |
| [CDP JS protocol](https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/js_protocol.json) | Delivered script source and source-map URLs differ from complete original projects |
| [Chrome source maps](https://developer.chrome.com/docs/devtools/javascript/source-maps) | Maps can load supplied authored source; pretty-printing formats deployed code |
| [Playwright Trace Viewer](https://playwright.dev/docs/trace-viewer) | Action snapshots and network records support evidence; its Source panel shows automation source |
| [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) | Capture environment affects output; thresholds and changed-pixel limits differ |
| [Playwright screenshot API](https://playwright.dev/docs/api/class-page#page-screenshot) | Disabling animations can finish transitions and fire events |
| [Playwright Clock](https://playwright.dev/docs/clock) | Timer controls help JS tests; they do not prove control over every media/GPU clock |
| [ffprobe main options](https://ffmpeg.org/ffprobe.html#Main-options) | Frames differ from packets; seeking is not exact; invalid fields may be omitted |
| [FFmpeg showinfo](https://ffmpeg.org/ffmpeg-filters.html#showinfo) | PTS supports temporal alignment |
| [FFmpeg select](https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect) and [scdet](https://ffmpeg.org/ffmpeg-filters.html#scdet-1) | Candidate cuts use different threshold scales |
| [FFmpeg fps](https://ffmpeg.org/ffmpeg-filters.html#fps-1) | Resampling can drop or duplicate frames |
| [FFmpeg silencedetect](https://ffmpeg.org/ffmpeg-filters.html#silencedetect) and [astats](https://ffmpeg.org/ffmpeg-filters.html#astats-1) | Audio measurements supply timing clues, not intent |
| [FFmpeg mestimate](https://ffmpeg.org/ffmpeg-filters.html#mestimate) | Block vectors describe image displacement, not semantic transforms |
| [fontTools TTFont](https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html) | Tables, variations and cmap support inventory; advance width differs from glyph bounds |
| [fontTools subset](https://fonttools.readthedocs.io/en/latest/subset/index.html) | Layout closure and explicit metadata retention matter; defaults are version-sensitive |
| [OpenType names](https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids) and [fsType](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fstype) | Metadata informs provenance without replacing a license |
| [WHATWG Canvas](https://html.spec.whatwg.org/multipage/canvas.html#the-canvas-element) | Canvas exports pixels and restricts origin-unclean export |
| [MDN Canvas CORS](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image) | Origin restrictions explain failed pixel extraction |
| Installed `agent-browser skills get core` and `--help` | Version-matched snapshots, HAR, recording, React inspection and accessibility commands |

Two bounded investigations inspected these sources. The lead independently checked decisive source-map, ffprobe and TTFont guidance and MDN excerpts. Source-map recovery, binary HAR replay, React introspection, clock control, GPU inspection, Lottie and Rive project recovery have no end-to-end experiment here. SVG and GPU guidance describes investigation, not a tested exporter. No exhaustive recovery claim is made.
