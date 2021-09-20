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
  detail: Texture is centered at 0,0 with coordinates from -0.5 to 0.5.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: UV Map Field
    name: uvField
    returnTypes:
    - vec4
    summary: When provided, this field is used to calculate the UV coordinates (in
      the x and y parts of the vec4).
  name: textureField
  opType: raytk.operators.field.textureField
  parameters:
  - label: Enable
    name: Enable
  - label: Coord Type
    menuOptions:
    - description: Uses the 1D coordinate as U and 0 for V.
      label: 1D
      name: float
    - description: Uses the provided 2D coordinates.
      label: 2D
      name: vec2
    - description: Uses the specified `Axis` to choose which axes to use for U and
        V.
      label: 3D
      name: vec3
    name: Coordtype
    summary: The type of coordinates used for UV mapping.
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
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
    summary: When used for materials, set to `MaterialContext`, otherwise use `Context`.
  - label: Plane
    menuOptions:
    - description: U=Y, V=Z
      label: YZ
      name: x
    - description: U=Z, V=X
      label: ZX
      name: y
    - description: U=X, V=Y
      label: XY
      name: z
    name: Axis
    summary: When using 3D coordinates, the axis that faces the plane used for UV.
      This is not used when a UV field input is attached.
  - label: Translate
    name: Translate
    summary: Offsets the UV coordinates.
  - label: Scale
    name: Scale
    summary: Scales the UV coordinates.
  - label: Texture
    name: Texture
    summary: TOP used for the texture.
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
    summary: How to handle UV coordinates outside the 0..1 range.
  summary: A float or vector field that looks up values from a texture.

---


A float or vector field that looks up values from a texture.

Texture is centered at 0,0 with coordinates from -0.5 to 0.5.