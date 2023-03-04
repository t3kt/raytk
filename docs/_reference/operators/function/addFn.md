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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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