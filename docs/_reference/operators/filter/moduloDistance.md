---
layout: operator
title: moduloDistance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloDistance
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloDistance/
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
  name: moduloDistance
  opType: raytk.operators.filter.moduloDistance
  parameters:
  - label: Enable
    name: Enable
  - label: Distance Mode
    menuOptions:
    - label: X Axis
      name: xaxis
    - label: Y Axis
      name: yaxis
    - label: Z Axis
      name: zaxis
    - label: Spherical
      name: spherical
    name: Distancemode
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
  - label: Length
    name: Length
  - label: Center
    name: Center
  - label: Iterate On Rings
    name: Iterateonrings
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# moduloDistance

Category: filter

