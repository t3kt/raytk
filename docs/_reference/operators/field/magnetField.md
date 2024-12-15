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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    label: Easing
    name: easing
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
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
    readOnlyHandling: baked
    regularHandling: baked
  - label: Amount
    name: Amount
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Fade
    name: Fade
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/field/magnetField_thumb.png

---
