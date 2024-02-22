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
    readOnlyHandling: baked
    regularHandling: baked
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
  summary: Field that returns the current iteration, from a downstream OP.

---


Field that returns the current iteration, from a downstream OP.