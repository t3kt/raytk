---
layout: operator
title: modulo2D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo2D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo2D/
op:
  name: modulo2D
  summary: Repeats space along 2 axes.
  opType: raytk.operators.filter.modulo2D
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Axis
      label: Axis
      menuOptions:
        - name: x
          label: YZ
        - name: y
          label: ZX
        - name: z
          label: XY
    - name: Size
      label: Size
    - name: Offset
      label: Offset
    - name: Shift
      label: Shift
    - name: Mirrortype
      label: Mirror Type
      menuOptions:
        - name: none
          label: None
        - name: mirror
          label: Mirror
        - name: grid
          label: Grid
    - name: Iterateoncells
      label: Iterate On Cells
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# modulo2D

Category: filter



Repeats space along 2 axes.