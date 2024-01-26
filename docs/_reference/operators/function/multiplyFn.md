---
layout: operator
title: multiplyFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/multiplyFn
redirect_from:
  - /reference/opType/raytk.operators.function.multiplyFn/
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
    - vec2
    - vec3
    - vec4
    label: Function 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp1
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
    label: Function 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-2]
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
    label: Function 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-3]
  name: multiplyFn
  opType: raytk.operators.function.multiplyFn
  parameters:
  - label: Enable
    name: Enable
  - label: Multiply
    name: Multiply
    summary: Multiply the values produced by the functions.
  summary: Multiplies the returned values produced by all of the connected input functions.

---


Multiplies the returned values produced by all of the connected input functions.