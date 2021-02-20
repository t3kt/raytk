---
layout: operator
title: fieldMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/fieldMat
redirect_from:
  - /reference/opType/raytk.operators.material.fieldMat/
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
    label: color_definition_in
    name: color_definition_in
    required: true
    returnTypes:
    - vec4
  name: fieldMat
  opType: raytk.operators.material.fieldMat
  parameters:
  - label: Enable
    name: Enable
  summary: 'A material that uses a vector field input to determine

    the color. Essentially this is a conversion from a

    field to a material, with no other features.'

---


A material that uses a vector field input to determine
the color. Essentially this is a conversion from a
field to a material, with no other features.