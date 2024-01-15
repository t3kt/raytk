---
layout: operator
title: applyTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/applyTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.applyTransform/
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 1
    name: transform
    required: true
    returnTypes:
    - vec4
  name: applyTransform
  opType: raytk.operators.filter.applyTransform
  parameters:
  - label: Enable
    name: Enable
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
  status: beta

---
