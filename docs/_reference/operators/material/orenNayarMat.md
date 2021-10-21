---
layout: operator
title: orenNayarMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/orenNayarMat
redirect_from:
  - /reference/opType/raytk.operators.material.orenNayarMat/
op:
  category: material
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: definition_in
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Shadow
    name: shadow
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColorField
    returnTypes:
    - float
    - vec4
  name: orenNayarMat
  opType: raytk.operators.material.orenNayarMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Diffuse
    name: Diffuse
  - label: Roughness
    name: Roughness
  - label: Albedo
    name: Albedo
  - label: Enable Shadow
    name: Enableshadow
  - label: Use Local Position
    name: Uselocalpos
  status: deprecated

---
