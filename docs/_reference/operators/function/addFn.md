---
layout: operator
title: addFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/addFn
redirect_from:
  - /reference/opType/raytk.operators.function.addFn/
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
    supportedVariableInputs:
    - inputOp[1-3]
  name: addFn
  opType: raytk.operators.function.addFn
  parameters:
  - label: Enable
    name: Enable
  - label: Add
    name: Add
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Adds an additional value to the inputs.
  summary: Adds the returned values produced by all of the connected input functions.

---


Adds the returned values produced by all of the connected input functions.