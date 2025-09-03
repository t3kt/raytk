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
    - VertexContext
    - PixelContext
    - PopContext
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
    - res
    - aspect
    - depth
    - firstslice
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
  - label: Resolution
    name: res
  - label: Aspect Ratio
    name: aspect
  - label: Depth
    name: depth
  - label: First Slice
    name: firstslice

---
