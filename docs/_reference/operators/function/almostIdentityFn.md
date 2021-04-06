---
layout: operator
title: almostIdentityFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/almostIdentityFn
redirect_from:
  - /reference/opType/raytk.operators.function.almostIdentityFn/
op:
  category: function
  detail: 'Then, rather than doing a conditional branch which introduces a discontinuity,
    you can smoothly blend your value with your Threshold.


    This is based on Inigo Quilez''s [article](https://iquilezles.org/www/articles/functions/functions.htm).'
  name: almostIdentityFn
  opType: raytk.operators.function.almostIdentityFn
  parameters:
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  - label: Threshold
    name: Threshold
    summary: The value above which things will be unchanged.
  - label: Base Value
    name: Basevalue
    summary: The constant value to use when the input is zero.
  summary: A mapping function that can change a value only when it's zero or very
    close to it, where it replaces the value with a small constant.

---


A mapping function that can change a value only when it's zero or very close to it, where it replaces the value with a small constant.

Then, rather than doing a conditional branch which introduces a discontinuity, you can smoothly blend your value with your Threshold.

This is based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).