---
layout: operator
title: chopField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/chopField
redirect_from:
  - /reference/opType/raytk.operators.field.chopField/
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
    label: Coordinate Field
    name: coord_field_definition_in
    returnTypes:
    - float
    summary: If connected, this field is used to determine what position in the CHOP
      to use at each point.
  name: chopField
  opType: raytk.operators.field.chopField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: Which axis to use to determine the position in the CHOP to use.
  - label: Translate
    name: Translate
    summary: Offsets the coordinate value. This is applied before the "Extend Mode".
  - label: Scale
    name: Scale
    summary: Scales the coordinate value. This is applied before the "Extend Mode".
  - label: CHOP
    name: Chop
  - label: Extend Mode
    menuOptions:
    - description: Clamp the coordinates to the 0..1 range.
      label: Hold
      name: hold
    - description: Return zero outside of the 0..1 range.
      label: Zero
      name: zero
    - description: Repeat coordinates outside the 0..1 range.
      label: Repeat
      name: repeat
    - description: Repeat coordinates outside the 0..1 range, mirrored back and forth.
      label: Mirror
      name: mirror
    name: Extendmode
    summary: How to handle coordinates outside the 0..1 range.
  summary: Field that provides values from a CHOP.

---


Field that provides values from a CHOP.