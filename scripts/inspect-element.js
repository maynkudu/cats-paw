/* Evaluate in a task-owned browser. This reads a bounded subtree without text or form data. */
(() => {
  const options = globalThis.CATS_PAW_OPTIONS ?? {};
  const selector = options.selector ?? 'body';
  const maxNodes = Math.min(1000, Math.max(1, Number(options.maxNodes) || 200));
  const root = document.querySelector(selector);
  if (!root) throw new Error(`Cat's Paw target not found: ${selector}`);
  const properties = [
    'display', 'position', 'box-sizing', 'width', 'height', 'min-width', 'max-width',
    'padding', 'margin', 'gap', 'grid-template-columns', 'flex-direction',
    'align-items', 'justify-content', 'overflow', 'color', 'background-color',
    'border-radius', 'border-width', 'font-family', 'font-size', 'font-weight',
    'font-style', 'font-variation-settings', 'font-feature-settings', 'line-height',
    'letter-spacing', 'transform', 'transform-origin', 'opacity', 'clip-path',
    'transition-property', 'transition-duration', 'transition-timing-function',
    'animation-name', 'animation-duration', 'animation-timing-function',
  ];
  const styles = (element, pseudo) => {
    const computed = getComputedStyle(element, pseudo);
    return Object.fromEntries(properties.map(key => [key, computed.getPropertyValue(key)]));
  };
  const nodes = [];
  const pending = [{element: root, parent: null, shadow: false}];
  while (pending.length && nodes.length < maxNodes) {
    const {element, parent, shadow} = pending.shift();
    const index = nodes.length;
    const rect = element.getBoundingClientRect();
    nodes.push({
      index, parent, shadow, tag: element.localName,
      rect: {x: rect.x, y: rect.y, width: rect.width, height: rect.height},
      styles: styles(element), before: styles(element, '::before'),
      after: styles(element, '::after'),
      animations: element.getAnimations().map(animation => ({
        playState: animation.playState,
        currentTime: animation.currentTime == null ? null : String(animation.currentTime),
        playbackRate: animation.playbackRate,
        timing: animation.effect?.getTiming() ?? null,
        keyframes: animation.effect?.getKeyframes?.() ?? null,
      })),
    });
    for (const child of element.children) pending.push({element: child, parent: index, shadow: false});
    if (element.shadowRoot) {
      for (const child of element.shadowRoot.children) pending.push({element: child, parent: index, shadow: true});
    }
  }
  return {
    schemaVersion: 1, selector, capturedAt: new Date().toISOString(),
    viewport: {width: innerWidth, height: innerHeight, dpr: devicePixelRatio},
    scroll: {x: scrollX, y: scrollY},
    reducedMotion: matchMedia('(prefers-reduced-motion: reduce)').matches,
    fontsStatus: document.fonts.status,
    fonts: Array.from(document.fonts, font => ({family: font.family, style: font.style,
      weight: font.weight, stretch: font.stretch, status: font.status})),
    truncated: pending.length > 0, nodes,
    limits: ['No text, HTML, form values or resource bodies captured.',
      'Closed shadow roots and iframe documents omitted.',
      'Animations reflect exposed element APIs at one instant; JS/GPU clocks may be absent.'],
  };
})()
