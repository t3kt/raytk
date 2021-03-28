---
layout: operator
title: modularMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/modularMat
redirect_from:
  - /reference/opType/raytk.operators.material.modularMat/
op:
  category: material
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Shadow
    name: shadow_definition_in
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_1
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_2
    returnTypes:
    - float
    - vec4
  name: modularMat
  opType: raytk.operators.material.modularMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Use Light Color
    name: Uselightcolor
  - label: Use Local Position
    name: Uselocalpos
  - label: Enable Ambient Occlusion
    name: Enableao
  - label: Enable Shadow
    name: Enableshadow
  status: beta

---
