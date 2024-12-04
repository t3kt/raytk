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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: C Field
    name: cField
    returnTypes:
    - vec4
    supportedVariables:
    - step
    - normstep
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
  - label: Step
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---
