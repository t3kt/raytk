---
layout: operator
title: reflect
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reflect
redirect_from:
  - /reference/opType/raytk.operators.filter.reflect/
op:
  name: reflect
  summary: Reflects space across a plane.
  detail: |
    Can optionally expose which side of the plane a point is on as an iteration value for upstream ops.
  opType: raytk.operators.filter.reflect
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
    - name: blend_func_definition_in
      label: blend_func_definition_in
      required: false
  parameters:
    - name: Enable
      label: Enable
    - name: Direction
      label: Direction
      menuOptions:
        - name: custom
          label: Custom
        - name: xpos
          label: X+
        - name: xneg
          label: X-
        - name: ypos
          label: Y+
        - name: yneg
          label: Y-
        - name: zpos
          label: Z+
        - name: zneg
          label: Z-
    - name: Planenormal
      label: Plane Normal
    - name: Offset
      label: Offset
    - name: Shift
      label: Shift
    - name: Exposeiteration
      label: Expose Iteration
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# reflect

Category: filter



Reflects space across a plane.

Can optionally expose which side of the plane a point is on as an iteration value for upstream ops.