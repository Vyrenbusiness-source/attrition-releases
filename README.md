<h1 align="center">ATTRITION</h1>

<p align="center"><b>A free hardcore tactical FPS for Windows: take your own gear into a destructible voxel city, fight AI squads alone or in co-op, and lose it all if you don't make it back.</b></p>

<p align="center"><a href="https://github.com/Vyrenbusiness-source/attrition-releases/releases/latest"><img src="https://img.shields.io/badge/Download%20free-Windows%2010%20%2F%2011-2ea44f?style=for-the-badge&logo=windows&logoColor=white" height="52" alt="Download ATTRITION for free"></a></p>

<p align="center">
<a href="https://github.com/Vyrenbusiness-source/attrition-releases/releases/latest"><img src="https://img.shields.io/github/v/release/Vyrenbusiness-source/attrition-releases?label=version&style=flat-square&color=e8a33d" alt="Latest version"></a>
<a href="https://github.com/Vyrenbusiness-source/attrition-releases/releases"><img src="https://img.shields.io/github/downloads/Vyrenbusiness-source/attrition-releases/total?label=downloads&style=flat-square" alt="Total downloads"></a>
<a href="https://github.com/Vyrenbusiness-source/attrition-releases/releases/latest"><img src="https://img.shields.io/github/release-date/Vyrenbusiness-source/attrition-releases?label=released&style=flat-square" alt="Release date"></a>
<img src="https://img.shields.io/badge/status-alpha-d9534f?style=flat-square" alt="Status: alpha">
<a href="LICENSE"><img src="https://img.shields.io/badge/license-free%20to%20play%20%26%20share-555?style=flat-square" alt="License: free to play and share"></a>
<img src="https://img.shields.io/badge/engine-Godot%204-478CBF?style=flat-square" alt="Godot 4">
</p>

<p align="center"><a href="https://www.youtube.com/watch?v=Mkiqu9hALas"><img src="https://img.youtube.com/vi/Mkiqu9hALas/maxresdefault.jpg" width="100%" alt="Watch the ATTRITION trailer on YouTube"></a><br><sub>▶ <a href="https://www.youtube.com/watch?v=Mkiqu9hALas">Watch the trailer on YouTube</a></sub></p>

<p align="center"><a href="#english">English</a> · <a href="#deutsch">Deutsch</a> · <a href="#latest-updates">Latest updates</a> · <a href="#neueste-updates">Neueste Updates</a> · <a href="CONTRIBUTING.md">Report a bug</a></p>

> [!IMPORTANT]
> **Early alpha – expect bugs and frequent updates.** New versions often ship several times a day, and the game installs them by itself.
>
> **Language:** the game is in German for now. An English version is on the way. Menus and the HUD are short and work fine without German.

---

<a id="english"></a>

## About the game

You are one soldier in a war that keeps going without you. Four factions fight over a city with hundreds of AI soldiers, tanks, helicopters and drones, and every wall can be shot through or blown apart.

What you take into a fight is yours to lose. You draw a free standard kit, or you go in with gear you bought or looted. If you die, it stays on your body, and whoever gets there first can take it. If you make it back, you keep everything and get paid for what you did out there.

<p align="center"><img src="media/hero.jpg" width="100%" alt="ATTRITION – soldier on a rooftop over a burning city at night"></p>

## Features

