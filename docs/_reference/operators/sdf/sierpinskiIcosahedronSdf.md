---
layout: operator
title: sierpinskiIcosahedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/sierpinskiIcosahedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.sierpinskiIcosahedronSdf/
op:
  category: sdf
  detail: Based on [3D Sierpinski Icosahedron - SDF](https://www.shadertoy.com/view/wcX3WB)
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
    - PopContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
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
    - PopContext
    coordTypes:
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - scaleField
    supportedVariables:
    - step
    - normstep
  keywords:
  - fractal
  name: sierpinskiIcosahedronSdf
  opType: raytk.operators.sdf.sierpinskiIcosahedronSdf
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
  - name: Power
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Sierpinski Icosahedron Fractal SDF
  thumb: assets/images/reference/operators/sdf/sierpinskiIcosahedronSdf_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---


Sierpinski Icosahedron Fractal SDF

Based on [3D Sierpinski Icosahedron - SDF](https://www.shadertoy.com/view/wcX3WB) by TheArchCoder.