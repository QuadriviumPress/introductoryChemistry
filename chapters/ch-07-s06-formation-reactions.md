---
title: "7.6 Formation Reactions"
---

(sec:ch07:s06)=

# 7.6 Formation Reactions

```{note} Learning Objectives

1. Define a *formation reaction* and be able to recognize one.
2. Use enthalpies of formation to determine the enthalpy of reaction.
```

Hess’s law allows us to construct new chemical reactions and predict what their enthalpies of reaction will be. This is a very useful tool because now we don’t have to measure the enthalpy changes of every possible reaction. We need measure only the enthalpy changes of certain benchmark reactions and then use these reactions to algebraically construct any possible reaction and combine the enthalpies of the benchmark reactions accordingly.

But what are the benchmark reactions? We need to have some agreed-on sets of reactions that provide the central data for any thermochemical equation.

**Formation reactions** (*A chemical reaction that forms one mole of a substance from its constituent elements in their standard states.*) are chemical reactions that form one mole of a substance from its constituent elements in their standard states. By *standard states* we mean as a diatomic molecule if that is how the element exists and the proper phase at normal temperatures (typically room temperature). The product is one mole of substance, which may require that coefficients on the reactant side be fractional (a change from our normal insistence that all coefficients be whole numbers). For example, the formation reaction for methane (CH<sub>4</sub>) is

$$
\text{C(s) + 2H}_{2}\text{(g) }\rightarrow{}\text{ CH}_{4}\text{(g)}
$$

The formation reaction for carbon dioxide (CO<sub>2</sub>) is

$$
\text{C(s) + O}_{2}\text{(g) }\rightarrow{}\text{ CO}_{2}\text{(g)}
$$

In both cases, one of the elements is a diatomic molecule because that is the standard state for that particular element. The formation reaction for H<sub>2</sub>O—

$$
\text{2H}_{2}\text{(g) + O}_{2}\text{(g) }\rightarrow{}\text{ 2H}_{2}\text{O(}\ell{}\text{)}
$$

—is *not* in a standard state because the coefficient on the product is 2; for a proper formation reaction, only one mole of product is formed. Thus, we have to divide all coefficients by 2:

$$
\text{H}_{2}\text{(g) + 1/2O}_{2}\text{(g) }\rightarrow{}\text{ H}_{2}\text{O(}\ell{}\text{)}
$$

On a molecular scale, we are using half of an oxygen molecule, which may be problematic to visualize. However, on a molar level, it implies that we are reacting only half of a mole of oxygen molecules, which should be an easy concept for us to understand.

```{exercise}
:label: ex:ball-ch07-s06-n02

**Example 11**

Which of the following are proper formation reactions?

1. H<sub>2</sub>(g) + Cl<sub>2</sub>(g) → 2HCl(g)
2. Si(s) + 2F<sub>2</sub>(g) → SiF<sub>4</sub>(g)
3. CaO(s) + CO<sub>2</sub> → CaCO<sub>3</sub>(s)
```

```{solution} ex:ball-ch07-s06-n02
:label: sol:ball-ch07-s06-n02
:class: dropdown

1. In this reaction, two moles of product are produced, so this is not a proper formation reaction.
2. In this reaction, one mole of a substance is produced from its elements in their standard states, so this is a proper formation reaction.
3. One mole of a substance is produced, but it is produced from two other compounds, not its elements. So this is not a proper formation reaction.
```

```{exercise}
:label: ex:ball-ch07-s06-n02-ty2

**Test Yourself**

Is this a proper formation reaction? Explain why or why not.

$\text{2Fe(s) + 3P(s) + 12O(g) }\rightarrow{}\text{ Fe}_{2}\text{(PO}_{4}\text{)}_{3}\text{(s)}$
```

```{solution} ex:ball-ch07-s06-n02-ty2
:label: sol:ball-ch07-s06-n02-ty2
:class: dropdown

This is not a proper formation reaction because oxygen is not written as a diatomic molecule.
```

Given the formula of any substance, you should be able to write the proper formation reaction for that substance.

```{exercise}
:label: ex:ball-ch07-s06-n03

**Example 12**

Write formation reactions for each of the following.

1. FeO(s)
2. C<sub>2</sub>H<sub>6</sub>(g)
```

