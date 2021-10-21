---
layout: operator
title: particleSystem
parent: Particles Operators
grand_parent: Operators
permalink: /reference/operators/particles/particleSystem
redirect_from:
  - /reference/opType/raytk.operators.particles.particleSystem/
op:
  category: particles
  inputs:
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Particle Spawn
    name: spawn
    returnTypes:
    - Particle
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Particle Process 1
    name: process1
    returnTypes:
    - Particle
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Particle Process 2
    name: process2
    returnTypes:
    - Particle
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Particle Process 3
    name: process3
    returnTypes:
    - Particle
  name: particleSystem
  opType: raytk.operators.particles.particleSystem
  parameters:
  - label: Resolution
    name: Res
  - label: Max Particles
    name: Maxparticles
  - label: Reset
    name: Reset
  - label: Reset Pulse
    name: Resetpulse
  - label: Time Reference Operator
    name: Timerefop
  status: alpha

---
