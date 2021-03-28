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
  - label: Level
    name: Level
  - label: Method
    menuOptions:
    - label: Lambert
      name: lambert
    - label: Oren-Nayar
      name: orennayar
    name: Method
  - label: Roughness
    name: Roughness
  - label: Albedo
    name: Albedo
  status: beta

---
