---
layout: operator
title: instanceField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/instanceField
redirect_from:
  - /reference/opType/raytk.operators.filter.instanceField/
op:
  category: filter
  detail: Note that this multiplies the work of the input once per instance.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - index
    - normindex
  name: instanceField
  opType: raytk.operators.filter.instanceField
  parameters:
  - label: Enable
    name: Enable
  - label: Instance Count
    name: Instancecount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of copies to produce and merge.
  - label: Operation
    menuOptions:
    - label: Add
      name: add
    - label: Subtract
      name: sub
    - label: Multiply
      name: mul
    - label: Divide
      name: div
    - label: Average
      name: avg
    - label: Minimum
      name: min
    - label: Maximum
      name: max
    name: Operation
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: How the field values should be combined.
  - label: Swap Order
    name: Swaporder
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Swaps the two inputs. This is only relevant for some of the `Operation`
      values like subtraction.
  summary: Repeats an input field multiple times and combines the results.
  variables:
  - label: Index
    name: index
  - label: Normalized Index (0..1)
    name: normindex

---


Repeats an input field multiple times and combines the results.

Note that this multiplies the work of the input once per instance.