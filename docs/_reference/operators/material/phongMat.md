---
layout: operator
title: phongMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/phongMat
redirect_from:
  - /reference/opType/raytk.operators.material.phongMat/
op:
  name: phongMat
  summary: |
    Material that uses phong shading.
  opType: raytk.operators.material.phongMat
  category: material
  inputs:
    - name: definition_in
      label: definition_in
      required: true
    - name: shadow_definition_in
      label: Shadow Definition
      required: false
      summary: |
        Used to customize the behavior of shadows for the material. Only used if `Enableshadow` is on.
  parameters:
    - name: Enable
      label: Enable
    - name: Ambientcolor
      label: Ambient Color
      summary: |
        Base color applied to the surface regardless of lights.
    - name: Diffusecolor
      label: Diffuse Color
      summary: |
        Color reflected by matte surfaces.
    - name: Specularcolor
      label: Specular Color
      summary: |
        Color reflected by glossy surfaces.
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

# phongMat

Category: material



Material that uses phong shading.