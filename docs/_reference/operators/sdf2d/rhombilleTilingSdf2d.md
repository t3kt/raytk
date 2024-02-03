---
layout: operator
title: rhombilleTilingSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/rhombilleTilingSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.rhombilleTilingSdf2d/
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
  name: rhombilleTilingSdf2d
  opType: raytk.operators.sdf2d.rhombilleTilingSdf2d
  parameters:
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Spacing
    name: Spacing
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/rhombilleTilingSdf2d_thumb.png

---
