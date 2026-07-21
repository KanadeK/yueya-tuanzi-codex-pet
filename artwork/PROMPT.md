# Source handling

This package deliberately does not use a generative prompt or an AI-redrawn character.

- The pet uses the user-approved reference image of the “妙脆角小猫” character.
- Public searches were used only to check the character label and visual cues; no external image was downloaded, copied, or included.
- `scripts/extract_reference_cutout.py` uses local U2Net foreground segmentation plus a small, documented background-residue cleanup. It does not synthesize, restyle, or alter the cat.
- `artwork/processed/miaocui-jiao-cat-cutout.png` is the processed source for the sprite atlas. The original input image is not stored in this repository.
- `scripts/build_assets.py` derives every animation frame using only affine transforms of that one cutout.
