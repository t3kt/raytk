---
layout: operator
title: pointMapRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/pointMapRender
redirect_from:
  - /reference/opType/raytk.operators.output.pointMapRender/
op:
  category: output
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
  name: pointMapRender
  opType: raytk.operators.output.pointMapRender
  parameters:
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  status: beta

---

# pointMapRender

Category: output

