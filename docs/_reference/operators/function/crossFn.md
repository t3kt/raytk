---
layout: operator
title: crossFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/crossFn
redirect_from:
  - /reference/opType/raytk.operators.function.crossFn/
op:
  category: function
  detail: A mix value of 0 is the first, 1 is the second. Values outside that range
    will linearly scale, as though the two input values are two points and a line
    extends off in the same direction on each end.
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
    required: true
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
    required: true
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
    label: Blending Function
    name: mixField
    returnTypes:
    - float
    - vec4
    summary: Function used to get the mix value used to blend between the first two
      inputs.
  name: crossFn
  opType: raytk.operators.function.crossFn
  parameters:
  - label: Enable
    name: Enable
  - label: Mix
    name: Mix
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Cross-fade between the first two inputs. This is not used if the third
      input is connected.
  summary: Cross-fades between two input functions, either based on a parameter or
    on a third function.

---


Cross-fades between two input functions, either based on a parameter or on a third function.

A mix value of 0 is the first, 1 is the second. Values outside that range will linearly scale, as though the two input values are two points and a line extends off in the same direction on each end.