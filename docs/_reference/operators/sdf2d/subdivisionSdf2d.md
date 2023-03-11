---
layout: operator
title: subdivisionSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/subdivisionSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.subdivisionSdf2d/
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
    coordTypes:
    - vec2
    label: Shape SDF
    name: shape
    returnTypes:
    - Sdf
  name: subdivisionSdf2d
  opType: raytk.operators.sdf2d.subdivisionSdf2d
  parameters:
  - label: Iterations
    name: Iterations
  - label: Size
    name: Size
  - label: Pattern Shift
    name: Patternshift
  status: beta
  thumb: assets/images/reference/operators/sdf2d/subdivisionSdf2d_thumb.png
  variables:
  - label: cellsize
    name: cellsize
  - label: cellid
    name: cellid

---