<table>
<tr>
<td width="50%" valign="top"><img src="media/squad-smoke.jpg" alt="Medic and rifleman in smoke at a tree line"><br><b>A war that fights back</b><br>The AI works in squads: it takes cover, throws smoke to cross open ground or to pull a wounded man out, and shoots at radio operators and leaders first. It only knows what it can see or hear.</td>
<td width="50%" valign="top"><img src="media/medic.jpg" alt="Applying a tourniquet in first person"><br><b>Wounds and field medicine</b><br>Hits follow wound ballistics: one rifle round to the torso usually puts you down. Bleeding, fractures and chest wounds each need the right fix: tourniquet, pressure bandage, combat gauze, chest seal, splint, morphine or an IV.</td>
</tr>
<tr>
<td width="50%" valign="top"><img src="media/trader.jpg" alt="Gunsmith with an HK416 selected and the locker on the right"><br><b>Traders and a war economy</b><br>Four traders, each with their own stock, trust levels and prices. Prices come from the war itself: destroy a factory and its goods get scarce. The gunsmith repairs plates and helmets.</td>
<td width="50%" valign="top"><img src="media/inventory.jpg" alt="Inventory with helmet, plate carrier and backpack"><br><b>Inventory that matters</b><br>Grid inventory with backpacks, plate carriers and plates that wear out. Magazines are filled round by round, in real time, while the fight goes on. Weight changes how fast and how loud you move.</td>
</tr>
<tr>
<td width="50%" valign="top"><img src="media/workbench.jpg" alt="Workbench with a suppressor preview on the rifle"><br><b>48 weapons, 110+ attachments</b><br>Every weapon can be bought right away. Attachments unlock with weapon level and go on at the workbench, with a 3D preview and before/after values for recoil, noise, weight and handling.</td>
<td width="50%" valign="top"><img src="media/forest.jpg" alt="Forest road in the evening light"><br><b>A world built from models</b><br>Rounded terrain, forests with real trunks and undergrowth, streets, rail yards and industry as proper 3D models. Every wall can still be shot through or blown up.</td>
</tr>
<tr>
<td width="50%" valign="top"><img src="media/street-fight.jpg" alt="Night fight in a burning street, first person"><br><b>Objectives with history</b><br>A match runs about 90 minutes over six objectives. Between stages the team votes on the next target. Events like armored pushes, artillery, a downed helicopter or a change in the weather can turn a round.</td>
<td width="50%" valign="top"><img src="media/rain.jpg" alt="Squad under red smoke in the rain"><br><b>Weather, day and night</b><br>Rain, fog, snow and darkness cut visibility for you and the AI alike. At night the fighting runs under flares and burning houses.</td>
</tr>
<tr>
<td colspan="2" valign="top"><img src="media/freight-yard.jpg" alt="Freight yard with wagons and containers"><br><b>Field promotion</b><br>Points from a round promote you up to lieutenant. Each rank adds call-ins such as mortar fire, a recon drone, a smoke screen, a transport helicopter, artillery or a single guided round. Dying costs you one rank.</td>
</tr>
</table>

## Simulated like the real thing

ATTRITION models the things that decide real firefights instead of hit points and health bars:

* **Wound ballistics.** Damage depends on caliber class and hit zone. One or two rifle hits to the torso usually take you out of the fight, a head hit kills with any caliber. Wounds cause blood loss, shock, fractures and chest wounds.
* **Field medicine after TCCC.** Each injury needs its own fix (tourniquet, pressure bandage, combat gauze, chest seal, splint, morphine, IV), and each treatment takes time while the fight goes on.
* **Armor plates that wear out.** Steel and ceramic plates hold a set number of hits depending on the caliber. Ceramic is lighter but cracks faster; once a plate is through, it is gone.
* **Sound at the speed of sound.** A shot is heard after distance ÷ 343 m/s. When rounds pass close, you hear the supersonic crack first and the muzzle report after it.
* **Bullets that travel.** Shots follow real trajectories and go through thin walls and cover, depending on the material.
* **Real weapon sounds.** Firing sounds are real recordings with several variations per shot, not synthesized effects.
* **AI that has to perceive you.** Soldiers only react to what they see or hear. Distance, light, weather, movement and your silhouette matter: a large backpack or radio pack makes you easier to spot.
* **A war economy.** Trader prices follow supply and demand from the war: destroy a factory and its goods get scarce.
* **Terrain as cover.** Slopes, ditches, walls and buildings block sight and fire, and every wall can be shot through or blown apart.

### The loop

1. **Draw your kit** at the spawn screen: a free standard kit for your role, or your own gear from the locker.
2. **Deploy** and fight for the current objective.
3. **Get paid.** Every kill pays, with a hazard bonus when you were outnumbered, under fire or fighting indoors. Friendly fire costs you.
4. **Loot** the fallen without a loading screen. Kneeling over a body is loud and you are exposed.
5. **Die and lose it**, or get **relieved**: 20 seconds without enemy contact at a base or rally point and your gear goes back into the locker.
6. **Settle up** at the end of the round with a personal statement of everything you earned and lost.

Weapon sound comes from real recordings, with several variations per shot. Distant shots arrive with the delay of the speed of sound: first the crack, then the report.

## Game modes

| Mode | |
|---|---|
| **Match** | About 90 minutes, six objectives one after another, all factions fight for the same target. |
| **Faction war** | Pick a faction and join an ongoing war across the whole map. |
| **Lone Wolf** | Alone between the front lines, no commander, no supply. |
| **Co-op** | Two players together in the same war, with shared looting and recovery of a fallen friend's gear. |
| **PvP** | Players only, two teams, up to four players. No gear loss in PvP. |

## Content

| | |
|---|---|
| Weapons | 48 |
| Attachments | 110+ |
| Traders | 4 |
| Medical items | 13 |
| Drone types | 5 |
| Factions | 4 |
| Field ranks | 5 (up to lieutenant) |

## System requirements

