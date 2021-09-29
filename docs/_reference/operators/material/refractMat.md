---
layout: operator
title: refractMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/refractMat
redirect_from:
  - /reference/opType/raytk.operators.material.refractMat/
op:
  category: material
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  name: refractMat
  opType: raytk.operators.material.refractMat
  parameters:
  - label: Enable
    name: Enable
  - label: Index of Refraction
    name: Ior
  status: alpha

---
