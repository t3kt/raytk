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
    - label: Auto
      name: auto
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
  summary: A float or vector field that evaluates to a constant value.

---


A float or vector field that evaluates to a constant value.