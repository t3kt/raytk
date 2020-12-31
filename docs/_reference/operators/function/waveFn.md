---
layout: operator
title: waveFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/waveFn
redirect_from:
  - /reference/opType/raytk.operators.function.waveFn/
op:
  name: waveFn
  summary: A function that uses a periodic wave, with the position as the parameter.
  opType: raytk.operators.function.waveFn
  category: function
  parameters:
    - name: Function
      label: Wave
      menuOptions:
        - name: sin
          label: Sine
        - name: cos
          label: Cosine
        - name: tri
          label: Triangle
        - name: ramp
          label: Ramp
        - name: square
          label: Square
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: float
          label: 1D
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Period
      label: Period
    - name: Phase
      label: Phase
    - name: Amplitude
      label: Amplitude
    - name: Offset
      label: Offset
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# waveFn

Category: function



A function that uses a periodic wave, with the position as the parameter.