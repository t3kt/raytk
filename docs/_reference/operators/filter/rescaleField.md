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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
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
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low end of the expected input values.
  - label: Input High
    name: Inputhigh
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The high end of the expected input values.
  - label: Output Low
    name: Outputlow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low end of the rescaled value range.
  - label: Output High
    name: Outputhigh
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The high end of the rescaled value range.
  - label: Return Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Multiply
    name: Multiply
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Multiply
    name: Mult
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Post Add
    name: Postadd
    readOnlyHandling: baked
    regularHandling: runtime
  shortcuts:
  - rf
  summary: Rescales the values produced by a field.

---


Rescales the values produced by a field.

This is equivalent to the "Range" parameters in a Math CHOP.

It works for either float value fields or vector fields. When using a float value field, only the first part of each of the range parameters is used.