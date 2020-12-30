---
layout: operator
title: simpleDiff
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/simpleDiff
redirect_from:
  - /reference/opType/raytk.operators.combine.simpleDiff/
op:
  name: simpleDiff
  summary: |
    Combines two SDFs using the difference operator.
  detail: |
    Produces the area of the first shape minus any areas overlapped by the second (or vice versa).
  opType: raytk.operators.combine.simpleDiff
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
      summary: |
        The first SDF, which has the second removed from it (unless `Swaporder` is used).
    - name: definition_in_2
      label: definition_in_2
      required: true
      summary: |
        The second SDF, which is removed from the first (unless `Swaporder` is used).
  parameters:
    - name: Enable
      label: Enable
    - name: Swaporder
      label: Swap Order
      summary: |
        Swaps the two inputs, subtracting the first from the second.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# simpleDiff

Category: combine



Combines two SDFs using the difference operator.

Produces the area of the first shape minus any areas overlapped by the second (or vice versa).