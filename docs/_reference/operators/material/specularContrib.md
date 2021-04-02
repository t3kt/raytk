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
  - label: Return Type
    menuOptions:
    - label: Level Only
      name: float
    - label: Color
      name: vec4
    name: Returntype
    summary: Whether the lighting should have coloration or just a brightness level.
  - label: Color
    name: Color
  - label: Level
    name: Level
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
    summary: The type of specular shading to use. Different methods support different
      combinations of the other parameters.
  - label: Shininess
    name: Shininess
  - label: Roughness
    name: Roughness
  - label: Fresnel
    name: Fresnel
  status: beta
  summary: A material element that provides specular light contribution.

---


A material element that provides specular light contribution.