---
layout: operator
title: reflectMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/reflectMat
redirect_from:
  - /reference/opType/raytk.operators.material.reflectMat/
op:
  name: reflectMat
  opType: raytk.operators.material.reflectMat
  category: material
  status: beta
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec3]
      contextTypes: [none,Context]
      returnTypes: [Sdf]
    - name: shadow_definition_in
      label: Shadow Definition
      required: false
      coordTypes: [vec3]
      contextTypes: [MaterialContext]
      returnTypes: [float]
  parameters:
    - name: Enable
      label: Enable
    - name: Color
      label: Color
      summary: |
        Base color applied to the surface regardless of lights.
    - name: Ks
      label: Ks
    - name: Reflectionamount
      label: Reflection Amount
    - name: Fresnel
      label: Fresnel
    - name: Shine
      label: Shine
      summary: |
        Specular exponent, which adjusts the light curve of specular highlights.
    - name: Enableshadow
      label: Enable Shadow
      summary: |
        Whether to use shadows. When enabled, if the *Shadow Definition* input is provided, that will be used. Otherwise a default shadow function will be used.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# reflectMat

Category: material

