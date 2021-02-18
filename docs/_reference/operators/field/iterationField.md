---
layout: operator
title: iterationField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/iterationField
redirect_from:
  - /reference/opType/raytk.operators.field.iterationField/
op:
  category: field
  name: iterationField
  opType: raytk.operators.field.iterationField
  parameters:
  - label: Format
    menuOptions:
    - label: Full Vector
      name: full
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: W
      name: w
    name: Format
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
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  summary: Field that returns the current iteration, from a downstream OP.

---

# iterationField

Category: field



Field that returns the current iteration, from a downstream OP.