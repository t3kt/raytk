---
layout: operator
title: exponentialSeriesTile
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/exponentialSeriesTile
redirect_from:
  - /reference/opType/raytk.operators.filter.exponentialSeriesTile/
op:
  category: filter
  detail: based on [Exponential Tiling by jt](https://www.shadertoy.com/view/wXcGz8)
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
    - vec2
    - vec3
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
  name: exponentialSeriesTile
  opType: raytk.operators.filter.exponentialSeriesTile
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - label: Along X Towards Y
      name: xy
    - label: Along Y Towards X
      name: yx
    - label: Along Z Towards X
      name: zy
    - label: Along Y Towards Z
      name: yz
    - label: Along Z Towards X
      name: zx
    - label: Along X Towards Z
      name: xz
    name: Direction
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Base
    name: Base
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Exponential series tiling

---


Exponential series tiling

based on [Exponential Tiling by jt](https://www.shadertoy.com/view/wXcGz8)