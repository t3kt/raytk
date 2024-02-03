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
    - Sdf
  name: quantizeValue
  opType: raytk.operators.filter.quantizeValue
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Size Multiplier
    name: Sizemult
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: constant
    regularHandling: constant
  - label: Smoothing
    name: Smoothing
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Smoothing Multiplier
    name: Smoothingmult

---
