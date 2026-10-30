---
title: "5.1 Stoichiometry"
---

(sec:ch05:s01)=

# 5.1 Stoichiometry

```{note} Learning Objectives

1. Define *stoichiometry*.
2. Relate quantities in a balanced chemical reaction on a molecular basis.
```

Consider a classic recipe for pound cake: 1 pound of eggs, 1 pound of butter, 1 pound of flour, and 1 pound of sugar. (That’s why it’s called “pound cake.”) If you have 4 pounds of butter, how many pounds of sugar, flour, and eggs do you need? You would need 4 pounds each of sugar, flour, and eggs.

Now suppose you have 1.00 g H<sub>2</sub>. If the chemical reaction follows the balanced chemical equation

$$
\text{2H}_{2}\text{(g) + O}_{2}\text{(g) }\rightarrow{}\text{ 2H}_{2}\text{O(}\ell{}\text{)}
$$

then what mass of oxygen do you need to make water?

Curiously, this chemical reaction question is very similar to the pound cake question. Both of them involve relating a quantity of one substance to a quantity of another substance or substances. The relating of one chemical substance to another using a balanced chemical reaction is called **stoichiometry** (*The relating of one chemical substance to another using a balanced chemical reaction.*). Using stoichiometry is a fundamental skill in chemistry; it greatly broadens your ability to predict what will occur and, more importantly, how much is produced.

Let us consider a more complicated example. A recipe for pancakes calls for 2 cups (c) of pancake mix, 1 egg, and 1/2 c of milk. We can write this in the form of a chemical equation:

$$
\text{2 c mix + 1 egg + 1/2 c milk }\rightarrow{}\text{ 1 batch of pancakes}
$$

If you have 9 c of pancake mix, how many eggs and how much milk do you need? It might take a little bit of work, but eventually you will find you need 4½ eggs and 2¼ c milk.

How can we formalize this? We can make a conversion factor using our original recipe and use that conversion factor to convert from a quantity of one substance to a quantity of another substance, similar to the way we constructed a conversion factor between feet and yards in {ref}`Chapter 2 "Measurements" <ch:ch02>`. Because one recipe’s worth of pancakes requires 2 c of pancake mix, 1 egg, and 1/2 c of milk, we actually have the following mathematical relationships that relate these quantities:

$$
\text{2 c pancake mix }\Leftrightarrow{}\text{ 1 egg }\Leftrightarrow{}\text{ 1/2 c milk}
$$

where ⇔ is the mathematical symbol for “is equivalent to.” This does not mean that 2 c of pancake mix equal 1 egg. However, *as far as this recipe is concerned*, these are the equivalent quantities needed for a single recipe of pancakes. So, any possible quantities of two or more ingredients must have the same numerical ratio as the ratios in the equivalence.

We can deal with these equivalences in the same way we deal with equalities in unit conversions: we can make conversion factors that essentially equal 1. For example, to determine how many eggs we need for 9 c of pancake mix, we construct the conversion factor

$$
\frac{\text{1 egg}}{\text{2 c pancake mix}}
$$

This conversion factor is, in a strange way, equivalent to 1 because the recipe relates the two quantities. Starting with our initial quantity and multiplying by our conversion factor,

$$
\text{9}\text{ c pancake mix}\times{}\frac{\text{1 egg}}{\text{2}\text{ c pancake mix}}=4.5\text{ eggs}
$$

Note how the units *cups pancake mix* canceled, leaving us with units of *eggs*. This is the formal, mathematical way of getting our amounts to mix with 9 c of pancake mix. We can use a similar conversion factor for the amount of milk:

$$
\text{9}\text{ c pancake mix}\times{}\frac{\text{1/2 c milk}}{2\text{ c pancake mix}}=2.25\text{ c milk}
$$

Again, units cancel, and new units are introduced.

A balanced chemical equation is nothing more than *a recipe for a chemical reaction*. The difference is that a balanced chemical equation is written in terms of atoms and molecules, not cups, pounds, and eggs.

For example, consider the following chemical equation:

$$
\text{2H}_{2}\text{(g) + O}_{2}\text{(g) }\rightarrow{}\text{ 2H}_{2}\text{O(}\ell{}\text{)}
$$

