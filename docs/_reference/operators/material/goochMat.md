---
layout: operator
title: goochMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/goochMat
redirect_from:
  - /reference/opType/raytk.operators.material.goochMat/
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
  name: goochMat
  opType: raytk.operators.material.goochMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Warm Color
    name: Warmcolor
  - label: Cool Color
    name: Coolcolor

---
