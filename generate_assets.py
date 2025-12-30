import os
import sys
import random
import math

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

def create_cosmic_style(path):
    # (This function remains unchanged from the previous iteration)
    """
    Generates the Cosmic Crisp apple with a true heart/apple shape
    (dips at both top and bottom) and rounded cheeks.
    """
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    pixels = img.load()

    # --- Palette ---
    BASE_RED = (170, 10, 30)
    HIGHLIGHT = (230, 100, 50)
    SHADOW = (90, 5, 15)
    SPECKLE = (240, 230, 140)
    STEM_COLOR = SHADOW

    cx, cy = 7.5, 7.5

    for y in range(16):
        for x in range(16):
            dx = x - cx
            dy = y - cy

            # 1. Shape Logic (Plump "Heart" Shape)
            # We use a slightly wider ellipse to make the sides round
            if (dx * 0.85)**2 + dy**2 < 7.4**2:

                # --- CUTOUTS (The "Butty" Logic) ---

                # Bottom Dip (The "Butt")
                # Remove pixels at the very bottom center to separate the cheeks
                if y >= 13 and (x >= 6 and x <= 9):
                    if y == 13 and (x == 6 or x == 9): pass # Soften the corner
                    else: continue

                    # Top Dip (The Stem Cavity)
                # Remove pixels at the very top center to create the heart top
                if y <= 2 and (x >= 6 and x <= 9):
                    # We allow row 2 to exist at the edges (6 and 9) for a curve
                    if y == 2 and (x == 6 or x == 9): pass
                    # We allow row 1 to exist at the far edges (x=5 or 10 would be outside anyway)
                    # But we cut out the middle of top rows
                    elif y < 2 and (x >= 7 and x <= 8): continue
                    elif y == 0: continue # Clear the very top row center

                # --- Base Shading ---
                dist_from_center = math.sqrt(dx**2 + dy**2)
                shadow_factor = max(0.0, (dist_from_center - 3.0) / 4.5)
                shadow_factor = min(1.0, shadow_factor)

                r = int(BASE_RED[0] * (1 - shadow_factor) + SHADOW[0] * shadow_factor)
                g = int(BASE_RED[1] * (1 - shadow_factor) + SHADOW[1] * shadow_factor)
                b = int(BASE_RED[2] * (1 - shadow_factor) + SHADOW[2] * shadow_factor)

                # --- Highlight Logic ---
                hx, hy = 4.0, 4.0
                dist_from_highlight = math.sqrt((x - hx)**2 + (y - hy)**2)
                highlight_factor = 0.0

                if dist_from_highlight < 4.5:
                    highlight_factor = (4.5 - dist_from_highlight) / 4.5
                    r = int(r * (1 - highlight_factor) + HIGHLIGHT[0] * highlight_factor)
                    g = int(g * (1 - highlight_factor) + HIGHLIGHT[1] * highlight_factor)
                    b = int(b * (1 - highlight_factor) + HIGHLIGHT[2] * highlight_factor)

                # --- Speckles ---
                # Keep speckles rare and away from the shiny halo
                if random.random() > 0.95 and shadow_factor < 0.7 and highlight_factor < 0.2:
                    pixels[x, y] = (SPECKLE[0], SPECKLE[1], SPECKLE[2], 255)
                else:
                    pixels[x, y] = (r, g, b, 255)

    # --- Stem Logic ---
    # Since we cut out the top, we need to plant the stem deep in the dip
    pixels[7, 0] = STEM_COLOR
    pixels[7, 1] = STEM_COLOR
    pixels[7, 2] = STEM_COLOR # Connects to the apple body at y=2
    pixels[8, 1] = STEM_COLOR # Little curve

    # Deepen the cavity shading right under the stem
    if pixels[6, 3][3] != 0: pixels[6, 3] = SHADOW
    if pixels[8, 3][3] != 0: pixels[8, 3] = SHADOW
    if pixels[7, 3][3] != 0: pixels[7, 3] = SHADOW

    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")

def create_classic_style(path):
    """Generates the Flat/Vanilla Stardew Look."""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    pixels = img.load()
    center_x, center_y, radius = 7.5, 7.5, 7.0

    # Bright Vanilla Red
    red = (220, 20, 60)

    for y in range(16):
        for x in range(16):
            dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            if dist <= radius:
                pixels[x, y] = (red[0], red[1], red[2], 255)

    # Stem
    pixels[7, 0] = (101, 67, 33, 255)
    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")

