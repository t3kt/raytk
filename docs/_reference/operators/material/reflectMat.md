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
    - none
    - Context
    coordTypes:
    - vec3
    label: definition_in
    name: definition_in
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
    summary: Base color applied to the surface regardless of lights.
  - label: Ks
    name: Ks
  - label: Reflection Amount
    name: Reflectionamount
  - label: Fresnel
    name: Fresnel
  - label: Shine
    name: Shine
    summary: Specular exponent, which adjusts the light curve of specular highlights.
  - label: Enable Shadow
    name: Enableshadow
    summary: Whether to use shadows. When enabled, if the *Shadow Definition* input
      is provided, that will be used. Otherwise a default shadow function will be
      used.
  status: beta

---
