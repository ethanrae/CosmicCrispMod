# Cosmic Crisp Apples (Stardew Valley Mod)

Adds the **Cosmic Crisp Apple** to Stardew Valley.
This is a high-tech apple variety engineered for shelf stability.
It is worth a fortune when the market demands it in the Fall, but nearly worthless the rest of the year.

## 🎨 Art Styles & Customization

This mod produces zero asset bloat. All textures are procedurally generated on your machine when you install the mod.

**How to Generate Art:**
1. `pip install Pillow` (Required for art generation)
2. Run `python generate_assets.py`
3. Edit `config.json` to select your style:

| Style | Description |
| :--- | :--- |
| **Cosmic** (Default) | Modern, speckled, realistic texture with deep red tones. |
| **Genome** | Cute, plump shape with bold black outlines and flat coloring. |
| **Classic** | Traditional flat, vanilla-style colors matching the base game. |

## Features
* **New Tree:** Cosmic Crisp Sapling (Buy at Pierre's in Fall for 2000g).
* **Dynamic Pricing:** * **Fall:** 500g (High Demand)
  * **Spring/Summer/Winter:** 2g (Market Crash)
* **Growth:** Takes 28 days to mature (standard Fruit Tree).

## Requirements
* [Stardew Valley](https://www.stardewvalley.net/) (v1.6+)
* [SMAPI](https://smapi.io/)
* [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915)

---

## Developer Setup (For Contributors)

### 1. Clone the Repo
    git clone https://github.com/YOUR_USERNAME/CosmicCrispMod.git
    cd CosmicCrispMod

### 2. Link to Game
    python3 setup_link.py
*Follow the on-screen prompts.*

---

## Testing & Debug Strategy

### 1. Verify Shop & Growth
Walk into Pierre's General Store.
debug season fall

* **Check:** Pierre should now sell "Cosmic Crisp Sapling" for 2000g.
* **Action:** Buy one and plant it (requires 3x3 clear space).
* **Fast Forward:** Hover over the sapling and type:
  debug grow
  *(Repeat ~4 times until it looks like a full tree).*

### 2. Verify Harvest
    debug season fall
* **Check:** The tree should have an apple. Shake it to harvest.
* **Check Price:** The apple should sell for **500g**.

### 3. Verify Crash Price
    debug season spring
* **Check Price:** The apple should now sell for **2g**.

---

## License
MIT