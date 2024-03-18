---
layout: operator
title: positionField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/positionField
redirect_from:
  - /reference/opType/raytk.operators.field.positionField/
op:
  category: field
  name: positionField
  opType: raytk.operators.field.positionField
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
  - name: Contexttype
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    name: Returntype
    summary: Whether to return a single axis value or a vector of all coordinate parts.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Position Type
    menuOptions:
    - label: Local Position
      name: local
    - label: Global Position
      name: global
    - label: Pixel UV Coordinate
      name: pixeluv
    - label: Pixel Coordinate
      name: pixelcoord
    name: Positiontype
    readOnlyHandling: baked
    regularHandling: baked
  shortcuts:
  - pos
  summary: A vector field that produces the coordinates in space where it is checked.
  thumb: assets/images/reference/operators/field/positionField_thumb.png

---


A vector field that produces the coordinates in space where it is checked.