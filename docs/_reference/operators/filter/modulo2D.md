---
layout: operator
title: modulo2D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo2D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo2D/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
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
  name: modulo2D
  opType: raytk.operators.filter.modulo2D
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
  - label: Size
    name: Size
  - label: Offset
    name: Offset
  - label: Shift
    name: Shift
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    - label: Grid
      name: grid
    name: Mirrortype
  - label: Iterate On Cells
    name: Iterateoncells
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Repeats space along 2 axes.

---

# modulo2D

Category: filter



Repeats space along 2 axes.