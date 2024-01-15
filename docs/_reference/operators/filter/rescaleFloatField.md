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
  - label: Output Range
    name: Outputrange
  - label: Multiply
    name: Multiply
  - label: Post Add
    name: Postadd

---
