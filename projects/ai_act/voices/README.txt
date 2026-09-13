Narrator voice for "The Instrument".

Put the chosen reference clip here as narrator.wav, matching `voice: narrator` in series.yaml.
10s+ of clean, single-speaker audio at 24 kHz or better. The SAME clip is reused for every chunk
and every episode — that is the primary defence against timbre drift across a long series.

`prosodia submit` bundles this clip into the render job automatically, so the render box needs
no extra flags. To cut one from a longer recording:

    prosodia voice-prep source.wav --start 1:30 --out projects/ai_act/voices/narrator.wav
