---
title: "12.6 The pH Scale"
---

(sec:ch12:s06)=

# 12.6 The pH Scale

```{note} Learning Objectives

1. Define *pH*.
2. Determine the pH of acidic and basic solutions.
```

As we have seen, [H<sup>+</sup>] and [OH<sup>−</sup>] values can be markedly different from one aqueous solution to another. So chemists defined a new scale that succinctly indicates the concentrations of either of these two ions.

**pH** (*The negative logarithm of the hydrogen ion concentration.*) is a logarithmic function of [H<sup>+</sup>]:

$$
\text{pH = }-\text{log[H}^{+}\text{]}
$$

pH is usually (but not always) between 0 and 14. Knowing the dependence of pH on [H<sup>+</sup>], we can summarize as follows:

- If pH &lt; 7, then the solution is acidic.
- If pH = 7, then the solution is neutral.
- If pH > 7, then the solution is basic.

This is known as the **pH scale** (*The range of values from 0 to 14 that describes the acidity or basicity of a solution.*). You can use pH to make a quick determination whether a given aqueous solution is acidic, basic, or neutral.

```{exercise}
:label: ex:ball-ch12-s06-n02

**Example 12**

Label each solution as acidic, basic, or neutral based only on the stated pH.

1. milk of magnesia, pH = 10.5
2. pure water, pH = 7
3. wine, pH = 3.0
```

```{solution} ex:ball-ch12-s06-n02
:label: sol:ball-ch12-s06-n02
:class: dropdown

1. With a pH greater than 7, milk of magnesia is basic. (Milk of magnesia is largely Mg(OH)<sub>2</sub>.)
2. Pure water, with a pH of 7, is neutral.
3. With a pH of less than 7, wine is acidic.
```

```{exercise}
:label: ex:ball-ch12-s06-n02-ty2

**Test Yourself**

Identify each substance as acidic, basic, or neutral based only on the stated pH.

1. human blood, pH = 7.4
2. household ammonia, pH = 11.0
3. cherries, pH = 3.6
```

```{solution} ex:ball-ch12-s06-n02-ty2
:label: sol:ball-ch12-s06-n02-ty2
:class: dropdown

1. basic
2. basic
3. acidic
```

{ref}`Table 12.3 "Typical pH Values of Various Substances\*" <tbl:ch12:s06:t01>` gives the typical pH values of some common substances. Note that several food items are on the list, and most of them are acidic.

```{table} Typical pH Values of Various Substances*
:label: tbl:ch12:s06:t01

| Substance | pH |
| --- | --- |
| stomach acid | 1.7 |
| lemon juice | 2.2 |
| vinegar | 2.9 |
| soda | 3.0 |
| wine | 3.5 |
| coffee, black | 5.0 |
| milk | 6.9 |
| pure water | 7.0 |
| blood | 7.4 |
| seawater | 8.5 |
| milk of magnesia | 10.5 |
| ammonia solution | 12.5 |
| 1.0 M NaOH | 14.0 |

\*Actual values may vary depending on conditions.
```

pH is a *logarithmic* scale. A solution that has a pH of 1.0 has 10 times the [H<sup>+</sup>] as a solution with a pH of 2.0, which in turn has 10 times the [H<sup>+</sup>] as a solution with a pH of 3.0 and so forth.

Using the definition of pH, it is also possible to calculate [H<sup>+</sup>] (and [OH<sup>−</sup>]) from pH and vice versa. The general formula for determining [H<sup>+</sup>] from pH is as follows:

$$
\text{[H}^{+}\text{] = 10}^{-\text{pH}}
$$

You need to determine how to evaluate the above expression on your calculator. Ask your instructor if you have any questions. The other issue that concerns us here is significant figures. Because the number(s) before the decimal point in a logarithm relate to the power on 10, the number of digits *after* the decimal point is what determines the number of significant figures in the final answer:

![12.6 The pH Scale](../images/figures/fa128b489345bee29deadc0eb3b6fd74.jpg)