We can interpret this as, literally, “two hydrogen molecules react with one oxygen molecule to make two water molecules.” That interpretation leads us directly to some equivalences, just as our pancake recipe did:

$$
\text{2H}_{2}\text{ molecules }\Leftrightarrow{}\text{ 1O}_{2}\text{ molecule }\Leftrightarrow{}\text{ 2H}_{2}\text{O molecules}
$$

These equivalences allow us to construct conversion factors:

$$
\begin{aligned}
\frac{{\text{2 molecules H}}_{\text{2}}}{{\text{1 molecule O}}_{\text{2}}} & \frac{{\text{2 molecules H}}_{\text{2}}}{{\text{ 2 molecules H}}_{2}\text{O}} & \frac{{\text{1 molecule O}}_{\text{2}}}{{\text{2 molecules H}}_{\text{2}}\text{O}}
\end{aligned}
$$

and so forth. These conversions can be used to relate quantities of one substance to quantities of another. For example, suppose we need to know how many molecules of oxygen are needed to react with 16 molecules of H<sub>2</sub>. As we did with converting units, we start with our given quantity and use the appropriate conversion factor:

$$
16{\text{ molecules H}}_{\text{2}}\times{}\frac{1{\text{ molecule O}}_{\text{2}}}{2{\text{ molecules H}}_{\text{2}}}=8{\text{ molecules O}}_{\text{2}}
$$

Note how the unit *molecules H*<sub>*2*</sub> cancels algebraically, just as any unit does in a conversion like this. The conversion factor came directly from the coefficients in the balanced chemical equation. This is another reason why a properly balanced chemical equation is important.

```{exercise}
:label: ex:ball-ch05-s01-n02

**Example 1**

How many molecules of SO<sub>3</sub> are needed to react with 144 molecules of Fe<sub>2</sub>O<sub>3</sub> given this balanced chemical equation?

$\text{Fe}_{2}\text{O}_{3}\text{(s) + 3SO}_{3}\text{(g) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}$
```

```{solution} ex:ball-ch05-s01-n02
:label: sol:ball-ch05-s01-n02
:class: dropdown

We use the balanced chemical equation to construct a conversion factor between Fe<sub>2</sub>O<sub>3</sub> and SO<sub>3</sub>. The number of molecules of Fe<sub>2</sub>O<sub>3</sub> goes on the bottom of our conversion factor so it cancels with our given amount, and the molecules of SO<sub>3</sub> go on the top. Thus, the appropriate conversion factor is

$$
\frac{{\text{3 molecules SO}}_{\text{3}}}{{\text{1 molecule Fe}}_{\text{2}}{\text{O}}_{\text{3}}}
$$

Starting with our given amount and applying the conversion factor, the result is

$$
144{\text{ molecules Fe}}_{\text{2}}{\text{O}}_{\text{3}}\times{}\frac{{\text{3 molecules SO}}_{\text{3}}}{\text{1}{\text{ molecule Fe}}_{\text{2}}{\text{O}}_{\text{3}}}=432{\text{ molecules SO}}_{\text{3}}
$$

We need 432 molecules of SO<sub>3</sub> to react with 144 molecules of Fe<sub>2</sub>O<sub>3</sub>.
```

```{exercise}
:label: ex:ball-ch05-s01-n02-ty2

**Test Yourself**

How many molecules of H<sub>2</sub> are needed to react with 29 molecules of N<sub>2</sub> to make ammonia if the balanced chemical equation is N<sub>2</sub> + 3H<sub>2</sub> → 2NH<sub>3</sub>?
```

```{solution} ex:ball-ch05-s01-n02-ty2
:label: sol:ball-ch05-s01-n02-ty2
:class: dropdown

87 molecules
```

Chemical equations also allow us to make conversions regarding the number of atoms in a chemical reaction because a chemical formula lists the number of atoms of each element in a compound. The formula *H*<sub>*2*</sub>*O* indicates that there are two hydrogen atoms and one oxygen atom in each molecule, and these relationships can be used to make conversion factors:

