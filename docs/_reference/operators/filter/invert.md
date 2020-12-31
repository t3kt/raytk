---
layout: operator
title: invert
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/invert
redirect_from:
  - /reference/opType/raytk.operators.filter.invert/
op:
  name: invert
  summary: Invert an SDF, so that the inside is the outside.
  detail: |
    If used on a box, this can create an empty room with the shape filling all the space outside the room.
  opType: raytk.operators.filter.invert
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# invert

Category: filter



Invert an SDF, so that the inside is the outside.

If used on a box, this can create an empty room with the shape filling all the space outside the room.