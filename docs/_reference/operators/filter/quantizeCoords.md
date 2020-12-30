---
layout: operator
title: quantizeCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quantizeCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.quantizeCoords/
op:
  name: quantizeCoords
  summary: |
    Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.
  opType: raytk.operators.filter.quantizeCoords
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Size
      label: Size
    - name: Sizemult
      label: Size Multiplier
    - name: Offset
      label: Offset
    - name: Smoothing
      label: Smoothing
    - name: Smoothingmult
      label: Smoothing Multiplier
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# quantizeCoords

Category: filter



Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.