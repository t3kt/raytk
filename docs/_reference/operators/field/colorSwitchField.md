---
layout: operator
title: colorSwitchField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorSwitchField
redirect_from:
  - /reference/opType/raytk.operators.field.colorSwitchField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: indexField
    required: true
    returnTypes:
    - float
  name: colorSwitchField
  opType: raytk.operators.field.colorSwitchField
  parameters:
  - label: Extend
    menuOptions:
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    - label: Zig-Zag
      name: zigzag
    name: Extend
  - label: Blend Indices
    name: Blendindices
  - label: Offset
    name: Offset
  - label: Count
    name: Count
  - label: Color 1
    name: Color1
  - label: Color 2
    name: Color2
  - label: Color 3
    name: Color3
  - label: Color 4
    name: Color4
  - label: Color 5
    name: Color5
  - label: Color 6
    name: Color6
  - label: Color 7
    name: Color7
  - label: Color 8
    name: Color8
  status: beta

---
