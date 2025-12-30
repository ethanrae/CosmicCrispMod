import os
import sys

# Try to import Pillow. If it fails, give helpful instructions.
try:
    from PIL import Image
except ImportError:
    print("\n!!! ERROR: Pillow library not found. !!!")
    print("Please install it by typing this in your terminal:")
    print("pip install Pillow\n")
    sys.exit(1)

# --- Configuration ---
ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
APPLE_COLOR = (220, 20, 60, 255)   # Crimson Red
SEEDS_COLOR = (139, 69, 19, 255)   # Saddle Brown
# ---------------------

def create_placeholder(filename, color):
    """Creates a 16x16 solid color PNG."""
    # Ensure assets directory exists
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        print(f"Created missing directory: {ASSETS_DIR}")

    # Create the image
    img = Image.new('RGBA', (16, 16), color)

    # Save path
    filepath = os.path.join(ASSETS_DIR, filename)
    img.save(filepath, 'PNG')
    print(f"[SUCCESS] Created placeholder: assets/{filename}")

if __name__ == "__main__":
    print("--- Generating Placeholder Assets ---")
    create_placeholder('apple.png', APPLE_COLOR)
    create_placeholder('seeds.png', SEEDS_COLOR)
    print("--- Done. You can now run the mod. ---")