---
layout: operator
title: crossSection
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/crossSection
redirect_from:
  - /reference/opType/raytk.operators.convert.crossSection/
op:
  category: convert
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
  name: crossSection
  opType: raytk.operators.convert.crossSection
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
    - label: YX
      name: yx
    - label: YZ
      name: yz
    - label: ZY
      name: zy
    - label: XZ
      name: xz
    - label: ZX
      name: zx
    name: Axes
  - label: Offset
    name: Offset
  status: beta

---
