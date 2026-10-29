---
title: "7.2 Work and Heat"
---

(sec:ch07:s02)=

# 7.2 Work and Heat

```{note} Learning Objectives

1. Define a type of work in terms of pressure and volume.
2. Define *heat*.
3. Relate the amount of heat to a temperature change.
```

We have already defined work as a force acting through a distance. It turns out that there are other equivalent definitions of work that are also important in chemistry.

When a certain volume of a gas expands, it works against an external pressure to expand ({ref}`Figure 7.2 "Volume versus Pressure" <fig:ch07:s02:f01>`). That is, the gas must perform work. Assuming that the external pressure *P*<sub>ext</sub> is constant, the amount of work done by the gas is given by the equation

$$
\text{w = }-\text{Pext }\times{}\text{ }\Delta{}\text{V}
$$

where Δ*V* is the change in volume of the gas. This term is always the final volume minus the initial volume,

$$
\Delta{}\text{V = Vfinal }-\text{ Vinitial}
$$

and can be positive or negative, depending on whether *V*<sub>final</sub> is larger (is expanding) or smaller (is contracting) than *V*<sub>initial</sub>. The negative sign in the equation for work is important and implies that as volume expands (Δ*V* is positive), the gas in the system is *losing* energy as work. On the other hand, if the gas is contracting, Δ*V* is negative, and the two negative signs make the work positive, so energy is being added to the system.

```{figure} ../images/figures/efdb6de28bfe8ea6defac3c0c836b602.jpg
:label: fig:ch07:s02:f01
:alt: "Volume versus Pressure. When a gas expands against an external pressure, the gas does work."
:align: center
:width: 85%

Volume versus Pressure. When a gas expands against an external pressure, the gas does work.
```

Finally, let us consider units. Volume changes are usually expressed in units like liters, while pressures are usually expressed in atmospheres. When we use the equation to determine work, the unit for work comes out as liter·atmospheres, or L·atm. This is not a very common unit for work. However, there is a conversion factor between L·atm and the common unit of work, joules:

$$
\text{1 L}\cdot{}\text{atm = 101.32 J}
$$

Using this conversion factor and the previous equation for work, we can calculate the work performed when a gas expands or contracts.

```{exercise}
:label: ex:ball-ch07-s02-n02

**Example 2**

What is the work performed by a gas if it expands from 3.44 L to 6.19 L against a constant external pressure of 1.26 atm? Express the final answer in joules.
```

```{solution} ex:ball-ch07-s02-n02
:label: sol:ball-ch07-s02-n02
:class: dropdown

First we need to determine the change in volume, Δ*V*. A change is always the final value minus the initial value:

$\Delta{}\text{V = Vfinal }-\text{ Vinitial = 6.19 L }-\text{ 3.44 L = 2.75 L}$

Now we can use the definition of work to determine the work done:

$\text{w = }-\text{Pext }\cdot{}\text{ }\Delta{}\text{V = }-\text{(1.26 atm)(2.75 L) = }-\text{3.47 L}\cdot{}\text{atm}$

Now we construct a conversion factor from the relationship between liter·atmospheres and joules:

$$
-3.47\text{ L}\cdot{}\text{atm}\,\times{}\,\frac{\text{101}\text{.32 J}}{1\text{ L}\cdot{}\text{atm}}=-351\text{ J}
$$

We limit the final answer to three significant figures, as appropriate.
```

```{exercise}
:label: ex:ball-ch07-s02-n02-ty2

**Test Yourself**

What is the work performed when a gas expands from 0.66 L to 1.33 L against an external pressure of 0.775 atm?
```

```{solution} ex:ball-ch07-s02-n02-ty2
:label: sol:ball-ch07-s02-n02-ty2
:class: dropdown

−53 J
```

Heat is another aspect of energy. **Heat** (*The transfer of energy from one body to another due to a difference in temperature.*) is the transfer of energy from one body to another due to a difference in temperature. For example, when we touch something with our hands, we interpret that object as either hot or cold depending on how energy is transferred: If energy is transferred into your hands, the object feels hot. If energy is transferred from your hands to the object, your hands feel cold. Because heat is a measure of energy transfer, heat is also measured in joules.

For a given object, the amount of heat (*q*) involved is proportional to two things: the mass of the object (*m*) and the temperature change (Δ*T*) evoked by the energy transfer. We can write this mathematically as

$$
q\propto{}m\,\times{}\,\Delta{}T
$$

