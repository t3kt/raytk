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
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Shadow
    name: shadow_definition_in
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColor_definition_in
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
  status: beta

---
