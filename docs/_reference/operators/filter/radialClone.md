---
layout: operator
title: radialClone
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/radialClone
redirect_from:
  - /reference/opType/raytk.operators.filter.radialClone/
op:
  name: radialClone
  summary: |
    Repeats an SDF radially around an axis, combining the resulting shapes.
  detail: |
    Note that this runs its input multiple times, which can lead to performance issues.
  opType: raytk.operators.filter.radialClone
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
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Count
      label: Count
    - name: Anglerange
      label: Angle Range
    - name: Angleoffset
      label: Angle Offset
    - name: Radiusoffset
      label: Radius Offset
    - name: Mergetype
      label: Merge Type
      menuOptions:
        - name: union
          label: Union
        - name: smoothunion
          label: Smooth Union
    - name: Mergeradius
      label: Merge Radius
    - name: Iterationtype
      label: Iteration Type
      menuOptions:
        - name: none
          label: None
        - name: index
          label: Clone Index
        - name: scaled
          label: Scaled Clone Index
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# radialClone

Category: filter



Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.