---
layout: operator
title: rescaleField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rescaleField
redirect_from:
  - /reference/opType/raytk.operators.filter.rescaleField/
op:
  category: filter
  detail: 'This is equivalent to the "Range" parameters in a Math CHOP.


    It works for either float value fields or vector fields. When using a float value
    field, only the first part of each of the range parameters is used.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
  keywords:
  - range
  - remap
  - rescale
  name: rescaleField
  opType: raytk.operators.filter.rescaleField
  parameters:
  - label: Enable
    name: Enable
  - label: Input Low
    name: Inputlow
    summary: The low end of the expected input values.
  - label: Input High
    name: Inputhigh
    summary: The high end of the expected input values.
  - label: Output Low
    name: Outputlow
    summary: The low end of the rescaled value range.
  - label: Output High
    name: Outputhigh
    summary: The high end of the rescaled value range.
  - label: Multiply
    name: Mult
  - label: Multiply
    name: Multiply
  - label: Post Add
    name: Postadd
  summary: Rescales the values produced by a field.

---


Rescales the values produced by a field.

This is equivalent to the "Range" parameters in a Math CHOP.

It works for either float value fields or vector fields. When using a float value field, only the first part of each of the range parameters is used.