---
layout: operator
title: quantizeValue
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quantizeValue
redirect_from:
  - /reference/opType/raytk.operators.filter.quantizeValue/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
  name: quantizeValue
  opType: raytk.operators.filter.quantizeValue
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size Multiplier
    name: Sizemult
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Smoothing
    name: Smoothing
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Smoothing Multiplier
    name: Smoothingmult

---
