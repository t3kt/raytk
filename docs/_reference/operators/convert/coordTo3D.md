---
layout: operator
title: coordTo3D
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/coordTo3D
redirect_from:
  - /reference/opType/raytk.operators.convert.coordTo3D/
op:
  category: convert
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    label: 1D / 2D Input
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: coordTo3D
  opType: raytk.operators.convert.coordTo3D
  parameters:
  - label: Enable
    name: Enable
  - label: Part X
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Zero
      name: zero
    name: Partx
  - label: Part Y
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Zero
      name: zero
    name: Party
  summary: Converts a 2D (or 1D) operator to work in a 3D context.

---


Converts a 2D (or 1D) operator to work in a 3D context.