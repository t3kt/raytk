---
layout: operator
title: hsvColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/hsvColorField
redirect_from:
  - /reference/opType/raytk.operators.field.hsvColorField/
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
    label: Hue Field
    name: hue_field_definition_in
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
    label: Saturation Field
    name: saturation_field_definition_in
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
    label: Value Field
    name: value_field_definition_in
    returnTypes:
    - float
  name: hsvColorField
  opType: raytk.operators.field.hsvColorField
  parameters:
  - label: Hue Offset
    name: Hueoffset
  - label: Value
    name: Value
  - label: Saturation
    name: Saturation
  - label: Coord Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: Auto
      name: auto
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

---
