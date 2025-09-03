---
layout: operator
title: blobbyCrossSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/blobbyCrossSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.blobbyCrossSdf2d/
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
    label: Tightness Field
    name: tightnessField
    returnTypes:
    - float
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
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - tightnessField
  name: blobbyCrossSdf2d
  opType: raytk.operators.sdf2d.blobbyCrossSdf2d
  parameters:
  - label: Tightness
    name: Tightness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/blobbyCrossSdf2d_thumb.png

---
