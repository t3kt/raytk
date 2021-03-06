---
layout: operator
title: triPlanarTextureField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/triPlanarTextureField
redirect_from:
  - /reference/opType/raytk.operators.field.triPlanarTextureField/
op:
  category: field
  detail: 'On a cube centered at the origin, this has the effect of placing the texture
    on each side of the cube.

    For a sphere, the texture for each axis will smoothly blend as the surface normal
    shifts from one axis to another.


    Textures are centered at 0,0 with coordinates ranging from -0.5 to 0.5.'
  name: triPlanarTextureField
  opType: raytk.operators.field.triPlanarTextureField
  parameters:
  - label: Enable
    name: Enable
  - label: Return Type
    menuOptions:
    - description: Single float value (from the R channel).
      label: Float
      name: float
    - description: RGBA values.
      label: Vector
      name: vec4
    name: Returntype
    summary: Type of value to produce.
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Use Separate Textures
    name: Useseparatetextures
    summary: Whether to use a single texture for all axes, or a separate texture for
      each axis.
  - label: Texture
    name: Texture
  - label: Texture X
    name: Texturex
  - label: Texture Y
    name: Texturey
  - label: Texture Z
    name: Texturez
  - label: Extend Mode
    menuOptions:
    - description: Clamp the coordinates so that the last pixel on each side is extended
        out infinitely.
      label: Hold
      name: hold
    - description: Produces values of 0 outside the bounds.
      label: Zero
      name: zero
    - description: Tiles the texture.
      label: Repeat
      name: repeat
    - description: Tiles the texture, but flips alternating copies of it.
      label: Mirror
      name: mirror
    name: Extendmode
    summary: How to handle coordinates outside the texture's bounds.
  summary: Texture field that uses surface normals to apply a texture facing each
    axis.

---


Texture field that uses surface normals to apply a texture facing each axis.

On a cube centered at the origin, this has the effect of placing the texture on each side of the cube.
For a sphere, the texture for each axis will smoothly blend as the surface normal shifts from one axis to another.

Textures are centered at 0,0 with coordinates ranging from -0.5 to 0.5.