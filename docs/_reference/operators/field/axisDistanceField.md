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
    - label: Use Input
      name: useinput
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
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: A float field that provides the distance from a specific point along a
    single axis.

---

# axisDistanceField

Category: field



A float field that provides the distance from a specific point along a single axis.