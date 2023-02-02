---
layout: operator
title: directionalLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/directionalLight
redirect_from:
  - /reference/opType/raytk.operators.light.directionalLight/
op:
  category: light
  detail: The light always comes from the specified direction, rather than from a
    point.
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
  name: directionalLight
  opType: raytk.operators.light.directionalLight
  parameters:
  - label: Direction
    name: Direction
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Rotate
    name: Rotate
  - label: Enable Shadow
    name: Enableshadow
  summary: A directional light.

---


A directional light.

The light always comes from the specified direction, rather than from a point.