| | |
|---|---|
| OS | Windows 10 or 11, 64-bit |
| Graphics | GPU with Vulkan or Direct3D 12 support |
| **Recommended (tested)** | AMD Ryzen 7 7800X3D · NVIDIA GeForce RTX 5070 · 32 GB RAM, aiming for 144 fps on Ultra |
| Older PCs | Use the Medium or Low quality preset |

## Download and updates

1. Open the [latest release](https://github.com/Vyrenbusiness-source/attrition-releases/releases/latest).
2. Download all files of that release (`ATTRITION.exe`, `ATTRITION.pck` and the `.dll` files) into one folder.
3. Start `ATTRITION.exe`.

After that the game updates itself. It checks this page at start and in the main menu, downloads only changed files and checks their signature before installing.

## Controls

| Key | Action | Key | Action |
|---|---|---|---|
| W A S D | Move | Tab | Inventory |
| Space / Shift / Ctrl | Jump / sprint / crouch | X | Treat wounds |
| Q / E | Lean | G / H | Grenade / grenade type |
| R | Reload | B | FPV drone |
| F | Interact, loot, vehicles | M | Map |
| 4 – 7 | Quick slots | P (hold) | Scoreboard |

All keys can be rebound in the settings.

<a id="latest-updates"></a>

## Latest updates

Updated automatically from the [releases](https://github.com/Vyrenbusiness-source/attrition-releases/releases). Release notes are written in German.

<!-- updates:en:start -->
| Version | Date | What changed |
|---|---|---|
| [**1.0.175**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.175) | Oct 24, 2026 | M9 mit Drei-Punkt-Visier, AKS-74U mit Seitenschiene (Kobra/1P63/PK-120) und PBS-4 |
| [**1.0.174**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.174) | Oct 24, 2026 | 10 neue Rucksäcke, 5 neue Munitionsarten (Mk 262, 7U1, 7N14, .45 +P, Nr. 4 Buck); Rucksack-Symbole ohne schwebende Gurte |
| [**1.0.173**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.173) | Oct 24, 2026 | 3 neue Waffen (AKS-74U, HK417A2, Beretta M9) mit Magazinen; Leichen/Bodenwaffen verschwinden nach 30–40 s, über 200 m oder außer Sicht sofort (nicht beim Plündern) |
| [**1.0.172**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.172) | Oct 24, 2026 | Pistolen: Ego-Hände wieder wie vor dem Arm-Update |
| [**1.0.171**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.171) | Oct 24, 2026 | Händler: Reiterleiste ohne Überlappung – alle Reiter (inkl. Magazine, Reparatur) passen, Texte nicht mehr abgeschnitten |
| [**1.0.170**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.170) | Oct 23, 2026 | Händler: eigener Reiter „Magazine“ (wie bei Aufsätzen) |
| [**1.0.169**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.169) | Oct 23, 2026 | WICHTIG: Abstürze im Gameplay behoben (Physikabfragen außerhalb des Physiktakts führten im Spiel zur Zugriffsverletzung) |
| [**1.0.168**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.168) | Oct 23, 2026 | Magazine beim Händler einzeln kaufbar (alle Typen mit Marktpreis, landen leer im Spind, passende werden zur Waffe hervorgehoben) und jedes Magazin mit echtem Aussehen: STANAG, G36/SIG durchscheinend … |
<!-- updates:en:end -->

## Credits and licenses

Made with the [Godot Engine](https://godotengine.org) (MIT). Weapon, vehicle and ambient sounds are real recordings: free recordings under CC0, CC BY or public domain, plus purchased sound packs. Every source is credited in the game under *Mitwirkende & Lizenzen*.

## Share it, stream it

ATTRITION is free, and you are welcome to pass it on. You may share the unmodified game files for free, mirror or re-upload them, and make videos, Let's Plays and streams, monetized or not. You may not sell the game or release a modified version as your own game. All rights stay with the developer, and third-party sounds and textures keep their own licenses. Details are in the [LICENSE](LICENSE).

Found a bug or have an idea? Open an [issue](https://github.com/Vyrenbusiness-source/attrition-releases/issues/new/choose); [CONTRIBUTING](CONTRIBUTING.md) explains what helps most.

---

<a id="deutsch"></a>

## Über das Spiel

Du bist ein Soldat in einem Krieg, der auch ohne dich weiterläuft. Vier Fraktionen kämpfen mit hunderten KI-Soldaten, Panzern, Hubschraubern und Drohnen um eine Stadt, und jede Wand lässt sich durchschießen oder sprengen.

Was du mitnimmst, kannst du verlieren. Du fasst kostenlos die Truppenausgabe oder ziehst mit Ausrüstung los, die du gekauft oder erbeutet hast. Fällst du, bleibt sie an deiner Leiche liegen, und wer zuerst da ist, nimmt sie mit. Kommst du zurück, behältst du alles und bekommst Sold für das, was du draußen geleistet hast.

**Frühe Alpha – mit Fehlern ist zu rechnen, Updates kommen häufig.**

## Kurz gesagt

* KI-Trupps, die Deckung nehmen, Nebel werfen, Verwundete bergen und nur wissen, was sie sehen oder hören
* Wundballistik und Sanität nach TCCC: Aderpresse, Druckverband, Chest Seal, Schiene, Morphin, Infusion
* Händler, Spind und Kriegswirtschaft: Ausrüstung kaufen, erbeuten, verlieren
* 48 Waffen, über 110 Aufsätze, Werkbank mit Vorher/Nachher-Werten
* Zerstörbare Voxel-Welt, Wetter, Tag und Nacht
* Match, Koop und PvP

## Herunterladen und Updates

1. Die [neueste Version](https://github.com/Vyrenbusiness-source/attrition-releases/releases/latest) öffnen.
2. Alle Dateien dieser Version (`ATTRITION.exe`, `ATTRITION.pck` und die `.dll`-Dateien) in einen gemeinsamen Ordner laden.
3. `ATTRITION.exe` starten.

Danach aktualisiert sich das Spiel selbst. Alle Tasten lassen sich in den Einstellungen neu belegen.

<a id="neueste-updates"></a>

## Neueste Updates

Wird automatisch aus den [Veröffentlichungen](https://github.com/Vyrenbusiness-source/attrition-releases/releases) erzeugt.

<!-- updates:de:start -->
| Version | Datum | Was ist neu |
|---|---|---|
| [**1.0.175**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.175) | 24.10.2026 | M9 mit Drei-Punkt-Visier, AKS-74U mit Seitenschiene (Kobra/1P63/PK-120) und PBS-4 |
| [**1.0.174**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.174) | 24.10.2026 | 10 neue Rucksäcke, 5 neue Munitionsarten (Mk 262, 7U1, 7N14, .45 +P, Nr. 4 Buck); Rucksack-Symbole ohne schwebende Gurte |
| [**1.0.173**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.173) | 24.10.2026 | 3 neue Waffen (AKS-74U, HK417A2, Beretta M9) mit Magazinen; Leichen/Bodenwaffen verschwinden nach 30–40 s, über 200 m oder außer Sicht sofort (nicht beim Plündern) |
| [**1.0.172**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.172) | 24.10.2026 | Pistolen: Ego-Hände wieder wie vor dem Arm-Update |
| [**1.0.171**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.171) | 24.10.2026 | Händler: Reiterleiste ohne Überlappung – alle Reiter (inkl. Magazine, Reparatur) passen, Texte nicht mehr abgeschnitten |
| [**1.0.170**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.170) | 23.10.2026 | Händler: eigener Reiter „Magazine“ (wie bei Aufsätzen) |
| [**1.0.169**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.169) | 23.10.2026 | WICHTIG: Abstürze im Gameplay behoben (Physikabfragen außerhalb des Physiktakts führten im Spiel zur Zugriffsverletzung) |
| [**1.0.168**](https://github.com/Vyrenbusiness-source/attrition-releases/releases/tag/v1.0.168) | 23.10.2026 | Magazine beim Händler einzeln kaufbar (alle Typen mit Marktpreis, landen leer im Spind, passende werden zur Waffe hervorgehoben) und jedes Magazin mit echtem Aussehen: STANAG, G36/SIG durchscheinend … |
<!-- updates:de:end -->

## Mitwirkende und Lizenzen

Gebaut mit der [Godot Engine](https://godotengine.org) (MIT). Waffen-, Fahrzeug- und Umgebungsklänge sind echte Aufnahmen: freie Aufnahmen unter CC0, CC BY oder gemeinfrei sowie gekaufte Soundpakete. Jede Quelle steht im Spiel unter *Mitwirkende & Lizenzen*.

Das Spiel ist kostenlos und darf unverändert frei weitergegeben werden, auch als Mirror; Videos und Streams sind ausdrücklich erwünscht, auch monetarisiert. Verkauf und veränderte Fassungen als eigenes Spiel sind nicht erlaubt, siehe [LICENSE](LICENSE). Fehler gefunden oder eine Idee? Einfach ein [Issue](https://github.com/Vyrenbusiness-source/attrition-releases/issues/new/choose) eröffnen.

---

<sub>Keywords: free war game, hardcore shooter, tactical FPS, extraction shooter, military shooter, voxel shooter, destructible environment, AI squads, co-op shooter, PvP, Godot 4, Windows · kostenloses Kriegsspiel, Taktik-Shooter, Hardcore-Shooter</sub>
