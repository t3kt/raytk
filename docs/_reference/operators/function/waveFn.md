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
    - label: Additive Square (2)
      name: addsquare2
    - label: Additive Square (4)
      name: addsquare4
    - label: Additive Square (8)
      name: addsquare8
    name: Function
    readOnlyHandling: baked
    regularHandling: runtime
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
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  summary: A function that uses a periodic wave, with the position as the parameter.
  thumb: assets/images/reference/operators/function/waveFn_thumb.png

---


A function that uses a periodic wave, with the position as the parameter.