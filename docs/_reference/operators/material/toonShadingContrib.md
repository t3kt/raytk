---
layout: operator
title: toonShadingContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/toonShadingContrib
redirect_from:
  - /reference/opType/raytk.operators.material.toonShadingContrib/
op:
  category: material
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    label: Color Ramp
    name: colorRamp
    required: true
    returnTypes:
    - float
    - vec4
  name: toonShadingContrib
  opType: raytk.operators.material.toonShadingContrib
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
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  - label: Use Surface Color
    name: Usesurfacecolor
    readOnlyHandling: baked
    regularHandling: baked
  status: beta
  summary: Modular shading element which uses a cell/toon shading technique with a
    color ramp.
  thumb: assets/images/reference/operators/material/toonShadingContrib_thumb.png

---


Modular shading element which uses a cell/toon shading technique with a color ramp.