---
layout: operator
title: flipFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/flipFn
redirect_from:
  - /reference/opType/raytk.operators.function.flipFn/
op:
  category: function
  inputs:
  - contextTypes:
    - none
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
  name: flipFn
  opType: raytk.operators.function.flipFn
  parameters:
  - label: Enable
    name: Enable
  - label: Flip Type
    menuOptions:
    - description: Negates the coordinate passed to the input function, flipping the
        x axis of a function graph across the y axis.
      label: Flip Domain
      name: flipdomain
    - description: Negates the input function's return value, flipping the y axis
        of a function graph across the x axis.
      label: Flip Range
      name: fliprange
    - description: Mirrors the coordinate so only the positive half is used, reflecting
        the positive side of a function graph across the y axis replacing the negative
        side.
      label: Mirror Positive Domain
      name: mirrorposdomain
    - description: Mirrors the coordinate so only the positive half is used, but also
        flips the return value when on the negative side, reflecting the positive
        side of a function graph across the y axis but then also flipping that side
        upside down.
      label: Flip Negative Domain
      name: flipnegdomain
    name: Fliptype
    summary: The type of flipping to apply.
  - label: Return Type
    menuOptions:
    - label: Sdf
      name: Sdf
    - label: vec4
      name: vec4
    - label: float
      name: float
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
  - label: Context Type
    menuOptions:
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: Function that flips its input in one of several different modes.

---


Function that flips its input in one of several different modes.