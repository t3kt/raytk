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
    returnTypes:
    - float
    - vec4
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
    label: definition_in_2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
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
    label: definition_in_3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
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
    label: definition_in_4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
  name: addFn
  opType: raytk.operators.function.addFn
  parameters:
  - label: Enable
    name: Enable
  - label: Add
    name: Add
    summary: Adds an additional value to the inputs.
  summary: Adds the returned values produced by all of the connected input functions.

---


Adds the returned values produced by all of the connected input functions.