```{solution} ex:ball-ch07-s06-n03
:label: sol:ball-ch07-s06-n03
:class: dropdown

In both cases, there is one mole of the substance as product, and the coefficients of the reactants may have to be fractional to balance the reaction.

1. Fe(s) + 1/2O<sub>2</sub>(g) → FeO(s)
2. 2C(s) + 3H<sub>2</sub>(g) → C<sub>2</sub>H<sub>6</sub>(g)
```

```{exercise}
:label: ex:ball-ch07-s06-n03-ty2

**Test Yourself**

Write the equation for the formation of CaCO<sub>3</sub>(s).
```

```{solution} ex:ball-ch07-s06-n03-ty2
:label: sol:ball-ch07-s06-n03-ty2
:class: dropdown

$\text{Ca(s) + C(s) + 3/2O}_{2}\text{(g) }\rightarrow{}\text{ CaCO}_{3}\text{(s)}$
```

The enthalpy change for a formation reaction is called the **enthalpy of formation** (*The enthalpy change for a formation reaction; denoted $\Delta{}{H}_{\text{f}}$.*) and is given the symbol Δ*H*<sub>f</sub>. The subscript *f* is the clue that the reaction of interest is a formation reaction. Thus, for the formation of FeO(s),

$$
\text{Fe(s)}+\frac{1}{2}{\text{O}}_{\text{2}}\text{(g)}\rightarrow{}\text{FeO(s)}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\Delta{}H\equiv{}\Delta{}{H}_{\text{f}}=-\text{272 kJ/mol}
$$

Note that now we are using kJ/mol as the unit because it is understood that the enthalpy change is for one mole of substance. Note, too, by definition, that the enthalpy of formation of an element is exactly zero because making an element from an element is no change. For example,

$$
\text{H}_{2}\text{(g) }\rightarrow{}\text{ H}_{2}\text{(g)     }\Delta{}H_{\text{f}}\text{ = 0}
$$

Formation reactions and their enthalpies are important because *these are the thermochemical data that are tabulated* for any chemical reaction. {ref}`Table 7.2 "Enthalpies of Formation for Various Substances" <tbl:ch07:s06:t01>` lists some enthalpies of formation for a variety of substances; in some cases, however, phases can be important (e.g., for H<sub>2</sub>O).

It is easy to show that any general chemical equation can be written in terms of the formation reactions of its reactants and products, some of them reversed (which means the sign must change in accordance with Hess’s law). For example, consider

$$
\text{2NO}_{2}\text{(g) }\rightarrow{}\text{ N}_{2}\text{O}_{4}\text{(g)}
$$

We can write it in terms of the (reverse) formation reaction of NO<sub>2</sub> and the formation reaction of N<sub>2</sub>O<sub>4</sub>:

```{figure} ../images/figures/8a0b798c104aff2c5de827cb54992b4a.jpg
:label: fig:fwk:ball:eq07:003
:alt: "7.6 Formation Reactions"
:align: center
:width: 85%

7.6 Formation Reactions
```

We must multiply the first reaction by 2 to get the correct overall balanced equation. We are simply using Hess’s law in combining the Δ*H*<sub>f</sub> values of the formation reactions.

