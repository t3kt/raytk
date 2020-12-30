---
layout: operator
title: combineChamfer
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineChamfer
redirect_from:
  - /reference/opType/raytk.operators.combine.combineChamfer/
op:
  name: combineChamfer
  summary: |
    Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.
  opType: raytk.operators.combine.combineChamfer
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
    - name: Radius
      label: Radius
      summary: |
        The size of the blending region.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# combineChamfer

Category: combine



Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.