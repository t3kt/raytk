---
layout: operator
title: boundsCheck
parent: Particles Operators
grand_parent: Operators
permalink: /reference/operators/particles/boundsCheck
redirect_from:
  - /reference/opType/raytk.operators.particles.boundsCheck/
op:
  category: particles
  inputs:
  - contextTypes:
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: bounds_in
    name: bounds
    returnTypes:
    - float
    - Sdf
  name: boundsCheck
  opType: raytk.operators.particles.boundsCheck
  parameters:
  - label: Active
    name: Active
  - label: Bound Center
    name: Boundcenter
  - label: Bound Box Size
    name: Boundboxsize
  status: alpha

---
