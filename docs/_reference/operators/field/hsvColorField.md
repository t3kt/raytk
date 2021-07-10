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
  detail: By default, the X axis is used for the hue.
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
    summary: Optional field that can calculate the hue setting based on position or
      other attributes.
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
    summary: Optional field that can calculate the saturation setting based on position
      or other attributes.
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
    summary: Optional field that can calculate the value setting based on position
      or other attributes.
  name: hsvColorField
  opType: raytk.operators.field.hsvColorField
  parameters:
  - label: Hue Offset
    name: Hueoffset
  - label: Saturation
    name: Saturation
  - label: Value
    name: Value
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
  status: beta
  summary: A field that uses HSV-based parameters to produce colors.

---


A field that uses HSV-based parameters to produce colors.

By default, the X axis is used for the hue.