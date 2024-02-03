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
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the base of the pyramid.
  - label: Top Size
    name: Topsize
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Bottom Size
    name: Bottomsize
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Height
    name: Height
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/truncatedPyramidSdf_thumb.png
  variables:
  - label: normoffset
    name: normoffset

---
