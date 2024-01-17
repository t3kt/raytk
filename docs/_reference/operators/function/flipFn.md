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
    - description: Flips the x axis in the 0..1 range so that what used to be x=0
        is now x=1 and what used to be x=1 is now x=0.
      label: Flip 0-1 Domain
      name: flipdomain01
    - description: Flips the y (value) axis in the 0..1 range so that what used to
        be y=0 is now y=1 and what used to be y=1 is now y=0.
      label: Flip 0-1 Range
      name: fliprange01
    name: Fliptype
    summary: The type of flipping to apply.
  - label: Return Type
    menuOptions:
    - label: SDF Result
      name: Sdf
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
  summary: Function that flips its input in one of several different modes.

---


Function that flips its input in one of several different modes.