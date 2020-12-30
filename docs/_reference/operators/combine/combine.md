---
layout: operator
title: combine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combine
redirect_from:
  - /reference/opType/raytk.operators.combine.combine/
op:
  name: combine
  summary: |
    Combines SDFs in various ways.
  detail: |
    Depending on which `Combine` option is selected, different parameters will be enabled.
    This operator only supports two input SDFs (along with a value field to control blending).
    To combine more than two SDFs, use one of the specialized operators like `simpleUnion`.
  opType: raytk.operators.combine.combine
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
    - name: definition_in_2
      label: definition_in_2
      required: true
    - name: radius_field_definition_in
      label: radius_field_definition_in
      required: false
  parameters:
    - name: Enable
      label: Enable
    - name: Combine
      label: Combine
      summary: |
        The type of combination operation to perform.
      menuOptions:
        - name: simpleUnion
          label: Simple Union
          description: |
            The combined areas of each of the inputs.
        - name: simpleIntersect
          label: Simple Intersect
          description: |
            The overlapping areas of each of the inputs.
        - name: simpleDiff
          label: Simple Difference
          description: |
            The first input with the second input removed from it.
        - name: smoothUnion
          label: Smooth Union
          description: |
            Like `simpleUnion` but with the intersecting edges rounded out.
        - name: smoothIntersect
          label: Smooth Intersect
          description: |
            Like `simpleIntersect` but with the intersecting edges rounded out.
        - name: smoothDiff
          label: Smooth Difference
          description: |
            Like `simpleDiff` but with the intersecting edges rounded out.
        - name: roundUnion
          label: Round Union
          description: |
            Uses a quarter circle blending area along the edges.
        - name: roundIntersect
          label: Round Intersect
        - name: roundDiff
          label: Round Difference
        - name: chamferUnion
          label: Chamfer Union
          description: |
            Uses a 45 degree flat slope to blend along the edges.
        - name: chamferIntersect
          label: Chamfer Intersect
        - name: chamferDiff
          label: Chamfer Difference
        - name: stairUnion
          label: Stair Union
          description: |
            Uses vertical and horizontal stairs to blend along the edges.
        - name: stairIntersect
          label: Stair Intersect
        - name: stairDiff
          label: Stair Difference
        - name: columnUnion
          label: Column Union
          description: |
            Uses multiple circular tubes to blend along the edges.
        - name: columnIntersect
          label: Column Intersect
        - name: columnDiff
          label: Column Difference
    - name: Swapinputs
      label: Swap Inputs
      summary: |
        Swaps the order of the inputs. This is only relevant for "diff" modes.
    - name: Radius
      label: Radius
      summary: |
        The size of the blending region.
    - name: Number
      label: Number
      summary: |
        For stair and column modes, this controls how many steps are used in the blending regions.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# combine

Category: combine



Combines SDFs in various ways.

Depending on which `Combine` option is selected, different parameters will be enabled.
This operator only supports two input SDFs (along with a value field to control blending).
To combine more than two SDFs, use one of the specialized operators like `simpleUnion`.