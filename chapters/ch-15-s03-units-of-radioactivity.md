---
title: "15.3 Units of Radioactivity"
---

(sec:ch15:s03)=

# 15.3 Units of Radioactivity

```{note} Learning Objective

1. Express amounts of radioactivity in a variety of units.
```

In {ref}`Chapter 15 "Nuclear Chemistry" <ch:ch15>`, {ref}`Section 15.2 "Half-Life" <sec:ch15:s02>`, we used mass to indicate the amount of radioactive substance present. Its *activity* is the number of nuclear decays per unit time. Radiation *dose* describes energy deposited in matter and, with appropriate weighting, its effects on tissue. Activity and dose measure different quantities.

Perhaps the direct way of reporting radioactivity is the number of radioactive decays per second. One decay per second is called one **becquerel (Bq)** (*A unit of radioactivity equal to 1 decay per second.*). Even in a small mass of radioactive material, however, there are thousands upon thousands of decays or disintegrations per second. The unit **curie (Ci)** (*A unit of radioactivity equal to $3.7\times{}{10}^{10}$ decays/s.*), now defined as 3.7 × 10<sup>10</sup> decays/s, was originally defined as the number of decays per second in 1 g of radium. Many radioactive samples have activities that are on the order of microcuries (µCi) or more. Both the becquerel and the curie can be used in place of grams to describe quantities of radioactive material. As an example, the amount of americium in an average smoke detector has an activity of 0.9 µCi. (The curie is named after Polish scientist Marie Curie, who performed some of the initial investigations into radioactive phenomena in the early 1900s; the becquerel is named after Henri Becquerel, who discovered radioactivity in 1896.)

```{exercise}
:label: ex:ball-ch15-s03-n02

**Example 5**

A sample of radium has an activity of 16.0 mCi (millicuries). If the half-life of radium is 1,600 y, how long before the sample’s activity is 1.0 mCi?
```

```{solution} ex:ball-ch15-s03-n02
:label: sol:ball-ch15-s03-n02
:class: dropdown

The following table shows the activity of the radium sample over multiple half-lives:

| Time in Years | Activity |
| --- | --- |
| 0 | 16.0 mCi |
| 1,600 | 8.0 mCi |
| 3,200 | 4.0 mCi |
| 4,800 | 2.0 mCi |
| 6,400 | 1.0 mCi |

Over a period of 4 half-lives, the activity of the radium will be halved four times, at which point its activity will be 1.0 mCi. Thus it takes 4 half-lives, or 4 × 1,600 y = 6,400 y, for the activity to decrease to 1.0 mCi.
```

```{exercise}
:label: ex:ball-ch15-s03-n02-ty2

**Test Yourself**

A sample of radon has an activity of 60,000 Bq. If the half-life of radon is 15 h, how long before the sample’s activity is 3,750 Bq?
```

```{solution} ex:ball-ch15-s03-n02-ty2
:label: sol:ball-ch15-s03-n02-ty2
:class: dropdown

60 h
```

```{exercise}
:label: ex:ball-ch15-s03-n03

**Example 6**

A sample of radium has an activity of 16.0 mCi. If the half-life of radium is 1,600 y, how long before the sample’s activity is 5.6 mCi?
```

```{solution} ex:ball-ch15-s03-n03
:label: sol:ball-ch15-s03-n03
:class: dropdown

In this case we do not have an exact number of half-lives, so we need to use the more complicated equation (in {ref}`Chapter 15 "Nuclear Chemistry" <ch:ch15>`, {ref}`Section 15.2 "Half-Life" <sec:ch15:s02>`) and solve for time. If the initial amount is represented by 16.0 mCi and the final amount is 5.6 mCi, we have

$\text{5.6 mCi = (16.0 mCi)}e^{-0.693t/(1{,}600\text{ y})}$

To solve, we divide both sides of the equation by 16.0 mCi to cancel the millicurie units:

$$
\frac{5.6}{16.0}={e}^{-0.692t/(1{,}600\text{ y)}}
$$

By taking the natural logarithm of both sides; the natural logarithm cancels the exponential function. The natural logarithm of 5.6/16.0 is −1.050. So

$-\text{1.050 = }-\text{0.692}t\text{/(1,600 y)}$

The negative sign cancels, and we solve for *t*. Thus

$\text{t = 2,420 y}$

It makes sense that the time is greater than one half-life (1,600 y) because we have less than one-half of the original activity left.
```

```{exercise}
:label: ex:ball-ch15-s03-n03-ty2

**Test Yourself**

A sample of radon has an activity of 60,000 Bq. If the half-life of radon is 15 h, how long before the sample’s activity is 10,000 Bq?
```

```{solution} ex:ball-ch15-s03-n03-ty2
:label: sol:ball-ch15-s03-n03-ty2
:class: dropdown

38.8 h
```

Radiation can transfer energy to tissue through moving particles and through the absorption of electromagnetic radiation such as gamma rays. The energy deposited per unit mass is called *absorbed dose*. Its SI unit is the **gray (Gy)** (*An absorbed dose of 1 joule per kilogram.*). The older unit **rad** (*An absorbed dose of 0.01 joule per kilogram.*) is still encountered, especially in US sources:

