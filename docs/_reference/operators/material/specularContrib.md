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
  keywords:
  - ggx
  - lighting
  - material
  - modularmat
  - phong
  - shading
  - specular
  name: specularContrib
  opType: raytk.operators.material.specularContrib
  parameters:
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
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  - label: Use Light Color
    name: Uselightcolor
    summary: Whether to apply the light color to the color produced by this element.
  - label: Enable Shadow
    name: Enableshadow
    summary: Whether to apply the shadow to the color/level produced by this element.
  summary: A material element that provides specular light contribution.

---


A material element that provides specular light contribution.