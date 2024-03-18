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
    supportedVariables:
    - RTK_raytk_operators_sdf_juliaSdf_step
    - RTK_raytk_operators_sdf_juliaSdf_normstep
  keywords:
  - fractal
  - julia
  - quaternion
  name: juliaSdf
  opType: raytk.operators.sdf.juliaSdf
  parameters:
  - label: C 1
    name: C1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: C 2
    name: C2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: C 3
    name: C3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: C 4
    name: C4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Iterations
    name: Iterations
    readOnlyHandling: semibaked
    regularHandling: semibaked
  thumb: assets/images/reference/operators/sdf/juliaSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_juliaSdf_step
    name: RTK_raytk_operators_sdf_juliaSdf_step
  - label: RTK_raytk_operators_sdf_juliaSdf_normstep
    name: RTK_raytk_operators_sdf_juliaSdf_normstep

---
