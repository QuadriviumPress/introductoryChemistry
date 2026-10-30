---
title: "13.4 Calculating Equilibrium Constant Values"
---

(sec:ch13:s04)=

# 13.4 Calculating Equilibrium Constant Values

```{note} Learning Objective

1. Calculate equilibrium concentrations from the values of the initial amounts and the *K*<sub>eq</sub>.
```

There are some circumstances in which, given some initial amounts and the *K*<sub>eq</sub>, you will have to determine the concentrations of all species when equilibrium is achieved. Such calculations are not difficult to do, especially if a consistent approach is applied. We will consider such an approach here.

Suppose we have this simple equilibrium. Its associated *K*<sub>eq</sub> is 4.0, and the initial concentration of each reactant is 1.0 M:

$$
\begin{aligned}
{\text{H}}_{\text{2}}\text{(g)} & + & {\text{Cl}}_{\text{2}}\text{(g)} & \rightleftarrows{} & \text{2HCl(g)} & \,\, & {K}_{\text{eq}}=4.0 \\
\text{1}\text{.0 M} &  & \text{1}\text{.0 M} &  &  &  & 
\end{aligned}
$$

Because we have concentrations for the reactants but not the products, we presume that the reaction will proceed in the forward direction to make products. But by how much will it proceed? We don’t know, so let us assign it a variable. Let us assume that *x* M H<sub>2</sub> reacts as the reaction goes to equilibrium. This means that at equilibrium, we have (1.0 − *x*) M H<sub>2</sub> left over.

According to the balanced chemical equation, H<sub>2</sub> and Cl<sub>2</sub> react in a 1:1 ratio. How do we know that? The coefficients of these two species in the balanced chemical equation are 1 (unwritten, of course). This means that if *x* M H<sub>2</sub> reacts, *x* M Cl<sub>2</sub> reacts as well. If we start with 1.0 M Cl<sub>2</sub> at the beginning and we react *x* M, we have (1.0 − *x*) M Cl<sub>2</sub> left at equilibrium.

How much HCl is made? We start with zero, but we also see that 2 mol of HCl are made for every mole of H<sub>2</sub> (or Cl<sub>2</sub>) that reacts (from the coefficients in the balanced chemical equation), so if we lose *x* M H<sub>2</sub>, we gain 2*x* M HCl. So now we know the equilibrium concentrations of our species:

$$
\begin{aligned}
{\text{H}}_{\text{2}}\text{(g)} & + & {\text{Cl}}_{\text{2}}\text{(g)} & \rightleftarrows{} & \text{2HCl(g)} & \,\, & {K}_{\text{eq}}=4.0 \\
\text{(}1.0-x\text{)}\,\text{M} &  & \text{(}1.0-x\text{)}\,\text{M} &  & 2x\,\text{M} &  & 
\end{aligned}
$$

We can substitute these concentrations into the *K*<sub>eq</sub> expression for this reaction and combine it with the known value of *K*<sub>eq</sub>:

$$
{K}_{\text{eq}}=\frac{{[\text{HCl]}}^{2}}{[{\text{H}}_{2}][{\text{Cl}}_{2}]}=\frac{{(2x)}^{2}}{(1-x)(1-x)}=4.0
$$

This is an equation in one variable, so we should be able to solve for the unknown value. This expression may look formidable, but first we can simplify the denominator and write it as a perfect square as well:

$$
\frac{{(2x)}^{2}}{{(1-x)}^{2}}=4.0
$$

The fraction is a perfect square, as is the 4.0 on the right. So we can take the square root of both sides:

$$
\frac{2x}{1-x}=2.0
$$

Now we rearrange and solve (be sure you can follow each step):

$$
\begin{aligned}
2x=2.0-2.0x \\
4x=2.0 \\
x=0.50
\end{aligned}
$$

Now we have to remind ourselves what *x* is—the amount of H<sub>2</sub> and Cl<sub>2</sub> that reacted—and 2*x* is the equilibrium [HCl]. To determine the equilibrium concentrations, we need to go back and evaluate the expressions 1 − *x* and 2*x* to get the equilibrium concentrations of our species:

