---
title: "2.4 Converting Units"
---

(sec:ch02:s04)=

# 2.4 Converting Units

```{note} Learning Objective

1. Convert from one unit to another unit of the same type.
```

In {ref}`Section 2.2 "Expressing Units" <sec:ch02:s02>`, we showed some examples of how to replace initial units with other units of the same type to get a numerical value that is easier to comprehend. In this section, we will formalize the process.

Consider a simple example: how many feet are there in 4 yards? Most people will almost automatically answer that there are 12 feet in 4 yards. How did you make this determination? Well, if there are 3 feet in 1 yard and there are 4 yards, then there are 4 × 3 = 12 feet in 4 yards.

This is correct, of course, but it is informal. Let us formalize it in a way that can be applied more generally. We know that 1 yard (yd) equals 3 feet (ft):

$$
\text{1 yd = 3 ft}
$$

In math, this expression is called an *equality*. The rules of algebra say that you can change (i.e., multiply or divide or add or subtract) the equality (as long as you don’t divide by zero) and the new expression will still be an equality. For example, if we divide both sides by 2, we get

$$
\frac{1}{2}\text{ yd}=\frac{3}{2}\text{ ft}
$$

We see that one-half of a yard equals 3/2, or one and a half, feet—something we also know to be true, so the above equation is still an equality. Going back to the original equality, suppose we divide both sides of the equation by 1 yard (number *and* unit):

$$
\frac{\text{1 yd}}{\text{1 yd}}=\frac{\text{3 ft}}{\text{1 yd}}
$$

The expression is still an equality, by the rules of algebra. The left fraction equals 1. It has the same quantity in the numerator and the denominator, so it must equal 1. The quantities in the numerator and denominator cancel, both the number *and* the unit:

$$
\frac{\text{1}\text{ yd}}{\text{1}\text{ yd}}=\frac{\text{3 ft}}{\text{1 yd}}
$$

When everything cancels in a fraction, the fraction reduces to 1:

$$
1=\frac{\text{3 ft}}{\text{1 yd}}
$$

We have an expression, $\frac{\text{3 ft}}{\text{1 yd}}$, that equals 1. This is a strange way to write 1, but it makes sense: 3 ft equal 1 yd, so the quantities in the numerator and denominator are the same quantity, just expressed with different units. The expression $\frac{\text{3 ft}}{\text{1 yd}}$ is called a **conversion factor** (*A fraction that can be used to convert a quantity from one unit to another.*), and it is used to formally change the unit of a quantity into another unit. (The process of converting units in such a formal fashion is sometimes called *dimensional analysis* or the *factor label method*.)

To see how this happens, let us start with the original quantity:

$$
\text{4 yd}
$$

Now let us multiply this quantity by 1. When you multiply anything by 1, you don’t change the value of the quantity. Rather than multiplying by just 1, let us write 1 as $\frac{\text{3 ft}}{\text{1 yd}}$:

$$
\text{4 yd}\,\times{}\,\frac{\text{3 ft}}{\text{1 yd}}
$$

The 4 yd term can be thought of as $\frac{\text{4 yd}}{1}$; that is, it can be thought of as a fraction with 1 in the denominator. We are essentially multiplying fractions. If the same thing appears in the numerator and denominator of a fraction, they cancel. In this case, what cancels is the unit *yard*:

$$
\text{4}\text{ yd}\,\times{}\,\frac{\text{3 ft}}{\text{1}\text{ yd}}
$$

That is all that we can cancel. Now, multiply and divide all the numbers to get the final answer:

$$
\frac{4\,\times{}\,3\text{ ft}}{1}=\frac{\text{12 ft}}{1}=12\text{ ft}
$$

Again, we get an answer of 12 ft, just as we did originally. But in this case, we used a more formal procedure that is applicable to a variety of problems.

How many millimeters are in 14.66 m? To answer this, we need to construct a conversion factor between millimeters and meters and apply it correctly to the original quantity. We start with the definition of a millimeter, which is

$$
\text{1 mm = 1/1,000 m}
$$

The 1/1,000 is what the prefix *milli-* means. Most people are more comfortable working without fractions, so we will rewrite this equation by bringing the 1,000 into the numerator of the other side of the equation:

$$
\text{1,000 mm = 1 m}
$$

Now we construct a conversion factor by dividing one quantity into both sides. But now a question arises: which quantity do we divide by? It turns out that we have two choices, and the two choices will give us different conversion factors, both of which equal 1:

