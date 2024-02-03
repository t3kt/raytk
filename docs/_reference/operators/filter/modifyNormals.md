---
layout: operator
title: modifyNormals
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modifyNormals
redirect_from:
  - /reference/opType/raytk.operators.filter.modifyNormals/
op:
  category: filter
  detail: 'This must be used *within* the modular material network, rather than on
    an SDF that

    uses such a material. In other words, insert it between an operator like `diffuseContrib`

    and the `modularMat`.


    This can be combined with a `noiseField` or `textureField` to apply bump mapping
    to a surface.'
  inputs:
  - contextTypes:
    - MaterialContext
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Shading Element
    name: shadingElement
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    summary: Shading element that will use the modified normals. This should be something
      like `diffuseContrib` or `specularContrib`.
  - contextTypes:
    - MaterialContext
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Modifier Field
    name: modifierField
    returnTypes:
    - float
    - vec4
    summary: Field used to modify the normals.
  keywords:
  - bumpmap
  - material
  - modularmat
  - normals
  - shading
  - surface
  - texture
  name: modifyNormals
  opType: raytk.operators.filter.modifyNormals
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - description: The modifier values are added to the normals.
      label: Add
      name: add
    - description: The normals are multiplied by the modifier values.
      label: Multiply
      name: mul
    - label: Replace
      name: replace
    name: Mode
    summary: How the modifier values are applied to the normals.
  - label: Mix
    name: Mix
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Mix between the original normals and the modified normals.
  status: beta
  summary: Use a field to modify the normals (bump mapping) used by shading elements
    in a modular material.

---


Use a field to modify the normals (bump mapping) used by shading elements in a modular material.

This must be used *within* the modular material network, rather than on an SDF that
uses such a material. In other words, insert it between an operator like `diffuseContrib`
and the `modularMat`.

This can be combined with a `noiseField` or `textureField` to apply bump mapping to a surface.