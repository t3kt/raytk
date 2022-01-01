---
layout: operator
title: provideVariable
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/provideVariable
redirect_from:
  - /reference/opType/raytk.operators.utility.provideVariable/
op:
  category: utility
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
  name: provideVariable
  opType: raytk.operators.utility.provideVariable
  parameters:
  - label: Enable
    name: Enable
  - label: Name
    name: Name
  - label: Label
    name: Label
  - label: Data Type
    menuOptions:
    - label: float
      name: float
    - label: vec4
      name: vec4
    name: Datatype
  - label: Value
    name: Value
  status: beta

---
