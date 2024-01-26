---
layout: operator
title: stairSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/stairSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.stairSdf2d/
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
    label: Scale Field
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
    label: Steps Field
    name: stepsField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - sizeField
  name: stairSdf2d
  opType: raytk.operators.sdf2d.stairSdf2d
  parameters:
  - label: Size
    name: Size
  - label: Steps
    name: Steps
  status: beta
  thumb: assets/images/reference/operators/sdf2d/stairSdf2d_thumb.png

---
