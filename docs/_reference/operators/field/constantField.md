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
    - label: Auto
      name: auto
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
  - label: Value
    name: Value
    readOnlyHandling: baked
    regularHandling: runtime
  summary: A float or vector field that evaluates to a constant value.
  thumb: assets/images/reference/operators/field/constantField_thumb.png

---


A float or vector field that evaluates to a constant value.