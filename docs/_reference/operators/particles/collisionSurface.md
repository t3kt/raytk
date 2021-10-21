---
layout: operator
title: collisionSurface
parent: Particles Operators
grand_parent: Operators
permalink: /reference/operators/particles/collisionSurface
redirect_from:
  - /reference/opType/raytk.operators.particles.collisionSurface/
op:
  category: particles
  inputs:
  - contextTypes:
    - ParticleContext
    coordTypes:
    - vec3
    label: surface_sdf_in
    name: surface
    required: true
    returnTypes:
    - Sdf
  name: collisionSurface
  opType: raytk.operators.particles.collisionSurface
  parameters:
  - label: Active
    name: Active
  - label: Behavior
    menuOptions:
    - label: None
      name: none
    - label: Kill
      name: kill
    - label: Bounce
      name: bounce
    name: Behavior
  status: alpha

---
