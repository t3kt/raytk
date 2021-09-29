---
layout: operator
title: spawnParticles
parent: Particles Operators
grand_parent: Operators
permalink: /reference/operators/particles/spawnParticles
redirect_from:
  - /reference/opType/raytk.operators.particles.spawnParticles/
op:
  category: particles
  inputs:
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: position_field_in
    name: positionField
    returnTypes:
    - vec4
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: direction_field_in
    name: directionField
    returnTypes:
    - vec4
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: velocity_field_in
    name: velocityField
    returnTypes:
    - float
    - vec4
  name: spawnParticles
  opType: raytk.operators.particles.spawnParticles
  parameters:
  - label: Active
    name: Active
  - label: Position Mode
    menuOptions:
    - label: Point
      name: point
    name: Positionmode
  - label: Point
    name: Point
  - label: Life
    name: Life
  - label: Life Jitter
    name: Lifejitter
  status: alpha

---