$$
\text{1.0 }-\text{ }x\text{ = 1.0 }-\text{ 0.50 = 0.50 M = [H}_{2}\text{] = [Cl}_{2}\text{]}
$$

$$
\text{2}x\text{ = 2(0.50) = 1.0 M = [HCl]}
$$

The units are assumed to be molarity. To check, we simply substitute these concentrations and verify that we get the numerical value of the *K*<sub>eq</sub>, in this case 4.0:

$$
\frac{{(1.0)}^{2}}{(0.50)(0.50)}=4.0\,
$$

We formalize this process by introducing the ICE chart, where ICE stands for initial, change, and equilibrium. The initial values go in the first row of the chart. The change values, usually algebraic expressions because we do not yet know their exact numerical values, go in the next row. However, the change values *must* be in the proper stoichiometric ratio as indicated by the balanced chemical equation. Finally, the equilibrium expressions in the last row are a combination of the initial value and the change value for each species. The expressions in the equilibrium row are substituted into the *K*<sub>eq</sub> expression, which yields an algebraic equation that we try to solve.

The ICE chart for the above example would look like this:

|   | H<sub>2</sub>(g) | + | Cl<sub>2</sub>(g) | $\rightleftarrows{}$ | 2HCl(g) | *K*<sub>eq</sub> = 4.0 |
| --- | --- | --- | --- | --- | --- | --- |
| I | 1.0 |   | 1.0 |   | 0 |   |
| C | −*x* |   | −*x* |   | +2*x* |   |
| E | 1.0 − *x* |   | 1.0 − *x* |   | +2*x* |   |

Substituting the last row into the expression for the *K*<sub>eq</sub> yields

$$
{K}_{\text{eq}}=\frac{{[\text{HCl]}}^{2}}{[{\text{H}}_{2}][{\text{Cl}}_{2}]}=\frac{{(2x)}^{2}}{(1-x)(1-x)}=4.0
$$

which, of course, is the same expression we have already solved and yields the same answers for the equilibrium concentrations. The ICE chart is a more formalized way to do these types of problems. The + sign is included explicitly in the change row of the ICE chart to avoid any confusion.

Sometimes when an ICE chart is set up and the *K*<sub>eq</sub> expression is constructed, a more complex algebraic equation will result. One of the more common equations has an *x*<sup>2</sup> term in it and is called a *quadratic equation*. There will be two values possible for the unknown *x*, and for a quadratic equation with the general formula *ax*<sup>2</sup> + *bx* + *c* = 0 (where *a*, *b*, and *c* are the *coefficients* of the quadratic equation), the two possible values are as follows:

$$
x=\frac{-b\pm{}\sqrt{{b}^{2}-4ac}}{2a}
$$

One value of *x* is the + sign used in the numerator, and the other value of *x* is the − sign used in the numerator. In this case, one value of *x* typically makes no sense as an answer and can be discarded as physically impossible, leaving only one possible value and the resulting set of concentrations. Example 9 illustrates this.

