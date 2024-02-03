---
layout: operator
title: magnetField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/magnetField
redirect_from:
  - /reference/opType/raytk.operators.field.magnetField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    label: Easing
    name: easing
    returnTypes:
    - float
  name: magnetField
  opType: raytk.operators.field.magnetField
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
  - label: Format
    menuOptions:
    - label: Amount Only
      name: amount
    - label: Vector & Amount
      name: vectoramt
    - label: Center & Amount
      name: centeramt
    - label: Scaled Vector
      name: scaledvec
    name: Format
  - label: Amount
    name: Amount
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Fade
    name: Fade
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/field/magnetField_thumb.png

---
