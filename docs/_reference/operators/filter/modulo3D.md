---
layout: operator
title: modulo3D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo3D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo3D/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    coordTypes:
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
  name: modulo3D
  opType: raytk.operators.filter.modulo3D
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
  - label: Offset
    name: Offset
  - label: Shift
    name: Shift
  summary: Repeats space along all 3 axes.

---

# modulo3D

Category: filter



Repeats space along all 3 axes.