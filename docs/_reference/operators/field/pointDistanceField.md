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
  - label: Axes
    menuOptions:
    - label: XYZ
      name: xyz
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: XZ
      name: xz
    name: Axes
  summary: A float field that provides the distance from a specific point in space.
  thumb: assets/images/reference/operators/field/pointDistanceField_thumb.png

---


A float field that provides the distance from a specific point in space.