```{table} Enthalpies of Formation for Various Substances
:label: tbl:ch07:s06:t01

| Compound | Δ*H*<sub>f</sub> (kJ/mol) | Compound | Δ*H*<sub>f</sub> (kJ/mol) | Compound | Δ*H*<sub>f</sub> (kJ/mol) | Compound | Δ*H*<sub>f</sub> (kJ/mol) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ag(s) | 0 | Ca(s) | 0 | Hg<sub>2</sub>Cl<sub>2</sub>(s) | −265.37 | NaHCO<sub>3</sub>(s) | −950.81 |
| AgBr(s) | −100.37 | CaCl<sub>2</sub>(s) | −795.80 | I<sub>2</sub>(s) | 0 | NaN<sub>3</sub>(s) | 21.71 |
| AgCl(s) | −127.01 | CaCO<sub>3</sub>(s, arag) | −1,207.1 | K(s) | 0 | Na<sub>2</sub>CO<sub>3</sub>(s) | −1,130.77 |
| Al(s) | 0 | CaCO<sub>3</sub>(s, calc) | −1,206.9 | KBr(s) | −393.8 | Na<sub>2</sub>O(s) | −417.98 |
| Al<sub>2</sub>O<sub>3</sub>(s) | −1,675.7 | Cl<sub>2</sub>(g) | 0 | KCl(s) | −436.5 | Na<sub>2</sub>SO<sub>4</sub>(s) | −1,387.1 |
| Ar(g) | 0 | Cr(s) | 0 | KF(s) | −567.3 | Ne(g) | 0 |
| Au(s) | 0 | Cr<sub>2</sub>O<sub>3</sub>(s) | −1,134.70 | KI(s) | −327.9 | Ni(s) | 0 |
| BaSO<sub>4</sub>(s) | −1,473.19 | Cs(s) | 0 | Li(s) | 0 | O<sub>2</sub>(g) | 0 |
| Br<sub>2</sub>(ℓ) | 0 | Cu(s) | 0 | LiBr(s) | −351.2 | O<sub>3</sub>(g) | 142.67 |
| C(s, dia) | 1.897 | F<sub>2</sub>(g) | 0 | LiCl(s) | −408.27 | PH<sub>3</sub>(g) | 5.4 |
| C(s, gra) | 0 | Fe(s) | 0 | LiF(s) | −616.0 | Pb(s) | 0 |
| CCl<sub>4</sub>(ℓ) | −128.4 | Fe<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub>(s) | −2,583.00 | LiI(s) | −270.4 | PbCl<sub>2</sub>(s) | −359.41 |
| CH<sub>2</sub>O(g) | −115.90 | Fe<sub>2</sub>O<sub>3</sub>(s) | −825.5 | Mg(s) | 0 | PbO<sub>2</sub>(s) | −274.47 |
| CH<sub>3</sub>COOH(ℓ) | −483.52 | Ga(s) | 0 | MgO(s) | −601.60 | PbSO<sub>4</sub>(s) | −919.97 |
| CH<sub>3</sub>OH(ℓ) | −238.4 | HBr(g) | −36.29 | NH<sub>3</sub>(g) | −45.94 | Pt(s) | 0 |
| CH<sub>4</sub>(g) | −74.87 | HCl(g) | −92.31 | NO(g) | 90.29 | S(s) | 0 |
| CO(g) | −110.5 | HF(g) | −273.30 | NO<sub>2</sub>(g) | 33.10 | SO<sub>2</sub>(g) | −296.81 |
| CO<sub>2</sub>(g) | −393.51 | HI(g) | 26.5 | N<sub>2</sub>(g) | 0 | SO<sub>3</sub>(g) | −395.77 |
| C<sub>2</sub>H<sub>5</sub>OH(ℓ) | −277.0 | HNO<sub>2</sub>(g) | −76.73 | N<sub>2</sub>O(g) | 82.05 | SO<sub>3</sub>(ℓ) | −438 |
| C<sub>2</sub>H<sub>6</sub>(g) | −83.8 | HNO<sub>3</sub>(g) | −134.31 | N<sub>2</sub>O<sub>4</sub>(g) | 9.08 | Si(s) | 0 |
| C<sub>6</sub>H<sub>12</sub>(ℓ) | −157.7 | H<sub>2</sub>(g) | 0 | N<sub>2</sub>O<sub>5</sub>(g) | 11.30 | U(s) | 0 |
| C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>(s) | −1277 | H<sub>2</sub>O(g) | −241.8 | Na(s) | 0 | UF<sub>6</sub>(s) | −2,197.0 |
| C<sub>6</sub>H<sub>14</sub>(ℓ) | −198.7 | H<sub>2</sub>O(ℓ) | −285.83 | NaBr(s) | −361.1 | UO<sub>2</sub>(s) | −1,085.0 |
| C<sub>6</sub>H<sub>5</sub>CH<sub>3</sub>(ℓ) | 12.0 | H<sub>2</sub>O(s) | −292.72 | NaCl(s) | −411.2 | Xe(g) | 0 |
| C<sub>6</sub>H<sub>6</sub>(ℓ) | 48.95 | He(g) | 0 | NaF(s) | −576.6 | Zn(s) | 0 |
| C<sub>10</sub>H<sub>8</sub>(s) | 77.0 | Hg(ℓ) | 0 | NaI(s) | −287.8 | ZnCl<sub>2</sub>(s) | −415.05 |
| C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(s) | −2,221.2 |   |   |   |   |   |   |
```