$$
\frac{1{,}000\text{ mm}}{1{,}000\text{ mm}}=\frac{1\text{ m}}{1{,}000\text{ mm}}\,\text{or}\,\frac{1{,}000\text{ mm}}{1\text{ m}}=\frac{1\text{ m}}{1\text{ m}}
$$

$$
1=\frac{1\text{ m}}{1{,}000\text{ mm}}\,\text{or}\,\frac{1{,}000\text{ mm}}{1\text{ m}}=1
$$

Which conversion factor do we use? The answer is based on *what unit you want to get rid of in your initial quantity*. The original unit of our quantity is meters, which we want to convert to millimeters. Because the original unit is assumed to be in the numerator, to get rid of it, we want the meter unit in the *denominator*; then they will cancel. Therefore, we will use the second conversion factor. Canceling units and performing the mathematics, we get

$$
\text{14}.\text{66}\text{ m}\,\times{}\,\frac{1{,}000\text{ mm}}{1\text{ m}}=14{,}660\text{ mm}
$$

Note how m cancels, leaving mm, which is the unit of interest.

The ability to construct and apply proper conversion factors is a very powerful mathematical technique in chemistry. You need to master this technique if you are going to be successful in this and future courses.

```{exercise}
:label: ex:ball-ch02-s04-n02

**Example 7**

1. Convert 35.9 kL to liters.
2. Convert 555 nm to meters.
```

```{solution} ex:ball-ch02-s04-n02
:label: sol:ball-ch02-s04-n02
:class: dropdown

1. We will use the fact that 1 kL = 1,000 L. Of the two conversion factors that can be defined, the one that will work is $\frac{1{,}000\text{ L}}{1\text{ kL}}$. Applying this conversion factor, we get

   $$
   35.9\text{ kL}\,\times{}\,\frac{1{,}000\text{ L}}{1\text{ kL}}=35{,}900\text{ L}
   $$
2. We will use the fact that 1 nm = 1/1,000,000,000 m, which we will rewrite as 1,000,000,000 nm = 1 m, or 10<sup>9</sup> nm = 1 m. Of the two possible conversion factors, the appropriate one has the nm unit in the denominator: $\frac{1\text{ m}}{{10}^{9}\text{ nm}}$. Applying this conversion factor, we get

   $$
   \text{555}\text{ nm}\,\times{}\,\frac{1\text{ m}}{{10}^{9}\text{ nm}}=0.000000\text{555 m}=\text{5}.\text{55}\,\times{}\,\text{1}{0}^{-\text{7}}\text{ m}
   $$

   In the final step, we expressed the answer in scientific notation.
```

```{exercise}
:label: ex:ball-ch02-s04-n02-ty2

**Test Yourself**

1. Convert 67.08 μL to liters.
2. Convert 56.8 m to kilometers.
```

```{solution} ex:ball-ch02-s04-n02-ty2
:label: sol:ball-ch02-s04-n02-ty2
:class: dropdown

1. 6.708 × 10<sup>−5</sup> L
2. 5.68 × 10<sup>−2</sup> km
```

What if we have a derived unit that is the product of more than one unit, such as m<sup>2</sup>? Suppose we want to convert square meters to square centimeters? The key is to remember that m<sup>2</sup> means m × m, which means we have *two* meter units in our derived unit. That means we have to include *two* conversion factors, one for each unit. For example, to convert 17.6 m<sup>2</sup> to square centimeters, we perform the conversion as follows:

$$
17.6{\text{ m}}^{2}=17.6(\text{ m}\,\times{}\,\text{ m})\,\times{}\,\frac{100\text{ cm}}{1\,\text{ m}}\,\times{}\,\frac{100\text{ cm}}{1\,\text{ m}}=176{,}000\text{ cm}\,\times{}\,\text{cm}=1.76\,\times{}\,{10}^{5}{\text{ cm}}^{2}
$$

```{exercise}
:label: ex:ball-ch02-s04-n03

**Example 8**

How many cubic centimeters are in 0.883 m<sup>3</sup>?
```

