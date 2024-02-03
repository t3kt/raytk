---
layout: operator
title: parabolaSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/parabolaSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.parabolaSdf2d/
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
    label: Width Field
    name: widthField
    returnTypes:
    - float
  name: parabolaSdf2d
  opType: raytk.operators.sdf2d.parabolaSdf2d
  parameters:
  - label: Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/parabolaSdf2d_thumb.png

---
