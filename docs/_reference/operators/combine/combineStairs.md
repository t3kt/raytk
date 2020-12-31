---
layout: operator
title: combineStairs
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineStairs
redirect_from:
  - /reference/opType/raytk.operators.combine.combineStairs/
op:
  name: combineStairs
  summary: Stair SDF combine, producing steps along the blend region.
  opType: raytk.operators.combine.combineStairs
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
    - name: offset_definition_in
      label: Offset Field
      required: false
      summary: |
        Value field that can be used to vary the offset of the stairs at different points in space, by *adding* to the value of the `Offset` parameter.
  parameters:
    - name: Enable
      label: Enable
    - name: Operation
      label: Operation
      summary: |
        The type of combine operation.
      menuOptions:
        - name: union
          label: Union
          description: |
            Produces the combined area of both inputs.
        - name: intersect
          label: Intersect
          description: |
            Produces the area where both inputs overlap.
        - name: diff
          label: Difference
          description: |
            Subtracts the second input from the first.
    - name: Swapinputs
      label: Swap Inputs
      summary: |
        Swaps the order of the inputs. This is only used for the `diff` mode.
    - name: Number
      label: Number
      summary: |
        The number of steps in the blending region.
    - name: Radius
      label: Radius
      summary: |
        The size of the blending region.
    - name: Offset
      label: Offset
      summary: |
        Shifts the steps along the blend region, with 0 being no shift, and 1 being a full shift of the total number of steps.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# combineStairs

Category: combine



Stair SDF combine, producing steps along the blend region.