def create_genome_style(path):
    """
    Generates the 'Genome Cosmic Crisp' style:
    A cute, plump shape with a bold black outline and no face.
    """
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    pixels = img.load()

    # --- Palette ---
    OUTLINE_COLOR = (0, 0, 0, 255)
    FILL_COLOR_TOP = (200, 50, 60)
    FILL_COLOR_BOTTOM = (150, 20, 30)
    STEM_COLOR = OUTLINE_COLOR

    cx, cy = 7.5, 7.5

    # First pass: Fill the shape
    for y in range(16):
        for x in range(16):
            dx = x - cx
            dy = y - cy
            # Use the plump heart shape logic
            if (dx * 0.85)**2 + dy**2 < 7.4**2:
                # Bottom cutout
                if y >= 13 and (x >= 6 and x <= 9):
                    if y == 13 and (x == 6 or x == 9): pass
                    else: continue
                    # Top cutout
                if y <= 2 and (x >= 6 and x <= 9):
                    if y == 2 and (x == 6 or x == 9): pass
                    elif y < 2 and (x >= 7 and x <= 8): continue
                    elif y == 0: continue

                # Simple vertical gradient fill
                factor = y / 16.0
                r = int(FILL_COLOR_TOP[0] * (1 - factor) + FILL_COLOR_BOTTOM[0] * factor)
                g = int(FILL_COLOR_TOP[1] * (1 - factor) + FILL_COLOR_BOTTOM[1] * factor)
                b = int(FILL_COLOR_TOP[2] * (1 - factor) + FILL_COLOR_BOTTOM[2] * factor)
                pixels[x, y] = (r, g, b, 255)

    # Second pass: Apply the black outline
    # We check neighbors to find the edge pixels.
    img_copy = img.copy()
    pixels_copy = img_copy.load()

    for y in range(1, 15):
        for x in range(1, 15):
            # If this pixel is part of the apple...
            if pixels_copy[x, y][3] != 0:
                # Check its 4 cardinal neighbors. If any are transparent, this is an edge.
                is_edge = (pixels_copy[x-1, y][3] == 0 or
                           pixels_copy[x+1, y][3] == 0 or
                           pixels_copy[x, y-1][3] == 0 or
                           pixels_copy[x, y+1][3] == 0)
                if is_edge:
                    pixels[x, y] = OUTLINE_COLOR

    # --- Stem Logic (Black) ---
    pixels[7, 0] = STEM_COLOR
    pixels[7, 1] = STEM_COLOR
    pixels[7, 2] = STEM_COLOR
    pixels[8, 1] = STEM_COLOR

    img.save(os.path.join(path, 'apple.png'))
    print(f"Generated: {path}/apple.png")

# Create simple seeds for all (shared for now)
def create_seeds(path, style_name):
    """Generates a shaped seed packet with transparent corners."""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    pixels = img.load()
    start_x, end_x = 3, 13
    start_y, end_y = 2, 14
    paper_color = (210, 195, 150, 255)
    shadow_color = (180, 165, 120, 255)

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if x == start_x or x == end_x - 1 or y == end_y - 1:
                pixels[x, y] = shadow_color
            else:
                pixels[x, y] = paper_color

    # Emblem color based on style
    if style_name == "Cosmic":
        emblem_color = (160, 10, 30, 255)
    elif style_name == "Genome":
        emblem_color = (0, 0, 0, 255) # Black emblem for Genome style
    else:
        emblem_color = (220, 20, 60, 255)

    for y in range(6, 10):
        for x in range(6, 10):
            pixels[x, y] = emblem_color

    img.save(os.path.join(path, 'seeds.png'))
    print(f"Generated Shaped Seeds: {path}/seeds.png")

# --- TREE GENERATION ENGINE ---

