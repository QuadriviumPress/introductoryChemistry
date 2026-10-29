---
title: "13.2 The Equilibrium Constant"
---

(sec:ch13:s02)=

# 13.2 The Equilibrium Constant

```{note} Learning Objectives

1. Explain the importance of the equilibrium constant.
2. Construct an equilibrium constant expression for a chemical reaction.
```

In the mid 1860s, Norwegian scientists C. M. Guldberg and P. Waage noted a peculiar relationship between the amounts of reactants and products in an equilibrium. No matter how many reactants they started with, a certain ratio of reactants and products was achieved at equilibrium. Today, we call this observation the **law of mass action** (*The relationship of the amounts of reactants and products at equilibrium.*). It relates the amounts of reactants and products at equilibrium for a chemical reaction. For a general chemical reaction occurring in solution,

$$
a\text{A + }b\text{B}\rightleftarrows{}c\text{C + }d\text{D}
$$

the **equilibrium constant** (*A numerical value that relates to the ratio of products and reactants at equilibrium.*), also known as *K*<sub>eq</sub>, is defined by the following expression:

$$
{K}_{\text{eq}}=\frac{{[\text{C]}}^{c}{[\text{D]}}^{d}}{{[\text{A]}}^{a}{[\text{B]}}^{b}}
$$

where [A] is the molar concentration of species A at equilibrium, and so forth. The coefficients *a*, *b*, *c*, and *d* in the chemical equation become exponents in the expression for *K*<sub>eq</sub>. The *K*<sub>eq</sub> is a characteristic numerical value for a given reaction at a given temperature; that is, each chemical reaction has its own characteristic *K*<sub>eq</sub>. The concentration of each reactant and product in a chemical reaction at equilibrium is *related*; the concentrations cannot be random values, but they depend on each other. The numerator of the expression for *K*<sub>eq</sub> has the concentrations of every product (however many products there are), while the denominator of the expression for *K*<sub>eq</sub> has the concentrations of every reactant, leading to the common *products over reactants* definition for the *K*<sub>eq</sub>.

Let us consider a simple example. Suppose we have this equilibrium:

$$
\text{A}\rightleftarrows{}\text{B}
$$

There is one reactant, one product, and the coefficients on each are just 1 (assumed, not written). The *K*<sub>eq</sub> expression for this equilibrium is

$$
{K}_{\text{eq}}=\frac{[\text{B]}}{[\text{A]}}
$$

(Exponents of 1 on each concentration are understood.) Suppose the numerical value of *K*<sub>eq</sub> for this chemical reaction is 2.0. If [B] = 4.0 M, then [A] must equal 2.0 M so that the value of the fraction equals 2.0:

$$
{K}_{\text{eq}}=\frac{[\text{B]}}{[\text{A]}}=\frac{4.0}{2.0}=2.0
$$

By convention, the units are understood to be M and are omitted from the *K*<sub>eq</sub> expression. Suppose [B] were 6.0 M. For the *K*<sub>eq</sub> value to remain constant (it is, after all, called the equilibrium *constant*), then [A] would have to be 3.0 M at equilibrium:

$$
{K}_{\text{eq}}=\frac{[\text{B]}}{[\text{A]}}=\frac{6.0}{3.0}=2.0
$$

If [A] were *not* equal to 3.0 M, the reaction would not be at equilibrium, and a net reaction would occur until that ratio was indeed 2.0. At that point, the reaction is at equilibrium, and any net change would cease. (Recall, however, that the forward and reverse reactions do not stop because chemical equilibrium is dynamic.)

The issue is the same with more complex expressions for the *K*<sub>eq</sub>; only the mathematics becomes more complex. Generally speaking, given a value for the *K*<sub>eq</sub> and all but one concentration at equilibrium, the missing concentration can be calculated.

```{exercise}
:label: ex:ball-ch13-s02-n02

**Example 2**

Given the following reaction:

$$
{\text{H}}_{\text{2}}{\text{+ I}}_{\text{2}}\rightleftarrows{}\text{2HI}
$$

If the equilibrium [HI] is 0.75 M and the equilibrium [H<sub>2</sub>] is 0.20 M, what is the equilibrium [I<sub>2</sub>] if the *K*<sub>eq</sub> is 0.40?
```

