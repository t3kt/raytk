---
layout: operator
title: boundLimit
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/boundLimit
redirect_from:
  - /reference/opType/raytk.operators.combine.boundLimit/
op:
  category: combine
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
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - Sdf
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
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - Sdf
  name: boundLimit
  opType: raytk.operators.combine.boundLimit
  parameters:
  - label: Enable
    name: Enable
  status: alpha

---