*12.6 The pH Scale*

```{exercise}
:label: ex:ball-ch12-s06-n03

**Example 13**

What are [H<sup>+</sup>] and [OH<sup>−</sup>] for an aqueous solution whose pH is 4.88?
```

```{solution} ex:ball-ch12-s06-n03
:label: sol:ball-ch12-s06-n03
:class: dropdown

We need to evaluate the expression

$\text{[H}^{+}\text{] = 10}^{-4.88}$

Depending on the calculator you use, the method for solving this problem will vary. In some cases, the “−4.88” is entered and a “10<sup>x</sup>” key is pressed; for other calculators, the sequence of keystrokes is reversed. In any case, the correct numerical answer is as follows:

$\text{[H}^{+}\text{] = 1.3 }\times{}\text{ 10}^{-5}\text{ M}$

Because 4.88 has two digits after the decimal point, [H<sup>+</sup>] is limited to two significant figures. From this, [OH<sup>−</sup>] can be determined:

$$
{\text{[OH}}^{-}]=\frac{1\times{}{10}^{-14}}{1.3\times{}{10}^{-5}}=7.7\times{}{10}^{-10}\,\text{M}
$$
```

```{exercise}
:label: ex:ball-ch12-s06-n03-ty2

**Test Yourself**

What are [H<sup>+</sup>] and [OH<sup>−</sup>] for an aqueous solution whose pH is 10.36?
```

```{solution} ex:ball-ch12-s06-n03-ty2
:label: sol:ball-ch12-s06-n03-ty2
:class: dropdown

[H<sup>+</sup>] = 4.4 × 10<sup>−11</sup> M; [OH<sup>−</sup>] = 2.3 × 10<sup>−4</sup> M
```

There is an easier way to relate [H<sup>+</sup>] and [OH<sup>−</sup>]. We can also define **pOH** (*The negative logarithm of the hydroxide ion concentration.*) similar to pH:

$$
\text{pOH = }-\text{log[OH}^{-}\text{]}
$$

(In fact, p“anything” is defined as the negative logarithm of that anything.) This also implies that

$$
\text{[OH}^{-}\text{] = 10}^{-\text{pOH}}
$$

A simple and useful relationship is that for any aqueous solution,

$$
\text{pH + pOH = 14}
$$

This relationship makes it simple to determine pH from pOH or pOH from pH and then calculate the resulting ion concentration.

```{exercise}
:label: ex:ball-ch12-s06-n04

**Example 14**

The pH of a solution is 8.22. What are pOH, [H<sup>+</sup>], and [OH<sup>−</sup>]?
```

```{solution} ex:ball-ch12-s06-n04
:label: sol:ball-ch12-s06-n04
:class: dropdown

Because the sum of pH and pOH equals 14, we have

$\text{8.22 + pOH = 14}$

Subtracting 8.22 from 14, we get

$\text{pOH = 5.78}$

Now we evaluate the following two expressions:

$\text{[H}^{+}\text{] = 10}^{-8.22}$

$\text{[OH}^{-}\text{] = 10}^{-5.78}$

So

$\text{[H}^{+}\text{] = 6.0 }\times{}\text{ 10}^{-9}\text{ M}$

$\text{[OH}^{-}\text{] = 1.7 }\times{}\text{ 10}^{-6}\text{ M}$
```

```{exercise}
:label: ex:ball-ch12-s06-n04-ty2

**Test Yourself**

The pOH of a solution is 12.04. What are pH, [H<sup>+</sup>], and [OH<sup>−</sup>]?
```

```{solution} ex:ball-ch12-s06-n04-ty2
:label: sol:ball-ch12-s06-n04-ty2
:class: dropdown

pH = 1.96; [H<sup>+</sup>] = 1.1 × 10<sup>−2</sup> M; [OH<sup>−</sup>] = 9.1 × 10<sup>−13</sup> M
```

