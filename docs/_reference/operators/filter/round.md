---
layout: page
title: round
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/round
redirect_from:
  - /reference/opType/raytk.operators.filter.round/
---

# round

Category: filter



Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.

Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Mt3BDj).

## Parameters

* `Amount` *Amount*: positive numbers increase and round out the shape, negative numbers shrink it.
* `Usefield`: whether to use the second input to determine the amount of rounding using a value field so various positions can use different amounts of rounding.
* `Enable` *Enable*
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`: 
* `amount_field_definition_in`: 