---
layout: operator
title: spread
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/spread
redirect_from:
  - /reference/opType/raytk.operators.filter.spread/
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
    - float
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
  name: spread
  opType: raytk.operators.filter.spread
  parameters:
  - label: Enable
    name: Enable
  - label: Spread Axes
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: XZ
      name: xz
    - label: XYZ
      name: xyz
    name: Spreadaxes
  - label: Center
    name: Center
  - label: Width
    name: Width
  - label: Blending
    name: Blending
  status: alpha

---
