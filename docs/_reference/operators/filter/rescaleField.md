---
layout: operator
title: rescaleField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rescaleField
redirect_from:
  - /reference/opType/raytk.operators.filter.rescaleField/
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
  name: rescaleField
  opType: raytk.operators.filter.rescaleField
  parameters:
  - label: Enable
    name: Enable
  - label: Input Low
    name: Inputlow
  - label: Input High
    name: Inputhigh
  - label: Output Low
    name: Outputlow
  - label: Output High
    name: Outputhigh
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# rescaleField

Category: filter

