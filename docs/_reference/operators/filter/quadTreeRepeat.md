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
  - label: Cell ID Hash (XY)
    name: Createrefcell
    summary: 'Create reference to variable: Cell ID Hash (XY)'
  - label: Layer Index
    name: Createreflayer
    summary: 'Create reference to variable: Layer Index'
  status: beta
  thumb: assets/images/reference/operators/filter/quadTreeRepeat_thumb.png

---
