---
layout: operator
title: cartesianToPolar
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/cartesianToPolar
redirect_from:
  - /reference/opType/raytk.operators.filter.cartesianToPolar/
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
  name: cartesianToPolar
  opType: raytk.operators.filter.cartesianToPolar
  parameters:
  - label: Enable
    name: Enable
  - label: Conversion
    menuOptions:
    - label: Spherical
      name: spherical
    - label: Cylindrical X
      name: cylindricalx
    - label: Cylindrical Y
      name: cylindricaly
    - label: Cylindrical Z
      name: cylindricalz
    - label: Log-Cylindrical X
      name: logcylindricalx
    - label: Log-Cylindrical Y
      name: logcylindricaly
    - label: Log-Cylindrical Z
      name: logcylindricalz
    name: Conversion
  - label: Angle Unit
    menuOptions:
    - label: Ratio (0..1)
      name: ratio
    - label: Degrees
      name: degrees
    - label: Radians
      name: radians
    name: Angleunit
  summary: Convert from cartesian space to various types of polar spaces.
  thumb: assets/images/reference/operators/filter/cartesianToPolar_thumb.png

---


Convert from cartesian space to various types of polar spaces.