```{solution} ex:ball-ch02-s04-n03
:label: sol:ball-ch02-s04-n03
:class: dropdown

With an exponent of 3, we have three length units, so by extension we need to use three conversion factors between meters and centimeters. Thus, we have

$$
0.883{\text{ m}}^{3}\,\times{}\,\frac{\text{100 cm}}{1\text{ m}}\,\times{}\,\frac{\text{100 cm}}{1\text{ m}}\,\times{}\,\frac{\text{100 cm}}{\text{1}\text{ m}}=883{,}000{\text{ cm}}^{3}=8.83\,\times{}\,{10}^{5}{\text{ cm}}^{3}
$$

You should demonstrate to yourself that the three meter units do indeed cancel.
```

```{exercise}
:label: ex:ball-ch02-s04-n03-ty2

**Test Yourself**

How many cubic millimeters are present in 0.0923 m<sup>3</sup>?
```

```{solution} ex:ball-ch02-s04-n03-ty2
:label: sol:ball-ch02-s04-n03-ty2
:class: dropdown

9.23 × 10<sup>7</sup> mm<sup>3</sup>
```

Suppose the unit you want to convert is in the denominator of a derived unit; what then? Then, in the conversion factor, the unit you want to remove must be in the *numerator*. This will cancel with the original unit in the denominator and introduce a new unit in the denominator. The following example illustrates this situation.

```{exercise}
:label: ex:ball-ch02-s04-n04

**Example 9**

Convert 88.4 m/min to meters/second.
```

```{solution} ex:ball-ch02-s04-n04
:label: sol:ball-ch02-s04-n04
:class: dropdown

We want to change the unit in the denominator from minutes to seconds. Because there are 60 seconds in 1 minute (60 s = 1 min), we construct a conversion factor so that the unit we want to remove, minutes, is in the numerator: $\frac{1\text{ min}}{60\text{ s}}$. Apply and perform the math:

$$
\frac{88.4\text{ m}}{\text{ min}}\,\times{}\,\frac{\text{1}\text{ min}}{\text{60 s}}=1.47\text{ m/s}
$$

Notice how the 88.4 automatically goes in the numerator. That’s because any number can be thought of as being in the numerator of a fraction divided by 1.
```

```{exercise}
:label: ex:ball-ch02-s04-n04-ty2

**Test Yourself**

Convert 0.203 m/min to meters/second.
```

```{solution} ex:ball-ch02-s04-n04-ty2
:label: sol:ball-ch02-s04-n04-ty2
:class: dropdown

0.00338 m/s or 3.38 × 10<sup>−3</sup> m/s
```

```{figure} ../images/restored/snail.jpg
:label: fig:ch02:s04:f01
:enumerator: 2.8
:alt: A garden snail with a brown spiral shell on the ground.
:align: center
:width: 70%

**How Fast Is Fast?.** A garden snail provides a familiar comparison for slow motion. A representative speed of 0.2 m/min is about 0.003 m/s, or 3 mm/s. The photograph does not measure the speed of this particular snail.

Credits: [Cornu aspersum - December 2022 - Sarah Stierch — Missvain](https://commons.wikimedia.org/wiki/File:Cornu_aspersum_-_December_2022_-_Sarah_Stierch.jpg), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0). Images resized for the web.
```

Sometimes there will be a need to convert from one unit with one numerical prefix to another unit with a different numerical prefix. How do we handle those conversions? Well, you could memorize the conversion factors that interrelate all numerical prefixes. Or you can go the easier route: first convert the quantity to the base unit, the unit with no numerical prefix, using the definition of the original prefix. Then convert the quantity in the base unit to the desired unit using the definition of the second prefix. You can do the conversion in two separate steps or as one long algebraic step. For example, to convert 2.77 kg to milligrams:

$$
\begin{aligned}
2.77\text{ kg}\,\times{}\,\frac{\text{1,000 g}}{1\text{ kg}}=2{,}770\text{ g} & (\text{convert to the base unit of grams})
\end{aligned}
$$

$$
\begin{aligned}
2{,}770\text{ g}\,\times{}\,\frac{\text{1,000 mg}}{\text{1}\text{ g}}=2{,}770{,}000\text{ mg}=\text{2}\text{.77}\,\times{}\,{\text{10}}^{6}\text{ mg} & (\text{convert to desired unit})
\end{aligned}
$$

Alternatively, it can be done in a single multistep process:

$$
2.77\text{ kg}\,\times{}\,\frac{\text{1,000}\text{ g}}{\text{1}\text{ kg}}\,\times{}\,\frac{\text{1,000 mg}}{\text{1}\text{ g}}=2{,}770{,}000\text{ mg}=\text{2}\text{.77}\,\times{}\,{\text{10}}^{6}\text{ mg}
$$

