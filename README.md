# Cat's Paw

A portable agent skill for reconstructing a reference using source, runtime behavior and measured comparisons. Covers websites, components, motion, video, fonts and non-DOM visual artifacts.

The repository root is the skill directory. Install or link the whole directory as `cats-paw` in your agent's skills location, preserving references and scripts. Codex and compatible hosts can discover `~/.agents/skills/cats-paw/SKILL.md`; check your host's settings. The skill itself requires no MCP server or paid service.

Example requests:

> Use Cat's Paw to reproduce this component exactly in our stack, including hover, keyboard and interrupted transitions.

> Rebuild the first four seconds of this video as editable web animation. Identify what you can verify.

Browser capture uses optional Agent Browser or suitable host tools. Media uses optional FFmpeg; font inspection uses optional fontTools. The local comparator needs optional Pillow in an existing document environment or isolated virtualenv:

```sh
python scripts/pixel_diff.py expected.png actual.png --output diff.png
```

Exit status is 0 when no pixels exceed the threshold, 1 for differences, and 2 for invalid arguments. The script refuses resizing and existing output paths. Read [verification](references/verification.md) before making fidelity claims.

The companion [Zephyr](https://github.com/maynkudu/zephyr) skill adapts captured mechanisms into an original design. Both work independently. See [research](references/research.md) for primary sources. Original repositories, private backends and editable authoring projects cannot always be recovered from delivered artifacts.

Run the focused checks with an environment containing Pillow:

```sh
python -m unittest discover -s tests -v
RUN_BROWSER_TESTS=1 python -m unittest discover -s tests -v
```

The second command also requires Agent Browser and its browser runtime. It operates only the bundled local fixture and closes its own session. The skill instructions and helpers are MIT licensed. Third-party captured artifacts retain their own terms.