def draw_blob_tree(pixels, start_x, width, height, season, style):
    """
    Procedurally draws a tree stage into the pixels array.
    season: 'growth1', 'growth2', 'growth3', 'spring', 'summer', 'fall', 'winter'
    style: 'Cosmic', 'Classic', 'Genome'
    """
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
        OUTLINE = (0, 0, 0, 255) # Bold Outline
    else: # Cosmic (Realistic/Dark)
        BARK = (70, 40, 30, 255)
        LEAF_SUMMER = (30, 90, 40, 255)
        LEAF_FALL = (160, 110, 30, 255)
        LEAF_SPRING = (180, 210, 180, 255) # Pale blossom look
        OUTLINE = None

    # Center of this tile
    cx = start_x + 24
    base_y = 75 # Ground level in the tile (80px tall)

    # --- 1. DEFINE SHAPES (Trunk Height & Canopy Radius) ---
    trunk_h = 0
    trunk_w = 0
    canopy_r = 0
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

    # --- 2. DRAW TRUNK ---
    # Genome Style: Draw thick black outline first
    if style == "Genome":
        for y in range(base_y - trunk_h - 1, base_y + 1):
            for x in range(cx - trunk_w - 1, cx + trunk_w + 2):
                if 0 <= x < width + start_x and 0 <= y < height:
                    pixels[x, y] = OUTLINE

    # Draw Trunk Fill
    for y in range(base_y - trunk_h, base_y):
        for x in range(cx - trunk_w, cx + trunk_w + 1):
            # Noise for texture
            noise = random.randint(-20, 20)
            r = max(0, min(255, BARK[0] + noise))
            g = max(0, min(255, BARK[1] + noise))
            b = max(0, min(255, BARK[2] + noise))

            if 0 <= x < width + start_x and 0 <= y < height:
                pixels[x, y] = (r, g, b, 255)

    # --- 3. DRAW CANOPY ---
    if canopy_r > 0 and season != 'winter':
        canopy_y = base_y - trunk_h + 5

        # Genome Style: Draw black canopy outline first
        if style == "Genome":
            for y in range(canopy_y - canopy_r - 2, canopy_y + canopy_r + 2):
                for x in range(cx - canopy_r - 2, cx + canopy_r + 2):
                    dist = math.sqrt((x - cx)**2 + (y - canopy_y)**2)
                    if dist <= canopy_r + 1.5:
                        if 0 <= x < width + start_x and 0 <= y < height:
                            pixels[x, y] = OUTLINE

        # Draw Leaf Fill
        for y in range(canopy_y - canopy_r, canopy_y + canopy_r + 1):
            for x in range(cx - canopy_r, cx + canopy_r + 1):
                dist = math.sqrt((x - cx)**2 + (y - canopy_y)**2)

                # Make the canopy irregular (not a perfect circle)
                noise_r = canopy_r + random.randint(-2, 1)

                if dist <= noise_r:
                    # Leaf Color gradients
                    noise = random.randint(-30, 30)
                    r = max(0, min(255, leaf_color[0] + noise))
                    g = max(0, min(255, leaf_color[1] + noise))
                    b = max(0, min(255, leaf_color[2] + noise))

                    if 0 <= x < width + start_x and 0 <= y < height:
                        pixels[x, y] = (r, g, b, 255)

    # Winter Mode (Branches instead of Leaves)
    if season == 'winter':
        # Simple diagonal branches
        branch_color = (BARK[0]+20, BARK[1]+20, BARK[2]+20, 255)
        start_y = base_y - trunk_h
        for i in range(15):
            # Left branch
            pixels[cx - int(i/1.5), start_y - i] = branch_color
            # Right branch
            pixels[cx + int(i/1.5), start_y - i] = branch_color


def create_tree_spritesheet(path, style):
    """Generates the full 432x80 spritesheet."""
    # Stardew Tree Sheets are 432px wide (9 tiles of 48px) x 80px tall
    WIDTH, HEIGHT = 432, 80
    TILE_W = 48

    img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    pixels = img.load()

    # 1. Sprout (Frame 0)
    draw_blob_tree(pixels, TILE_W * 0, WIDTH, HEIGHT, 'growth1', style)
    # 2. Bush (Frame 1)
    draw_blob_tree(pixels, TILE_W * 1, WIDTH, HEIGHT, 'growth2', style)
    # 3. Sapling (Frame 2)
    draw_blob_tree(pixels, TILE_W * 2, WIDTH, HEIGHT, 'growth3', style)
    # 4. Spring Mature (Frame 3)
    draw_blob_tree(pixels, TILE_W * 3, WIDTH, HEIGHT, 'spring', style)
    # 5. Summer Mature (Frame 4)
    draw_blob_tree(pixels, TILE_W * 4, WIDTH, HEIGHT, 'summer', style)
    # 6. Fall Mature (Frame 5)
    draw_blob_tree(pixels, TILE_W * 5, WIDTH, HEIGHT, 'fall', style)
    # 7. Winter Mature (Frame 6)
    draw_blob_tree(pixels, TILE_W * 6, WIDTH, HEIGHT, 'winter', style)

    # Save it
    filename = 'tree.png'
    img.save(os.path.join(path, filename))
    print(f"Generated Tree Spritesheet: {path}/{filename}")

def main():
    print("--- Building Art Variants ---")
    ensure_dirs()

    # 1. Cosmic Style
    create_cosmic_style(os.path.join(BASE_DIR, 'Cosmic'))
    create_seeds(os.path.join(BASE_DIR, 'Cosmic'), "Cosmic")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Cosmic'), "Cosmic") # <--- NEW

    # 2. Classic Style
    create_classic_style(os.path.join(BASE_DIR, 'Classic'))
    create_seeds(os.path.join(BASE_DIR, 'Classic'), "Classic")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Classic'), "Classic") # <--- NEW

    # 3. Genome Style
    create_genome_style(os.path.join(BASE_DIR, 'Genome'))
    create_seeds(os.path.join(BASE_DIR, 'Genome'), "Genome")
    create_tree_spritesheet(os.path.join(BASE_DIR, 'Genome'), "Genome") # <--- NEW

    print("--- Build Complete ---")

if __name__ == "__main__":
    main()