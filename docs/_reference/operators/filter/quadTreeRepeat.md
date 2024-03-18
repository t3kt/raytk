---
layout: operator
title: quadTreeRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quadTreeRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.quadTreeRepeat/
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
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - offsetField
    - shiftField
    supportedVariables:
    - RTK_raytk_operators_filter_quadTreeRepeat_cell
    - RTK_raytk_operators_filter_quadTreeRepeat_layer
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
    label: Shift Field
    name: shiftField
    required: true
    returnTypes:
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
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    required: true
    returnTypes:
    - vec4
    supportedVariableInputs:
    - shiftField
    supportedVariables:
    - RTK_raytk_operators_filter_quadTreeRepeat_cell
    - RTK_raytk_operators_filter_quadTreeRepeat_layer
  name: quadTreeRepeat
  opType: raytk.operators.filter.quadTreeRepeat
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
  - label: Division
    name: Division
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 1 Chance
    name: Chance1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 2 Chance
    name: Chance2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Rescale
    name: Enablerescale
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Id (xy) & Layer (z)
      name: cell
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/quadTreeRepeat_thumb.png
  variables:
  - label: RTK_raytk_operators_filter_quadTreeRepeat_cell
    name: RTK_raytk_operators_filter_quadTreeRepeat_cell
  - label: RTK_raytk_operators_filter_quadTreeRepeat_layer
    name: RTK_raytk_operators_filter_quadTreeRepeat_layer

---
