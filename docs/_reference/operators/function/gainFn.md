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
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: A function that expands the sides of the coordinate range and compresses
    the center.

---


A function that expands the sides of the coordinate range and compresses the center.

Effectively what that means is that it smooths out transition from 0 to 1 in various ways.

Based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).