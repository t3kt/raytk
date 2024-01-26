---
layout: operator
title: triangularGridSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/triangularGridSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.triangularGridSdf2d/
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
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
  name: triangularGridSdf2d
  opType: raytk.operators.sdf2d.triangularGridSdf2d
  parameters:
  - label: Size
    name: Size
  - label: Spacing
    name: Spacing
  thumb: assets/images/reference/operators/sdf2d/triangularGridSdf2d_thumb.png

---
