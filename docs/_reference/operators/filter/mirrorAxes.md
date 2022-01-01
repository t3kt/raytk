---
layout: operator
title: mirrorAxes
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorAxes
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorAxes/
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
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
    label: Direction Field
    name: directionField
    returnTypes:
    - float
    - vec4
  name: mirrorAxes
  opType: raytk.operators.filter.mirrorAxes
  parameters:
  - label: Enable
    name: Enable
  - label: Axes
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
    - label: ZX
      name: zx
    - label: XYZ
      name: xyz
    name: Axes
  - label: Direction X
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirx
  - label: Direction Y
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Diry
  - label: Direction Z
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirz
  - label: Center
    name: Center
  - label: Offset
    name: Offset
  - label: Axis Sides (+/- 1)
    name: Createrefsides
    summary: 'Create reference to variable: Axis Sides (+/- 1)'
  status: beta
  thumb: assets/images/reference/operators/filter/mirrorAxes_thumb.png

---
