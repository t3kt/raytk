---
layout: operator
title: parallelogramSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/parallelogramSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.parallelogramSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    label: Size Field
    name: sizeField
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
    - PopContext
    coordTypes:
    - vec2
    label: Skew Field
    name: skewField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
  name: parallelogramSdf2d
  opType: raytk.operators.sdf2d.parallelogramSdf2d
  parameters:
  - label: Width
    name: Width
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Skew
    name: Skew
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/parallelogramSdf2d_thumb.png

---
