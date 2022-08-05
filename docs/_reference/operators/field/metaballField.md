---
layout: operator
title: metaballField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/metaballField
redirect_from:
  - /reference/opType/raytk.operators.field.metaballField/
op:
  category: field
  name: metaballField
  opType: raytk.operators.field.metaballField
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
  - label: Center
    name: Center
    summary: Center position of the ball.
  - label: Radius
    name: Radius
    summary: Radius of the ball on each axis. In 2D mode, only x and y are used. In
      1D only x is used.
  - label: Radius Scale
    name: Radiusscale
    summary: Scales the radius on all axes.
  - label: Weight
    name: Weight
    summary: The returned values are multiplied by this.
  - label: Exponent
    name: Exponent
    summary: Controls the shape of the ball by applying exponential scaling to coordinates.
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
  summary: Metaball value field.
  thumb: assets/images/reference/operators/field/metaballField_thumb.png

---


Metaball value field.