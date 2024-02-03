---
layout: operator
title: matCapContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/matCapContrib
redirect_from:
  - /reference/opType/raytk.operators.material.matCapContrib/
op:
  category: material
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
  name: matCapContrib
  opType: raytk.operators.material.matCapContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Level
    name: Level
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Mat Cap Texture TOP
    name: Texturetop
  - label: Map Cap Texture File
    name: Texturefile
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: macro
    regularHandling: macro
  status: beta

---
