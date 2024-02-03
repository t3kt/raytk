---
layout: operator
title: kochSnowflakeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/kochSnowflakeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.kochSnowflakeSdf2d/
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
    label: Steps Field
    name: stepsField
    returnTypes:
    - float
  name: kochSnowflakeSdf2d
  opType: raytk.operators.sdf2d.kochSnowflakeSdf2d
  parameters:
  - label: Steps
    name: Steps
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf2d/kochSnowflakeSdf2d_thumb.png

---
