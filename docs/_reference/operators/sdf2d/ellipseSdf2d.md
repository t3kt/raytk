---
layout: operator
title: ellipseSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/ellipseSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.ellipseSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  keywords:
  - circle
  - ellipse
  - oval
  name: ellipseSdf2d
  opType: raytk.operators.sdf2d.ellipseSdf2d
  parameters:
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds
      name: bounds
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  thumb: assets/images/reference/operators/sdf2d/ellipseSdf2d_thumb.png

---
