import os
import shutil
import subprocess
import zipfile

# --- CONFIGURATION ---
MOD_NAME = "eCHOMP_CosmicCrisp"  # The name of the folder inside the zip
ZIP_NAME = "eCHOMP_CosmicCrisp_Release" # The name of the zip file
FILES_TO_INCLUDE = [
    "content.json",
    "manifest.json",
    "config.json",
    "assets" # Copies the entire folder
]
# ---------------------

def clean_previous_builds():
    """Removes old temp folders and zip files."""
    if os.path.exists(MOD_NAME):
        shutil.rmtree(MOD_NAME)
    if os.path.exists(f"{ZIP_NAME}.zip"):
        os.remove(f"{ZIP_NAME}.zip")
    print("🧹 Cleaned up old build files.")

def generate_art():
    """Runs the art generator script to ensure assets are fresh."""
    print("🎨 Generating fresh assets...")
    try:
        subprocess.run(["python", "generate_assets.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error: generate_assets.py failed! Do you have Pillow installed?")
        exit(1)

def create_package():
    """Copies files into a clean folder."""
    print(f"📦 Packaging mod into '{MOD_NAME}'...")
    os.makedirs(MOD_NAME)

    for item in FILES_TO_INCLUDE:
        if os.path.isdir(item):
            shutil.copytree(item, os.path.join(MOD_NAME, item))
        elif os.path.isfile(item):
            shutil.copy(item, MOD_NAME)
        else:
            print(f"⚠️ Warning: Could not find '{item}'. skipping.")

def zip_package():
    """Zips the folder into a release-ready archive."""
    print(f"🤐 Zipping into {ZIP_NAME}.zip...")
    shutil.make_archive(ZIP_NAME, 'zip', root_dir='.', base_dir=MOD_NAME)

    # Cleanup the temp folder
    shutil.rmtree(MOD_NAME)
    print(f"✅ SUCCESS! Created {ZIP_NAME}.zip")

if __name__ == "__main__":
    clean_previous_builds()
    generate_art()
    create_package()
    zip_package()