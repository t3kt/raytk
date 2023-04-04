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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Pattern Shift Field
    name: patternShiftField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Seed Field
    name: seedField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Size Field
    name: sizeField
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
    coordTypes:
    - vec2
    label: Minimum Size Field
    name: minSizeField
    returnTypes:
    - float
  name: subdivisionSdf2d
  opType: raytk.operators.sdf2d.subdivisionSdf2d
  parameters:
  - label: Iterations
    name: Iterations
  - label: Size
    name: Size
  - label: Pattern Shift
    name: Patternshift
  - label: Minimum Size
    name: Minsize
  - label: Seed
    name: Seed
  status: beta
  thumb: assets/images/reference/operators/sdf2d/subdivisionSdf2d_thumb.png
  variables:
  - label: cellsize
    name: cellsize
  - label: cellid
    name: cellid

---