```{solution} ex:ball-ch13-s02-n02
:label: sol:ball-ch13-s02-n02
:class: dropdown

We start by writing the *K*<sub>eq</sub> expression. Using the *products over reactants* approach, the *K*<sub>eq</sub> expression is as follows:

$$
{K}_{\text{eq}}=\frac{{[\text{HI]}}^{2}}{[{\text{H}}_{2}][{\text{I}}_{2}]}
$$

Note that [HI] is squared because of the coefficient 2 in the balanced chemical equation. Substituting for the equilibrium [H<sub>2</sub>] and [HI] and for the given value of *K*<sub>eq</sub>:

$$
0.40=\frac{{(0.75)}^{2}}{(0.20)[{\text{I}}_{2}]}
$$

To solve for [I<sub>2</sub>], we have to do some algebraic rearrangement: divide the 0.40 into both sides of the equation and multiply both sides of the equation by [I<sub>2</sub>]. This brings [I<sub>2</sub>] into the numerator of the left side and the 0.40 into the denominator of the right side:

$$
[{\text{I}}_{2}]=\frac{{(0.75)}^{2}}{(0.20)(0.40)}
$$

Solving,

$\text{[I2] = 7.0 M}$

The concentration unit is assumed to be molarity. This value for [I<sub>2</sub>] can be easily verified by substituting 0.75, 0.20, and 7.0 into the expression for *K*<sub>eq</sub> and evaluating: you should get 0.40, the numerical value of *K*<sub>eq</sub> (and you do).
```

```{exercise}
:label: ex:ball-ch13-s02-n02-ty2

**Test Yourself**

Given the following reaction:

$$
{\text{H}}_{\text{2}}{\text{+ I}}_{\text{2}}\rightleftarrows{}\text{2HI}
$$

If the equilibrium [HI] is 0.060 M and the equilibrium [I<sub>2</sub>] is 0.90 M, what is the equilibrium [H<sub>2</sub>] if the *K*<sub>eq</sub> is 0.40?
```

```{solution} ex:ball-ch13-s02-n02-ty2
:label: sol:ball-ch13-s02-n02-ty2
:class: dropdown

0.010 M
```

In some types of equilibrium problems, square roots, cube roots, or even higher roots need to be analyzed to determine a final answer. Make sure you know how to perform such operations on your calculator; if you do not know, ask your instructor for assistance.

```{exercise}
:label: ex:ball-ch13-s02-n03

**Example 3**

The following reaction is at equilibrium:

$$
{\text{N}}_{\text{2}}{\text{+ 3H}}_{\text{2}}\rightleftarrows{}2{\text{NH}}_{\text{3}}
$$

The *K*<sub>eq</sub> at a particular temperature is 13.7. If the equilibrium [N<sub>2</sub>] is 1.88 M and the equilibrium [NH<sub>3</sub>] is 6.62 M, what is the equilibrium [H<sub>2</sub>]?
```

```{solution} ex:ball-ch13-s02-n03
:label: sol:ball-ch13-s02-n03
:class: dropdown

We start by writing the *K*<sub>eq</sub> expression from the balanced chemical equation:

$$
{K}_{\text{eq}}=\frac{{[{\text{NH}}_{3}]}^{2}}{[{\text{N}}_{2}]{[{\text{H}}_{2}]}^{3}}
$$

Substituting for the known equilibrium concentrations and the *K*<sub>eq</sub>, this becomes

$$
13.7=\frac{{(6.62)}^{2}}{(1.88){[{\text{H}}_{2}]}^{3}}
$$

Rearranging algebraically and then evaluating the numerical expression, we get

$$
{[{\text{H}}_{2}]}^{3}=\frac{{(6.22)}^{2}}{(1.88)(13.7)}=1.502112129
$$

To solve for [H<sub>2</sub>], we need to take the cube root of the equation. Performing this operation, we get

$\text{[H2] = 1.15 M}$

You should verify that this is correct using your own calculator to confirm that you know how to do a cube root correctly.
```

```{exercise}
:label: ex:ball-ch13-s02-n03-ty2

**Test Yourself**

The following reaction is at equilibrium:

$$
{\text{N}}_{\text{2}}{\text{+ 3H}}_{\text{2}}\rightleftarrows{}2{\text{NH}}_{\text{3}}
$$

The *K*<sub>eq</sub> at a particular temperature is 13.7. If the equilibrium [N<sub>2</sub>] is 0.055 M and the equilibrium [H<sub>2</sub>] is 1.62 M, what is the equilibrium [NH<sub>3</sub>]?
```

