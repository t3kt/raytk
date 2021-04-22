---
layout: operator
title: bezierSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/bezierSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.bezierSdf2d/
op:
  category: sdf2d
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
  name: bezierSdf2d
  opType: raytk.operators.sdf2d.bezierSdf2d
  parameters:
  - label: Point A
    name: Pointa
  - label: Point B
    name: Pointb
  - label: Point C
    name: Pointc
  status: beta

---