```{exercise}
:label: ex:ball-ch13-s04-n02

**Example 9**

Set up an ICE chart and solve for the equilibrium concentrations in this chemical reaction.

$$
\begin{aligned}
{\text{COI}}_{\text{2}}\text{(g)} \\
0.55\,\text{M}
\end{aligned}\begin{aligned}
\,\rightleftarrows{}\, \\
\,
\end{aligned}\begin{aligned}
\text{CO(g)} \\
0
\end{aligned}\begin{aligned}
+ \\
\,
\end{aligned}\begin{aligned}
{\text{I}}_{\text{2}}\text{(g)} \\
0
\end{aligned}\,\,\,\,\,\,\,\,\,\,\begin{aligned}
{K}_{\text{eq}}=0.00088 \\
\,
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-n02
:label: sol:ball-ch13-s04-n02
:class: dropdown

The ICE chart is set up like this. First, the initial values:

|   | COI<sub>2</sub>(g) | $\rightleftarrows{}$ | CO(g) | + | I<sub>2</sub>(g) |
| --- | --- | --- | --- | --- | --- |
| I | 0.55 |   | 0 |   | 0 |
| C |   |   |   |   |   |
| E |   |   |   |   |   |

Some of the COI<sub>2</sub> will be lost, but how much? We don’t know, so we represent it by the variable *x*. So *x* M COI<sub>2</sub> will be lost, and for each COI<sub>2</sub> that is lost, *x* M CO and *x* M I<sub>2</sub> will be produced. These expressions go into the change row:

|   | COI<sub>2</sub>(g) | $\rightleftarrows{}$ | CO(g) | + | I<sub>2</sub>(g) |
| --- | --- | --- | --- | --- | --- |
| I | 0.55 |   | 0 |   | 0 |
| C | −*x* |   | +*x* |   | +*x* |
| E |   |   |   |   |   |

At equilibrium, the resulting concentrations will be a combination of the initial amount and the changes:

|   | COI<sub>2</sub>(g) | $\rightleftarrows{}$ | CO(g) | + | I<sub>2</sub>(g) |
| --- | --- | --- | --- | --- | --- |
| I | 0.55 |   | 0 |   | 0 |
| C | −*x* |   | +*x* |   | +*x* |
| E | 0.55 − *x* |   | +*x* |   | +*x* |

The expressions in the equilibrium row go into the *K*<sub>eq</sub> expression:

$$
{K}_{\text{eq}}=\frac{[{\text{CO][I}}_{2}]}{[{\text{COI}}_{2}]}=0.00088=\frac{(x)(x)}{(0.55-x)}
$$

We rearrange this into a quadratic equation that equals 0:

$\text{0.000484 }-\text{ 0.00088}x\text{ = }x^{2}$

$x^{2}\text{ + 0.00088}x\text{ }-\text{ 0.000484 = 0}$

Now we use the quadratic equation to solve for the two possible values of *x*:

$$
x=\frac{-0.00088\pm{}\sqrt{{(0.00088)}^{2}-4(1)(-0.000484)}}{2(1)}
$$

Evaluate for both signs in the numerator—first the + sign and then the − sign:

$x\text{ = 0.0216 or }x\text{ = }-\text{0.0224}$

Because *x* is the final concentration of both CO and I<sub>2</sub>, it cannot be negative, so we discount the second numerical answer as impossible. Thus *x* = 0.0216.

Going back to determine the final concentrations using the expressions in the E row of our ICE chart, we have

$\text{[COI}_{2}\text{] = 0.55 }-\text{ }x\text{ = 0.55 }-\text{ 0.0216 = 0.53 M}$

$\text{[CO] = }x\text{ = 0.0216 M}$

$\text{[I}_{2}\text{] = }x\text{ = 0.0216 M}$

You can verify that these numbers are correct by substituting them into the *K*<sub>eq</sub> expression and evaluating and comparing to the known *K*<sub>eq</sub> value.
```

```{exercise}
:label: ex:ball-ch13-s04-n02-ty2

**Test Yourself**

Set up an ICE chart and solve for the equilibrium concentrations in this chemical reaction.

$$
\begin{aligned}
{\text{N}}_{\text{2}}{\text{H}}_{2}\text{(g)} \\
0.0\text{75}\,\text{M}
\end{aligned}\begin{aligned}
\,\rightleftarrows{}\, \\
\,
\end{aligned}\begin{aligned}
{\text{N}}_{\text{2}}\text{(g)} \\
0
\end{aligned}\begin{aligned}
+ \\

\end{aligned}\begin{aligned}
{\text{H}}_{\text{2}}\text{(g)} \\
0
\end{aligned}\,\,\,\,\,\,\,\,\,\,\begin{aligned}
{K}_{\text{eq}}=0.052 \\
\,
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-n02-ty2
:label: sol:ball-ch13-s04-n02-ty2
:class: dropdown

The completed ICE chart is as follows:

|   | N<sub>2</sub>H<sub>2</sub>(g) | $\rightleftarrows{}$ | N<sub>2</sub>(g) | + | H<sub>2</sub>(g) |
| --- | --- | --- | --- | --- | --- |
| I | 0.075 |   | 0 |   | 0 |
| C | −*x* |   | +*x* |   | +*x* |
| E | 0.075 − *x* |   | +*x* |   | +*x* |

Solving for *x* gives the equilibrium concentrations as [N<sub>2</sub>H<sub>2</sub>] = 0.033 M; [N<sub>2</sub>] = 0.042 M; and [H<sub>2</sub>] = 0.042 M
```

