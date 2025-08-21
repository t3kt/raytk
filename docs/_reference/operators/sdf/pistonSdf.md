---
layout: operator
title: pistonSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/pistonSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.pistonSdf/
op:
  category: sdf
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
    - vec3
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - offsetField
  name: pistonSdf
  opType: raytk.operators.sdf.pistonSdf
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
    - label: Z+ (Forward)
      name: zpos
    - label: Z- (Backward)
      name: zneg
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
  thumb: assets/images/reference/operators/sdf/pistonSdf_thumb.png

---
