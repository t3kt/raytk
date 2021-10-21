---
layout: operator
title: truchetTile
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/truchetTile
redirect_from:
  - /reference/opType/raytk.operators.filter.truchetTile/
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
  name: truchetTile
  opType: raytk.operators.filter.truchetTile
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
  status: alpha

---
