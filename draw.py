#!/usr/bin/env python3
"""Render the invitation letter to entry.png (1024x1024).

Drawn with Pillow: warm paper, a small hand-drawn-style house-and-garden
illustration, and a short, legible serif letter. Text is wrapped by measured
width so nothing overflows.
"""

import math
import random

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "entry.png"

SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"

# Palette: warm cream paper, dark brown ink, muted garden colours.
PAPER = (247, 240, 221)
PAPER_DEEP = (238, 228, 202)
INK = (58, 44, 32)
INK_SOFT = (96, 78, 60)
ACCENT = (176, 92, 52)          # terracotta
ACCENT_DARK = (140, 66, 36)
GREEN = (106, 138, 86)
GREEN_DARK = (78, 108, 62)
GOLD = (201, 154, 74)
SKY = (214, 228, 226)
SEAL = (150, 48, 44)

random.seed(7)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Word-wrap `text` to lines no wider than max_w (measured pixels)."""
    lines = []
    for para in text.split("\n"):
        words = para.split(" ")
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def draw_house_scene(d):
    """A small cosy house with garden, sun and a steaming teacup."""
    cx = W // 2
    base_y = 232          # ground line
    house_w, house_h = 300, 150
    hx0, hx1 = cx - house_w // 2, cx + house_w // 2
    hy0, hy1 = base_y - house_h, base_y

    # Soft sky wash behind the house, drawn first so the sun sits on top.
    d.ellipse([cx - 430, 40, cx + 430, 300], fill=SKY)

    # Sun, top left of the scene.
    sun_x, sun_y, sun_r = cx - 330, 118, 26
    d.ellipse([sun_x - sun_r, sun_y - sun_r, sun_x + sun_r, sun_y + sun_r],
              fill=(233, 196, 106))
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        x0 = sun_x + int((sun_r + 6) * math.cos(a))
        y0 = sun_y + int((sun_r + 6) * math.sin(a))
        x1 = sun_x + int((sun_r + 16) * math.cos(a))
        y1 = sun_y + int((sun_r + 16) * math.sin(a))
        d.line([x0, y0, x1, y1], fill=(233, 196, 106), width=4)

    # Garden ground.
    d.ellipse([cx - 430, base_y - 14, cx + 430, base_y + 46], fill=(196, 214, 168))
    d.ellipse([cx - 380, base_y - 4, cx + 380, base_y + 30], fill=(178, 200, 148))

    # Chimney + smoke curls drifting sideways (kept inside the canvas).
    ch_x0, ch_y0 = cx + 92, hy0 - 58
    d.rectangle([ch_x0, ch_y0, ch_x0 + 30, hy0 + 6], fill=ACCENT_DARK)
    d.rectangle([ch_x0 - 4, ch_y0 - 8, ch_x0 + 34, ch_y0], fill=ACCENT_DARK)
    for i, (sx, sy, sr) in enumerate([(cx + 128, hy0 - 52, 9),
                                      (cx + 146, hy0 - 64, 11),
                                      (cx + 162, hy0 - 56, 10)]):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr],
                  outline=(170, 160, 140), width=3)

    # Roof.
    d.polygon([(hx0 - 26, hy0 + 6), (cx, hy0 - 78), (hx1 + 26, hy0 + 6)],
              fill=ACCENT)
    d.polygon([(hx0 - 26, hy0 + 6), (cx, hy0 - 78), (cx, hy0 + 6)],
              fill=ACCENT_DARK)

    # Walls.
    d.rectangle([hx0, hy0, hx1, hy1], fill=(250, 243, 224),
                outline=(120, 96, 70), width=3)

    # Door (arched top) with a little step.
    dx0, dx1 = cx - 26, cx + 26
    d.rectangle([dx0, hy1 - 78, dx1, hy1], fill=(122, 84, 52))
    d.pieslice([dx0, hy1 - 104, dx1, hy1 - 52], 180, 360, fill=(122, 84, 52))
    d.ellipse([cx + 12, hy1 - 44, cx + 20, hy1 - 36], fill=GOLD)
    d.rectangle([dx0 - 10, hy1 - 4, dx1 + 10, hy1 + 6], fill=(190, 170, 140))

    # Windows, warmly lit, with cross frames.
    for wx in (hx0 + 34, hx1 - 34 - 56):
        d.rectangle([wx, hy0 + 34, wx + 56, hy0 + 90], fill=(247, 214, 130),
                    outline=(120, 96, 70), width=3)
        d.line([wx + 28, hy0 + 34, wx + 28, hy0 + 90], fill=(120, 96, 70), width=3)
        d.line([wx, hy0 + 62, wx + 56, hy0 + 62], fill=(120, 96, 70), width=3)

    # Flowers along the garden.
    for fx, fy, col in [(cx - 330, base_y + 8, (196, 110, 110)),
                        (cx - 290, base_y + 20, (233, 196, 106)),
                        (cx + 300, base_y + 12, (196, 110, 110)),
                        (cx + 340, base_y + 22, (233, 196, 106)),
                        (cx - 250, base_y + 26, (176, 120, 160)),
                        (cx + 255, base_y + 28, (176, 120, 160))]:
        d.line([fx, fy, fx, fy - 14], fill=GREEN_DARK, width=3)
        d.ellipse([fx - 7, fy - 24, fx + 7, fy - 10], fill=col)

    # Bushes.
    d.ellipse([hx0 - 66, base_y - 34, hx0 - 6, base_y + 2], fill=GREEN)
    d.ellipse([hx1 + 6, base_y - 30, hx1 + 66, base_y + 2], fill=GREEN_DARK)

    # Steaming teacup, bottom right of the scene: a taller cup on a saucer,
    # with wavy steam rising from it.
    tx, ty = cx + 330, base_y - 6
    # Saucer.
    d.ellipse([tx - 38, ty + 2, tx + 38, ty + 14], fill=(232, 222, 200),
              outline=(120, 96, 70), width=2)
    # Cup body, taller than wide so it reads as a cup, not a blob.
    d.rounded_rectangle([tx - 30, ty - 30, tx + 30, ty + 4], radius=8,
                        fill=(255, 255, 255), outline=(120, 96, 70), width=3)
    # Tea surface.
    d.ellipse([tx - 26, ty - 30, tx + 26, ty - 18], fill=(196, 148, 92))
    # Handle.
    d.arc([tx + 24, ty - 26, tx + 52, ty + 2], 270, 90, fill=(120, 96, 70),
          width=4)
    # Wavy steam: two rising sine-wave wisps above the cup.
    for sx in (tx - 12, tx + 10):
        pts = []
        for step in range(13):
            t = step / 12.0
            pts.append((sx + 5 * math.sin(t * 2 * math.pi),
                        ty - 34 - t * 26))
        d.line(pts, fill=(150, 138, 120), width=3, joint="curve")


def draw_wax_seal(d, cx, cy, r=30):
    """A small red wax seal with a heart pressed in it."""
    pts = []
    for i in range(28):
        a = 2 * math.pi * i / 28
        rr = r + random.uniform(-3, 3)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=SEAL)
    d.ellipse([cx - r + 7, cy - r + 7, cx + r - 7, cy + r - 7],
              outline=(120, 30, 28), width=2)
    # Heart.
    hx, hy, s = cx, cy + 2, 11
    d.polygon([(hx, hy + s), (hx - s, hy - 2), (hx, hy - s)], fill=(247, 240, 221))
    d.polygon([(hx, hy + s), (hx + s, hy - 2), (hx, hy - s)], fill=(247, 240, 221))
    d.ellipse([hx - s, hy - s - 2, hx, hy + 2], fill=(247, 240, 221))
    d.ellipse([hx, hy - s - 2, hx + s, hy + 2], fill=(247, 240, 221))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Subtle paper texture: faint speckles.
    for _ in range(900):
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        d.point((x, y), fill=(232, 222, 196))

    # Double border, dark brown.
    d.rectangle([30, 30, W - 31, H - 31], outline=INK, width=3)
    d.rectangle([42, 42, W - 43, H - 43], outline=(150, 126, 96), width=1)

    draw_house_scene(d)

    f_header = font(SERIF_BOLD, 27)
    f_salut = font(SERIF_BOLD, 44)
    f_body = font(SERIF, 35)
    f_sign = font(SERIF_ITALIC, 33)
    f_ps = font(SERIF_ITALIC, 29)

    margin = 96
    text_w = W - 2 * margin

    # Small-caps style header.
    header = "·  A N  I N V I T A T I O N  ·"
    hw = d.textlength(header, font=f_header)
    d.text(((W - hw) / 2, 268), header, font=f_header, fill=ACCENT_DARK)

    # Salutation.
    y = 312
    d.text((margin, y), "Dear Judge,", font=f_salut, fill=INK)
    y += 62

    body = (
        "You have judged a thousand homes from a screen — now come and sit "
        "in a real one. The kettle is already on, the rice is steaming, and "
        "the old armchair by the window has your name on it (in pencil, so "
        "you can erase it if you must).",
        "No forms. No scores. Just one slow afternoon, a garden, and someone "
        "glad you came.",
        "Come and see — you are already welcome here.",
    )
    leading = 52
    for p, para in enumerate(body):
        for line in wrap(d, para, f_body, text_w):
            d.text((margin, y), line, font=f_body, fill=INK)
            y += leading
        if p + 1 < len(body):
            y += 12  # breathing room between paragraphs
    y += 14

    # Sign-off.
    sign = "— Your host, the human with the kettle"
    d.text((margin, y), sign, font=f_sign, fill=INK_SOFT)
    y += 52

    # Wax seal beside the sign-off.
    draw_wax_seal(d, W - margin - 34, y - 8, r=30)

    # Postscript: the knowing wink.
    ps = "P.S. No travel required — a good score still counts as a visit."
    d.text((margin, y + 26), ps, font=f_ps, fill=ACCENT_DARK)

    img.save(OUT, "PNG")
    print(f"saved {OUT} {W}x{H}")


if __name__ == "__main__":
    main()
