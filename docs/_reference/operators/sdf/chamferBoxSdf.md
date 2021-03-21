---
layout: operator
title: chamferBoxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chamferBoxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chamferBoxSdf/
op:
  category: sdf
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
  name: chamferBoxSdf
  opType: raytk.operators.sdf.chamferBoxSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Translate
    name: Translate
  - label: Uniform Scale
    name: Uniformscale
  - label: Chamfer
    name: Chamfer
  - label: Scale
    name: Scale
  - label: Round
    name: Round

---