You get the same answer either way.

```{exercise}
:label: ex:ball-ch02-s04-n05

**Example 10**

How many nanoseconds are in 368.09 μs?
```

```{solution} ex:ball-ch02-s04-n05
:label: sol:ball-ch02-s04-n05
:class: dropdown

You can either do this as a one-step conversion from microseconds to nanoseconds or convert to the base unit first and then to the final desired unit. We will use the second method here, showing the two steps in a single line. Using the definitions of the prefixes *micro-* and *nano-*,

$$
368.09\,\mu{}\text{s}\,\times{}\,\frac{\text{1}\text{ s}}{1{,}000{,}000\,\mu{}\text{s}}\,\times{}\,\frac{1{,}000{,}000{,}000\text{ ns}}{1\text{ s}}=368{,}090\text{ ns}=\text{3}\text{.6809}\,\times{}\,{\text{10}}^{5}\text{ ns}
$$
```

```{exercise}
:label: ex:ball-ch02-s04-n05-ty2

**Test Yourself**

How many milliliters are in 607.8 kL?
```

```{solution} ex:ball-ch02-s04-n05-ty2
:label: sol:ball-ch02-s04-n05-ty2
:class: dropdown

6.078 × 10<sup>8</sup> mL
```

When considering the significant figures of a final numerical answer in a conversion, there is one important case where a number does not impact the number of significant figures in a final answer—the so-called **exact number** (*A number from a defined relationship that technically has an infinite number of significant figures.*). An exact number is a number from a defined relationship, not a measured one. For example, the prefix *kilo-* means 1,000—*exactly* 1,000, no more or no less. Thus, in constructing the conversion factor

$$
\frac{1{,}000\text{ g}}{1\text{ kg}}
$$

neither the 1,000 nor the 1 enter into our consideration of significant figures. The numbers in the numerator and denominator are defined exactly by what the prefix *kilo-* means. Another way of thinking about it is that these numbers can be thought of as having an infinite number of significant figures, such as

$$
\frac{1{,}000.0000000000\text{…}\text{ g}}{1.0000000000\text{…}\text{ kg}}
$$

The other numbers in the calculation will determine the number of significant figures in the final answer.

```{exercise}
:label: ex:ball-ch02-s04-n06

**Example 11**

A rectangular plot in a garden has the dimensions 36.7 cm by 128.8 cm. What is the area of the garden plot in square meters? Express your answer in the proper number of significant figures.
```

```{solution} ex:ball-ch02-s04-n06
:label: sol:ball-ch02-s04-n06
:class: dropdown

Area is defined as the product of the two dimensions, which we then have to convert to square meters and express our final answer to the correct number of significant figures, which in this case will be three.

$$
36.7\text{ cm}\,\times{}\,\text{128}\text{.8}\text{ cm}\,\times{}\,\frac{1\text{ m}}{100\text{ cm}}\,\times{}\,\frac{1\text{ m}}{100\text{ cm}}=0.472696{\text{ m}}^{2}=0.473{\text{ m}}^{2}
$$

The 1 and 100 in the conversion factors do not affect the determination of significant figures because they are exact numbers, defined by the centi- prefix.
```

```{exercise}
:label: ex:ball-ch02-s04-n06-ty2

**Test Yourself**

What is the volume of a block in cubic meters whose dimensions are 2.1 cm × 34.0 cm × 118 cm?
```

```{solution} ex:ball-ch02-s04-n06-ty2
:label: sol:ball-ch02-s04-n06-ty2
:class: dropdown

0.0084 m<sup>3</sup>
```

