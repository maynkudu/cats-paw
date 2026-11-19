# Media and fonts

## Video and audio

Preserve original files. Inventory streams, resolution, pixel aspect ratio, color metadata, time bases, start offsets and audio. Confirm installed capabilities through `ffprobe` and `ffmpeg` help. Use new output paths:

```sh
ffprobe -v error -show_format -show_streams -of json input.mp4 > streams.json
ffprobe -v error -select_streams v:0 -show_frames \
  -show_entries frame=pts,pts_time,best_effort_timestamp_time,duration_time,key_frame \
  -of json input.mp4 > frames.json
mkdir frames
ffmpeg -n -i input.mp4 -map 0:v:0 -vf showinfo \
  -fps_mode passthrough frames/frame-%06d.png 2> frames.log
ffmpeg -i input.mp4 -vf 'scdet=threshold=10,metadata=print' -an -f null - 2> scenes.log
ffmpeg -i input.mp4 -map 0:a:0 -af 'silencedetect=n=-40dB:d=0.15' -f null - 2> silence.log
```

Align by decoded presentation timestamps, retaining stream offsets and rational time bases. Frame number divided by average fps is unreliable for variable-frame-rate media. Mark best-effort timestamps as estimates. Seeking can start away from the requested timestamp. Constant-fps sampling can duplicate or drop frames; use it for overviews, not timing proof.

Scene detection supplies candidate cuts. Inspect surrounding frames and unflagged intervals. `scdet` uses a 0..100 threshold; `select`'s `scene` uses 0..1. Audio silence, RMS, waveform and onset analysis supply timing clues, not editorial intent or guaranteed beats. Listen to sync points when supported. Preserve audio/video offsets, codec delay and any resampling record.

Track landmarks, silhouettes, occlusion, transforms and phase relationships. Optical flow, block motion vectors and curve fitting can test hypotheses; image displacement is not proof of a CSS transform, spring or camera model. Separate camera motion from object motion. Rebuild from source where available; label inferred mechanisms and compare intermediate phases and actual playback.

## Fonts

Start with delivered font files, actual rendered faces and CSS `@font-face`. Record file/version, weight/style/stretch, fallback runs, variable axes, optical sizing, features, shaping and language. Screenshot font matching remains a hypothesis until file evidence confirms it.

Use fontTools `TTFont` to inspect names, metrics, `cmap`, `fvar`, `STAT`, `avar`, `GSUB`, `GPOS` and relevant color tables. For collections select the actual member. Names have platform/encoding/language variants; IDs 0, 13 and 14 can carry copyright and licensing data. `OS/2.fsType` is version-sensitive and does not replace the actual license.

```python
from fontTools.ttLib import TTFont

with TTFont('font.woff2', lazy=True) as font:
    print('tables', font.keys())
    for record in font['name'].names if 'name' in font else []:
        if record.nameID in {0, 1, 2, 4, 5, 6, 13, 14, 16, 17}:
            print(record.nameID, record.platformID, record.platEncID,
                  record.langID, record.toUnicode())
    if 'fvar' in font:
        for axis in font['fvar'].axes:
            print(axis.axisTag, axis.minValue, axis.defaultValue, axis.maxValue)
```

Repackaging or permitted subsetting transforms a format; it cannot recover missing outlines. Check installed defaults and explicitly preserve required metadata and shaping records. Test dynamic content, scripts, marks, ligatures and variation instances in the actual renderer. Missing licensing records mean unknown status. Keep originals separate from derivatives.

## SVG, Canvas and GPU scenes

For SVG preserve XML, `viewBox`, paths, transforms, text, CSS, filters, masks, clips, patterns and referenced images/fonts. Inventory dependencies and inherited styling; serialization alone does not establish a self-contained artifact. Compare the exported file in its intended renderer.

For Canvas record CSS and bitmap dimensions separately. `toBlob`/`toDataURL` export pixels, not drawing code or layers. An origin-unclean canvas denies pixel export. Use authorized visible capture and report that limitation. A screenshot cannot recover an editable scene graph.

For WebGL/WebGPU record backend, viewport, DPR, clock, seed, camera, assets and source/uniforms when available. Supported GPU debugging can investigate draw calls in a disposable authorized context; feature-detect and preserve an uninstrumented baseline. Verify frame capture is nonempty and at the intended phase. Buffer behavior and export require version-specific investigation. Shader, mesh and rig recovery remain inferred or unavailable unless those artifacts are supplied or delivered.

For Lottie, Rive, 3D and other formats inventory supplied files, runtime version, dependencies and inputs. Use documented runtime controls to seek when supported. Runtime files, exported animation and editor projects are different deliverables. Inspect format-specific primary docs before promising editable-project recovery; no universal converter is assumed.

For an unfamiliar artifact identify its native format and renderer, obtain the strongest accessible source, observe behavior, test an isolated reconstruction and compare actual exports. Report unsupported branches. A general workflow cannot guarantee a lossless inverse for every artifact.
