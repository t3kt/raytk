---
layout: operator
title: textureField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/textureField
redirect_from:
  - /reference/opType/raytk.operators.field.textureField/
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
    label: UV Field
    name: uv_field_definition_in
    returnTypes:
    - vec4
  name: textureField
  opType: raytk.operators.field.textureField
  parameters:
  - label: Enable
    name: Enable
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
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Texture
    name: Texture
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
  summary: A float or vector field that looks up values from a texture.

---

# textureField

Category: field



A float or vector field that looks up values from a texture.