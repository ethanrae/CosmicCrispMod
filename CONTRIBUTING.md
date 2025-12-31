# 🤝 How to Help with Cosmic Crisp Mod

We want to make this mod a joy to work on. You don't need to be a "coder" or install complex tools.
Find the section below that matches what you have installed!

---

### 🟢 Level 1: "I have nothing installed (Web Browser Only)"
**Great for:** Typos, Art tweaks, JSON config changes.

You can edit this mod entirely in your browser using **GitHub Codespaces**. It gives you a full code editor in the cloud.

1. Click the green **Code** button at the top of this repo.
2. Click the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait ~30 seconds. A VS Code window will open in your browser.
5. To test your art changes, type this in the terminal at the bottom:
   `python generate_assets.py`
6. When finished, click the **Source Control** icon (left sidebar) to commit your changes!

---

### 🟡 Level 2: "I have Python installed"
**Great for:** Local testing, experimenting with the art algorithm.

1. Clone this repo.
2. Install the art library:
   `pip install Pillow`
3. Run the generator:
   `python generate_assets.py`
4. Copy the files to your Game Mods folder manually (or use `setup_link.py` if you are on PC/Mac).

---

### 🔴 Level 3: "I have Docker installed"
**Great for:** Clean, one-command builds without installing Python locally.

Open your terminal in this folder and run:
`docker build -t echomp-builder . ; docker run --rm -v ${PWD}:/output echomp-builder`

*(Note: Requires the Dockerfile in the repo)*

---

### 🚀 How to Release a New Version
**No one needs to build the zip file manually.** 1. Go to the repo homepage.
2. Click **Releases** (on the right) -> **Draft a new release**.
3. Create a new tag (e.g., `v1.0.1`).
4. Click **Publish release**.

5. **Wait 1 minute.** GitHub Actions will automatically build the mod, generate the art, zip it, and attach it to your release for players to download.
