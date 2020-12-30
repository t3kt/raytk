---
layout: operator
title: flip
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/flip
redirect_from:
  - /reference/opType/raytk.operators.filter.flip/
op:
  name: flip
  opType: raytk.operators.filter.flip
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
    - name: Offset
      label: Offset
    - name: Shift
      label: Shift
    - name: Mergetype
      label: Merge Type
      menuOptions:
        - name: none
          label: None
        - name: union
          label: Union
        - name: smoothUnion
          label: Smooth Union
    - name: Mergeradius
      label: Merge Radius
    - name: Iterateonsides
      label: Iterate On Sides
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# flip

Category: filter

