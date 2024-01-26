---
layout: operator
title: cutDiscSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/cutDiscSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.cutDiscSdf2d/
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
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
    supportedVariableInputs:
    - radiusField
    - offsetField
  name: cutDiscSdf2d
  opType: raytk.operators.sdf2d.cutDiscSdf2d
  parameters:
  - label: Radius
    name: Radius
  - label: Cut Offset
    name: Offset
  - label: Rotate
    name: Rotate
  thumb: assets/images/reference/operators/sdf2d/cutDiscSdf2d_thumb.png

---
