---
layout: operator
title: diffuseContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/diffuseContrib
redirect_from:
  - /reference/opType/raytk.operators.material.diffuseContrib/
op:
  category: material
  images:
  - assets/images/reference/operators/material/diffuseContrib_lambert.png
  - assets/images/reference/operators/material/diffuseContrib_orennayar.png
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Roughness
    name: roughnessField
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Albedo
    name: albedoField
    returnTypes:
    - float
    supportedVariableInputs:
    - roughnessField
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - roughnessField
    - albedoField
  keywords:
  - diffuse
  - lambert
  - lighting
  - material
  - modularmat
  - oren-nayar
  - shading
  name: diffuseContrib
  opType: raytk.operators.material.diffuseContrib
  parameters:
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Method
    menuOptions:
    - label: Lambert
      name: lambert
    - label: Oren-Nayar
      name: orennayar
    - label: Burley
      name: burley
    name: Method
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The type of diffuse shading to use. Different methods support different
      combinations of the other parameters.
  - label: Roughness
    name: Roughness
  - label: Albedo
    name: Albedo
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  - label: Use Light Color
    name: Uselightcolor
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to apply the light color to the color produced by this element.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to apply the shadow to the color/level produced by this element.
  - label: Enable
    name: Enable
  - label: Use Surface Color
    name: Usesurfacecolor
    readOnlyHandling: semibaked
    regularHandling: semibaked
  shortcuts:
  - dc
  summary: A material element that provides diffuse light contribution.
  thumb: assets/images/reference/operators/material/diffuseContrib_thumb.png

---


A material element that provides diffuse light contribution.