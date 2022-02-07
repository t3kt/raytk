---
layout: operator
title: kink
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/kink
redirect_from:
  - /reference/opType/raytk.operators.filter.kink/
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
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: kink
  opType: raytk.operators.filter.kink
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - label: Along X Toward Y
      name: xy
    - label: Along X Toward Z
      name: xz
    - label: Along Y Toward X
      name: yx
    - label: Along Y Toward Z
      name: yz
    - label: Along Z Toward X
      name: zx
    - label: Along Z Toward Y
      name: zy
    name: Direction
  - label: Side
    menuOptions:
    - label: Negative
      name: neg
    - label: Positive
      name: pos
    name: Side
  - label: Amount
    name: Amount
  - label: Offset
    name: Offset
  - label: Spread
    name: Spread
  thumb: assets/images/reference/operators/filter/kink_thumb.png

---
