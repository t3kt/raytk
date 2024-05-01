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
  detail: 'As far as a material is concerned, an ambient light is always right in
    front of any point on a surface.


    Use cases for this are relatively rare.'
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
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Ambient light source that doesn't come from a particular location.
  variables:
  - label: lightdir
    name: lightdir

---


Ambient light source that doesn't come from a particular location.

As far as a material is concerned, an ambient light is always right in front of any point on a surface.

Use cases for this are relatively rare.