```{tip} Chemistry Is Everywhere: The Gimli Glider

On July 23, 1983, an Air Canada Boeing 767 jet had to glide to an emergency landing at Gimli Industrial Park Airport in Gimli, Manitoba, because it unexpectedly ran out of fuel during flight. There was no loss of life in the course of the emergency landing, only some minor injuries associated in part with the evacuation of the craft after landing. For the remainder of its operational life (the plane was retired in 2008), the aircraft was nicknamed “the Gimli Glider.”

(fig:ch02:s04:f02)=

![The Gimli Glider is the Boeing 767 that ran out of fuel and glided to safety at Gimli Airport. The aircraft ran out of fuel because of confusion over the units used to express the amount of fuel.](../images/figures/0f7101ae04a77cfd8e935edff18e3e21.jpg)

*The Gimli Glider is the Boeing 767 that ran out of fuel and glided to safety at Gimli Airport. The aircraft ran out of fuel because of confusion over the units used to express the amount of fuel.*

The 767 took off from Montreal on its way to Ottawa, ultimately heading for Edmonton, Canada. About halfway through the flight, all the engines on the plane began to shut down because of a lack of fuel. When the final engine cut off, all electricity (which was generated by the engines) was lost; the plane became, essentially, a powerless glider. Captain Robert Pearson was an experienced glider pilot, although he had never flown a glider the size of a 767. First Officer Maurice Quintal quickly determined that the aircraft would not be able make it to Winnipeg, the next large airport. He suggested his old Royal Air Force base at Gimli Station, one of whose runways was still being used as a community airport. Between the efforts of the pilots and the flight crew, they managed to get the airplane safely on the ground (although with buckled landing gear) and all passengers off safely.

What happened? At the time, Canada was transitioning from the older English system to the metric system. The Boeing 767s were the first aircraft whose gauges were calibrated in the metric system of units (liters and kilograms) rather than the English system of units (gallons and pounds). Thus, when the fuel gauge read 22,300, the gauge meant kilograms, but the ground crew mistakenly fueled the plane with 22,300 *pounds* of fuel. This ended up being just less than half of the fuel needed to make the trip, causing the engines to quit about halfway to Ottawa. Quick thinking and extraordinary skill saved the lives of 61 passengers and 8 crew members—an incident that would not have occurred if people were watching their units.
```

```{important} Key Takeaways

- Units can be converted to other units using the proper conversion factors.
- Conversion factors are constructed from equalities that relate two different units.
- Conversions can be a single step or multistep.
- Unit conversion is a powerful mathematical technique in chemistry that must be mastered.
- Exact numbers do not affect the determination of significant figures.
```

## Exercises

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa01

**Exercise 1.**

Write the two conversion factors that exist between the two given units.

a. milliliters and liters
b. microseconds and seconds
c. kilometers and meters
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa01
:label: sol:ball-ch02-s04-qs01-qd01-qa01
:class: dropdown

a. $\frac{\text{1,000 mL}}{1\text{ L}}$ and $\frac{\text{1 L}}{\text{1,000 mL}}$
b. $\frac{\text{1,000,000 }\mu{}\text{s}}{1\text{ s}}$ and $\frac{\text{1 s}}{\text{1,000,000 }\mu{}\text{s}}$
c. $\frac{\text{1,000 m}}{1\text{ km}}$ and $\frac{\text{1 km}}{\text{1,000 m}}$
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa02

**Exercise 2.**

Write the two conversion factors that exist between the two given units.

a. kilograms and grams
b. milliseconds and seconds
c. centimeters and meters
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa03

**Exercise 3.**

Perform the following conversions.

a. 5.4 km to meters
b. 0.665 m to millimeters
c. 0.665 m to kilometers
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa03
:label: sol:ball-ch02-s04-qs01-qd01-qa03
:class: dropdown

a. 5,400 m
b. 665 mm
c. 6.65 × 10<sup>−4</sup> km
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa04

**Exercise 4.**

Perform the following conversions.

a. 90.6 mL to liters
b. 0.00066 ML to liters
c. 750 L to kiloliters
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa05

**Exercise 5.**

Perform the following conversions.

a. 17.8 μg to grams
b. 7.22 × 10<sup>2</sup> kg to grams
c. 0.00118 g to nanograms
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa05
:label: sol:ball-ch02-s04-qs01-qd01-qa05
:class: dropdown

a. 1.78 × 10<sup>−5</sup> g
b. 7.22 × 10<sup>5</sup> g
c. 1.18 × 10<sup>6</sup> ng
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa06

**Exercise 6.**

Perform the following conversions.

a. 833 ns to seconds
b. 5.809 s to milliseconds
c. 2.77 × 10<sup>6</sup> s to megaseconds
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa07

**Exercise 7.**

Perform the following conversions.

a. 9.44 m<sup>2</sup> to square centimeters
b. 3.44 × 10<sup>8</sup> mm<sup>3</sup> to cubic meters
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa07
:label: sol:ball-ch02-s04-qs01-qd01-qa07
:class: dropdown

a. 94,400 cm<sup>2</sup>
b. 0.344 m<sup>3</sup>
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa08

**Exercise 8.**

