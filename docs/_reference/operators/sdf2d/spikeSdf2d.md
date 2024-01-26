---
layout: operator
title: spikeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/spikeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.spikeSdf2d/
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
    label: Height Field
    name: heightField
    returnTypes:
    - float
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
  name: spikeSdf2d
  opType: raytk.operators.sdf2d.spikeSdf2d
  parameters:
  - label: Direction
    menuOptions:
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    name: Direction
  - label: Height
    name: Height
  - label: Offset
    name: Offset
  - label: Center
    name: Center
  thumb: assets/images/reference/operators/sdf2d/spikeSdf2d_thumb.png

---
