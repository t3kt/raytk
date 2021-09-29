---
layout: operator
title: linkedTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/linkedTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.linkedTransform/
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
  name: linkedTransform
  opType: raytk.operators.filter.linkedTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Object
    name: Object
  status: alpha

---