```{solution} ex:ball-ch13-s02-n03-ty2
:label: sol:ball-ch13-s02-n03-ty2
:class: dropdown

1.79 M
```

The *K*<sub>eq</sub> was defined earlier in terms of concentrations. For gas-phase reactions, the *K*<sub>eq</sub> can also be defined in terms of the partial pressures of the reactants and products, *P*<sub>*i*</sub>. For the gas-phase reaction

$$
a\text{A(g) + }b\text{B(g)}\rightleftarrows{}c\text{C(g) + }d\text{D(g)}
$$

the pressure-based equilibrium constant, *K*<sub>P</sub>, is defined as follows:

$$
{K}_{\text{P}}=\frac{{P}_{\text{C}}^{c}{P}_{\text{D}}^{d}}{{P}_{\text{A}}^{a}{P}_{\text{B}}^{b}}
$$

where *P*<sub>A</sub> is the partial pressure of substance A at equilibrium in atmospheres, and so forth. As with the concentration-based equilibrium constant, the units are omitted when substituting into the expression for *K*<sub>P</sub>.

```{exercise}
:label: ex:ball-ch13-s02-n04

**Example 4**

What is the *K*<sub>P</sub> for this reaction, given the equilibrium partial pressures of 0.664 atm for NO<sub>2</sub> and 1.09 for N<sub>2</sub>O<sub>4</sub>?

$$
{\text{2NO}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{N}}_{\text{2}}{\text{O}}_{\text{4}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-n04
:label: sol:ball-ch13-s02-n04
:class: dropdown

Write the *K*<sub>P</sub> expression for this reaction:

$$
{K}_{\text{P}}=\frac{{P}_{{\text{N}}_{2}{\text{O}}_{4}}}{{P}_{{\text{NO}}_{2}}^{2}}
$$

Then substitute the equilibrium partial pressures into the expression and evaluate:

$$
{K}_{\text{P}}=\frac{(1.09)}{{(0.664)}^{2}}=2.47
$$
```

```{exercise}
:label: ex:ball-ch13-s02-n04-ty2

**Test Yourself**

What is the *K*<sub>P</sub> for this reaction, given the equilibrium partial pressures of 0.44 atm for H<sub>2</sub>, 0.22 atm for Cl<sub>2</sub>, and 2.98 atm for HCl?

$$
{\text{H}}_{\text{2}}{\text{ + Cl}}_{\text{2}}\rightleftarrows{}\text{2HCl}
$$
```

```{solution} ex:ball-ch13-s02-n04-ty2
:label: sol:ball-ch13-s02-n04-ty2
:class: dropdown

91.7
```

There is a simple relationship between *K*<sub>eq</sub> (based on concentration units) and *K*<sub>P</sub> (based on pressure units):

$$
{K}_{\text{P}}={K}_{\text{eq}}\cdot{}{(RT)}^{\Delta{}n}
$$

where *R* is the ideal gas law constant (in units of L·atm/mol·K), *T* is the absolute temperature, and Δ*n* is the change in the number of moles of gas in the balanced chemical equation, defined as *n*<sub>gas,prods</sub> − *n*<sub>gas,rcts</sub>. Note that this equation implies that if the number of moles of gas are the same in reactants and products, *K*<sub>eq</sub> = *K*<sub>P</sub>.

```{exercise}
:label: ex:ball-ch13-s02-n05

**Example 5**

What is the *K*<sub>P</sub> at 25°C for this reaction if the *K*<sub>eq</sub> is 4.2 × 10<sup>−2</sup>?

$$
{\text{N}}_{\text{2}}{\text{(g) + 3H}}_{\text{2}}\text{(g)}\rightleftarrows{}2{\text{NH}}_{\text{3}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-n05
:label: sol:ball-ch13-s02-n05
:class: dropdown

Before we use the relevant equation, we need to do two things: convert the temperature to kelvins and determine Δ*n*. Converting the temperature is easy:

$\text{T = 25 + 273 = 298 K}$

To determine the change in the number of moles of gas, take the number of moles of gaseous products and subtract the number of moles of gaseous reactants. There are 2 mol of gas as product and 4 mol of gas of reactant:

$\Delta{}\text{n = 2 }-\text{ 4 = }-\text{2 mol}$

Note that Δ*n* is negative. Now we can substitute into our equation, using *R* = 0.08205 L·atm/mol·K. The units are omitted for clarity:

$\text{KP = (4.2 }\times{}\text{ 10}-\text{2)(0.08205)(298)}-\text{2}$

Solving,

$\text{KP = 7.0 }\times{}\text{ 10}-\text{5}$
```

