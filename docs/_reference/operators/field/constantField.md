---
layout: operator
title: constantField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantField
redirect_from:
  - /reference/opType/raytk.operators.field.constantField/
op:
  category: field
  name: constantField
  opType: raytk.operators.field.constantField
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
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
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
  - label: Value
    name: Value
  summary: A float or vector field that evaluates to a constant value.

---

# constantField

Category: field



A float or vector field that evaluates to a constant value.