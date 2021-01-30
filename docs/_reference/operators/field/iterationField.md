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
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
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
  - label: Iteration Mode
    menuOptions:
    - label: Index
      name: index
    - label: Scaled Index
      name: scaledindex
    - label: Full Data
      name: full
    name: Iterationmode
  summary: Field that returns the current iteration, from a downstream OP.

---

# iterationField

Category: field



Field that returns the current iteration, from a downstream OP.