```{exercise}
:label: ex:ball-ch07-s06-n04

**Example 13**

Show that the reaction

$\text{Fe}_{2}\text{O}_{3}\text{(s) + 3SO}_{3}\text{(g) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}\text{(s)}$

can be written as a combination of formation reactions.
```

```{solution} ex:ball-ch07-s06-n04
:label: sol:ball-ch07-s06-n04
:class: dropdown

There will be three formation reactions. The one for the products will be written as a formation reaction, while the ones for the reactants will be written in reverse. Furthermore, the formation reaction for SO<sub>3</sub> will be multiplied by 3 because there are three moles of SO<sub>3</sub> in the balanced chemical equation. The formation reactions are as follows:

$$
{\text{Fe}}_{\text{2}}{\text{O}}_{\text{3}}\text{(s)}\rightarrow{}\text{2 Fe(s)}+\frac{3}{2}{\text{O}}_{\text{2}}\text{(g)}
$$

$$
\text{3}\times{}[{\text{SO}}_{\text{3}}\text{(g)}\rightarrow{}\text{S(s)}+\frac{3}{2}{\text{O}}_{\text{2}}\text{(g)}]
$$

$\text{2Fe(s) + 3S(s) + 6O}_{2}\text{(g) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}\text{(s)}$

When these three equations are combined and simplified, the overall reaction is

$\text{Fe}_{2}\text{O}_{3}\text{(s) + 3SO}_{3}\text{(s) }\rightarrow{}\text{ Fe}_{2}\text{(SO}_{4}\text{)}_{3}\text{(s)}$
```

```{exercise}
:label: ex:ball-ch07-s06-n04-ty2

**Test Yourself**

Write the formation reactions that will yield

$\text{2SO}_{2}\text{(g) + O}_{2}\text{(g) }\rightarrow{}\text{ 2SO}_{3}\text{(g).}$
```

```{solution} ex:ball-ch07-s06-n04-ty2
:label: sol:ball-ch07-s06-n04-ty2
:class: dropdown

$$
\text{2}\times{}[{\text{SO}}_{\text{2}}\text{(g)}\rightarrow{}\text{S(s)}+{\text{O}}_{\text{2}}\text{(g)}]
$$

$$
\text{2}\times{}[\text{S(s)}+\frac{3}{2}{\text{O}}_{\text{2}}\text{(g)}\rightarrow{}{\text{2SO}}_{\text{3}}\text{(g)}]
$$
```

Now that we have established formation reactions as the major type of thermochemical reaction we will be interested in, do we always need to write all the formation reactions when we want to determine the enthalpy change of any random chemical reaction? No. There is an easier way. You may have noticed in all our examples that we change the signs on all the enthalpies of formation of the reactants, and we don’t change the signs on the enthalpies of formation of the products. We also multiply the enthalpies of formation of any substance by its coefficient—technically, even when it is just 1. This allows us to make the following statement: *the enthalpy change of any chemical reaction is equal to the sum of the enthalpies of formation of the products minus the sum of the enthalpies of formation of the reactants*. In mathematical terms,

$$
\Delta{}{H}_{\text{rxn}}=\sum{}{n}_{\text{p}}\Delta{}{H}_{\text{f,p}}-\sum{}{n}_{\text{r}}\Delta{}{H}_{\text{f,r}}
$$

where *n*<sub>p</sub> and *n*<sub>r</sub> are the number of moles of products and reactants, respectively (even if they are just 1 mol), and Δ*H*<sub>f,p</sub> and Δ*H*<sub>f,r</sub> are the enthalpies of formation of the product and reactant species, respectively. This *products-minus-reactants* scheme is very useful in determining the enthalpy change of any chemical reaction, if the enthalpy of formation data are available. Because the mol units cancel when multiplying the amount by the enthalpy of formation, the enthalpy change of the chemical reaction has units of energy (joules or kilojoules) only.

