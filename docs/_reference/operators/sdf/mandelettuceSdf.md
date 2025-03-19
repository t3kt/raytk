---
layout: operator
title: mandelettuceSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mandelettuceSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mandelettuceSdf/
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
    supportedVariables:
    - step
    - normstep
  keywords:
  - fractal
  name: mandelettuceSdf
  opType: raytk.operators.sdf.mandelettuceSdf
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf/mandelettuceSdf_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---
