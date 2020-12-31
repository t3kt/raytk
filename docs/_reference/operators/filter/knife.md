---
layout: operator
title: knife
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/knife
redirect_from:
  - /reference/opType/raytk.operators.filter.knife/
op:
  name: knife
  summary: Cuts off an SDF along a plane.
  opType: raytk.operators.filter.knife
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Side
      label: Keep Side
      summary: |
        Which side of the cut to keep.
      menuOptions:
        - name: above
          label: Above Plane
        - name: below
          label: Below Plane
    - name: Offset
      label: Offset
      summary: |
        Shifts the cut plane along the axis that it faces.
    - name: Rotateplane
      label: Rotate Plane
      summary: |
        Rotate the cut plane in XYZ.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# knife

Category: filter



Cuts off an SDF along a plane.