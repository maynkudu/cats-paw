# Browser capture

## Observe first

Read the installed Agent Browser skill and `agent-browser skills get core`. Discover version-specific flags through help rather than assuming this recipe matches every release. Use an isolated task session, fix the viewport and environment, open the source, snapshot, operate discovered elements, and snapshot after changes. Wait for the relevant readiness condition; perpetual analytics can prevent network idle.

On the inspected local version, the useful commands include:

```sh
agent-browser --session cats-paw-TASK open https://SOURCE
agent-browser --session cats-paw-TASK snapshot -i
agent-browser --session cats-paw-TASK screenshot reference/rest.png
agent-browser --session cats-paw-TASK network har start
# Operate the scoped interaction using fresh discovered refs.
agent-browser --session cats-paw-TASK network har stop reference/private.har
agent-browser --session cats-paw-TASK record start reference/motion.webm --fps 60
# Replay the trigger, reversal and endpoint.
agent-browser --session cats-paw-TASK record stop
agent-browser --session cats-paw-TASK close
```

Use the host's recording workflow when one exists. A recorded 60 fps file does not prove the page rendered 60 distinct frames per second. Preserve the action sequence and actual timing; repeatable recordings need a reproducible script and capture setup.

## Inspect the rendered component

`scripts/inspect-element.js` is a read-only browser expression. Set `globalThis.CATS_PAW_OPTIONS = {selector: '#target', maxNodes: 200}` in the task session, then feed the file to `agent-browser eval --stdin`. It records geometry, selected computed properties, `::before`/`::after`, open shadow descendants, currently exposed animations and loaded font metadata. It omits text, form values, HTML and network resources. Review even this output before sharing. It is an observation at one instant, not a component exporter.

Take focused DOM/HTML snapshots separately when needed. Inspect inherited tokens and `getComputedStyle(element).getPropertyValue('--token')`. Capture CSS rule origins through DevTools when specificity matters. Computed values alone lose stylesheet structure, original units, conditions and design intent. Inspect image `currentSrc`, responsive `srcset`, SVG `viewBox`, clip/mask/filter definitions, paint order, and pseudo-elements.

Traverse open shadow roots deliberately. Closed shadow roots and cross-origin frames require supported debugger/frame tooling or remain gaps. Attach no global monkey patches to an unrelated live app. Debugger inspection is version-dependent and cannot guarantee complete internals. Observe same-origin frames in their own document coordinate system.

## Capture delivered dependencies

Start network recording before the relevant navigation or interaction. Capture lazy chunks by exercising the requested states. HAR text bodies can contain HTML/CSS/JS/JSON; binary inclusion depends on the recorder's mode. Validate response body presence, decoded encoding, status, MIME and file signatures. Cache/service-worker responses and streamed media may need separate supported body capture. A network request list is not an offline archive.

Use network response bodies or a scoped browser archive for HTML, CSS, scripts, fonts, images and media. Resolve CSS imports and asset URLs relative to their originating response, preserve URL-to-file mapping, and record failed dependencies. A bounded authorized downloader needs origin/path limits, redirect validation, size/count budgets and content verification. Never download every linked route by default.

Inspect sanitized HARs offline. Replay can explain dependencies, but recorded API success does not recreate a backend. Use disposable fixtures when exercising mutations. Keep application requests and live actions within the user's scope.

## Responsive and motion probes

Compare widths just above and below observed reflow boundaries, long content, theme, coarse-pointer behavior and reduced motion. Track geometry at controlled scroll offsets to distinguish sticky layout, scroll-linked animation and time-based loops. Reverse the input to test causality.

For CSS/WAAPI animations inspect `getAnimations()`, effect keyframes and timing. In a disposable copy, pause and set time to sample deterministic phases. JS timelines, springs, Canvas and GPU renderers may use separate clocks and require their own controls. Never claim `document.getAnimations()` captures all motion.
