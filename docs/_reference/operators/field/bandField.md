---
layout: operator
title: bandField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/bandField
redirect_from:
  - /reference/opType/raytk.operators.field.bandField/
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
    label: Coordinate Field
    name: coord_field_definition_in
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
    label: Inside Value Field
    name: inside_value_definition_in
    returnTypes:
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
    label: Outside Value Field
    name: outside_value_definition_in
    returnTypes:
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
    label: Blend Function
    name: blend_function_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: bandField
  opType: raytk.operators.field.bandField
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
  - label: Center
    name: Center
  - label: Width
    name: Width
  - label: Enable Blending
    name: Enableblending
  - label: Blending
    name: Blending
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Inside Value
    name: Insidevalue
  - label: Outside Value
    name: Outsidevalue
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype

---