$$
\begin{aligned}
\frac{\text{2 atoms H}}{{\text{1 molecule H}}_{\text{2}}\text{O}} & \frac{{\text{1 molecule H}}_{\text{2}}\text{O}}{\text{1 atom O}}
\end{aligned}
$$

Conversion factors like this can also be used in stoichiometry calculations.

```{exercise}
:label: ex:ball-ch05-s01-n03

**Example 2**

How many molecules of NH<sub>3</sub> can you make if you have 228 atoms of H<sub>2</sub>?
```

```{solution} ex:ball-ch05-s01-n03
:label: sol:ball-ch05-s01-n03
:class: dropdown

From the formula, we know that one molecule of NH<sub>3</sub> has three H atoms. Use that fact as a conversion factor:

$$
228\text{ atoms H}\times{}\frac{{\text{1 molecule NH}}_{\text{3}}}{\text{3}\text{ atoms H}}=76{\text{ molecules NH}}_{\text{3}}
$$
```

```{exercise}
:label: ex:ball-ch05-s01-n03-ty2

**Test Yourself**

How many molecules of Fe<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> can you make from 777 atoms of S?
```

```{solution} ex:ball-ch05-s01-n03-ty2
:label: sol:ball-ch05-s01-n03-ty2
:class: dropdown

259 molecules
```

```{important} Key Takeaway

- Quantities of substances can be related to each other using balanced chemical equations.
```

## Exercises

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa01

**Exercise 1.**

Think back to the pound cake recipe. What possible conversion factors can you construct relating the components of the recipe?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa01
:label: sol:ball-ch05-s01-qs01-qd01-qa01
:class: dropdown

$\frac{\text{1 pound butter}}{\text{1 pound flour}}$ or $\frac{\text{1 pound sugar}}{\text{1 pound eggs}}$ are two conversion factors that can be constructed from the pound cake recipe. Other conversion factors are also possible.
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa02

**Exercise 2.**

Think back to the pancake recipe. What possible conversion factors can you construct relating the components of the recipe?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa03

**Exercise 3.**

What are all the conversion factors that can be constructed from the balanced chemical reaction 2H<sub>2</sub>(g) + O<sub>2</sub>(g) → 2H<sub>2</sub>O(ℓ)?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa03
:label: sol:ball-ch05-s01-qs01-qd01-qa03
:class: dropdown

$\frac{{\text{2 molecules H}}_{2}}{{\text{1 molecule O}}_{2}}$, $\frac{{\text{1 molecule O}}_{2}}{{\text{2 molecules H}}_{2}\text{O}}$, $\frac{{\text{2 molecules H}}_{2}}{{\text{2 molecules H}}_{2}\text{O}}$, and their reciprocals are the conversion factors that can be constructed.
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa04

**Exercise 4.**

What are all the conversion factors that can be constructed from the balanced chemical reaction N<sub>2</sub>(g) + 3H<sub>2</sub>(g) → 2NH<sub>3</sub>(g)?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa05

**Exercise 5.**

Given the chemical equation

$\text{Na(s) + H}_{2}\text{O(}\ell{}\text{) }\rightarrow{}\text{ NaOH(aq) + H}_{2}\text{(g)}$

a. Balance the equation.
b. How many molecules of H<sub>2</sub> are produced when 332 atoms of Na react?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa05
:label: sol:ball-ch05-s01-qs01-qd01-qa05
:class: dropdown

a. 2Na(s) + 2H<sub>2</sub>O(ℓ) → 2NaOH(aq) + H<sub>2</sub>(g)
b. 166 molecules
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa06

**Exercise 6.**

Given the chemical equation

$\text{S(s) + O}_{2}\text{(g) }\rightarrow{}\text{ SO}_{3}\text{(g)}$

a. Balance the equation.
b. How many molecules of O<sub>2</sub> are needed when 38 atoms of S react?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa07

**Exercise 7.**

For the balanced chemical equation

$\text{6H}^{+}\text{(aq) + 2MnO}_{4}^{-}\text{(aq) + 5H}_{2}\text{O}_{2}\text{(}\ell{}\text{) }\rightarrow{}\text{ 2Mn}^{2+}\text{(aq) + 5O}_{2}\text{(g) + 8H}_{2}\text{O(}\ell{}\text{)}$