where ∝ means “is proportional to.” To make a proportionality an equality, we include a proportionality constant. In this case, the proportionality constant is labeled *c* and is called the **specific heat capacity** (*The proportionality constant between heat, mass, and temperature change; also called specific heat.*), or, more succinctly, **specific heat**:

$$
\text{q = mc}\Delta{}\text{T}
$$

where the mass, specific heat, and change in temperature are multiplied together. Specific heat is a measure of how much energy is needed to change the temperature of a substance; the larger the specific heat, the more energy is needed to change the temperature. The units for specific heat are $\frac{\text{J}}{\text{g}\cdot{}^{\circ}\text{C}}$ or $\frac{\text{J}}{\text{g}\cdot{}\text{K}}$, depending on what the unit of Δ*T* is. You may note a departure from the insistence that temperature be expressed in Kelvin. That is because a *change* in temperature has the same value whether the temperatures are expressed in degrees Celsius or kelvins.

```{exercise}
:label: ex:ball-ch07-s02-n03

**Example 3**

Calculate the heat involved when 25.0 g of Fe increase temperature from 22°C to 76°C. The specific heat of Fe is 0.449 J/g·°C.
```

```{solution} ex:ball-ch07-s02-n03
:label: sol:ball-ch07-s02-n03
:class: dropdown

First we need to determine Δ*T*. A change is always the final value minus the initial value:

$\Delta{}\text{T = 76}^{\circ}\text{C }-\text{ 22}^{\circ}\text{C = 54}^{\circ}\text{C}$

Now we can use the expression for *q*, substitute for all variables, and solve for heat:

$$
q=(25.0\text{ g)}(0.449\,\frac{\text{J}}{\text{ g}\cdot{}^{\circ}\text{C}})(54^{\circ}\text{C)}\text{= }610\text{ J}
$$

Note how the g and °C units cancel, leaving J, a unit of heat. Also note that this value of *q* is inherently positive, meaning that energy is going into the system.
```

```{exercise}
:label: ex:ball-ch07-s02-n03-ty2

**Test Yourself**

Calculate the heat involved when 76.5 g of Ag increase temperature from 17.8°C to 144.5°C. The specific heat of Ag is 0.233 J/g·°C.
```

```{solution} ex:ball-ch07-s02-n03-ty2
:label: sol:ball-ch07-s02-n03-ty2
:class: dropdown

2,260 J
```

As with any equation, when you know all but one variable in the expression for *q*, you can determine the remaining variable by using algebra.

```{exercise}
:label: ex:ball-ch07-s02-n04

**Example 4**

It takes 5,408 J of heat to raise the temperature of 373 g of Hg by 104°C. What is the specific heat of Hg?
```

```{solution} ex:ball-ch07-s02-n04
:label: sol:ball-ch07-s02-n04
:class: dropdown

We can start with the equation for *q*, but now different values are given, and we need to solve for specific heat. Note that Δ*T* is given directly as 104°C. Substituting,

$\text{5,408 J = (373 g)c(104}^{\circ}\text{C)}$

We divide both sides of the equation by 373 g and 104°C:

$$
c=\frac{5408\text{ J}}{(\text{373 g)(104}^{\circ}\text{C)}}
$$

Combining the numbers and bringing together all the units, we get

$$
c=0.139\frac{\text{J}}{\text{g}\cdot{}^{\circ}\text{C}}
$$
```

```{exercise}
:label: ex:ball-ch07-s02-n04-ty2

**Test Yourself**

Gold has a specific heat of 0.129 J/g·°C. If 1,377 J are needed to increase the temperature of a sample of gold by 99.9°C, what is the mass of the gold?
```

```{solution} ex:ball-ch07-s02-n04-ty2
:label: sol:ball-ch07-s02-n04-ty2
:class: dropdown

107 g
```

{ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>` lists the specific heats of some substances. Specific heat is a physical property of substances, so it is a characteristic of the substance. The general idea is that the lower the specific heat, the less energy is required to change the temperature of the substance by a certain amount.

```{table} Specific Heats of Various Substances
:label: tbl:ch07:s02:t01

| Substance | Specific Heat (J/g·°C) |
| --- | --- |
| water | 4.184 |
| iron | 0.449 |
| gold | 0.129 |
| mercury | 0.139 |
| aluminum | 0.900 |
| ethyl alcohol | 2.419 |
| magnesium | 1.03 |
| helium | 5.171 |
| oxygen | 0.918 |
```

```{important} Key Takeaways

- Work can be defined as a gas changing volume against a constant external pressure.
- Heat is the transfer of energy due to temperature differences.
- Heat can be calculated in terms of mass, temperature change, and specific heat.
```

## Exercises

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa01

**Exercise 1.**

Give two definitions of work.
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa01
:label: sol:ball-ch07-s02-qs01-qd01-qa01
:class: dropdown

Work is a force acting through a distance or a volume changing against some pressure.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa02

**Exercise 2.**

What is the sign on work when a sample of gas increases its volume? Explain why work has that sign.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa03

**Exercise 3.**

What is the work when a gas expands from 3.00 L to 12.60 L against an external pressure of 0.888 atm?
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa03
:label: sol:ball-ch07-s02-qs01-qd01-qa03
:class: dropdown

−864 J
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa04

**Exercise 4.**

What is the work when a gas expands from 0.666 L to 2.334 L against an external pressure of 2.07 atm?
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa05

**Exercise 5.**

What is the work when a gas contracts from 3.45 L to 0.97 L under an external pressure of 0.985 atm?
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa05
:label: sol:ball-ch07-s02-qs01-qd01-qa05
:class: dropdown

248 J
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa06

**Exercise 6.**

What is the work when a gas contracts from 4.66 L to 1.22 L under an external pressure of 3.97 atm?
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa07

**Exercise 7.**

Like work, the sign on heat can be positive or negative. What is happening to the total energy of a system if heat is positive?
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa07
:label: sol:ball-ch07-s02-qs01-qd01-qa07
:class: dropdown

When heat is positive, the total energy of the system is increasing.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa08

**Exercise 8.**

Like work, the sign on heat can be positive or negative. What is happening to the total energy of a system if heat is negative?
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa09

**Exercise 9.**

What is the heat when 55.6 g of Fe increase temperature from 25.6°C to 177.9°C? The heat capacity of Fe is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa09
:label: sol:ball-ch07-s02-qs01-qd01-qa09
:class: dropdown

3.80 × 10<sup>3</sup> J
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa10

**Exercise 10.**

What is the heat when 0.444 g of Au increases temperature from 17.8°C to 222.5°C? The heat capacity of Au is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa11

**Exercise 11.**

What is the heat when 245 g of H<sub>2</sub>O cool from 355 K to 298 K? The heat capacity of H<sub>2</sub>O is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa11
:label: sol:ball-ch07-s02-qs01-qd01-qa11
:class: dropdown

−58,400 J
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa12

**Exercise 12.**

What is the heat when 100.0 g of Mg cool from 725 K to 552 K? The heat capacity of Mg is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa13

**Exercise 13.**

It takes 452 J of heat to raise the temperature of a 36.8 g sample of a metal from 22.9°C to 98.2°C. What is the heat capacity of the metal?
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa13
:label: sol:ball-ch07-s02-qs01-qd01-qa13
:class: dropdown

0.163 J/g·°C
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa14

**Exercise 14.**

It takes 2,267 J of heat to raise the temperature of a 44.5 g sample of a metal from 33.9°C to 288.3°C. What is the heat capacity of the metal?
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa15

**Exercise 15.**

An experimenter adds 336 J of heat to a 56.2 g sample of Hg. What is its change in temperature? The heat capacity of Hg is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa15
:label: sol:ball-ch07-s02-qs01-qd01-qa15
:class: dropdown

43.0°C
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa16

**Exercise 16.**

To a 0.444 g sample of H<sub>2</sub>O, 23.4 J of heat are added. What is its change in temperature? The heat capacity of H<sub>2</sub>O is in {ref}`Table 7.1 "Specific Heats of Various Substances" <tbl:ch07:s02:t01>`.
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa17

**Exercise 17.**

An unknown mass of Al absorbs 187.9 J of heat and increases its temperature from 23.5°C to 35.6°C. What is the mass of the aluminum? How many moles of aluminum is this?
```

```{solution} ex:ball-ch07-s02-qs01-qd01-qa17
:label: sol:ball-ch07-s02-qs01-qd01-qa17
:class: dropdown

17.3 g; 0.640 mol
```

```{exercise}
:label: ex:ball-ch07-s02-qs01-qd01-qa18

**Exercise 18.**

A sample of He goes from 19.4°C to 55.9°C when 448 J of energy are added. What is the mass of the helium? How many moles of helium is this?
```
