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
    supportedVariables:
    - lightdir
  name: directionalLight
  opType: raytk.operators.light.directionalLight
  parameters:
  - label: Direction
    name: Direction
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Intensity
    name: Intensity
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color
    name: Color
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: constant
    regularHandling: runtime
  summary: A directional light.
  variables:
  - label: lightdir
    name: lightdir

---


A directional light.

The light always comes from the specified direction, rather than from a point.