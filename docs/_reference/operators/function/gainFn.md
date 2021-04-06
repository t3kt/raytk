---
layout: operator
title: gainFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/gainFn
redirect_from:
  - /reference/opType/raytk.operators.function.gainFn/
op:
  category: function
  detail: 'Effectively what that means is that it smooths out transition from 0 to
    1 in various ways.


    Based on Inigo Quilez''s [article](https://iquilezles.org/www/articles/functions/functions.htm).'
  name: gainFn
  opType: raytk.operators.function.gainFn
  parameters:
  - label: Exponent
    name: Exponent
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
  summary: A function that expands the sides of the coordinate range and compresses
    the center.

---


A function that expands the sides of the coordinate range and compresses the center.

Effectively what that means is that it smooths out transition from 0 to 1 in various ways.

Based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).