---
title: "15.3 Units of Radioactivity"
---

(sec:ch15:s03)=

# 15.3 Units of Radioactivity

```{note} Learning Objective

1. Express amounts of radioactivity in a variety of units.
```

In {ref}`Chapter 15 "Nuclear Chemistry" <ch:ch15>`, {ref}`Section 15.2 "Half-Life" <sec:ch15:s02>`, we used mass to indicate the amount of radioactive substance present. This is only one of several units used to express amounts of radiation. Some units describe the number of radioactive events occurring per unit time, while others express the amount of a person’s exposure to radiation.

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

Other measures of radioactivity are based on the effects it has on living tissue. Radioactivity can transfer energy to tissues in two ways: through the kinetic energy of the particles hitting the tissue and through the electromagnetic energy of the gamma rays being absorbed by the tissue. Either way, the transferred energy—like the thermal energy from boiling water—can damage the tissue.

The **rad** (*A unit of radioactive exposure equal to 0.01 J/kg of tissue.*) (an acronym for radiation absorbed dose) is a unit equivalent to 1 kg of tissue absorbing 0.01 J:

$$
\text{1 rad = 0.01 J/kg}
$$

Another unit of radiation absorption is the gray (Gy):

$$
\text{1 Gy = 100 rad}
$$

The rad is more common. To get an idea of the amount of energy this represents, consider that the absorption of 1 rad by 70,000 g of water (approximately the same mass as a 150 lb person) would increase the temperature of the water by only about 2 × 10<sup>−6</sup>°C. This may not seem like a lot, but it is enough energy to break about 1 × 10<sup>18</sup> molecular C–C bonds in a person’s body. That amount of damage would not be desirable.

Predicting the effects of radiation is complicated by the fact that different types of emissions affect various tissues differently. To quantify these effects, the unit **rem** (*A unit of radioactive exposure that includes a factor to account for the type of radioactivity.*) (an acronym for röntgen equivalent man) is defined as

$$
\text{rem = rad }\times{}\text{ factor}
$$

where factor is a number greater than or equal to 1 that takes into account the type of radioactive emission and sometimes the type of tissue being exposed. For beta particles, the factor equals 1. For alpha particles striking most tissues, the factor is 10, but for eye tissue the factor is 30. Most radioactive emissions that people are exposed to are on the order of a few dozen millirems (mrem) or less; a medical X-ray is about 20 mrem. A sievert (Sv) is a related unit and is defined as 100 rem.

What is a person’s annual exposure to radioactivity and radiation? {ref}`Table 15.3 "Average Annual Radiation Exposure (Approximate)" <tbl:ch15:s03:t01>` lists the sources and annual amounts of radiation exposure. It may surprise you to learn that fully 82% of the radioactivity and radiation exposure we receive is from natural sources—sources we cannot avoid. Fully 10% of the exposure comes from our own bodies—largely from carbon-14 and potassium-40.

```{table} Average Annual Radiation Exposure (Approximate)
:label: tbl:ch15:s03:t01

| Source | Amount (mrem) |
| --- | --- |
| radon gas | 200 |
| medical sources | 53 |
| radioactive atoms in the body naturally | 39 |
| terrestrial sources | 28 |
| cosmic sources | 28\* |
| consumer products | 10 |
| nuclear energy | 0.05 |
| **Total** | 358 |

\*Flying from New York City to San Francisco adds 5 mrem to your overall radiation exposure because the plane flies above much of the atmosphere, which protects us from cosmic radiation.
```

The actual effects of radioactivity and radiation exposure on a person’s health depend on the type of radioactivity, the length of exposure, and the tissues exposed. {ref}`Table 15.4 "Effects of Short-Term Exposure to Radioactivity and Radiation" <tbl:ch15:s03:t02>` lists the potential threats to health at various amounts of exposure over short periods of time (hours or days).

```{table} Effects of Short-Term Exposure to Radioactivity and Radiation
:label: tbl:ch15:s03:t02

| Exposure (rem) | Effect |
| --- | --- |
| 1 (over a full year) | no detectable effect |
| ∼20 | increased risk of some cancers |
| ∼100 | damage to bone marrow and other tissues; possible internal bleeding; decrease in white blood cell count |
| 200–300 | visible “burns” in skin, nausea, vomiting, fatigue |
| >300 | loss of white blood cells; hair loss |
| ∼600 | death |
```

One of the simplest ways of detecting radioactivity is by using a piece of photographic film embedded in a badge or a pen. On a regular basis, the film is developed and checked for exposure. Comparing the exposure level of the film with a set of standard exposures indicates the amount of radiation a person was exposed to.

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

- Radioactivity can be expressed in a variety of units, including rems, rads, and curies.
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

a unit of radioactive exposure equal to 0.01 J of energy per kilogram of tissue
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

Describe how a radiation exposure in rems is determined.
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa13
:label: sol:ball-ch15-s03-qs01-qd01-qa13
:class: dropdown

by using a film badge, which is exposed by the radiation, or a Geiger counter
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa14

**Exercise 14.**

Which contributes more to the rems of exposure—alpha or beta particles? Why?
```

```{exercise}
:label: ex:ball-ch15-s03-qs01-qd01-qa15

**Exercise 15.**

Use {ref}`Table 15.4 "Effects of Short-Term Exposure to Radioactivity and Radiation" <tbl:ch15:s03:t02>` to determine which sources of radiation exposure are inescapable and which can be avoided. What percentage of radiation is unavoidable?
```

```{solution} ex:ball-ch15-s03-qs01-qd01-qa15
:label: sol:ball-ch15-s03-qs01-qd01-qa15
:class: dropdown

Radioactive atoms in the body, most terrestrial sources, cosmic sources, and nuclear energy sources are likely unavoidable, which is about 27% of the total exposure. If exposure to radon gas is added, the total unavoidable exposure increases to 82%.
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
