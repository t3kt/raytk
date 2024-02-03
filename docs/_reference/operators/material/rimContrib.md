---
layout: operator
title: rimContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/rimContrib
redirect_from:
  - /reference/opType/raytk.operators.material.rimContrib/
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariables:
    - normangle
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - thicknessField
    supportedVariables:
    - normangle
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - thicknessField
    - blendingField
    supportedVariables:
    - normangle
  name: rimContrib
  opType: raytk.operators.material.rimContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Level
    name: Level
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  - label: Color
    name: Color
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Use Surface Color
    name: Usesurfacecolor
    readOnlyHandling: constant
    regularHandling: constant
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: macro
    regularHandling: macro
    summary: Whether to apply the shadow to the color/level produced by this element.
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/material/rimContrib_thumb.png
  variables:
  - label: normangle
    name: normangle

---
