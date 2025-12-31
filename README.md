# 🍎 Cosmic Crisp Apple (Stardew Valley Mod)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Stardew](https://img.shields.io/badge/Stardew_Valley-1.6+-green) ![License](https://img.shields.io/badge/license-MIT-orange)

**The Future of Fruit is Here.**

This mod adds the **Cosmic Crisp Apple** to Stardew Valley—a high-tech, genetically engineered super-fruit designed for massive shelf-life and crispness.

In-game, this plays out as a high-risk, high-reward investment. The market for these "designer apples" is volatile: they are worth a fortune during the peak demand of **Fall**, but the market crashes to near-zero value for the rest of the year.

---

## ✨ Key Features

* **🌱 New Fruit Tree:** The **Cosmic Crisp Sapling**.
  * *Growth:* Takes **28 days** to mature (standard fruit tree rules).
  * *Season:* Bears fruit in **Fall**.
* **📈 Dynamic Economy:**
  * **Fall (Peak Season):** Apples sell for **500g** each.
  * **Off-Season:** Price crashes to **2g** (shelf-stable, but worthless).
* **🎨 Zero-Bloat Art Engine:**
  * This mod contains **no image files**.
  * All textures are **procedurally generated** by Python code when you install or build the mod.
  * Choose from 3 unique aesthetic styles (Realistic, Cute, or Classic).

---

## 📥 Installation

### For Players (Standard Install)
1.  Download the latest `.zip` from the **[Releases](https://github.com/eCHOMP/CosmicCrispMod/releases)** page.
2.  Unzip the folder.
3.  Drag the `eCHOMP_CosmicCrisp` folder into your Stardew Valley `Mods` folder.
4.  Run the game!

### For Developers (Manual Build)
If you want to modify the code or generate the art yourself:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/eCHOMP/CosmicCrispMod.git](https://github.com/eCHOMP/CosmicCrispMod.git)
    cd CosmicCrispMod
    ```
2.  **Generate Assets:**
    ```bash
    pip install Pillow
    python generate_assets.py
    ```
3.  **Link to Game:**
    ```bash
    python setup_link.py
    ```

---

## 🎨 Art Styles & Configuration

You can switch the visual style of the apples and trees at any time.
* **Method 1:** Edit `config.json` in the mod folder.
* **Method 2:** Use **Generic Mod Config Menu** in-game.

| Style | Description |
| :--- | :--- |
| **Cosmic** (Default) | Modern, speckled, realistic texture with deep red tones. |
| **Genome** | Cute, plump shape with bold black outlines and flat coloring. |
| **Classic** | Traditional flat, vanilla-style colors matching the base game. |

---

## 🛠️ Testing & Debugging

You don't need to wait 28 days to verify the mod works. Use the SMAPI Console commands below:

**1. Verify Shop & Growth**
```bash
debug season fall
```
* **Check:** Go to Pierre's. He should sell "Cosmic Crisp Sapling" for **2000g**.
* **Action:** Plant one. Hover over it and run `debug grow` ~4 times until mature.

**2. Verify Market Boom (Fall)**
```bash
debug season fall
```
* **Check:** Harvest an apple. It should sell for **500g**.

**3. Verify Market Crash (Spring/Summer/Winter)**
```bash
debug season spring
```
* **Check:** The same apple should now sell for only **2g**.

---

## 📋 Requirements

* [Stardew Valley](https://www.stardewvalley.net/) (v1.6+)
* [SMAPI](https://smapi.io/)
* [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915)

---

## 📄 License

**The GFSF License** © Ethan Rae (eCHOMP)

This mod is free for personal use.

⚠️ **Commercial Use:**
If you wish to sell this mod or include it in a paid product, you must select one of the following licensing tiers:
1.  **Revenue Share:** 50% of your gross profits (prorated by usage).
2.  **Enterprise Buyout:** One-time fee of **$100,000,000 USD**.

*See `LICENSE` file for legal details. Serious inquiries only.*