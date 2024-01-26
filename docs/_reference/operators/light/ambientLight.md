---
layout: operator
title: ambientLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/ambientLight
redirect_from:
  - /reference/opType/raytk.operators.light.ambientLight/
op:
  category: light
  inputs:
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - lightdir
  name: ambientLight
  opType: raytk.operators.light.ambientLight
  parameters:
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Enable Shadow
    name: Enableshadow
  status: beta
  variables:
  - label: lightdir
    name: lightdir

---
