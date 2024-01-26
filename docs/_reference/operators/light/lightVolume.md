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
    name: boundVolume
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - boundVolume
  name: lightVolume
  opType: raytk.operators.light.lightVolume
  parameters:
  - label: Level
    name: Level
  - label: Color
    name: Color
  - label: Use Light Color
    name: Uselightcolor
  - label: Use Bounds SDF Surface Color
    name: Usesdfcolor
  - label: Blending
    name: Blending
  - label: Offset
    name: Offset
  - label: Enable Shadow
    name: Enableshadow
  status: beta
  thumb: assets/images/reference/operators/light/lightVolume_thumb.png

---
