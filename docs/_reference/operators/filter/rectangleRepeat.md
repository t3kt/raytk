---
layout: operator
title: rectangleRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rectangleRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.rectangleRepeat/
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
  name: rectangleRepeat
  opType: raytk.operators.filter.rectangleRepeat
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    name: Plane
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Grid Size
    name: Gridsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Spacing
    name: Spacing
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/rectangleRepeat_thumb.png

---
