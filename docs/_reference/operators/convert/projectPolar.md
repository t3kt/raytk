---
layout: operator
title: projectPolar
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/projectPolar
redirect_from:
  - /reference/opType/raytk.operators.convert.projectPolar/
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
    - vec3
    - vec4
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
  name: projectPolar
  opType: raytk.operators.convert.projectPolar
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Projection
    menuOptions:
    - label: Spherical
      name: spherical
    - label: Cylindrical
      name: cylindrical
    - label: Toroid
      name: toroid
    name: Projection
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Height
    name: Height
  status: beta
  summary: Projects coordinates into various types of polar spaces.

---


Projects coordinates into various types of polar spaces.