import math
import os
import random
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Please install Pillow: pip install Pillow")
    sys.exit(1)

BASE_DIR = os.path.join(os.getcwd(), 'assets')


def ensure_dirs():
    """Creates subfolders for the config options."""
    for style in ['Cosmic', 'Classic', 'Genome']:
        path = os.path.join(BASE_DIR, style)
        if not os.path.exists(path):
            os.makedirs(path)


# --- APPLE ART GENERATORS ---

def create_cosmic_style(path):
    """Generates the Cosmic Crisp apple (Realistic)."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    pixels = img.load()

    BASE_RED = (170, 10, 30)
    HIGHLIGHT = (230, 100, 50)
    SHADOW = (90, 5, 15)
    SPECKLE = (240, 230, 140)
    STEM_COLOR = SHADOW
    cx, cy = 7.5, 7.5

    for y in range(16):
        for x in range(16):
            dx, dy = x - cx, y - cy
            if (dx * 0.85) ** 2 + dy ** 2 < 7.4 ** 2:
                # Cutouts
                if y >= 13 and (x >= 6 and x <= 9):
                    if not (y == 13 and (x == 6 or x == 9)): continue
                if y <= 2 and (x >= 6 and x <= 9):
                    if y == 2 and (x == 6 or x == 9):
                        pass
                    elif y < 2 and (x >= 7 and x <= 8):
                        continue
                    elif y == 0:
                        continue

                # Shading
                dist = math.sqrt(dx ** 2 + dy ** 2)
                shadow = max(0.0, min(1.0, (dist - 3.0) / 4.5))
                r = int(BASE_RED[0] * (1 - shadow) + SHADOW[0] * shadow)
                g = int(BASE_RED[1] * (1 - shadow) + SHADOW[1] * shadow)
                b = int(BASE_RED[2] * (1 - shadow) + SHADOW[2] * shadow)

                # Highlight
                h_dist = math.sqrt((x - 4.0) ** 2 + (y - 4.0) ** 2)
                if h_dist < 4.5:
                    h_factor = (4.5 - h_dist) / 4.5
                    r = int(r * (1 - h_factor) + HIGHLIGHT[0] * h_factor)
                    g = int(g * (1 - h_factor) + HIGHLIGHT[1] * h_factor)
                    b = int(b * (1 - h_factor) + HIGHLIGHT[2] * h_factor)

                # Speckles
                if random.random() > 0.95 and shadow < 0.7 and h_dist > 2.0:
                    pixels[x, y] = (SPECKLE[0], SPECKLE[1], SPECKLE[2], 255)
                else:
                    pixels[x, y] = (r, g, b, 255)

    # Stem
    for i in range(3): pixels[7, i] = STEM_COLOR
    pixels[8, 1] = STEM_COLOR
    if pixels[7, 3][3] != 0: pixels[7, 3] = SHADOW

    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")


def create_classic_style(path):
    """Generates the Classic apple (Vanilla Flat)."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    pixels = img.load()
    cx, cy = 7.5, 7.5
    red = (220, 20, 60)

    for y in range(16):
        for x in range(16):
            if math.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= 7.0:
                pixels[x, y] = (red[0], red[1], red[2], 255)
    pixels[7, 0] = (101, 67, 33, 255)
    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")


