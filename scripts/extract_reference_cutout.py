from __future__ import annotations

import argparse
import sys
from pathlib import Path
from types import ModuleType

from PIL import Image, ImageDraw


def _stub(name: str, **members: object) -> None:
    module = ModuleType(name)
    for member, value in members.items():
        setattr(module, member, value)
    sys.modules[name] = module


def _install_unused_alpha_matting_stubs() -> None:
    """Use rembg's ordinary U2Net path without its optional alpha-matting code."""
    unused = lambda *args, **kwargs: None
    _stub("pymatting")
    _stub("pymatting.alpha")
    _stub("pymatting.alpha.estimate_alpha_cf", estimate_alpha_cf=unused)
    _stub("pymatting.foreground")
    _stub("pymatting.foreground.estimate_foreground_ml", estimate_foreground_ml=unused)
    _stub("pymatting.util")
    _stub("pymatting.util.util", stack_images=unused)


def _clear_known_background_residue(image: Image.Image) -> Image.Image:
    """Remove blue-purple source-background fragments below the cat's paws."""
    cleaned: list[tuple[int, int, int, int]] = []
    for y in range(image.height):
        for red, green, blue, alpha in [
            image.getpixel((x, y)) for x in range(image.width)
        ]:
            is_lower_blue_residue = y > 590 and blue > red + 10 and blue > green + 8
            cleaned.append((red, green, blue, 0 if is_lower_blue_residue else alpha))
    image.putdata(cleaned)
    # The reference has a visible platform between the two feet.  It is not
    # part of the character and is made transparent after segmentation.
    ImageDraw.Draw(image).polygon(
        [(380, 625), (470, 625), (492, 735), (358, 735)], fill=(0, 0, 0, 0)
    )
    return image


def build_cutout(source: Path, output: Path) -> None:
    _install_unused_alpha_matting_stubs()
    from rembg import new_session, remove

    session = new_session("u2netp")
    cutout = remove(Image.open(source).convert("RGBA"), session=session)
    output.parent.mkdir(parents=True, exist_ok=True)
    _clear_known_background_residue(cutout).save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a source-faithful transparent pet cutout")
    parser.add_argument("--input", required=True, type=Path, help="Authorized reference image")
    parser.add_argument("--output", required=True, type=Path, help="PNG cutout destination")
    args = parser.parse_args()
    build_cutout(args.input, args.output)


if __name__ == "__main__":
    main()
