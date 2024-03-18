---
layout: operator
title: modifyDistance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modifyDistance
redirect_from:
  - /reference/opType/raytk.operators.filter.modifyDistance/
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
    label: SDF
    name: sdf_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Value Field
    name: valueField
    required: true
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - sdf_definition_in
  name: modifyDistance
  opType: raytk.operators.filter.modifyDistance
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - label: Add
      name: add
    - label: Multiply
      name: mul
    - label: Replace
      name: replace
    name: Mode
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Mix
    name: Mix
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Mix between the original distance and the original distance.
  status: beta
  variables:
  - label: RTK_raytk_operators_filter_modifyDistance_sdf
    name: RTK_raytk_operators_filter_modifyDistance_sdf
  - label: RTK_raytk_operators_filter_modifyDistance_dist
    name: RTK_raytk_operators_filter_modifyDistance_dist

---
