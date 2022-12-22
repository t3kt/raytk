---
layout: operator
title: axisLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/axisLight
redirect_from:
  - /reference/opType/raytk.operators.light.axisLight/
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
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    label: Attenuation Field
    name: attenuationField
    returnTypes:
    - float
    - vec4
  name: axisLight
  opType: raytk.operators.light.axisLight
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Position
    name: Position
  - label: Rotate
    name: Rotate
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Attenuated
    name: Enableattenuation
  - label: Attenuation Start
    name: Attenuationstart
  - label: Attenuation End
    name: Attenuationend
  - label: Enable Shadow
    name: Enableshadow
  summary: Light that emits from along an axis, similar to an infinitely long tube
    light.

---


Light that emits from along an axis, similar to an infinitely long tube light.