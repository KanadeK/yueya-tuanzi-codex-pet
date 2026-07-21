from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


# The path follows the outline of the user-supplied reference at 820 px wide.
# It is deliberately a deterministic mask: no generative model redraws or alters
# the cat.  It can be retuned only with another authorized source image.
SILHOUETTE = (
    (206, 35), (248, 57), (286, 78), (343, 83), (408, 80), (477, 80),
    (535, 88), (594, 76), (646, 70), (643, 126), (628, 177), (632, 239),
    (636, 317), (637, 407), (634, 496), (622, 558), (602, 607), (572, 635),
    (537, 652), (514, 672), (476, 680), (440, 678), (414, 664), (400, 645),
    (380, 646), (364, 665), (335, 679), (300, 680), (267, 666), (247, 644),
    (218, 626), (198, 590), (187, 548), (181, 486), (181, 416), (185, 345),
    (190, 285), (194, 219), (201, 165), (201, 105),
)


def build_cutout(source: Path, output: Path) -> None:
    image = Image.open(source).convert("RGBA")
    if image.width != 820 or image.height < 700:
        raise ValueError(
            f"Expected the approved 820 px-wide reference image, got {image.size}"
        )

    scale = 4
    mask = Image.new("L", (image.width * scale, image.height * scale), 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon([(x * scale, y * scale) for x, y in SILHOUETTE], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=1.2 * scale)).resize(
        image.size, Image.Resampling.LANCZOS
    )
    # Contract the feathered edge by six pixels.  This removes the light
    # source-background halo without changing the visible cat artwork.
    mask = mask.filter(ImageFilter.MinFilter(size=13))
    result = image.copy()
    result.putalpha(mask)
    # The source background has saturated cyan accents.  They cannot belong to
    # the gray-and-white cat, so remove only those pixels left inside the broad
    # hand-drawn silhouette while leaving neutral fur and white paws intact.
    pixels = []
    for red, green, blue, alpha in result.get_flattened_data():
        is_cyan_background = green > red + 22 and blue > red + 30 and green > 150
        pixels.append((red, green, blue, 0 if is_cyan_background else alpha))
    result.putdata(pixels)
    output.parent.mkdir(parents=True, exist_ok=True)
    result.save(output, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a transparent, source-faithful pet cutout")
    parser.add_argument("--input", required=True, type=Path, help="Authorized reference image")
    parser.add_argument("--output", required=True, type=Path, help="PNG cutout destination")
    args = parser.parse_args()
    build_cutout(args.input, args.output)


if __name__ == "__main__":
    main()
