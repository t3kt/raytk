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
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Use Light Color
    name: Uselightcolor
    readOnlyHandling: baked
    regularHandling: baked
  - label: Use Bounds SDF Surface Color
    name: Usesdfcolor
    readOnlyHandling: baked
    regularHandling: baked
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  status: beta
  thumb: assets/images/reference/operators/light/lightVolume_thumb.png

---
