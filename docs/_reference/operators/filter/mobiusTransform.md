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
    label: Center Field
    name: centerField
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
    label: Point Field
    name: pointField
    returnTypes:
    - vec4
  name: mobiusTransform
  opType: raytk.operators.filter.mobiusTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: XZ
      name: y
    - label: XY
      name: z
    name: Axis
    summary: The plane whose axes will be transformed.
  - label: Center
    name: Center
  - label: Point
    name: Point
  thumb: assets/images/reference/operators/filter/mobiusTransform_thumb.png

---
