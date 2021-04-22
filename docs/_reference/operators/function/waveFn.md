---
layout: operator
title: waveFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/waveFn
redirect_from:
  - /reference/opType/raytk.operators.function.waveFn/
op:
  category: function
  name: waveFn
  opType: raytk.operators.function.waveFn
  parameters:
  - label: Wave
    menuOptions:
    - label: Sine
      name: sin
    - label: Cosine
      name: cos
    - label: Triangle
      name: tri
    - label: Ramp
      name: ramp
    - label: Square
      name: square
    name: Function
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Period
    name: Period
  - label: Phase
    name: Phase
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  summary: A function that uses a periodic wave, with the position as the parameter.

---


A function that uses a periodic wave, with the position as the parameter.