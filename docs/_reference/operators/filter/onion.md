---
layout: operator
title: onion
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/onion
redirect_from:
  - /reference/opType/raytk.operators.filter.onion/
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
  name: onion
  opType: raytk.operators.filter.onion
  parameters:
  - label: Enable
    name: Enable
  - label: Thickness
    name: Thickness

---
