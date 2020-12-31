---
layout: operator
title: smoothUnion
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/smoothUnion
redirect_from:
  - /reference/opType/raytk.operators.combine.smoothUnion/
op:
  name: smoothUnion
  summary: Combines SDFs using a smooth union operator.
  detail: |
    Produces the combined areas of the input shapes, blended to smooth out the intersections.
  opType: raytk.operators.combine.smoothUnion
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
      summary: |
        The first SDF to combine.
    - name: definition_in_2
      label: definition_in_2
      required: true
      summary: |
        The second SDF to combine.
    - name: definition_in_3
      label: Radius Field
      required: false
      summary: |
        Float value field that can vary the amount of blending at different points in space.
  parameters:
    - name: Enable
      label: Enable
    - name: Amount
      label: Amount
      summary: |
        Size of the blending region.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# smoothUnion

Category: combine



Combines SDFs using a smooth union operator.

Produces the combined areas of the input shapes, blended to smooth out the intersections.