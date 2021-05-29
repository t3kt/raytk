---
layout: operator
title: axisDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/axisDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.axisDistanceField/
op:
  category: field
  name: axisDistanceField
  opType: raytk.operators.field.axisDistanceField
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Center
    name: Center
    summary: The position along the axis from which the distance is calculated.
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
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
  summary: A float field that provides the distance from a specific point along a
    single axis.

---


A float field that provides the distance from a specific point along a single axis.