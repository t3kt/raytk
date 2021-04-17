---
layout: operator
title: colorRampField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorRampField
redirect_from:
  - /reference/opType/raytk.operators.field.colorRampField/
op:
  category: field
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
    label: definition_in
    name: definition_in
    returnTypes:
    - float
  name: colorRampField
  opType: raytk.operators.field.colorRampField
  parameters:
  - label: Enable
    name: Enable
  - label: Color 1
    name: Color1
  - label: Color 2
    name: Color2
  - label: Alpha 1
    name: Alpha1
  - label: Alpha 2
    name: Alpha2
  - label: Extend Mode
    menuOptions:
    - label: Hold
      name: hold
    - label: Zero
      name: zero
    - label: Repeat
      name: repeat
    - label: Mirror
      name: mirror
    name: Extendmode
  - label: Context Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    - label: Ray Context
      name: RayContext
    name: Contexttype
  summary: A vector field that maps an input field to values from a range of colors.

---


A vector field that maps an input field to values from a range of colors.