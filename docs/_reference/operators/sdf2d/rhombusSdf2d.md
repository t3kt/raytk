---
layout: operator
title: rhombusSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/rhombusSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.rhombusSdf2d/
op:
  category: sdf2d
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  name: rhombusSdf2d
  opType: raytk.operators.sdf2d.rhombusSdf2d
  parameters:
  - label: Scale
    name: Scale
    summary: The size of the rhombus along the X and Y axes.
  summary: SDF for a 2D rhombus (diamond), with its corners aligned to the axes.

---


SDF for a 2D rhombus (diamond), with its corners aligned to the axes.