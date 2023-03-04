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
  detail: Deprecated in favor of using Phong mode in specularContrib in a modularMat.
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
  status: deprecated
  summary: Material that uses phong shading.

---


Material that uses phong shading.

Deprecated in favor of using Phong mode in specularContrib in a modularMat.