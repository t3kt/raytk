---
layout: operator
title: round
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/round
redirect_from:
  - /reference/opType/raytk.operators.filter.round/
op:
  name: round
  summary: Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.
  detail: |
    Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
    See [example](https://www.shadertoy.com/view/Mt3BDj).
  opType: raytk.operators.filter.round
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
    - name: amount_field_definition_in
      label: amount_field_definition_in
      required: false
  parameters:
    - name: Amount
      label: Amount
      summary: |
        positive numbers increase and round out the shape, negative numbers shrink it.
    - name: Usefield
      label: Usefield
      summary: |
        whether to use the second input to determine the amount of rounding using a value field so various positions can use different amounts of rounding.
    - name: Enable
      label: Enable
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# round

Category: filter



Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.

Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Mt3BDj).