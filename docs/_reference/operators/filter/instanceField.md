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
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
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
  - label: Swap Order
    name: Swaporder
    summary: Swaps the two inputs. This is only relevant for some of the `Operation`
      values.
  status: beta
  variables:
  - label: index
    name: index
  - label: normindex
    name: normindex

---
