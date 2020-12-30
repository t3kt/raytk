---
layout: operator
title: limitField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitField
redirect_from:
  - /reference/opType/raytk.operators.filter.limitField/
op:
  name: limitField
  opType: raytk.operators.filter.limitField
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Limittype
      label: Limit Type
      menuOptions:
        - name: off
          label: Off
        - name: clamp
          label: Clamp
        - name: loop
          label: Loop
        - name: zigzag
          label: Zig-Zag
    - name: Low
      label: Input Low
    - name: High
      label: Input High
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# limitField

Category: filter

