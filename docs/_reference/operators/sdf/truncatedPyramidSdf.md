---
layout: operator
title: truncatedPyramidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/truncatedPyramidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.truncatedPyramidSdf/
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
    label: Height Field
    name: heightField
    returnTypes:
    - float
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
    label: Top Size Field
    name: topSizeField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - normoffset
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
    label: Bottom Size Field
    name: bottomSizeField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - normoffset
  name: truncatedPyramidSdf
  opType: raytk.operators.sdf.truncatedPyramidSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the base of the pyramid.
  - label: Top Size
    name: Topsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bottom Size
    name: Bottomsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/truncatedPyramidSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_truncatedPyramidSdf_normoffset
    name: RTK_raytk_operators_sdf_truncatedPyramidSdf_normoffset

---
