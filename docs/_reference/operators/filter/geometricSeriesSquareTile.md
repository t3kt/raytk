---
layout: operator
title: geometricSeriesSquareTile
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/geometricSeriesSquareTile
redirect_from:
  - /reference/opType/raytk.operators.filter.geometricSeriesSquareTile/
op:
  category: filter
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: geometricSeriesSquareTile
  opType: raytk.operators.filter.geometricSeriesSquareTile
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: constant
    regularHandling: constant
  - label: Density
    name: Density
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Zoom
    name: Zoom
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  summary: Repeats space in a square arrangement that gets smaller in the center.
  thumb: assets/images/reference/operators/filter/geometricSeriesSquareTile_thumb.png
  variables:
  - label: scale
    name: scale

---


Repeats space in a square arrangement that gets smaller in the center.