def create_genome_style(path):
    """Generates the Genome apple (Cute/Outline)."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    pixels = img.load()
    OUTLINE = (0, 0, 0, 255)
    TOP, BOT = (200, 50, 60), (150, 20, 30)
    cx, cy = 7.5, 7.5

    for y in range(16):
        for x in range(16):
            dx, dy = x - cx, y - cy
            if (dx * 0.85) ** 2 + dy ** 2 < 7.4 ** 2:
                if y >= 13 and (x >= 6 and x <= 9):
                    if not (y == 13 and (x == 6 or x == 9)): continue
                if y <= 2 and (x >= 6 and x <= 9):
                    if y == 2 and (x == 6 or x == 9):
                        pass
                    elif y < 2 and (x >= 7 and x <= 8):
                        continue
                    elif y == 0:
                        continue

                f = y / 16.0
                r = int(TOP[0] * (1 - f) + BOT[0] * f)
                g = int(TOP[1] * (1 - f) + BOT[1] * f)
                b = int(TOP[2] * (1 - f) + BOT[2] * f)
                pixels[x, y] = (r, g, b, 255)

    # Outline Pass
    img_copy = img.copy()
    p_copy = img_copy.load()
    for y in range(1, 15):
        for x in range(1, 15):
            if p_copy[x, y][3] != 0:
                if (p_copy[x - 1, y][3] == 0 or p_copy[x + 1, y][3] == 0 or
                        p_copy[x, y - 1][3] == 0 or p_copy[x, y + 1][3] == 0):
                    pixels[x, y] = OUTLINE

    pixels[7, 0] = OUTLINE
    pixels[7, 1] = OUTLINE
    pixels[8, 1] = OUTLINE
    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")


# --- SAPLING ICON GENERATOR (Replaces Seeds) ---

def create_sapling_icon(path, style_name):
    """Generates a Sapling Pot icon (Orange pot with a small tree)."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    pixels = img.load()

    # 1. Draw the Pot (Trapezoid shape)
    pot_color = (200, 90, 20, 255)  # Terracotta orange
    pot_shadow = (160, 60, 10, 255)

    # Pot Rim
    for x in range(4, 12):
        pixels[x, 10] = pot_color

    # Pot Body
    for y in range(11, 15):
        for x in range(5, 11):
            pixels[x, y] = pot_color
            if x == 5 or x == 10:  # Shadow on edges
                pixels[x, y] = pot_shadow

    # 2. Draw the Sapling Stem
    stem_color = (100, 60, 20, 255)
    for y in range(4, 11):
        pixels[7, y] = stem_color
        pixels[8, y] = stem_color  # 2px wide stem

    # 3. Draw the Leaves (Style Dependent)
    if style_name == "Cosmic":
        leaf_color = (40, 160, 60, 255)
    elif style_name == "Genome":
        leaf_color = (60, 200, 80, 255)
    else:  # Classic
        leaf_color = (60, 200, 60, 255)

    # Simple clump of leaves at the top
    for y in range(1, 6):
        for x in range(5, 11):
            dist = math.sqrt((x - 7.5) ** 2 + (y - 3.5) ** 2)
            if dist < 2.5:
                pixels[x, y] = leaf_color
                # Add Outline for Genome
                if style_name == "Genome" and dist > 1.5:
                    pixels[x, y] = (0, 0, 0, 255)

    img.save(os.path.join(path, 'sapling.png'))
    print(f"Generated Sapling Icon: {path}/sapling.png")


# --- TREE SPRITESHEET GENERATOR ---

