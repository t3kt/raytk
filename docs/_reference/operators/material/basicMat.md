---
layout: operator
title: basicMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/basicMat
redirect_from:
  - /reference/opType/raytk.operators.material.basicMat/
op:
  category: material
  inputs:
  - contextTypes:
    - none
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
    label: shadow_definition_in
    name: shadow_definition_in
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: baseColor_definition_in
    name: baseColor_definition_in
    returnTypes:
    - vec4
  name: basicMat
  opType: raytk.operators.material.basicMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Sky Color
    name: Skycolor
  - label: Sky Amount
    name: Skyamount
  - label: Sky Direction
    name: Skydir
  - label: Specular Amount
    name: Specularamount
  - label: Specular Exponent
    name: Specularexp
  - label: Enable Shadow
    name: Enableshadow
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# basicMat

Category: material

