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
    - label: ParticleContext
      name: ParticleContext
    name: Contexttype
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
  summary: A vector field that produces the coordinates in space where it is checked.
  thumb: assets/images/reference/operators/field/positionField_thumb.png

---


A vector field that produces the coordinates in space where it is checked.