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
    summary: Field controls the color of the light based on the position of surface
      hits where it is being applied. The resulting color is multiplied by the `Color`
      parameter and `Intensity`.
    supportedVariables:
    - lightdir
  name: ambientLight
  opType: raytk.operators.light.ambientLight
  parameters:
  - label: Intensity
    name: Intensity
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Brightness that is applied to the `Color`.
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color of the light.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether the light should produce shadows.
  status: beta
  summary: Ambient light source that doesn't come from a particular location.
  variables:
  - label: lightdir
    name: lightdir
    summary: Direction that the light is from the current position on a surface that's
      being shaded. This will always be directly in front of whatever point is being
      shaded based on the surface normal at that point.

---


Ambient light source that doesn't come from a particular location.

As far as a material is concerned, an ambient light is always right in front of any point on a surface.

Use cases for this are relatively rare.