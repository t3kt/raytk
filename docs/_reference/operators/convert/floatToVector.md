---
layout: operator
title: floatToVector
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/floatToVector
redirect_from:
  - /reference/opType/raytk.operators.convert.floatToVector/
op:
  category: convert
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
  name: floatToVector
  opType: raytk.operators.convert.floatToVector
  parameters:
  - label: Enable
    name: Enable
  - label: Part Source X
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Partsourcex
    summary: Which source to use for the X part of the vector field.
  - label: Part Source Y
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Partsourcey
  - label: Part Source Z
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Partsourcez
  - label: Part Source W
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Partsourcew
  summary: Converts one or more float value field inputs into a single vector value
    field.

---


Converts one or more float value field inputs into a single vector value field.