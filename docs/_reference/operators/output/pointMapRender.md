---
layout: operator
title: pointMapRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/pointMapRender
redirect_from:
  - /reference/opType/raytk.operators.output.pointMapRender/
op:
  name: pointMapRender
  opType: raytk.operators.output.pointMapRender
  category: output
  status: beta
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [Context]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Timerefop
      label: Time Reference Operator
    - name: Shaderbuilderconfig
      label: Shader Builder Config
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# pointMapRender

Category: output

