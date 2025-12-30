# Cosmic Crisp Apples (Stardew Valley Mod)

Adds the **Cosmic Crisp Apple** to Stardew Valley.
This is a high-tech apple variety engineered for shelf stability.
It is worth a fortune when the market demands it in the Fall, but nearly worthless the rest of the year.

| Cosmic Crisp Apple | Seed Packet |
| :---: | :---: |
| ![Apple](assets/apple.png) | ![Seeds](assets/seeds.png) |

## Features
* **New Crop:** Cosmic Crisp Seeds (Buy at Pierre's in Fall).
* **Dynamic Pricing:** * **Fall:** 500g (High Demand)
    * **Spring/Summer/Winter:** 2g (Market Crash)
* **Growth:** Takes 10 days to mature.

## Requirements
* [Stardew Valley](https://www.stardewvalley.net/) (v1.6+)
* [SMAPI](https://smapi.io/)
* [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915)

---

## Developer Setup (For Contributors)

If you want to edit the mod and verify changes instantly without copying files back and forth, follow these steps.

### 1. Clone the Repo

    git clone https://github.com/YOUR_USERNAME/CosmicCrispMod.git
    cd CosmicCrispMod

### 2. Link to Game
We have included a Python script to automatically link this folder to your Game Mods folder. This works on **Windows, Mac, and Linux**.

    python3 setup_link.py

*Follow the on-screen prompts. Once finished, any change you make in this code folder is instantly applied to the game (restart required for JSON logic changes).*

---

## Testing & Debug Strategy

You do not need to play through 28 days to test this mod. Use the SMAPI Console (the black window that opens with the game).

### 1. Verify Shop & Growth
Walk into Pierre's General Store.

    debug season fall

* **Check:** Pierre should now sell "Cosmic Crisp Seeds" for 100g.
* **Action:** Buy one and plant it.
* **Fast Forward:** Hover over the planted crop and type:

  debug grow

*(Repeat until harvestable)*.

### 2. Verify Price Logic
Harvest the apple and keep it in your inventory.

**Test Crash Price (Out of Season)**

    debug season spring

* **Check:** Hover over the apple. It should sell for **2g**.

**Test Boom Price (In Season)**

    debug season fall

* **Check:** Hover over the apple. It should sell for **500g**.

---

## License
MIT