---
layout: operator
title: render2D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/render2D
redirect_from:
  - /reference/opType/raytk.operators.output.render2D/
op:
  name: render2D
  opType: raytk.operators.output.render2D
  category: output
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2]
      contextTypes: [Context]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Res
      label: Resolution
    - name: Enableedge
      label: Enable Edge
    - name: Edgethickness
      label: Edge Thickness
    - name: Edgeblending
      label: Edge Blending
    - name: Edgecolor
      label: Edge Color
    - name: Insideperiod
      label: Inside Period
    - name: Insidecolor1
      label: Inside Color 1
    - name: Insidecolor2
      label: Inside Color 2
    - name: Outsideperiod
      label: Outside Period
    - name: Outsidecolor1
      label: Outside Color 1
    - name: Outsidecolor2
      label: Outside Color 2
    - name: Timerefop
      label: Time Reference Operator
    - name: Shaderbuilderconfig
      label: Shader Builder Config
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# render2D

Category: output

