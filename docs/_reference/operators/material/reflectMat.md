---
layout: operator
title: reflectMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/reflectMat
redirect_from:
  - /reference/opType/raytk.operators.material.reflectMat/
op:
  category: material
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  name: reflectMat
  opType: raytk.operators.material.reflectMat
  parameters:
  - label: Enable
    name: Enable
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Base color applied to the surface regardless of lights.
  - label: Ks
    name: Ks
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Reflection Amount
    name: Reflectionamount
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Fresnel
    name: Fresnel
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Shine
    name: Shine
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Specular exponent, which adjusts the light curve of specular highlights.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to use shadows. When enabled, if the *Shadow Definition* input
      is provided, that will be used. Otherwise a default shadow function will be
      used.
  - label: Apply When
    menuOptions:
    - label: Always
      name: always
    - label: Only If Unassigned
      name: missing
    name: Condition
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/material/reflectMat_thumb.png

---
