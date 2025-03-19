---
layout: operator
title: sierpinskiOctahedralSpongeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/sierpinskiOctahedralSpongeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.sierpinskiOctahedralSpongeSdf/
op:
  category: sdf
  detail: Based on [Octahedral Sponge - Fractal SDF](https://www.shadertoy.com/view/Wc2GWG)
    by TheArchCoder.
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
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
    supportedVariables:
    - step
    - normstep
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    supportedVariableInputs:
    - rotateField
    supportedVariables:
    - step
    - normstep
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
    supportedVariableInputs:
    - rotateField
    - scaleField
    supportedVariables:
    - step
    - normstep
  keywords:
  - fractal
  name: sierpinskiOctahedralSpongeSdf
  opType: raytk.operators.sdf.sierpinskiOctahedralSpongeSdf
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Sierpinski Octahedral Sponge Fractal SDF
  thumb: assets/images/reference/operators/sdf/sierpinskiOctahedralSpongeSdf_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---


Sierpinski Octahedral Sponge Fractal SDF

Based on [Octahedral Sponge - Fractal SDF](https://www.shadertoy.com/view/Wc2GWG) by TheArchCoder.