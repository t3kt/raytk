---
layout: operator
title: constantColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantColorField
redirect_from:
  - /reference/opType/raytk.operators.field.constantColorField/
op:
  category: field
  detail: This is the same as `constantField`, but the parameter is specified as a
    color instead of arbitrary float values.
  name: constantColorField
  opType: raytk.operators.field.constantColorField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Color
    name: Color
  - label: Alpha
    name: Alpha
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
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
  summary: A vector field that evaluates to a constant color value.

---


A vector field that evaluates to a constant color value.

This is the same as `constantField`, but the parameter is specified as a color instead of arbitrary float values.