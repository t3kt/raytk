---
layout: operator
title: moduloLine
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloLine
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloLine/
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
    supportedVariables:
    - RTK_raytk_operators_filter_moduloLine_cellcoord
    - RTK_raytk_operators_filter_moduloLine_normcoord
  name: moduloLine
  opType: raytk.operators.filter.moduloLine
  parameters:
  - label: Enable
    name: Enable
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Divisions
    name: Divisions
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How to the slices are varied.
  status: beta
  variables:
  - label: RTK_raytk_operators_filter_moduloLine_cellcoord
    name: RTK_raytk_operators_filter_moduloLine_cellcoord
  - label: RTK_raytk_operators_filter_moduloLine_normcoord
    name: RTK_raytk_operators_filter_moduloLine_normcoord

---
