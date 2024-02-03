---
layout: operator
title: jointSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/jointSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.jointSdf2d/
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
    label: Thickness Field
    name: thicknessField
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
    label: Length Field
    name: lengthField
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
    label: Bend Field
    name: bendField
    returnTypes:
    - float
  name: jointSdf2d
  opType: raytk.operators.sdf2d.jointSdf2d
  parameters:
  - label: Shape
    menuOptions:
    - label: Square
      name: square
    - label: Round
      name: round
    name: Shape
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Length
    name: Length
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Bend
    name: Bend
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/jointSdf2d_thumb.png

---
