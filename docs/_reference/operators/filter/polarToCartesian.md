---
layout: operator
title: polarToCartesian
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/polarToCartesian
redirect_from:
  - /reference/opType/raytk.operators.filter.polarToCartesian/
op:
  category: filter
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
  name: polarToCartesian
  opType: raytk.operators.filter.polarToCartesian
  parameters:
  - label: Enable
    name: Enable
  - label: Conversion
    menuOptions:
    - label: From Spherical
      name: spherical
    - label: From Cylindrical X
      name: cylindricalx
    - label: From Cylindrical Y
      name: cylindricaly
    - label: From Cylindrical Z
      name: cylindricalz
    name: Conversion
    readOnlyHandling: semibaked
    regularHandling: runtime
  status: beta
  summary: Converts coordinates from polar to cartesian.

---


Converts coordinates from polar to cartesian.