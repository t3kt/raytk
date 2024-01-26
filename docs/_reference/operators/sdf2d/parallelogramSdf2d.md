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
    - ParticleContext
    - VertexContext
    - PixelContext
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
    - ParticleContext
    - VertexContext
    - PixelContext
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
  - label: Height
    name: Height
  - label: Skew
    name: Skew
  thumb: assets/images/reference/operators/sdf2d/parallelogramSdf2d_thumb.png

---
