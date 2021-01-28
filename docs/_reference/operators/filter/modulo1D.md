---
layout: operator
title: modulo1D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo1D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo1D/
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
  name: modulo1D
  opType: raytk.operators.filter.modulo1D
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
    name: Mirrortype
  - label: Use Limit
    name: Uselimit
  - label: Limit Start
    name: Limitstart
  - label: Limit Stop
    name: Limitstop
  - label: Limit Offset
    name: Limitoffset
  - label: Iterate On Cells
    name: Iterateoncells
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# modulo1D

Category: filter

