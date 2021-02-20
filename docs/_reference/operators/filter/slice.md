---
layout: operator
title: slice
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/slice
redirect_from:
  - /reference/opType/raytk.operators.filter.slice/
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
    - Sdf
  name: slice
  opType: raytk.operators.filter.slice
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Offset
    name: Offset
  - label: Thickness
    name: Thickness
  - label: Enable Smoothing
    name: Enablesmoothing
  - label: Smooth Radius
    name: Smoothradius
  - label: Enable Mirror
    name: Enablemirror

---