```{exercise}
:label: ex:ball-ch13-s02-n05-ty2

**Test Yourself**

What is the *K*<sub>P</sub> at 25°C for this reaction if the *K*<sub>eq</sub> is 98.3?

$$
{\text{I}}_{\text{2}}\text{(g)}\rightleftarrows{}\text{2I(g) }
$$
```

```{solution} ex:ball-ch13-s02-n05-ty2
:label: sol:ball-ch13-s02-n05-ty2
:class: dropdown

2.40 × 10<sup>3</sup>
```

Finally, we recognize that many chemical reactions involve substances in the solid or liquid phases. For example, a particular chemical reaction is represented as follows:

$$
{\text{2NaHCO}}_{\text{3}}\text{(s)}\rightleftarrows{}{\text{Na}}_{\text{2}}{\text{CO}}_{\text{3}}{\text{(s) + CO}}_{\text{2}}{\text{(g) + H}}_{\text{2}}\text{O(}\ell{}\text{) }
$$

This chemical equation includes all three phases of matter. This kind of equilibrium is called a **heterogeneous equilibrium** (*An equilibrium in which more than one phase of reactants or products is present.*) because there is more than one phase present.

The rule for heterogeneous equilibria is as follows: *Do not include the concentrations of pure solids and pure liquids in* K<sub>*eq*</sub> *expressions.* Only partial pressures for gas-phase substances or concentrations in solutions are included in the expressions of equilibrium constants. As such, the equilibrium constant expression for this reaction would simply be

$$
{K}_{\text{P}}\,=\,{P}_{{\text{CO}}_{2}}
$$

because the two solids and one liquid would not appear in the expression.

```{important} Key Takeaways

- Every chemical equilibrium can be characterized by an equilibrium constant, known as *K*<sub>eq</sub>.
- The *K*<sub>eq</sub> and *K*<sub>P</sub> expressions are formulated as amounts of products divided by amounts of reactants; each amount (either a concentration or a pressure) is raised to the power of its coefficient in the balanced chemical equation.
- Solids and liquids do not appear in the expression for the equilibrium constant.
```

## Exercises

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa01

**Exercise 1.**

Define the *law of mass action*.
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa01
:label: sol:ball-ch13-s02-qs01-qd01-qa01
:class: dropdown

the relationship between the concentrations of reactants and products of a chemical reaction at equilibrium
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa02

**Exercise 2.**

What is an equilibrium constant for a chemical reaction? How is it constructed?
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa03

**Exercise 3.**

Write the *K*<sub>eq</sub> expression for each reaction.

a. ${\text{H}}_{\text{2}}{\text{ + Cl}}_{\text{2}}\rightleftarrows{}\text{2HCl}$
b. ${\text{NO + NO}}_{\text{2}}\rightleftarrows{}{\text{N}}_{\text{2}}{\text{O}}_{\text{3}}$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa03
:label: sol:ball-ch13-s02-qs01-qd01-qa03
:class: dropdown

a. ${K}_{\text{eq}}=\frac{{[\text{HCl}]}^{2}}{[{\text{H}}_{2}][{\text{Cl}}_{2}]}$
b. ${K}_{\text{eq}}=\frac{[{\text{N}}_{\text{2}}{\text{O}}_{\text{3}}\text{]}}{[{\text{NO][NO}}_{2}]}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa04

**Exercise 4.**

Write the *K*<sub>eq</sub> expression for each reaction.

a. ${\text{C}}_{\text{2}}{\text{H}}_{\text{5}}\text{OH + NaI}\rightleftarrows{}{\text{C}}_{\text{2}}{\text{H}}_{\text{5}}\text{I + NaOH}$
b. ${\text{PCl}}_{\text{3}}{\text{ + Cl}}_{\text{2}}\rightleftarrows{}{\text{PCl}}_{\text{5}}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa05

**Exercise 5.**

Write the *K*<sub>P</sub> expression for each reaction.

