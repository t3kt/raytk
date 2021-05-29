---
layout: operator
title: switch
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/switch
redirect_from:
  - /reference/opType/raytk.operators.combine.switch/
op:
  category: combine
  detail: Note that inputs that are not connected are skipped over when assigning
    numbers to them, so if inputs 1, 2, and 4 are connected, they will use indices
    0, 1, 2.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
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
    - Sdf
    - Ray
    - Light
  - contextTypes:
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
    - Sdf
    - Ray
    - Light
  - contextTypes:
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
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: switch
  opType: raytk.operators.combine.switch
  parameters:
  - label: Enable
    name: Enable
  - label: Source
    name: Source
    summary: When 0, the first source is used, 1 for the second, etc.
  summary: Switches between several inputs, without the need to rebuild the shader,
    allowing for fast switching.

---


Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.

Note that inputs that are not connected are skipped over when assigning numbers to them, so if inputs 1, 2, and 4 are connected, they will use indices 0, 1, 2.