```{important} Key Takeaway

- An ICE chart is a convenient way to determine equilibrium concentrations from starting amounts.
```

## Exercises

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa01

**Exercise 1.**

Describe the three parts of an ICE chart.
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa01
:label: sol:ball-ch13-s04-qs01-qd01-qa01
:class: dropdown

I = initial concentrations; C = change in concentrations; E = equilibrium concentrations
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa02

**Exercise 2.**

What is the relationship between the equilibrium row in an ICE chart and the other two rows?
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa03

**Exercise 3.**

Set up (but do not solve) an ICE chart for this reaction, given the initial conditions.

$$
\begin{aligned}
3{\text{O}}_{2}\text{(g)} & \rightleftarrows{} & 2{\text{O}}_{3}\text{(g)} \\
0.075\text{ M} &  & 
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa03
:label: sol:ball-ch13-s04-qs01-qd01-qa03
:class: dropdown

|   | 3O<sub>2</sub> | $\rightleftarrows{}$ | 2O<sub>3</sub> |
| --- | --- | --- | --- |
| I | 0.075 |   | 0 |
| C | −3*x* |   | +2*x* |
| E | 0.075 − 3*x* |   | +2*x* |
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa04

**Exercise 4.**

Set up (but do not solve) an ICE chart for this reaction, given the initial conditions.

$$
\begin{aligned}
{\text{CH}}_{\text{4}}\text{(g)} & + & {\text{2O}}_{\text{2}}\text{(g)} & \rightleftarrows{} & {\text{CO}}_{\text{2}}\text{(g)} & + & {\text{2H}}_{\text{2}}\text{O(g)} \\
0.\text{75}0\,\text{M} &  & 0.\text{45}0\,\text{M} &  &  &  & 
\end{aligned}
$$
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa05

**Exercise 5.**

Given that pure solids and liquids do not appear in *K*<sub>eq</sub> expressions, set up the ICE chart for this reaction, given the initial conditions.

$$
\begin{aligned}
{\text{CH}}_{\text{4}}\text{(g)} & + & {\text{2O}}_{\text{2}}\text{(g)} & \rightleftarrows{} & {\text{CO}}_{\text{2}}(\text{g}) & + & {\text{2H}}_{\text{2}}\text{O(}\ell{}\text{)} \\
0.0060\,\text{M} &  & 0.05\text{5}\,\text{M} &  &  &  & 
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa05
:label: sol:ball-ch13-s04-qs01-qd01-qa05
:class: dropdown

|   | CH<sub>4</sub> | + | 2O<sub>2</sub> | $\rightleftarrows{}$ | CO<sub>2</sub> | + | 2H<sub>2</sub>O |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I | 0.0060 |   | 0.055 |   | 0 |   | 0 |
| C | −*x* |   | −2*x* |   | +*x* |   | — |
| E | 0.0060 − *x* |   | 0.055 − 2*x* |   | +*x* |   | — |
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa06

**Exercise 6.**

Given that pure solids and liquids do not appear in *K*<sub>eq</sub> expressions, set up the ICE chart for this reaction, given the initial conditions.

$$
\begin{aligned}
{\text{N}}_{\text{2}}{\text{H}}_{\text{4}}(\ell{}) & + & {\text{O}}_{\text{2}}(\text{g}) & \rightleftarrows{} & {\text{N}}_{\text{2}}\text{(g)} & + & {\text{2H}}_{\text{2}}\text{O}(\ell{}) \\
2.33\,\text{M} &  & 1.09\,\text{M} &  &  &  & 
\end{aligned}
$$
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa07

