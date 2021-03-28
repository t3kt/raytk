---
layout: operator
title: specularContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/specularContrib
redirect_from:
  - /reference/opType/raytk.operators.material.specularContrib/
op:
  category: material
  name: specularContrib
  opType: raytk.operators.material.specularContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    name: Returntype
  - label: Color
    name: Color
  - label: Method
    menuOptions:
    - label: Phong
      name: phong
    - label: Blinn-Phong
      name: blinnphong
    - label: Beckmann
      name: beckmann
    - label: Cook-Torrance
      name: cooktorrance
    - label: Gaussian
      name: gaussian
    - label: GGX
      name: ggx
    name: Method
  - label: Shininess
    name: Shininess
  - label: Roughness
    name: Roughness
  - label: Fresnel
    name: Fresnel
  - label: Level
    name: Level
  status: beta
  summary: Calculates specular light contribution for use in a material.

---


Calculates specular light contribution for use in a material.