```{exercise}
:label: ex:ball-ch07-s06-n05

**Example 14**

Use the products-minus-reactants approach to determine the enthalpy of reaction for

$$
\begin{aligned}
 & \text{2HBr(g)} & + & {\text{Cl}}_{\text{2}}\text{(g)} & \rightarrow{} & \text{2HCl(g)} & + & {\text{Br}}_{\text{2}}(\ell{}) &  \\
\Delta{}{H}_{\text{f}} & -\text{36}.\text{3} &  & 0 &  & -\text{92}.\text{3} &  & 0 & \text{kJ/mol}
\end{aligned}
$$
```

```{solution} ex:ball-ch07-s06-n05
:label: sol:ball-ch07-s06-n05
:class: dropdown

The enthalpies of formation are multiplied by the number of moles of each substance in the chemical equation, and the total enthalpy of formation for reactants is subtracted from the total enthalpy of formation of the products:

$$
\begin{aligned}
\Delta{}{H}_{\text{rxn}}=[(\text{2}\text{ mol})(-\text{92}.\text{3 kJ/}\text{ mol})+(\text{1}\text{ mol})(0\text{ kJ/}\text{ mol})] \\
-[(\text{2}\text{ mol})(-\text{36}.\text{3 kJ/}\text{ mol})+(\text{1}\text{ mol})(0\text{ kJ/}\text{ mol})]
\end{aligned}
$$

All the mol units cancel. Multiplying and combining all the values, we get

$\Delta{}H_{\text{rxn}}\text{ = }-\text{112.0 kJ}$
```

```{exercise}
:label: ex:ball-ch07-s06-n05-ty2

**Test Yourself**

What is the enthalpy of reaction for this chemical equation?

$$
\begin{aligned}
 & \text{CO(g)} & + & {\text{H}}_{\text{2}}\text{O}(\ell{}) & \rightarrow{} & {\text{CO}}_{\text{2}}\text{(g)} & + & {\text{H}}_{\text{2}}\text{(g)} &  \\
\Delta{}{H}_{\text{f}} & -\text{11}0.\text{5} &  & -\text{285}.\text{8} &  & -\text{393}.\text{5} &  & 0 & \text{kJ/mol}
\end{aligned}
$$
```

```{solution} ex:ball-ch07-s06-n05-ty2
:label: sol:ball-ch07-s06-n05-ty2
:class: dropdown

+2.8 kJ
```

```{tip} Food and Drink App: Calories and Nutrition

{ref}`Section 7.1 "Energy" <sec:ch07:s01>` mentioned the connection between the calorie unit and nutrition: the calorie is the common unit of energy used in nutrition, but we really consider the kilocalorie (spelled Calorie with a capital C). A daily diet of 2,000 Cal is actually 2,000,000 cal, or over 8,000,000 J, of energy.

Nutritionists typically generalize the Calorie content of foods by separating it into the three main food types: proteins, carbohydrates, and fats. The general rule of thumb is as follows:

| If the food is | It has this energy content |
| --- | --- |
| protein | 4 Cal/g |
| carbohydrate | 4 Cal/g |
| fat | 9 Cal/g |

This table is very useful. Assuming a 2,000 Cal daily diet, if our diet consists solely of proteins and carbohydrates, we need only about 500 g of food for sustenance—a little more than a pound. If our diet consists solely of fats, we need only about 220 g of food—less than a half pound. Of course, most of us have a mixture of proteins, carbohydrates, and fats in our diets. Water has no caloric value in the diet, so any water in the diet is calorically useless. (However, it is important for hydration; also, many forms of water in our diet are highly flavored and sweetened, which bring other nutritional issues to bear.)

When your body works, it uses calories provided by the diet as its energy source. If we eat more calories than our body uses, we gain weight—about 1 lb of weight for every additional 3,500 Cal we ingest. Similarly, if we want to lose weight, we need to expend an extra 3,500 Cal than we ingest to lose 1 lb of weight. No fancy or fad diets are needed; maintaining an ideal body weight is a straightforward matter of thermochemistry—pure and simple.
```

