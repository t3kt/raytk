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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    required: true
    returnTypes:
    - vec4
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
  - label: Division
    name: Division
  - label: Level 1 Chance
    name: Chance1
  - label: Level 2 Chance
    name: Chance2
  - label: Offset
    name: Offset
  - label: Shift
    name: Shift
  - label: Enable Rescale
    name: Enablerescale
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Id (xy) & Layer (z)
      name: cell
    name: Iterationtype
  - label: Seed
    name: Seed
  status: beta
  thumb: assets/images/reference/operators/filter/quadTreeRepeat_thumb.png
  variables:
  - label: cell
    name: cell
  - label: layer
    name: layer

---
