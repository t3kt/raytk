---
layout: operator
title: combineFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineFields
redirect_from:
  - /reference/opType/raytk.operators.combine.combineFields/
op:
  name: combineFields
  summary: |
    Combines float or vector fields using one of several mathematical operations.
  opType: raytk.operators.combine.combineFields
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
    - name: definition_in_2
      label: definition_in_2
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Operation
      label: Operation
      menuOptions:
        - name: off
          label: Off
        - name: add
          label: Add
        - name: sub
          label: Subtract
        - name: mul
          label: Multiply
        - name: div
          label: Divide
        - name: avg
          label: Average
        - name: min
          label: Minimum
        - name: max
          label: Maximum
    - name: Swaporder
      label: Swap Order
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# combineFields

Category: combine



Combines float or vector fields using one of several mathematical operations.