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
    summary: Field controls the color of the light based on the position of surface
      hits where it is being applied. The resulting color is multiplied by the `Color`
      parameter and `Intensity`.
    supportedVariables:
    - lightdir
  name: directionalLight
  opType: raytk.operators.light.directionalLight
  parameters:
  - label: Direction
    name: Direction
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Vector pointing which direction the light shines. This vector is automatically
      normalized.
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
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotates the direction of the light on all 3 axes.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the light should produce shadows.
  summary: Directional or distant light which always comes from one direction.
  thumb: assets/images/reference/operators/light/directionalLight_thumb.png
  variables:
  - label: lightdir
    name: lightdir
    summary: Direction that the light is from the current position on a surface that's
      being shaded. This will always be the Direction with rotation applied.

---


Directional or distant light which always comes from one direction.

The light always comes from the specified direction, rather than from a point.