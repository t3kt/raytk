---
layout: operator
title: chamferRectangleSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/chamferRectangleSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.chamferRectangleSdf2d/
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
    name: scaleField
    returnTypes:
    - float
    - vec4
    summary: Field that multiplies the scale of the rectangle.
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
    label: Chamfer Field
    name: chamferField
    returnTypes:
    - float
    - vec4
    summary: Field that overrides the chamfer distances.
    supportedVariableInputs:
    - scaleField
  name: chamferRectangleSdf2d
  opType: raytk.operators.sdf2d.chamferRectangleSdf2d
  parameters:
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the rectangle on the x and y axes.
  - label: Chamfer
    name: Chamfer
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The distance of the corner cuts on each axis. Keep these the same to
      have 45 degree cuts.
  summary: Rectangle with corners cut off at angles.
  thumb: assets/images/reference/operators/sdf2d/chamferRectangleSdf2d_thumb.png

---


Rectangle with corners cut off at angles.