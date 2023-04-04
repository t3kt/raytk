---
layout: operator
title: axisRotate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/axisRotate
redirect_from:
  - /reference/opType/raytk.operators.filter.axisRotate/
op:
  category: filter
  detail: In many cases this will be more efficient than `rotate`.
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
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
    summary: Field providing the amount of rotation, in degrees.
  name: axisRotate
  opType: raytk.operators.filter.axisRotate
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
  - label: Rotate
    name: Rotate
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
  summary: A simplified and optimized version of `rotate`, which only supports rotating
    around a single axis (x, y, or z).

---


A simplified and optimized version of `rotate`, which only supports rotating around a single axis (x, y, or z).

In many cases this will be more efficient than `rotate`.