$$
1\ \mathrm{Gy} = 1\ \mathrm{J/kg} = 100\ \mathrm{rad}
$$

The gray is the SI unit used in scientific reporting. Absorbing 1 rad in a 70 kg body deposits only 0.7 J, but ionizing radiation can damage molecules and cells even when its overall heating effect is very small.

Radiation types differ in their biological effects. For a tissue exposed to one type of radiation, the *equivalent dose* is its mean absorbed dose multiplied by a radiation weighting factor:

$$
\text{equivalent dose (Sv)} = \text{absorbed dose (Gy)} \times \text{radiation weighting factor}
$$

The **sievert (Sv)** (*The SI unit of equivalent dose and effective dose.*) is related to the older **rem** (*A unit of equivalent dose or effective dose equal to 0.01 sievert.*) by 1 Sv = 100 rem. The weighting factor is 1 for photons and beta particles and 20 for alpha particles. *Effective dose* additionally weights the equivalent doses to different organs and tissues to account for differences in their sensitivity. These quantities are explained in the [FDA’s radiation units guide](https://www.fda.gov/radiation-emitting-products/medical-x-ray-imaging/radiation-quantities-and-units) and [OSHA’s radiation background reference](https://www.osha.gov/ionizing-radiation/background).

Annual effective dose depends on location, housing, medical procedures, and other circumstances. {ref}`Table 15.3 "Average Annual Radiation Exposure (Approximate)" <tbl:ch15:s03:t01>` gives a dated US population benchmark summarized by the Nuclear Regulatory Commission. It represents 2006 exposure data reported by NCRP in 2009. Roughly half came from natural background and half from human activities, mainly medicine. Natural background includes radon, cosmic radiation, terrestrial radiation, and radioactive isotopes in the body, including potassium-40 and carbon-14.

```{table} Average Annual Radiation Exposure (Approximate)
:label: tbl:ch15:s03:t01

| Source (US population, 2006 benchmark) | Effective dose (mSv/year) | Effective dose (mrem/year) |
| --- | --- | --- |
| natural background | 3.1 | 310 |
| human activities, mainly medical procedures | 3.1 | 310 |
| **Total** | **6.2** | **620** |

Source: [NRC, Doses in Our Daily Lives](https://www.nrc.gov/facilities-safety/radiation-protection/radiation-all-around-us/doses-in-our-daily-lives), summarizing NCRP Report No. 160 (2009). Values are rounded population averages, not an individual’s dose or a universal annual value.
```

Exposure patterns change. An [updated study using 2016 US medical exposure data](https://pubs.rsna.org/doi/10.1148/radiol.2020192256) estimated the medical contribution at about 2.3 mSv per person per year, compared with about 2.9 mSv in 2006 using comparable methods. This medical-only estimate does not replace the total in Table 15.3. Also, “natural” does not mean “unavoidable”: testing homes for radon and reducing elevated levels can lower exposure. See the [EPA’s radon guide](https://www.epa.gov/radon).

Health effects depend on absorbed dose, radiation type, the tissues exposed, and how quickly the dose is delivered. {ref}`Table 15.4 "Effects of Short-Term Exposure to Radioactivity and Radiation" <tbl:ch15:s03:t02>` summarizes approximate acute effects of penetrating radiation delivered to most of the body in a short time. These dose ranges overlap and do not predict an individual outcome. Effective dose in sieverts is used for radiation protection comparisons; absorbed dose in grays is used here to describe acute injury.

```{table} Effects of Short-Term Exposure to Radioactivity and Radiation
:label: tbl:ch15:s03:t02

| Absorbed dose (Gy) | Possible acute effects |
| --- | --- |
| about 0.3 and above | mild symptoms of radiation sickness may occur |
| about 0.7–10 | bone marrow injury; risk of infection and bleeding increases as dose rises |
| about 6 and above | gastrointestinal symptoms may occur |
| above about 10 | severe gastrointestinal syndrome; survival is extremely unlikely |

Source: [CDC, Acute Radiation Syndrome: Information for Clinicians](https://www.cdc.gov/radiation-emergencies/hcp/clinical-guidance/ars.html). Outcomes also depend on treatment, dose distribution, and dose rate. This table describes acute injury; it does not establish a threshold below which long-term cancer risk is absent.
```

A personal dosimeter measures radiation received by its wearer. Film badges provide a historical example: radiation darkens the film, and comparison with calibrated exposures allows dose to be estimated. Thermoluminescent, optically stimulated luminescent, and electronic dosimeters are also used. A dose estimate requires calibration appropriate to the radiation and measurement conditions.

Another means of detecting radioactivity is an electrical device called a **Geiger counter** (*An electrical device that detects radioactivity.*) ({ref}`Figure 15.2 "Detecting Radioactivity" <fig:ch15:s03:f01>`). It contains a gas-filled chamber with a thin membrane on one end that allows radiation emitted from radioactive nuclei to enter the chamber and knock electrons off atoms of gas (usually argon). The presence of electrons and positively charged ions causes a small current, which is detected by the Geiger counter and converted to a signal on a meter or, commonly, an audio circuit to produce an audible “click.”

```{figure} ../images/restored/fig-15-2.jpg
:label: fig:ch15:s03:f01
:enumerator: 15.2
:alt: A portable Geiger counter with a meter and a connected detector probe.
:align: center
:width: 70%

**Detecting Radioactivity.** A Geiger counter and its connected probe detect ionizing radiation. Radiation entering the detector produces electrical pulses that can be displayed or heard as clicks.

Credits: [Geiger counter 2 — TimVickers](https://commons.wikimedia.org/wiki/File:Geiger_counter_2.jpg), [Public domain](https://creativecommons.org/publicdomain/mark/1.0/). Images resized for the web.
```

```{important} Key Takeaway

- Activity is measured in becquerels (or curies), absorbed dose in grays (or rads), and equivalent or effective dose in sieverts (or rems).
```

## Exercises

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa01

**Exercise 1.**

Define *rad*.
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa01
:label: sol:ball-ch15-s03-qs01-qd01-qa01
:class: dropdown

a unit of absorbed dose equal to 0.01 J of energy per kilogram of matter
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa02

**Exercise 2.**

Define *rem*.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa03

**Exercise 3.**

How does a becquerel differ from a curie?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa03
:label: sol:ball-ch15-s03-qs01-qd01-qa03
:class: dropdown

A becquerel is 1 decay/s, whereas a curie is 3.7 × 10<sup>10</sup> decays/s.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa04

**Exercise 4.**

Define *curie*.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa05

**Exercise 5.**

A sample of radon gas has an activity of 140.0 mCi. If the half-life of radon is 3.823 d, how long before the activity of the sample is 8.75 mCi?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa05
:label: sol:ball-ch15-s03-qs01-qd01-qa05
:class: dropdown

15.29 d
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa06

**Exercise 6.**

A sample of curium has an activity of 1,600 Bq. If the half-life of curium is 24.0 s, how long before its activity is 25.0 Bq?
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa07

**Exercise 7.**

If a radioactive sample has an activity of 65 µCi, how many disintegrations per second are occurring?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa07
:label: sol:ball-ch15-s03-qs01-qd01-qa07
:class: dropdown

2.41 × 10<sup>6</sup> disintegrations per second
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa08

**Exercise 8.**

If a radioactive sample has an activity of 7.55 × 10<sup>5</sup> Bq, how many disintegrations per second are occurring?
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa09

**Exercise 9.**

A sample of fluorine-20 has an activity of 2.44 mCi. If its half-life is 11.0 s, what is its activity after 50.0 s?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa09
:label: sol:ball-ch15-s03-qs01-qd01-qa09
:class: dropdown

0.104 mCi
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa10

**Exercise 10.**

Strontium-90 has a half-life of 28.1 y. If 66.7 Bq of pure strontium-90 were allowed to decay for 15.0 y, what would the activity of the remaining strontium-90 be?
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa11

**Exercise 11.**

How long does it take 100.0 mCi of fluorine-20 to decay to 10.0 mCi if its half-life is 11.0 s?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa11
:label: sol:ball-ch15-s03-qs01-qd01-qa11
:class: dropdown

36.5 s
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa12

**Exercise 12.**

Technetium-99 is used in medicine as a source of radiation. A typical dose is 25 mCi. How long does it take for the activity to reduce to 0.100 mCi? The half-life of <sup>99</sup>Tc is 210,000 y.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa13

**Exercise 13.**

How is equivalent dose in rems calculated from absorbed dose in rads for one type of radiation?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa13
:label: sol:ball-ch15-s03-qs01-qd01-qa13
:class: dropdown

Multiply the absorbed dose in rads by the radiation weighting factor. For example, 1 rad of beta radiation corresponds to 1 rem, while 1 rad of alpha radiation corresponds to 20 rem of equivalent dose to the exposed tissue.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa14

**Exercise 14.**

Which contributes more to the rems of exposure—alpha or beta particles? Why?
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa15

**Exercise 15.**

Use {ref}`Table 15.3 "Average Annual Radiation Exposure (Approximate)" <tbl:ch15:s03:t01>` to calculate the percentage of the benchmark dose that came from natural background. Explain why this percentage does not describe an individual’s unavoidable exposure.
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa15
:label: sol:ball-ch15-s03-qs01-qd01-qa15
:class: dropdown

Natural background contributed approximately $310/620 \times 100\% = 50\%$ of the benchmark dose. The values are US population averages for a specified reference year. Individual exposures vary, and some natural exposure, especially from indoor radon, can be reduced.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa16

**Exercise 16.**

Name two isotopes that contribute to the radioactivity in our bodies.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa17

**Exercise 17.**

Explain how a film badge works to detect radiation.
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa17
:label: sol:ball-ch15-s03-qs01-qd01-qa17
:class: dropdown

Film is exposed by the radiation. The more radiation film is subjected to, the more exposed it becomes.
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa18

**Exercise 18.**

Explain how a Geiger counter works to detect radiation.
```
