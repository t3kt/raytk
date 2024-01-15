---
layout: operator
title: juliaSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/juliaSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.juliaSdf/
op:
  category: sdf
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
    - vec3
    label: C Field
    name: cField
    returnTypes:
    - vec4
  keywords:
  - fractal
  - julia
  - quaternion
  name: juliaSdf
  opType: raytk.operators.sdf.juliaSdf
  parameters:
  - label: C 1
    name: C1
  - label: C 2
    name: C2
  - label: C 3
    name: C3
  - label: C 4
    name: C4
  - label: Iterations
    name: Iterations
  status: beta
  thumb: assets/images/reference/operators/sdf/juliaSdf_thumb.png
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---
