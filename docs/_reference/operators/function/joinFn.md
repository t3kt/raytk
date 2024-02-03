---
layout: operator
title: joinFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/joinFn
redirect_from:
  - /reference/opType/raytk.operators.function.joinFn/
op:
  category: function
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
    label: Function 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
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
    label: Function 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
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
    label: Function 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
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
    label: Function 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
  name: joinFn
  opType: raytk.operators.function.joinFn
  parameters:
  - label: Enable
    name: Enable
  - label: Fit To Range
    name: Fitrange
    readOnlyHandling: macro
    regularHandling: macro
    summary: When enabled, the combined function is scaled back to a 0..1 range. Otherwise,
      coordinates 0..1 go to the first function, 1..2 to the second, etc.
  summary: Joins functions end on end.

---


Joins functions end on end.