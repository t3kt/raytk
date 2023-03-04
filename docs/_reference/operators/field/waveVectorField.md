---
layout: operator
title: waveVectorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/waveVectorField
redirect_from:
  - /reference/opType/raytk.operators.field.waveVectorField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  name: waveVectorField
  opType: raytk.operators.field.waveVectorField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
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
  - label: Period
    name: Period
  - label: Phase
    name: Phase
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  status: beta
  thumb: assets/images/reference/operators/field/waveVectorField_thumb.png

---
