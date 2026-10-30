# Sources and attribution

## Primary text

This MyST edition adapts the Saylor Academy HTML publication of *Introductory Chemistry*, version 1.0:

- HTML edition: [saylordotorg/text_introductory-chemistry](https://github.com/saylordotorg/text_introductory-chemistry)
- Reading copy: [Introductory Chemistry](https://saylordotorg.github.io/text_introductory-chemistry/index.html)
- Publisher of that HTML edition: Saylor Academy (2012)
- Upstream text: David W. Ball, *Introductory Chemistry*, version 1.0
- HTML maintenance: Andy Schmitz, [2012books.lardbucket.org](http://2012books.lardbucket.org)

The Saylor license page says the HTML text was adapted under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) “without attribution as requested by the work's original creator or licensor.” This edition still names David W. Ball. The source markup identifies the chapters as `ball-chNN`, public catalogs of this version name him as the author, and the Creative Commons license asks downstream users to credit the author. Recording that request does not remove the credit.

Share-alike applies. Adaptations of this edition, including this MyST text, stay under CC BY-NC-SA 3.0. Noncommercial terms apply to the textbook content. The page-build scripts copied from the QuadriviumPress MyST template remain under the MIT license in `LICENSE`.

## What changed in this edition

The wording, examples, exercises, and tables are the Saylor HTML text, converted to MyST Markdown, with documented corrections in the converter. Worked examples and end-of-section problems are `{exercise}` blocks. Answers that were present in the student HTML open in `{solution}` dropdowns. Even-numbered answers were empty in the source (marked instructor-only) and are still absent. Learning objectives, key takeaways, “Chemistry Is Everywhere,” and “Food and Drink App” notes use MyST callouts. Twenty-two cited figures have no figure block or image in that HTML edition. This edition supplies openly licensed replacements for those omissions, with new descriptive captions and resolved cross-references. The original 38-Calorie exercise is phrased as a hypothetical because the replacement FDA label shows 230 Calories.

## Figures and external resources

Legacy figures are the JPEG and PNG files shipped in `saylordotorg/text_introductory-chemistry`, copied here under `images/figures/` without redrawing, apart from the converter's documented electronegativity correction. They follow the same CC BY-NC-SA 3.0 terms as the text. Their captions are the source captions. No embedded simulations or third-party interactive media are added in this conversion.

Replacement assets in `images/restored/` retain their individual CC BY, CC BY-SA, CC0, or public-domain terms, listed below and in their figure captions. They are separately licensed works included in this collection; the textbook's noncommercial license does not replace or restrict their licenses. Each source page records the original work and its license. All files were retrieved on 2026-10-30, resized or re-encoded for web display without content changes; the nucleotide diagram is Wikimedia's PNG rendering of an SVG. Share-alike image adaptations retain the indicated image license.

The Creative Commons badge on the license page is the badge from that repository (`shared/images/by-nc-sa.png`).

## Figure audit and replacement credits (2026-10-30)

The audit decoded and visually reviewed all 419 legacy image files and compared all numbered figure citations with the 76 numbered figure blocks in the Saylor section HTML. All existing local assets were present and readable. The following 22 cited figures had no source figure block or image; all now have local replacements. This also restores the methane and nucleotide diagrams alongside the missing photographs and measurement displays. The 24 distinct replacement files are about 5.6 MB in total.

`images/restored/manifest.json` records the figure number, source target ID, chapter, caption, alt text, creator, source URL, license URL, changes, retrieval date, and SHA-256 of each delivered file. `npm run convert` reapplies these additions; `npm run verify` checks the files, hashes, attribution records, and figure placements.

| Figure | Replacement file | Work and creator | License |
| --- | --- | --- | --- |
| 1.1 — The Phases of Matter | `fig-1-1a.jpg` | [Ice cubes on water — Cleiton Andrade Andrade from Alfenas, Brasil](https://commons.wikimedia.org/wiki/File:Ice_cubes_on_water.jpg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| 1.1 — The Phases of Matter | `fig-1-1b.jpg` | [Glass of water — deavmi](https://commons.wikimedia.org/wiki/File:Glass_of_water.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 1.1 — The Phases of Matter | `fig-1-1c.jpg` | [Steaming Kettle - Boston, MA — Daderot](https://commons.wikimedia.org/wiki/File:Steaming_Kettle_-_Boston,_MA.jpg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| 1.2 — Chemical Properties | `fig-1-2.jpg` | [Burning matchstick 2010 — Maja Dumat from Deutschland (Germany)](https://commons.wikimedia.org/wiki/File:Burning_matchstick_2010.jpg) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| 1.3 — Physical Changes | `fig-1-3.jpg` | [Eiswürfel auf Stein — ThoBel-0043](https://commons.wikimedia.org/wiki/File:Eisw%C3%BCrfel_auf_Stein.jpg) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0) |
| 1.4 — Types of Mixtures | `fig-1-4a.jpg` | [Studentenfutter 01 — Thogru](https://commons.wikimedia.org/wiki/File:Studentenfutter_01.JPG) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| 1.4 — Types of Mixtures | `fig-1-1b.jpg` | [Glass of water — deavmi](https://commons.wikimedia.org/wiki/File:Glass_of_water.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 1.5 — Semimetals | `fig-1-5.jpg` | [SiliconCroda — Enricoros at English Wikipedia](https://commons.wikimedia.org/wiki/File:SiliconCroda.jpg) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 1.8 — Defining a Law | `fig-1-8.jpg` | [Speed Limit 20 sign on Commercial Drive, Southbridge, Massachusetts — Peter Cooper Jr.](https://commons.wikimedia.org/wiki/File:Speed_Limit_20_sign_on_Commercial_Drive,_Southbridge,_Massachusetts.jpg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| 2.1 — Using Scientific Notation | `fig-2-1.jpg` | [Scientific notation in calculator display 16 — Thirunavukkarasye-Raveendran](https://commons.wikimedia.org/wiki/File:Scientific_notation_in_calculator_display_16.JPG) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0) |
| 2.2 — Scientific Notation on a Calculator | `fig-2-2.jpg` | [Casio fx-991EX Scientific Calculator — David Wheatley](https://commons.wikimedia.org/wiki/File:Casio_fx-991EX_Scientific_Calculator.jpg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| 2.7 — Significant Figures | `fig-2-7.jpg` | [Digital odometer 1987 Oldsmobile Toronado — Jacek Rużyczka](https://commons.wikimedia.org/wiki/File:Digital_odometer_1987_Oldsmobile_Toronado.JPG) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 3.5 — NaCl = Table Salt | `fig-3-5.jpg` | [Table Salt (NaCl) Crystal — JJ Harrison ( https://www.jjharrison.com.au/ )](https://commons.wikimedia.org/wiki/File:Table_Salt_(NaCl)_Crystal.jpg) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| 7.1 — Calories on Food Labels | `fig-7-1.png` | [FDA Nutrition Facts Label 2016 — U.S. Food and Drug Administration](https://commons.wikimedia.org/wiki/File:FDA_Nutrition_Facts_Label_2016.png) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 10.3 — Liquids and Gravity | `fig-10-3.jpg` | [Water sphere aboard the International Space Station — NASA Johnson Space Center](https://commons.wikimedia.org/wiki/File:Iss072e069743_(Oct_19,_2024)_---_The_fingers_of_NASA_astronaut_and_Expedition_72_Flight_Engineer_Don_Pettit_are_refracted_in_this_sphere_of_water_in_the_microgravity_environment_of_the_International_Space_Station.jpg) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 10.10 — Effects of Surface Tension | `fig-10-10.jpg` | [Water droplets leaf — Dhivya dhivi DJ](https://commons.wikimedia.org/wiki/File:Water_droplets_leaf.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 10.11 — Walking on Water | `fig-10-11.jpg` | [Water strider on Natisone river — Vid Pogacnik](https://commons.wikimedia.org/wiki/File:Water_strider_on_Natisone_river.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 11.1 — Concentration in Commercial Applications | `fig-11-1.jpg` | [Hydrogen Peroxide Bottle — ThatOneEli](https://commons.wikimedia.org/wiki/File:Hydrogen_Peroxide_Bottle.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 11.2 — Salt and Safety | `fig-11-2.jpg` | [RoadSaltTrucks — James LeWorm](https://commons.wikimedia.org/wiki/File:RoadSaltTrucks.jpg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| 14.3 — Button Batteries | `fig-14-3.jpg` | [Coin-cells — Gerhard H Wrodnigg](https://commons.wikimedia.org/wiki/File:Coin-cells.jpg) | [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5) |
| 14.4 — Lead Storage Batteries | `fig-14-4.jpg` | [Cutaway view of a 1953 automotive lead-acid battery — National Institute of Standards and Technology Digital Collections, Gaithersburg, MD 20899](https://commons.wikimedia.org/wiki/File:Cutaway_view_of_a_1953_automotive_lead-acid_battery.jpg) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 15.2 — Detecting Radioactivity | `fig-15-2.jpg` | [Geiger counter 2 — TimVickers](https://commons.wikimedia.org/wiki/File:Geiger_counter_2.jpg) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 16.1 — Three-Dimensional Representation of Methane | `fig-16-1.png` | [Methane-3D-balls — Ben Mills (Benjah-bmm27)](https://commons.wikimedia.org/wiki/File:Methane-3D-balls.png) | [Public domain](https://creativecommons.org/publicdomain/mark/1.0/) |
| 16.2 — Combustion | `fig-16-2.jpg` | [Gas stove burner flame — Lisafern](https://commons.wikimedia.org/wiki/File:Gas_stove_burner_flame.jpg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| 16.6 — Nucleotides | `fig-16-6.png` | [Nucleotide nucleoside general — Yikrazuul](https://commons.wikimedia.org/wiki/File:Nucleotide_nucleoside_general.svg) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
