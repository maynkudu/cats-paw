# Verification

Define comparison conditions and tolerances before evaluating the result. Record browser/version, OS, viewport, DPR, fonts, zoom, theme, motion setting, content, seed, state, scroll and clock. Wait for font and image readiness. Compare on the same renderer when practical; font rasterization and GPU differences remain explicit limits.

Start with extracted facts. Compare SVG paths, actual token values, font family/file/axes, keyframes, durations, curves, breakpoints and geometry against pinned source. Equivalent rendering in another stack may use different structure; explain the mapping. Tests must bind to the pinned reference, not mirror new implementation constants.

Use screenshots at equal dimensions. Create a pixel diff and overlay; report changed-pixel proportion and the chosen channel threshold. `scripts/pixel_diff.py` supplies a small local comparator with optional Pillow. It refuses dimension mismatch and writes a difference image plus JSON metrics. It measures RGBA bytes, not perceptual similarity or semantic correctness. Inspect the images as well as metrics. A transparent image may need comparison against the same intended background.

Mask only unavoidable regions declared in the capture contract, retain the unmasked view, and explain the mask. Do not hide defects or increase tolerances because the output fails. Separate environment corrections from implementation corrections.

For motion, match the same input and authoritative time/scroll progress. Compare multiple phases including onset, overlap, interruption, reversal and endpoint. Use actual media timestamps for variable-frame-rate recordings. A matching first and last frame cannot prove easing, driver or temporal fidelity. Compare audio alignment and listen when audio is in scope.

Operate controls with pointer and keyboard, check focus and cancellation, reduced motion, reflow and console errors. Inspect layout overflow and text wrapping using real content. Use host QA tools and bounded exploration when available. Static diff, accessibility automation and performance traces each establish different facts.

Report by acceptance item:

| Item | Result | Evidence | Remaining difference |
| --- | --- | --- | --- |
| Resting geometry at declared width | verified / failed / unverified | capture pair + diff + metrics | concrete discrepancy or none measured |
| Transition driver and interruption | verified / failed / unverified | action script + recording + time samples | concrete discrepancy |
| Original source recovery | recovered / inferred / unavailable | source paths and map evidence | missing inputs |

Stop when the agreed acceptance conditions pass or a named gap blocks further evidence. No universal percentage makes a reconstruction "perfect".
