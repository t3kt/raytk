---
layout: operator
title: planeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/planeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.planeSdf2d/
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
  name: planeSdf2d
  opType: raytk.operators.sdf2d.planeSdf2d
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
  - label: Offset
    name: Offset
  thumb: assets/images/reference/operators/sdf2d/planeSdf2d_thumb.png

---