```{important} Key Takeaways

- A formation reaction is the formation of one mole of a substance from its constituent elements.
- Enthalpies of formation are used to determine the enthalpy change of any given reaction.
```

## Exercises

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa01

**Exercise 1.**

Define *formation reaction* and give an example.
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa01
:label: sol:ball-ch07-s06-qs01-qd01-qa01
:class: dropdown

A formation reaction is a reaction that produces one mole of a substance from its elements. Example: C(s) + O<sub>2</sub>(g) → CO<sub>2</sub>(g)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa02

**Exercise 2.**

Explain the importance of formation reactions in thermochemical equations.
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa03

**Exercise 3.**

Which of the following reactions is a formation reaction? If it is not a formation reaction, explain why.

a. H<sub>2</sub>(g) + S(s) → H<sub>2</sub>S(g)
b. 2HBr(g) + Cl<sub>2</sub>(g) → 2HCl(g) + Br<sub>2</sub>(ℓ)
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa03
:label: sol:ball-ch07-s06-qs01-qd01-qa03
:class: dropdown

a. formation reaction
b. It is not the formation of a single substance, so it is not a formation reaction.
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa04

**Exercise 4.**

Which of the following reactions is a formation reaction? If it is not a formation reaction, explain why.

a. Fe(g) + 1/2O<sub>2</sub>(g) → FeO(s)
b. Hg(ℓ) + 1/2O<sub>2</sub>(g) → HgO(s)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa05

**Exercise 5.**

Which of the following reactions is a formation reaction? If it is not a formation reaction, explain why.

a. H<sub>2</sub>(g) + S(s) + 2O<sub>2</sub>(g) → H<sub>2</sub>SO<sub>4</sub>(ℓ)
b. C<sub>3</sub>H<sub>8</sub>(g) + 5O<sub>2</sub>(g) → 3CO<sub>2</sub>(g) + 4H<sub>2</sub>O(ℓ)
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa05
:label: sol:ball-ch07-s06-qs01-qd01-qa05
:class: dropdown

a. formation reaction
b. It is not the formation of a single substance, so it is not a formation reaction.
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa06

**Exercise 6.**

Which of the following reactions is a formation reaction? If it is not a formation reaction, explain why.

a. Zn(s) + 2HCl(aq) → ZnCl<sub>2</sub>(aq) + H<sub>2</sub>(g)
b. 2Na(s) + C(s) + 3/2O<sub>2</sub>(g) → Na<sub>2</sub>CO<sub>3</sub>(s)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa07

**Exercise 7.**

Write a proper formation reaction for each substance.

a. H<sub>3</sub>PO<sub>4</sub>(s)
b. Na<sub>2</sub>O(s)
c. C<sub>3</sub>H<sub>7</sub>OH(ℓ)
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa07
:label: sol:ball-ch07-s06-qs01-qd01-qa07
:class: dropdown

a. 3/2H<sub>2</sub>(g) + P(s) + 2O<sub>2</sub>(g) → H<sub>3</sub>PO<sub>4</sub>(s)
b. 2Na(s) + 1/2O<sub>2</sub>(g) → Na<sub>2</sub>O(s)
c. 3C(s) + 1/2O<sub>2</sub>(g) + 4H<sub>2</sub>(g) → C<sub>3</sub>H<sub>7</sub>OH(ℓ)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa08

**Exercise 8.**

Write a proper formation reaction for each substance.

a. N<sub>2</sub>O<sub>5</sub>(g)
b. BaSO<sub>4</sub>(s)
c. Fe(OH)<sub>3</sub>(s)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa09

**Exercise 9.**

Write a proper formation reaction for each substance.

a. C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(s)
b. Zn(NO<sub>3</sub>)<sub>2</sub>(s)
c. Al(OH)<sub>3</sub>(s)
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa09
:label: sol:ball-ch07-s06-qs01-qd01-qa09
:class: dropdown

a. 12C(s) + 11H<sub>2</sub>(g) + 11/2O<sub>2</sub>(g) → C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(s)
b. Zn(s) + N<sub>2</sub>(g) + 3O<sub>2</sub>(g) → Zn(NO<sub>3</sub>)<sub>2</sub>
c. Al(s) + 3/2O<sub>2</sub>(g) + 3/2H<sub>2</sub>(g) → Al(OH)<sub>3</sub>(s)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa10

