---
layout: operator
title: reorderField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/reorderField
redirect_from:
  - /reference/opType/raytk.operators.field.reorderField/
op:
  category: field
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
    label: definition_in_1
    name: definition_in_1
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
  name: reorderField
  opType: raytk.operators.field.reorderField
  parameters:
  - label: Enable
    name: Enable
  - label: Source X
    menuOptions:
    - label: None
      name: none
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Source1
  - label: Source Y
    menuOptions:
    - label: None
      name: none
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Source2
  - label: Source Z
    menuOptions:
    - label: None
      name: none
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Source3
  - label: Source W
    menuOptions:
    - label: None
      name: none
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Source4
  - label: Part X / Red
    menuOptions:
    - label: X / Red
      name: x
    - label: Y / Green
      name: y
    - label: Z / Blue
      name: z
    - label: W / Alpha
      name: w
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Part1
  - label: Part Y / Green
    menuOptions:
    - label: X / Red
      name: x
    - label: Y / Green
      name: y
    - label: Z / Blue
      name: z
    - label: W / Alpha
      name: w
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Part2
  - label: Part Z / Blue
    menuOptions:
    - label: X / Red
      name: x
    - label: Y / Green
      name: y
    - label: Z / Blue
      name: z
    - label: W / Alpha
      name: w
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Part3
  - label: Part W / Alpha
    menuOptions:
    - label: X / Red
      name: x
    - label: Y / Green
      name: y
    - label: Z / Blue
      name: z
    - label: W / Alpha
      name: w
    - label: Zero
      name: zero
    - label: One
      name: one
    name: Part4

---

# reorderField

Category: field

