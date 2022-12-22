---
layout: operator
title: coordTo2D
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/coordTo2D
redirect_from:
  - /reference/opType/raytk.operators.convert.coordTo2D/
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
  name: coordTo2D
  opType: raytk.operators.convert.coordTo2D
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - label: Custom
      name: custom
    - label: XY Plane
      name: xy
    - label: YX Plane
      name: yx
    - label: YZ Plane
      name: yz
    - label: ZY Plane
      name: zy
    - label: XZ Plane
      name: xz
    - label: ZX Plane
      name: zx
    name: Mode
  - label: Plane Offset
    name: Planeoffset
  - label: Part X
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Partx
  - label: Part Y
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Party
  - label: Part Z
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Partz
  summary: Converts a 3D (or 1D) operator to work in a 2D plane on the chosen axes.

---


Converts a 3D (or 1D) operator to work in a 2D plane on the chosen axes.