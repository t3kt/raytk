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
  name: chamferRectangleSdf2d
  opType: raytk.operators.sdf2d.chamferRectangleSdf2d
  parameters:
  - label: Scale
    name: Scale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The size of the rectangle on the x and y axes.
  - label: Chamfer
    name: Chamfer
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/chamferRectangleSdf2d_thumb.png

---
