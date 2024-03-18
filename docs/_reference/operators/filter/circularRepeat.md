---
layout: operator
title: circularRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/circularRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.circularRepeat/
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
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    supportedVariables:
    - cellcoord
    - cellchecker
    - RTK_raytk_operators_filter_circularRepeat_cellcoord
    - RTK_raytk_operators_filter_circularRepeat_cellchecker
  name: circularRepeat
  opType: raytk.operators.filter.circularRepeat
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
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Size of the area to fill.
  - label: Cell Size
    name: Cellsize
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Spacing between copies.
  status: beta
  summary: Repeat an SDF to fill a 2D circular area.
  variables:
  - label: cellcoord
    name: cellcoord
  - label: cellchecker
    name: cellchecker
  - label: RTK_raytk_operators_filter_circularRepeat_cellcoord
    name: RTK_raytk_operators_filter_circularRepeat_cellcoord
  - label: RTK_raytk_operators_filter_circularRepeat_cellchecker
    name: RTK_raytk_operators_filter_circularRepeat_cellchecker

---


Repeat an SDF to fill a 2D circular area.