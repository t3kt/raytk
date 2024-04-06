---
layout: operator
title: pistonSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/pistonSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.pistonSdf2d/
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - offsetField
  name: pistonSdf2d
  opType: raytk.operators.sdf2d.pistonSdf2d
  parameters:
  - label: Direction
    menuOptions:
    - label: X+ (Right)
      name: xpos
    - label: X- (Left)
      name: xneg
    - label: Y+ (Up)
      name: ypos
    - label: Y- (Down)
      name: yneg
    name: Direction
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/pistonSdf2d_thumb.png

---
