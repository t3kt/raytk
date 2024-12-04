---
layout: operator
title: rescaleFloatField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rescaleFloatField
redirect_from:
  - /reference/opType/raytk.operators.filter.rescaleFloatField/
op:
  category: filter
  detail: This can be applied to either float or vector fields. In the case of vector
    fields, the same settings are used for all parts of the incoming vectors.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input field
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
  name: rescaleFloatField
  opType: raytk.operators.filter.rescaleFloatField
  parameters:
  - label: Enable
    name: Enable
  - label: Input Range
    name: Inputrange
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low/high ends of the expected input values.
  - label: Output Range
    name: Outputrange
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low/high ends of the rescaled values.
  - label: Multiply
    name: Multiply
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Multiplier applied to values after range scaling.
  - label: Post Add
    name: Postadd
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount added to values after the other steps.
  summary: Simplified version of `rescaleField` that only has single settings vs vectors
    for each.

---


Simplified version of `rescaleField` that only has single settings vs vectors for each.

This can be applied to either float or vector fields. In the case of vector fields, the same settings are used for all parts of the incoming vectors.