```{important} Key Takeaways

- pH is a logarithmic function of [H<sup>+</sup>].
- [H<sup>+</sup>] can be calculated directly from pH.
- pOH is related to pH and can be easily calculated from pH.
```

## Exercises

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa01

**Exercise 1.**

Define *pH*. How is it related to pOH?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa01
:label: sol:ball-ch12-s06-qs01-qd01-qa01
:class: dropdown

pH is the negative logarithm of [H<sup>+</sup>] and is equal to 14 − pOH.
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa02

**Exercise 2.**

Define *pOH*. How is it related to pH?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa03

**Exercise 3.**

What is the pH range for an acidic solution?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa03
:label: sol:ball-ch12-s06-qs01-qd01-qa03
:class: dropdown

pH &lt; 7
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa04

**Exercise 4.**

What is the pH range for a basic solution?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa05

**Exercise 5.**

What is [H<sup>+</sup>] for a neutral solution?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa05
:label: sol:ball-ch12-s06-qs01-qd01-qa05
:class: dropdown

1.0 × 10<sup>−7</sup> M
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa06

**Exercise 6.**

What is [OH<sup>−</sup>] for a neutral solution? Compare your answer to Exercise 6. Does this make sense?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa07

**Exercise 7.**

Which substances in {ref}`Table 12.3 "Typical pH Values of Various Substances\*" <tbl:ch12:s06:t01>` are acidic?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa07
:label: sol:ball-ch12-s06-qs01-qd01-qa07
:class: dropdown

Every entry above pure water is acidic.
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa08

**Exercise 8.**

Which substances in {ref}`Table 12.3 "Typical pH Values of Various Substances\*" <tbl:ch12:s06:t01>` are basic?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa09

**Exercise 9.**

What is the pH of a solution when [H<sup>+</sup>] is 3.44 × 10<sup>−4</sup> M?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa09
:label: sol:ball-ch12-s06-qs01-qd01-qa09
:class: dropdown

3.46
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa10

**Exercise 10.**

What is the pH of a solution when [H<sup>+</sup>] is 9.04 × 10<sup>−13</sup> M?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa11

**Exercise 11.**

What is the pH of a solution when [OH<sup>−</sup>] is 6.22 × 10<sup>−7</sup> M?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa11
:label: sol:ball-ch12-s06-qs01-qd01-qa11
:class: dropdown

7.79
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa12

**Exercise 12.**

What is the pH of a solution when [OH<sup>−</sup>] is 0.0222 M?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa13

**Exercise 13.**

What is the pOH of a solution when [H<sup>+</sup>] is 3.44 × 10<sup>−4</sup> M?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa13
:label: sol:ball-ch12-s06-qs01-qd01-qa13
:class: dropdown

10.54
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa14

**Exercise 14.**

What is the pOH of a solution when [H<sup>+</sup>] is 9.04 × 10<sup>−13</sup> M?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa15

**Exercise 15.**

What is the pOH of a solution when [OH<sup>−</sup>] is 6.22 × 10<sup>−7</sup> M?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa15
:label: sol:ball-ch12-s06-qs01-qd01-qa15
:class: dropdown

6.21
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa16

**Exercise 16.**

What is the pOH of a solution when [OH<sup>−</sup>] is 0.0222 M?
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa17

**Exercise 17.**

If a solution has a pH of 0.77, what is its pOH, [H<sup>+</sup>], and [OH<sup>−</sup>]?
```

```{solution} ex:ball-ch12-s06-qs01-qd01-qa17
:label: sol:ball-ch12-s06-qs01-qd01-qa17
:class: dropdown

pOH = 13.23; [H<sup>+</sup>] = 1.70 × 10<sup>−1</sup> M; [OH<sup>−</sup>] = 5.89 × 10<sup>−14</sup> M
```

```{exercise}
:label: ex:ball-ch12-s06-qs01-qd01-qa18

**Exercise 18.**

If a solution has a pOH of 13.09, what is its pH, [H<sup>+</sup>], and [OH<sup>−</sup>]?
```