**Exercise 10.**

Write a proper formation reaction for each substance.

a. O<sub>3</sub>(g)
b. Na<sub>2</sub>O<sub>2</sub>(s)
c. PCl<sub>5</sub>(g)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa11

**Exercise 11.**

Write this reaction in terms of formation reactions.

$\text{MgCO}_{3}\text{(s) }\rightarrow{}\text{ MgO(s) + CO}_{2}\text{(g)}$
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa11
:label: sol:ball-ch07-s06-qs01-qd01-qa11
:class: dropdown

MgCO<sub>3</sub>(s) → Mg(s) + C(s) + 3/2O<sub>2</sub>(g)

Mg(s) + 1/2O<sub>2</sub>(g) → MgO(s)

C(s) + O<sub>2</sub>(g) → CO<sub>2</sub>(g)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa12

**Exercise 12.**

Write this reaction in terms of formation reactions.

$\text{2NO + 4NO}_{2}\text{ }\rightarrow{}\text{ 2N}_{2}\text{O}_{5}\text{ + N}_{2}$
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa13

**Exercise 13.**

Write this reaction in terms of formation reactions.

$\text{2CuCl(s) }\rightarrow{}\text{ Cu(s) + CuCl}_{2}\text{(s)}$
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa13
:label: sol:ball-ch07-s06-qs01-qd01-qa13
:class: dropdown

2 × [CuCl(s) → Cu(s) + 1/2Cl<sub>2</sub>(g)]

Cu(s) → Cu(s)

Cu(s) + Cl<sub>2</sub>(g) → CuCl<sub>2</sub>(s)
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa14

**Exercise 14.**

Write this reaction in terms of formation reactions.

$\text{SiH}_{4}\text{ + 4F}_{2}\text{ }\rightarrow{}\text{ SiF}_{4}\text{ + 4HF}$
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa15

**Exercise 15.**

Determine the enthalpy change of this reaction. Data can be found in {ref}`Table 7.2 "Enthalpies of Formation for Various Substances" <tbl:ch07:s06:t01>`.

$\text{CH}_{2}\text{O(g) + O}_{2}\text{ }\rightarrow{}\text{ CO}_{2}\text{(g) + H}_{2}\text{O(}\ell{}\text{)}$
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa15
:label: sol:ball-ch07-s06-qs01-qd01-qa15
:class: dropdown

Δ*H* = −563.44 kJ
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa16

**Exercise 16.**

Determine the enthalpy change of this reaction. Data can be found in {ref}`Table 7.2 "Enthalpies of Formation for Various Substances" <tbl:ch07:s06:t01>`.

$\text{2AgBr(s) + Cl}_{2}\text{(g) }\rightarrow{}\text{ 2AgCl(s) + Br}_{2}\text{(}\ell{}\text{)}$
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa17

**Exercise 17.**

Determine the enthalpy change of this reaction. Data can be found in {ref}`Table 7.2 "Enthalpies of Formation for Various Substances" <tbl:ch07:s06:t01>`.

$\text{Mg(s) + N}_{2}\text{O}_{5}\text{(g) }\rightarrow{}\text{ MgO(s) + 2NO}_{2}\text{(g)}$
```

```{solution} ex:ball-ch07-s06-qs01-qd01-qa17
:label: sol:ball-ch07-s06-qs01-qd01-qa17
:class: dropdown

Δ*H* = −546.7 kJ
```

```{exercise}
:label: ex:ball-ch07-s06-qs01-qd01-qa18

**Exercise 18.**

Determine the enthalpy change of this reaction. Data can be found in {ref}`Table 7.2 "Enthalpies of Formation for Various Substances" <tbl:ch07:s06:t01>`.

$\text{2C}_{6}\text{H}_{6}\text{(}\ell{}\text{) + 15O}_{2}\text{(g) }\rightarrow{}\text{ 12CO}_{2}\text{(g) + 6H}_{2}\text{O(}\ell{}\text{)}$
```
