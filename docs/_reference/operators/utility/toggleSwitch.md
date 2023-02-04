---
layout: operator
title: toggleSwitch
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/toggleSwitch
redirect_from:
  - /reference/opType/raytk.operators.utility.toggleSwitch/
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
    label: Default
    name: default_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: toggleSwitch
  opType: raytk.operators.utility.toggleSwitch
  parameters:
  - label: Enable
    name: Enable
  - label: Default Value
    name: Defaultvalue
  status: deprecated

---
