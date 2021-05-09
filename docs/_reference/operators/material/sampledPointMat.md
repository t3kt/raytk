---
layout: operator
title: sampledPointMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/sampledPointMat
redirect_from:
  - /reference/opType/raytk.operators.material.sampledPointMat/
op:
  category: material
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
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Fill Color Field
    name: fill_color_field_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Edge Color Field
    name: edge_color_field_definition_in
    returnTypes:
    - float
    - vec4
  name: sampledPointMat
  opType: raytk.operators.material.sampledPointMat
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Fill
    name: Enablefill
  - label: Fill Color
    name: Fillcolor
  - label: Enable Edge
    name: Enableedge
  - label: Edge Color
    name: Edgecolor
  - label: Edge Thickness
    name: Edgethickness
  - label: Blending
    name: Blending
  - label: Use Local Position
    name: Uselocalpos
  status: beta

---
