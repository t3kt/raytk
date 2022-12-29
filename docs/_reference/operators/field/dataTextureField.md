---
layout: operator
title: dataTextureField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/dataTextureField
redirect_from:
  - /reference/opType/raytk.operators.field.dataTextureField/
op:
  category: field
  detail: This is designed to be used with pointMapRender to load in precomputed data
    that follows the same pixel layout as the coordinate map, or with cameraRemap
    to use a UV map to change where each pixel's ray starts.
  name: dataTextureField
  opType: raytk.operators.field.dataTextureField
  parameters:
  - label: Texture
    name: Texture
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  status: beta
  summary: Accesses data from a texture with the same layout as the renderer.

---


Accesses data from a texture with the same layout as the renderer.

This is designed to be used with pointMapRender to load in precomputed data that follows the same pixel layout as the coordinate map, or with cameraRemap to use a UV map to change where each pixel's ray starts.