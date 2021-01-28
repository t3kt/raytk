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
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
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
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
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
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
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
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
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
  name: switch
  opType: raytk.operators.combine.switch
  parameters:
  - label: Enable
    name: Enable
  - label: Source
    name: Source
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Switches between several inputs, without the need to rebuild the shader,
    allowing for fast switching.

---

# switch

Category: combine



Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.