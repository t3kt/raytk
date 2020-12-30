---
layout: operator
title: edgeEngrave
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeEngrave
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeEngrave/
op:
  name: edgeEngrave
  summary: |
    Carves a v-shaped groove where the second input intersects with the first.
  opType: raytk.operators.combine.edgeEngrave
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
    - name: definition_in_2
      label: definition_in_2
      required: true
    - name: radius_definition_in
      label: Radius Field
      required: false
      summary: |
        Value field that can be used to vary the radius of the groove at different points in space, by *multiplying* the value of the `Radius` parameter.
  parameters:
    - name: Enable
      label: Enable
    - name: Swapinputs
      label: Swap Inputs
    - name: Radius
      label: Radius
      summary: |
        Width of the groove.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# edgeEngrave

Category: combine



Carves a v-shaped groove where the second input intersects with the first.