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
    label: coord_field_definition_in
    name: coordField
    returnTypes:
    - float
  keywords:
  - color
  - gradient
  - ramp
  name: colorRampField
  opType: raytk.operators.field.colorRampField
  parameters:
  - label: Enable
    name: Enable
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
  - label: Color 1
    name: Color1
  - label: Alpha 1
    name: Alpha1
  - label: Color 2
    name: Color2
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
  summary: A vector field that maps an input field to values from a range of colors.

---


A vector field that maps an input field to values from a range of colors.