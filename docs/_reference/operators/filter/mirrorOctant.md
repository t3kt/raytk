---
layout: operator
title: mirrorOctant
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorOctant
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorOctant/
op:
  name: mirrorOctant
  summary: Mirror coordinates across two axes and the diagonals.
  opType: raytk.operators.filter.mirrorOctant
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
    - name: Rotateaxis
      label: Rotate Axis
    - name: Iterateoncells
      label: Iterate On Cells
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# mirrorOctant

Category: filter



Mirror coordinates across two axes and the diagonals.