import os
import sys
import platform
import subprocess

# --- CONFIGURATION ---
MOD_NAME = "CosmicCrispMod"
# ---------------------

def get_default_mods_path():
    """Attempts to find the default Stardew Valley Mods path based on OS."""
    system = platform.system()
    home = os.path.expanduser("~")

    if system == "Windows":
        # Common Steam path for Windows
        return r"C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Mods"
    elif system == "Darwin": # macOS
        return os.path.join(home, "Library/Application Support/Steam/steamapps/common/Stardew Valley/Contents/MacOS/Mods")
    elif system == "Linux":
        # Common Steam path for Linux (Proton/Native)
        return os.path.join(home, ".local/share/Steam/steamapps/common/Stardew Valley/Mods")
    return None

def create_symlink(source, target):
    """Creates a symbolic link in a cross-platform way."""
    print(f"Linking:\n  Source: {source}\n  Target: {target}")

    try:
        if os.path.exists(target):
            print(f"\n[!] Target already exists: {target}")
            print("    Please delete the existing folder in your Mods directory first.")
            return

        if platform.system() == "Windows":
            # Windows requires admin rights usually, or Developer Mode enabled.
            # Using mklink /D via cmd
            cmd = f'mklink /D "{target}" "{source}"'
            subprocess.run(cmd, shell=True, check=True)
        else:
            # Unix-based (Mac/Linux)
            os.symlink(source, target)

        print("\n[SUCCESS] Link created! You can now edit code here and see changes in-game.")

    except Exception as e:
        print(f"\n[ERROR] Could not create link: {e}")
        if platform.system() == "Windows":
            print("Note: On Windows, you may need to run this script as Administrator.")

def main():
    print(f"--- {MOD_NAME} Dev Setup ---")

    # 1. Get Source (Current Folder)
    source_dir = os.getcwd()

    # 2. Get Target (Game Mods Folder)
    default_target = get_default_mods_path()

    print(f"Detected OS: {platform.system()}")
    print("Enter your Stardew Valley 'Mods' folder path.")
    if default_target:
        print(f"Default detected: {default_target}")
        choice = input("Press [Enter] to use default, or paste a custom path: ").strip()
        mods_dir = choice if choice else default_target
    else:
        mods_dir = input("Path: ").strip()

    if not mods_dir:
        print("Operation cancelled.")
        return

    # 3. Create the Link
    full_target_path = os.path.join(mods_dir, MOD_NAME)
    create_symlink(source_dir, full_target_path)

if __name__ == "__main__":
    main()