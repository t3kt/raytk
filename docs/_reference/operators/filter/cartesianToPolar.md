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
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
    name: Conversion

---
