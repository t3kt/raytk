---
layout: operator
title: modifyNormals
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modifyNormals
redirect_from:
  - /reference/opType/raytk.operators.filter.modifyNormals/
op:
  category: filter
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
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
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - vec4
  name: modifyNormals
  opType: raytk.operators.filter.modifyNormals
  parameters:
  - label: Enable
    name: Enable
  status: beta

---
