---
layout: operator
title: edgePipe
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgePipe
redirect_from:
  - /reference/opType/raytk.operators.combine.edgePipe/
op:
  name: edgePipe
  summary: Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.
  detail: |
    Creates an entirely new SDF result, removing any materials and other settings from the inputs.
  opType: raytk.operators.combine.edgePipe
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
    - name: Radius
      label: Radius
      summary: |
        The width of the pipe.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# edgePipe

Category: combine



Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.

Creates an entirely new SDF result, removing any materials and other settings from the inputs.