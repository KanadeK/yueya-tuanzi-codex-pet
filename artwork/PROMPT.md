# Image generation prompt

The pose board was generated with the built-in OpenAI image generation tool. The user-provided image was used only to understand the request for a small cute cat; it was not supplied to the model as an input and is not included in this repository.

```text
Use case: stylized-concept
Asset type: source pose board for a Codex Desktop pet sprite atlas
Primary request: Create a completely original mascot character named 月牙团子 (Yueya Tuanzi, "crescent-bun cat"), a cheerful tiny ginger-and-cream tuxedo kitten assistant. It must not resemble or recreate any existing character, sticker, franchise, or the supplied reference image. Give it distinctive asymmetrical features: a small crescent-moon-shaped cream patch over one eyebrow, amber diamond-shaped eyes, a teal knitted neckerchief with a single tiny silver round bell, and a short tail with two dark caramel bands.
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background, no floor, no shadows, no gradients, no texture.
Composition/framing: a clean 3 by 3 pose board. Nine full-body poses in reading order: calm seated idle; trotting right; trotting left; waving; happy hop; frustrated with a gray rain cloud; seated waiting beside a crescent moon; concentrating beside an abstract terminal; presenting a teal checkmark.
Style/medium: polished original 2D game mascot illustration, thick charcoal outlines, rounded shapes, warm coral-orange and cream palette with teal accent.
Constraints: #00ff00 appears only in the background. No text, logos, brand names, watermark, or visual copying.
```

The chroma-key source was converted locally with the image-generation skill's `remove_chroma_key.py` helper. `scripts/build_assets.py` crops the nine poses, creates the native status animations, packs the lossless WebP atlas, and emits GIF previews.
