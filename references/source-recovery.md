# Source recovery

Escalate only when the next technique can answer a named uncertainty.

| Available evidence | Useful operation | What it cannot establish |
| --- | --- | --- |
| Original repository or editable project | Trace state, styles, imports and assets end to end | Runtime configuration and behavior without operating it |
| Delivered JS/CSS with a source map | Resolve declared map URLs, inspect `sources` and `sourcesContent`, map generated positions | Missing source bodies, private server source or omitted build-time inputs |
| Minified JS without maps | Format, parse AST, locate selectors/assets/easing constants, trace handlers and chunk imports | Original names, comments, file boundaries or framework source exactly |
| Runtime component inspection | Inspect exposed React/component state and ownership with supported tools | Complete original source or private props being safe to publish |
| Rendered DOM and styles | Measure output, layout dependencies and visible semantics | Original components, data model or backend |
| Pixels or a recording | Infer geometry and motion, test competing hypotheses | Unique causal implementation |

Read map metadata and source paths as data. Keep recovered paths within a controlled output root, reject traversal, inspect source contents before executing anything, and label virtual/bundler paths. Source maps may embed sensitive implementation material. Do not publish them wholesale.

Use actual delivered `sourceMappingURL` or headers and provided files. Publicly accessible maps are useful evidence; guessing private endpoints or defeating authentication is outside this workflow. A map without `sourcesContent` may reference files that are unavailable. Record that gap rather than manufacturing source.

On a local disposable copy, use formatting and AST tools already in the project. Scope searches to relevant constants, CSS classes, SVG paths, animation APIs and module imports. Trace event listener to state update to render/animation owner. Dynamic imports reveal code splitting, not necessarily original component boundaries. Keep a short dependency sketch with verified versus inferred edges.

Use breakpoints, event-listener inspection, DOM mutation breakpoints and supported framework tools for difficult transitions. Enable instrumentation before load when required. Record instrumentation effects and repeat uninstrumented behavior. Runtime React hooks and tree inspection depend on build and tooling support.

For offline reconstruction, inventory required assets and explicit API assumptions, then replace only unavailable external behavior with labeled fixtures. Keep that reconstruction distinct from the original capture. Inspect downloaded code and dependencies before running it; use a disposable project without credentials.

For WASM, shaders and GPU scenes, shipped binaries or shader sources may explain computation without recovering the authoring project. Inspect accessible models, textures, uniforms, camera and render targets. Keep observational reconstruction labeled when mesh, rig, shader source or simulation state is unavailable.
