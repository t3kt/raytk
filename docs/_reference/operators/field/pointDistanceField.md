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
    summary: The point from which distance is measured.
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
    summary: The type of coordinates to use.
  summary: A float field that provides the distance from a specific point in space.

---


A float field that provides the distance from a specific point in space.