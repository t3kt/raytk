---
layout: operator
title: diffuseContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/diffuseContrib
redirect_from:
  - /reference/opType/raytk.operators.material.diffuseContrib/
op:
  category: material
  name: diffuseContrib
  opType: raytk.operators.material.diffuseContrib
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
    - label: Lambert
      name: lambert
    - label: Oren-Nayar
      name: orennayar
    name: Method
    summary: The type of diffuse shading to use. Different methods support different
      combinations of the other parameters.
  - label: Roughness
    name: Roughness
  - label: Albedo
    name: Albedo
  status: beta
  summary: A material element that provides diffuse light contribution.

---


A material element that provides diffuse light contribution.