---
layout: page
title: round
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/round
---

Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.

Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Mt3BDj).

* `Amount` - positive numbers increase and round out the shape, negative numbers shrink it.
* `Use Field` - whether to use the second input to determine the amount of rounding using a value field so various positions can use different amounts of rounding.
