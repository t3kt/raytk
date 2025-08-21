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
    - VertexContext
    - PixelContext
    - PopContext
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
    - Volume
    - Ray
    - Light
    supportedVariables:
    - scale
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Density
    name: Density
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Zoom
    name: Zoom
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Repeats space in a square arrangement that gets smaller in the center.
  thumb: assets/images/reference/operators/filter/geometricSeriesSquareTile_thumb.png
  variables:
  - label: Scale
    name: scale

---


Repeats space in a square arrangement that gets smaller in the center.