---
layout: operator
title: pointDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/pointDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.pointDistanceField/
op:
  category: field
  name: pointDistanceField
  opType: raytk.operators.field.pointDistanceField
  parameters:
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
    - label: Ray Context
      name: RayContext
    name: Contexttype
  summary: A float field that provides the distance from a specific point in space.

---

# pointDistanceField

Category: field



A float field that provides the distance from a specific point in space.