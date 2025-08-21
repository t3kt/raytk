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
    - PopContext
    coordTypes:
    - vec3
    label: Pre Rotate Field
    name: preRotateField
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
    - PopContext
    coordTypes:
    - vec3
    label: Post Rotate Field
    name: postRotateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - preRotateField
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    supportedVariableInputs:
    - preRotateField
    - postRotateField
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
    - preRotateField
    - postRotateField
    - scaleField
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
    label: Vertex Shape
    name: vertexShape
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - preRotateField
    - postRotateField
    - scaleField
    - offsetField
  keywords:
  - fractal
  name: sierpinskiOctahedralSpongeSdf
  opType: raytk.operators.sdf.sierpinskiOctahedralSpongeSdf
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - name: Rotate
  - label: Pre Rotate
    name: Prerotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Post Rotate
    name: Postrotate
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