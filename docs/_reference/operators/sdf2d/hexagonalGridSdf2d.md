---
layout: operator
title: hexagonalGridSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/hexagonalGridSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.hexagonalGridSdf2d/
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
    label: Radius Field
    name: radiusField
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
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
  name: hexagonalGridSdf2d
  opType: raytk.operators.sdf2d.hexagonalGridSdf2d
  parameters:
  - label: Radius
    name: Radius
  - label: Spacing
    name: Spacing
  - label: Rounding
    name: Rounding
  thumb: assets/images/reference/operators/sdf2d/hexagonalGridSdf2d_thumb.png

---