a. ${\text{2H}}_{\text{2}}{\text{(g) + O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2H}}_{\text{2}}\text{O(g)}$
b. $2{\text{H}}_{\text{2}}{\text{O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2H}}_{\text{2}}{\text{O(g) + O}}_{\text{2}}\text{(g)}$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa05
:label: sol:ball-ch13-s02-qs01-qd01-qa05
:class: dropdown

a. ${K}_{\text{P}}=\frac{{P}_{{\text{H}}_{2}\text{O}}^{2}}{{P}_{{\text{H}}_{2}}^{2}{P}_{{\text{O}}_{2}}}$
b. ${K}_{\text{P}}=\frac{{P}_{{\text{H}}_{2}\text{O}}^{2}{P}_{{\text{O}}_{2}}}{{P}_{{\text{H}}_{2}{\text{O}}_{2}}^{2}}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa06

**Exercise 6.**

Write the *K*<sub>P</sub> expression for each reaction.

a. ${\text{CH}}_{\text{4}}{\text{(g) + 2O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{CO}}_{\text{2}}{\text{(g) + 2H}}_{\text{2}}\text{O(g)}$
b. ${\text{CH}}_{\text{4}}{\text{(g) + 4Cl}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{CCl}}_{\text{4}}\text{(g) + 4HCl(g)}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa07

**Exercise 7.**

The following reaction is at equilibrium:

$$
{\text{PBr}}_{\text{3}}{\text{ + Br}}_{\text{2}}\rightleftarrows{}{\text{PBr}}_{\text{5}}
$$

The equilibrium [Br<sub>2</sub>] and [PBr<sub>5</sub>] are 2.05 M and 0.55 M, respectively. If the *K*<sub>eq</sub> is 1.65, what is the equilibrium [PBr<sub>3</sub>]?
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa07
:label: sol:ball-ch13-s02-qs01-qd01-qa07
:class: dropdown

0.163 M
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa08

**Exercise 8.**

The following reaction is at equilibrium:

$$
{\text{CO + Cl}}_{\text{2}}\rightleftarrows{}{\text{CoCl}}_{\text{2}}
$$

The equilibrium [CO] and [Cl<sub>2</sub>] are 0.088 M and 0.103 M, respectively. If the *K*<sub>eq</sub> is 0.225, what is the equilibrium [COCl<sub>2</sub>]?
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa09

**Exercise 9.**

The following reaction is at equilibrium:

$$
{\text{CH}}_{\text{4}}{\text{ + 2Cl}}_{\text{2}}\rightleftarrows{}{\text{CH}}_{\text{2}}{\text{Cl}}_{\text{2}}\text{ + 2HCl}
$$

If [CH<sub>4</sub>] is 0.250 M, [Cl<sub>2</sub>] is 0.150 M, and [CH<sub>2</sub>Cl<sub>2</sub>] is 0.175 M at equilibrium, what is [HCl] at equilibrium if the *K*<sub>eq</sub> is 2.30?
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa09
:label: sol:ball-ch13-s02-qs01-qd01-qa09
:class: dropdown

0.272 M
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa10

**Exercise 10.**

The following reaction is at equilibrium:

$$
{\text{4HBr + O}}_{\text{2}}\rightleftarrows{}{\text{2H}}_{\text{2}}{\text{O + 2Br}}_{\text{2}}
$$

If [HBr] is 0.100 M, [O<sub>2</sub>] is 0.250 M, and [H<sub>2</sub>O] is 0.0500 M at equilibrium, what is [Br<sub>2</sub>] at equilibrium if the *K*<sub>eq</sub> is 0.770?
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa11

**Exercise 11.**

Write the *K*<sub>P</sub> expression for the following gas-phase reaction:

$$
{\text{4NO}}_{\text{2}}{\text{(g) + O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2N}}_{\text{2}}{\text{O}}_{\text{5}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa11
:label: sol:ball-ch13-s02-qs01-qd01-qa11
:class: dropdown

${K}_{\text{P}}=\frac{{P}_{{\text{N}}_{2}{\text{O}}_{5}}^{2}}{{P}_{{\text{NO}}_{2}}^{4}{P}_{{\text{O}}_{2}}}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa12

**Exercise 12.**

Write the *K*<sub>P</sub> expression for the following gas-phase reaction:

$$
{\text{ClO(g) + O}}_{\text{3}}\text{(g)}\rightleftarrows{}{\text{ClO}}_{\text{2}}{\text{(g) + O}}_{\text{2}}\text{(g)}
$$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa13

**Exercise 13.**

What is the equilibrium partial pressure of COBr<sub>2</sub> if the equilibrium partial pressures of CO and Br<sub>2</sub> are 0.666 atm and 0.235 atm and the *K*<sub>P</sub> for this equilibrium is 4.08?

$$
{\text{CO(g) + Br}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{COBr}}_{\text{2}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa13
:label: sol:ball-ch13-s02-qs01-qd01-qa13
:class: dropdown

0.639 atm
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa14

**Exercise 14.**

What is the equilibrium partial pressure of O<sub>3</sub> if the equilibrium partial pressure of O<sub>2</sub> is 0.0044 atm and *K*<sub>P</sub> for this equilibrium is 0.00755?

$$
{\text{3O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2O}}_{\text{3}}\text{(g)}
$$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa15

**Exercise 15.**

Calculate the *K*<sub>P</sub> for this reaction at 298 K if the *K*<sub>eq</sub> = 1.76 × 10<sup>−3</sup>.

$$
{\text{3O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2O}}_{\text{3}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa15
:label: sol:ball-ch13-s02-qs01-qd01-qa15
:class: dropdown

7.20 × 10<sup>−5</sup>
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa16

**Exercise 16.**

Calculate the *K*<sub>P</sub> for this reaction at 310 K if the *K*<sub>eq</sub> = 6.22 × 10<sup>3</sup>.

$$
{\text{4NO}}_{\text{2}}{\text{(g) + O}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{2N}}_{\text{2}}{\text{O}}_{\text{5}}\text{(g)}
$$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa17

**Exercise 17.**

Calculate the *K*<sub>eq</sub> for this reaction if the *K*<sub>P</sub> = 5.205 × 10<sup>−3</sup> at 660°C.

$$
{\text{CO(g)+ F}}_{\text{2}}\text{(g)}\rightleftarrows{}{\text{COF}}_{\text{2}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa17
:label: sol:ball-ch13-s02-qs01-qd01-qa17
:class: dropdown

*K*<sub>eq</sub> = 3.98 × 10<sup>−1</sup>
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa18

**Exercise 18.**

Calculate the *K*<sub>eq</sub> for this reaction if the *K*<sub>P</sub> = 78.3 at 100°C.

$$
{\text{4HCl(g) + O}}_{\text{2}}\text{(g)}\rightleftarrows{}2{\text{H}}_{\text{2}}{\text{O(g) + 2Cl}}_{\text{2}}\text{(g)}
$$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa19

**Exercise 19.**

Write the correct *K*<sub>eq</sub> expression for this reaction.

$$
\text{NaOH(aq) + HCl(aq)}\rightleftarrows{}{\text{NaCl(aq) + H}}_{\text{2}}\text{O(}\ell{}\text{)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa19
:label: sol:ball-ch13-s02-qs01-qd01-qa19
:class: dropdown

${K}_{\text{eq}}=\frac{[\text{NaCl]}}{[\text{NaOH][HCl]}}$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa20

**Exercise 20.**

Write the correct *K*<sub>eq</sub> expression for this reaction.

$$
{\text{AgNO}}_{\text{3}}\text{(aq) + NaCl(aq)}\rightleftarrows{}{\text{AgCl(s) + NaNO}}_{\text{3}}\text{(aq)}
$$
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa21

**Exercise 21.**

Write the correct *K*<sub>P</sub> expression for this reaction.

$$
{\text{CaCO}}_{\text{3}}\text{(s)}\rightleftarrows{}{\text{CaO(s) + CO}}_{\text{2}}\text{(g)}
$$
```

```{solution} ex:ball-ch13-s02-qs01-qd01-qa21
:label: sol:ball-ch13-s02-qs01-qd01-qa21
:class: dropdown

*K*<sub>P</sub> = *P*<sub>CO<sub>2</sub></sub>
```

```{exercise}
:label: ex:ball-ch13-s02-qs01-qd01-qa22

**Exercise 22.**

Write the correct *K*<sub>P</sub> expression for this reaction.

$$
{\text{C}}_{\text{2}}{\text{H}}_{\text{2}}{\text{(g) + 2I}}_{\text{2}}\text{(s)}\rightleftarrows{}{\text{C}}_{\text{2}}{\text{H}}_{\text{2}}{\text{I}}_{\text{4}}\text{(g)}
$$
```
