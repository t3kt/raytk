---
layout: operator
title: texture3dField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/texture3dField
redirect_from:
  - /reference/opType/raytk.operators.field.texture3dField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    supportedVariables:
    - RTK_raytk_operators_field_texture3dField_res
    - RTK_raytk_operators_field_texture3dField_aspect
    - RTK_raytk_operators_field_texture3dField_depth
    - RTK_raytk_operators_field_texture3dField_firstslice
  name: texture3dField
  opType: raytk.operators.field.texture3dField
  parameters:
  - label: Enable
    name: Enable
  - label: Texture Type
    menuOptions:
    - label: 3D
      name: 3d
    - label: Cube Map
      name: cube
    name: Texturetype
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Z Coord Mode
    menuOptions:
    - label: Raw
      name: raw
    - label: Normalized (0..1)
      name: norm
    - label: Depth (With Offset)
      name: depthoffset
    name: Zmode
    readOnlyHandling: semibaked
    regularHandling: runtime
  thumb: assets/images/reference/operators/field/texture3dField_thumb.png
  variables:
  - label: RTK_raytk_operators_field_texture3dField_res
    name: RTK_raytk_operators_field_texture3dField_res
  - label: RTK_raytk_operators_field_texture3dField_aspect
    name: RTK_raytk_operators_field_texture3dField_aspect
  - label: RTK_raytk_operators_field_texture3dField_depth
    name: RTK_raytk_operators_field_texture3dField_depth
  - label: RTK_raytk_operators_field_texture3dField_firstslice
    name: RTK_raytk_operators_field_texture3dField_firstslice

---
