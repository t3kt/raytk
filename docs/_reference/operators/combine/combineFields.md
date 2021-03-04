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
    - description: Only use the first input (or second depending on `Swaporder`).
      label: 'Off'
      name: 'off'
    - description: Add the fields.
      label: Add
      name: add
    - description: Subtract the second from the first.
      label: Subtract
      name: sub
    - description: Multiply the fields.
      label: Multiply
      name: mul
    - description: Divide the first by the second.
      label: Divide
      name: div
    - description: Average the fields.
      label: Average
      name: avg
    - description: Use the smaller of the field values.
      label: Minimum
      name: min
    - description: Use the larger of the field values.
      label: Maximum
      name: max
    name: Operation
    summary: What operation to use to combine the field values.
  - label: Swap Order
    name: Swaporder
    summary: Swaps the two inputs. This is only relevant for some of the `Operation`
      values.
  summary: Combines float or vector fields using one of several mathematical operations.

---


Combines float or vector fields using one of several mathematical operations.