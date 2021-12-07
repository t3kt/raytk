---
layout: operator
title: mobiusTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mobiusTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.mobiusTransform/
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
  name: mobiusTransform
  opType: raytk.operators.filter.mobiusTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: The axis around which to twist.
  - label: Center
    name: Center
  - label: Point
    name: Point
  thumb: assets/images/reference/operators/filter/mobiusTransform_thumb.png

---
