---
layout: operator
title: mergeFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/mergeFields
redirect_from:
  - /reference/opType/raytk.operators.combine.mergeFields/
op:
  category: combine
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
  name: mergeFields
  opType: raytk.operators.combine.mergeFields
  parameters:
  - label: Enable
    name: Enable
  - label: X Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcex
  - label: Y Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcey
  - label: Z Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcez
  - label: W Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcew

---
