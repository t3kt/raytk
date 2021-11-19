---
layout: operator
title: backgroundFieldContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/backgroundFieldContrib
redirect_from:
  - /reference/opType/raytk.operators.material.backgroundFieldContrib/
op:
  category: material
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
  name: backgroundFieldContrib
  opType: raytk.operators.material.backgroundFieldContrib
  parameters:
  - label: Level
    name: Level
  status: beta

---
