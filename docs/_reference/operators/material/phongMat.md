---
layout: operator
title: phongMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/phongMat
redirect_from:
  - /reference/opType/raytk.operators.material.phongMat/
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
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Shadow Definition
    name: shadow_definition_in
    returnTypes:
    - float
    summary: Used to customize the behavior of shadows for the material. Only used
      if `Enableshadow` is on.
  name: phongMat
  opType: raytk.operators.material.phongMat
  parameters:
  - label: Enable
    name: Enable
  - label: Ambient Color
    name: Ambientcolor
    summary: Base color applied to the surface regardless of lights.
  - label: Diffuse Color
    name: Diffusecolor
    summary: Color reflected by matte surfaces.
  - label: Specular Color
    name: Specularcolor
    summary: Color reflected by glossy surfaces.
  - label: Shine
    name: Shine
    summary: Specular exponent, which adjusts the light curve of specular highlights.
  - label: Enable Shadow
    name: Enableshadow
    summary: Whether to use shadows. When enabled, if the *Shadow Definition* input
      is provided, that will be used. Otherwise a default shadow function will be
      used.
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Material that uses phong shading.

---

# phongMat

Category: material



Material that uses phong shading.