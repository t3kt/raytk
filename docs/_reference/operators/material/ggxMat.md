---
layout: operator
title: ggxMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/ggxMat
redirect_from:
  - /reference/opType/raytk.operators.material.ggxMat/
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
    - Sdf
  name: ggxMat
  opType: raytk.operators.material.ggxMat
  parameters:
  - label: Enable
    name: Enable
  - label: Fresnel
    name: Fresnel
  - label: Base Color
    name: Basecolor
  - label: Diffuse
    name: Diffuse
  - label: Roughness
    name: Roughness
  status: deprecated

---