def draw_blob_tree(pixels, start_x, width, height, season, style):
    # Palette
    if style == "Classic":
        BARK = (120, 80, 40, 255)
        LEAF_SUMMER = (40, 180, 40, 255)
        LEAF_FALL = (220, 100, 40, 255)
        LEAF_SPRING = (100, 220, 100, 255)
        OUTLINE = None
    elif style == "Genome":
        BARK = (100, 50, 50, 255)
        LEAF_SUMMER = (60, 200, 80, 255)
        LEAF_FALL = (200, 80, 60, 255)
        LEAF_SPRING = (100, 240, 120, 255)
        OUTLINE = (0, 0, 0, 255)
    else:  # Cosmic
        BARK = (70, 40, 30, 255)
        LEAF_SUMMER = (30, 90, 40, 255)
        LEAF_FALL = (160, 110, 30, 255)
        LEAF_SPRING = (180, 210, 180, 255)
        OUTLINE = None

    cx = start_x + 24
    base_y = 75
    trunk_h, trunk_w, canopy_r = 0, 0, 0
    leaf_color = LEAF_SUMMER

    if season == 'growth1':
        trunk_h, trunk_w, canopy_r = 10, 2, 0
    elif season == 'growth2':
        trunk_h, trunk_w, canopy_r = 18, 3, 8
    elif season == 'growth3':
        trunk_h, trunk_w, canopy_r = 30, 4, 14
    elif season in ['spring', 'summer', 'fall', 'winter']:
        trunk_h, trunk_w, canopy_r = 45, 6, 20
        if season == 'fall': leaf_color = LEAF_FALL
        if season == 'spring': leaf_color = LEAF_SPRING

    # Trunk
    if style == "Genome":
        for y in range(base_y - trunk_h - 1, base_y + 1):
            for x in range(cx - trunk_w - 1, cx + trunk_w + 2):
                if 0 <= x < width + start_x and 0 <= y < height: pixels[x, y] = OUTLINE
    for y in range(base_y - trunk_h, base_y):
        for x in range(cx - trunk_w, cx + trunk_w + 1):
            noise = random.randint(-20, 20)
            r = max(0, min(255, BARK[0] + noise))
            g = max(0, min(255, BARK[1] + noise))
            b = max(0, min(255, BARK[2] + noise))
            if 0 <= x < width + start_x and 0 <= y < height: pixels[x, y] = (r, g, b, 255)

    # Canopy
    if canopy_r > 0 and season != 'winter':
        canopy_y = base_y - trunk_h + 5
        if style == "Genome":
            for y in range(canopy_y - canopy_r - 2, canopy_y + canopy_r + 2):
                for x in range(cx - canopy_r - 2, cx + canopy_r + 2):
                    if math.sqrt((x - cx) ** 2 + (y - canopy_y) ** 2) <= canopy_r + 1.5:
                        if 0 <= x < width + start_x and 0 <= y < height: pixels[x, y] = OUTLINE
        for y in range(canopy_y - canopy_r, canopy_y + canopy_r + 1):
            for x in range(cx - canopy_r, cx + canopy_r + 1):
                if math.sqrt((x - cx) ** 2 + (y - canopy_y) ** 2) <= canopy_r + random.randint(-2, 1):
                    noise = random.randint(-30, 30)
                    r = max(0, min(255, leaf_color[0] + noise))
                    g = max(0, min(255, leaf_color[1] + noise))
                    b = max(0, min(255, leaf_color[2] + noise))
                    if 0 <= x < width + start_x and 0 <= y < height: pixels[x, y] = (r, g, b, 255)

    if season == 'winter':
        branch_color = (BARK[0] + 20, BARK[1] + 20, BARK[2] + 20, 255)
        start_y = base_y - trunk_h
        for i in range(15):
            pixels[cx - int(i / 1.5), start_y - i] = branch_color
            pixels[cx + int(i / 1.5), start_y - i] = branch_color


def create_tree_spritesheet(path, style):
    WIDTH, HEIGHT, TILE_W = 432, 80, 48
    img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    pixels = img.load()
    stages = ['growth1', 'growth2', 'growth3', 'spring', 'summer', 'fall', 'winter']
    for i, stage in enumerate(stages):
        draw_blob_tree(pixels, TILE_W * i, WIDTH, HEIGHT, stage, style)
    img.save(os.path.join(path, 'tree.png'))
    print(f"Generated Tree Spritesheet: {path}/tree.png")


def main():
    print("--- Building Art Variants ---")
    ensure_dirs()

    # 1. Cosmic Style
    create_cosmic_style(os.path.join(BASE_DIR, 'Cosmic'))
    create_sapling_icon(os.path.join(BASE_DIR, 'Cosmic'), "Cosmic")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Cosmic'), "Cosmic")

    # 2. Classic Style
    create_classic_style(os.path.join(BASE_DIR, 'Classic'))
    create_sapling_icon(os.path.join(BASE_DIR, 'Classic'), "Classic")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Classic'), "Classic")

    # 3. Genome Style
    create_genome_style(os.path.join(BASE_DIR, 'Genome'))
    create_sapling_icon(os.path.join(BASE_DIR, 'Genome'), "Genome")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Genome'), "Genome")

    print("--- Build Complete ---")


if __name__ == "__main__":
    main()
