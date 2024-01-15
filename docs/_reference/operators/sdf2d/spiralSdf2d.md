---
layout: operator
title: spiralSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/spiralSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.spiralSdf2d/
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
    label: Spread Field
    name: spreadField
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
    label: Rotate Field
    name: rotateField
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
    label: Radius Limit Field
    name: radiusLimitField
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
  name: spiralSdf2d
  opType: raytk.operators.sdf2d.spiralSdf2d
  parameters:
  - label: Spread
    name: Spread
  - label: Thickness
    name: Thickness
  - label: Rotate
    name: Rotate
  - label: Use Radius Limit
    name: Useradiuslimit
  - label: Radius Limit
    name: Radiuslimit
  status: beta
  thumb: assets/images/reference/operators/sdf2d/spiralSdf2d_thumb.png

---
