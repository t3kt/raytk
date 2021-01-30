---
layout: operator
title: combineFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineFields
redirect_from:
  - /reference/opType/raytk.operators.combine.combineFields/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
  name: combineFields
  opType: raytk.operators.combine.combineFields
  parameters:
  - label: Enable
    name: Enable
  - label: Operation
    menuOptions:
    - label: 'Off'
      name: 'off'
    - label: Add
      name: add
    - label: Subtract
      name: sub
    - label: Multiply
      name: mul
    - label: Divide
      name: div
    - label: Average
      name: avg
    - label: Minimum
      name: min
    - label: Maximum
      name: max
    name: Operation
  - label: Swap Order
    name: Swaporder
  summary: Combines float or vector fields using one of several mathematical operations.

---

# combineFields

Category: combine



Combines float or vector fields using one of several mathematical operations.