how many molecules of H<sub>2</sub>O are produced when 75 molecules of H<sub>2</sub>O<sub>2</sub> react?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa07
:label: sol:ball-ch05-s01-qs01-qd01-qa07
:class: dropdown

120 molecules
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa08

**Exercise 8.**

For the balanced chemical reaction

$\text{2C}_{6}\text{H}_{6}\text{(}\ell{}\text{) + 15O}_{2}\text{(g) }\rightarrow{}\text{ 12CO}_{2}\text{(g) + 6H}_{2}\text{O(}\ell{}\text{)}$

how many molecules of CO<sub>2</sub> are produced when 56 molecules of C<sub>6</sub>H<sub>6</sub> react?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa09

**Exercise 9.**

Given the balanced chemical equation

$\text{Fe}_{2}\text{O}_{3}\text{(s) + 3SO}_{3}\text{(g) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}$

how many molecules of Fe<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> are produced if 321 atoms of S are reacted?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa09
:label: sol:ball-ch05-s01-qs01-qd01-qa09
:class: dropdown

107 molecules
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa10

**Exercise 10.**

For the balanced chemical equation

$\text{CuO(s) + H}_{2}\text{S(g) }\rightarrow{}\text{ CuS + H}_{2}\text{O(}\ell{}\text{)}$

how many molecules of CuS are formed if 9,044 atoms of H react?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa11

**Exercise 11.**

For the balanced chemical equation

$\text{Fe}_{2}\text{O}_{3}\text{(s) + 3SO}_{3}\text{(g) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}$

suppose we need to make 145,000 molecules of Fe<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub>. How many molecules of SO<sub>3</sub> do we need?
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa11
:label: sol:ball-ch05-s01-qs01-qd01-qa11
:class: dropdown

435,000 molecules
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa12

**Exercise 12.**

One way to make sulfur hexafluoride is to react thioformaldehyde, CH<sub>2</sub>S, with elemental fluorine:

$\text{CH}_{2}\text{S + 6F}_{2}\text{ }\rightarrow{}\text{ CF}_{4}\text{ + 2HF + SF}_{6}$

If 45,750 molecules of SF<sub>6</sub> are needed, how many molecules of F<sub>2</sub> are required?
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa13

**Exercise 13.**

Construct the three independent conversion factors possible for these two reactions:

a. 2H<sub>2</sub> + O<sub>2</sub> → 2H<sub>2</sub>O
b. H<sub>2</sub> + O<sub>2</sub> → H<sub>2</sub>O<sub>2</sub>

Why are the ratios between H<sub>2</sub> and O<sub>2</sub> different?

The conversion factors are different because the stoichiometries of the balanced chemical reactions are different.
```

```{solution} ex:ball-ch05-s01-qs01-qd01-qa13
:label: sol:ball-ch05-s01-qs01-qd01-qa13
:class: dropdown

a. $\frac{{\text{2 molecules H}}_{2}}{{\text{1 molecule O}}_{2}}$, $\frac{{\text{1 molecule O}}_{2}}{{\text{2 molecules H}}_{2}\text{O}}$, and $\frac{{\text{2 molecules H}}_{2}}{{\text{2 molecules H}}_{2}\text{O}}$
b. $\frac{{\text{1 molecule H}}_{2}}{{\text{1 molecule O}}_{2}}$, $\frac{{\text{1 molecule O}}_{2}}{{\text{1 molecule H}}_{2}{\text{O}}_{2}}$, and $\frac{{\text{1 molecule H}}_{2}}{{\text{1 molecule H}}_{2}{\text{O}}_{2}}$
```

```{exercise}
:label: ex:ball-ch05-s01-qs01-qd01-qa14

**Exercise 14.**

Construct the three independent conversion factors possible for these two reactions:

a. 2Na + Cl<sub>2</sub> → 2NaCl
b. 4Na + 2Cl<sub>2</sub> → 4NaCl

What similarities, if any, exist in the conversion factors from these two reactions?
```
