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
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
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
  - label: Z Coord Mode
    menuOptions:
    - label: Raw
      name: raw
    - label: Normalized (0..1)
      name: norm
    - label: Depth (With Offset)
      name: depthoffset
    name: Zmode
  status: beta
  thumb: assets/images/reference/operators/field/texture3dField_thumb.png
  variables:
  - label: res
    name: res
  - label: aspect
    name: aspect
  - label: depth
    name: depth
  - label: firstslice
    name: firstslice

---
