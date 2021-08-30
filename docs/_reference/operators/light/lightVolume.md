---
layout: operator
title: lightVolume
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/lightVolume
redirect_from:
  - /reference/opType/raytk.operators.light.lightVolume/
op:
  category: light
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Bound Volume
    name: bound_definition_in
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Field
    name: color_definition_in
    returnTypes:
    - float
    - vec4
  name: lightVolume
  opType: raytk.operators.light.lightVolume
  parameters:
  - label: Level
    name: Level
  - label: Color
    name: Color
  - label: Blending
    name: Blending
  - label: Offset
    name: Offset
  - label: Enable Shadow
    name: Enableshadow
  status: beta

---
