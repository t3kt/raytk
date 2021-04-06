---
layout: operator
title: impulseFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/impulseFn
redirect_from:
  - /reference/opType/raytk.operators.function.impulseFn/
op:
  category: function
  detail: Based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).
  name: impulseFn
  opType: raytk.operators.function.impulseFn
  parameters:
  - label: Function
    menuOptions:
    - label: Exponential Impulse
      name: exponential
    - label: Sustained Impulse
      name: sustained
    - label: Quad Impulse
      name: quad
    - label: Polynomial Impulse
      name: poly
    name: Function
  - label: Attack
    name: Attack
  - label: Release
    name: Release
  - label: Falloff
    name: Falloff
  - label: Polynomial Degree
    name: Polydegree
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
  summary: Impulse functions that are useful as trigger patterns or animation envelopes.

---


Impulse functions that are useful as trigger patterns or animation envelopes.

Based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).