---
layout: operator
title: edgeGroove
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeGroove
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeGroove/
op:
  name: edgeGroove
  summary: |
    Creates a raised bar or indented groove where the second input intersects with the first.
  opType: raytk.operators.combine.edgeGroove
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
    - name: definition_in_2
      label: definition_in_2
      required: true
    - name: radius_definition_in
      label: Radius Field
      required: false
      summary: |
        Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.
  parameters:
    - name: Enable
      label: Enable
    - name: Function
      label: Function
      menuOptions:
        - name: groove
          label: Groove
        - name: tongue
          label: Tongue
    - name: Swapinputs
      label: Swap Inputs
    - name: Depth
      label: Depth
      summary: |
        The depth/height of the bar/groove.
    - name: Radius
      label: Radius
      summary: |
        The width of the bar/groove.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# edgeGroove

Category: combine



Creates a raised bar or indented groove where the second input intersects with the first.