**Exercise 7.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
\text{HCN(g)} \\
2.00\,\text{M}
\end{aligned}\begin{aligned}
\,\rightleftarrows{}\, \\
\,
\end{aligned}\begin{aligned}
\text{HNC(g)} \\
\,
\end{aligned}\,\,\,\,\,\,\,\,\,\,\begin{aligned}
{K}_{\text{eq}}=4.50 \\
\,
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa07
:label: sol:ball-ch13-s04-qs01-qd01-qa07
:class: dropdown

[HCN] = 0.364 M; [HNC] = 1.64 M
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa08

**Exercise 8.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
{\text{IF}}_{\text{3}}\text{(g)} & + & {\text{F}}_{\text{2}}\text{(g)} & \rightleftarrows{} & {\text{IF}}_{\text{5}}\text{(g)} & \,\, & {K}_{\text{eq}}=7.59 \\
1.0\,\text{M} &  & 0.50\,\text{M} &  &  &  & 
\end{aligned}
$$
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa09

**Exercise 9.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
{\text{N}}_{\text{2}}{\text{O}}_{3}(\text{g}) \\
0.0663\,\text{M}
\end{aligned}\begin{aligned}
\rightleftarrows{}\, \\
\,
\end{aligned}\begin{aligned}
\text{NO(g)} \\
\,
\end{aligned}\begin{aligned}
+ \\
\,
\end{aligned}\begin{aligned}
{\text{NO}}_{\text{2}}\text{(g)} \\
\,
\end{aligned}\,\,\,\,\,\,\,\,\,\,\begin{aligned}
{K}_{\text{eq}}=2.50 \\
\,
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa09
:label: sol:ball-ch13-s04-qs01-qd01-qa09
:class: dropdown

[N<sub>2</sub>O<sub>3</sub>] = 0.0017 M; [NO] = [NO<sub>2</sub>] = 0.0646 M
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa10

**Exercise 10.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
\text{CO(g)} & + & {\text{H}}_{\text{2}}\text{O(g)} & \rightleftarrows{} & {\text{CO}}_{\text{2}}\text{(g)} & + & {\text{H}}_{\text{2}}\text{(g)} & \,\, & {K}_{\text{eq}}=16.0 \\
0.750\,\text{M} &  & 0.750\,\text{M} &  &  &  &  &  & 
\end{aligned}
$$
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa11

**Exercise 11.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
{\text{H}}_{\text{2}}\text{S(g)} \\
0.882\,\text{M}
\end{aligned}\begin{aligned}
\rightleftarrows{}\, \\
\,
\end{aligned}\begin{aligned}
{\text{H}}_{\text{2}}\text{(g)} \\
\,
\end{aligned}\begin{aligned}
+ \\
\,
\end{aligned}\begin{aligned}
\text{S(s)} \\
\,
\end{aligned}\,\,\,\,\,\,\,\,\,\,\begin{aligned}
{K}_{\text{eq}}=0.055 \\
\,
\end{aligned}
$$
```

```{solution} ex:ball-ch13-s04-qs01-qd01-qa11
:label: sol:ball-ch13-s04-qs01-qd01-qa11
:class: dropdown

[H<sub>2</sub>S] = 0.836 M; [H<sub>2</sub>] = 0.046 M
```

```{exercise}
:label: ex:ball-ch13-s04-qs01-qd01-qa12

**Exercise 12.**

Determine the equilibrium concentrations for this chemical reaction with the given *K*<sub>eq</sub>.

$$
\begin{aligned}
\text{2AgCl(s)} & + & {\text{F}}_{\text{2}}\text{(g)} & \rightleftarrows{} & \text{2AgF(s)} & + & {\text{Cl}}_{\text{2}}\text{(g)} & \,\, & {K}_{\text{eq}}=1.2\times{}{10}^{2} \\
 &  & 1.99\text{M} &  &  &  &  &  & 
\end{aligned}
$$
```