Perform the following conversions.

a. 0.00444 cm<sup>3</sup> to cubic meters
b. 8.11 × 10<sup>2</sup> m<sup>2</sup> to square nanometers
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa09

**Exercise 9.**

Why would it be inappropriate to convert square centimeters to cubic meters?
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa09
:label: sol:ball-ch02-s04-qs01-qd01-qa09
:class: dropdown

One is a unit of area, and the other is a unit of volume.
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa10

**Exercise 10.**

Why would it be inappropriate to convert from cubic meters to cubic seconds?
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa11

**Exercise 11.**

Perform the following conversions.

a. 45.0 m/min to meters/second
b. 0.000444 m/s to micrometers/second
c. 60.0 km/h to kilometers/second
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa11
:label: sol:ball-ch02-s04-qs01-qd01-qa11
:class: dropdown

a. 0.75 m/s
b. 444 µm/s
c. 1.666 × 10<sup>−2</sup> km/s
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa12

**Exercise 12.**

Perform the following conversions.

a. 3.4 × 10<sup>2</sup> cm/s to centimeters/minute
b. 26.6 mm/s to millimeters/hour
c. 13.7 kg/L to kilograms/milliliters
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa13

**Exercise 13.**

Perform the following conversions.

a. 0.674 kL to milliliters
b. 2.81 × 10<sup>12</sup> mm to kilometers
c. 94.5 kg to milligrams
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa13
:label: sol:ball-ch02-s04-qs01-qd01-qa13
:class: dropdown

a. 674,000 mL
b. 2.81 × 10<sup>6</sup> km
c. 9.45 × 10<sup>7</sup> mg
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa14

**Exercise 14.**

Perform the following conversions.

a. 6.79 × 10<sup>−6</sup> kg to micrograms
b. 1.22 mL to kiloliters
c. 9.508 × 10<sup>−9</sup> ks to milliseconds
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa15

**Exercise 15.**

Perform the following conversions.

a. 6.77 × 10<sup>14</sup> ms to kiloseconds
b. 34,550,000 cm to kilometers
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa15
:label: sol:ball-ch02-s04-qs01-qd01-qa15
:class: dropdown

a. 6.77 × 10<sup>8</sup> ks
b. 345.5 km
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa16

**Exercise 16.**

Perform the following conversions.

a. 4.701 × 10<sup>15</sup> mL to kiloliters
b. 8.022 × 10<sup>−11</sup> ks to microseconds
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa17

**Exercise 17.**

Perform the following conversions. Note that you will have to convert units in both the numerator and the denominator.

a. 88 ft/s to miles/hour (Hint: use 5,280 ft = 1 mi.)
b. 0.00667 km/h to meters/second
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa17
:label: sol:ball-ch02-s04-qs01-qd01-qa17
:class: dropdown

a. 6.0 × 10<sup>1</sup> mi/h
b. 0.00185 m/s
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa18

**Exercise 18.**

Perform the following conversions. Note that you will have to convert units in both the numerator and the denominator.

a. 3.88 × 10<sup>2</sup> mm/s to kilometers/hour
b. 1.004 kg/L to grams/milliliter
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa19

**Exercise 19.**

What is the area in square millimeters of a rectangle whose sides are 2.44 cm × 6.077 cm? Express the answer to the proper number of significant figures.
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa19
:label: sol:ball-ch02-s04-qs01-qd01-qa19
:class: dropdown

1.48 × 10<sup>3</sup> mm<sup>2</sup>
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa20

**Exercise 20.**

What is the volume in cubic centimeters of a cube with sides of 0.774 m? Express the answer to the proper number of significant figures.
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa21

**Exercise 21.**

The formula for the area of a triangle is 1/2 × base × height. What is the area of a triangle in square centimeters if its base is 1.007 m and its height is 0.665 m? Express the answer to the proper number of significant figures.
```

```{solution} ex:ball-ch02-s04-qs01-qd01-qa21
:label: sol:ball-ch02-s04-qs01-qd01-qa21
:class: dropdown

3.35 × 10<sup>3</sup> cm<sup>2</sup>
```

```{exercise}
:label: ex:ball-ch02-s04-qs01-qd01-qa22

**Exercise 22.**

The formula for the area of a triangle is 1/2 × base × height. What is the area of a triangle in square meters if its base is 166 mm and its height is 930.0 mm? Express the answer to the proper number of significant figures.
```
