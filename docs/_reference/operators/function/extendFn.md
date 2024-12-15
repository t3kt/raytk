---
layout: operator
title: extendFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/extendFn
redirect_from:
  - /reference/opType/raytk.operators.function.extendFn/
op:
  category: function
  detail: 'This is similar to the [Extend CHOP](https://docs.derivative.ca/Extend_CHOP).


    While primarily useful for 1D function operators, it also works for 2D and 3D
    operators, by applying the extend mode to each part of the coordinates.'
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  name: extendFn
  opType: raytk.operators.function.extendFn
  parameters:
  - label: Enable
    name: Enable
  - label: Extend Mode
    menuOptions:
    - label: Hold
      name: hold
    - label: Cycle
      name: cycle
    - label: Mirror
      name: mirror
    - label: Default Value
      name: default
    name: Extend
    readOnlyHandling: baked
    regularHandling: baked
  - label: Range
    name: Range
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Default Value
    name: Defval
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Defines the behavior of a function outside the normal expected range of
    coordinates.

---


Defines the behavior of a function outside the normal expected range of coordinates.

This is similar to the [Extend CHOP](https://docs.derivative.ca/Extend_CHOP).

While primarily useful for 1D function operators, it also works for 2D and 3D operators, by applying the extend mode to each part of the coordinates.