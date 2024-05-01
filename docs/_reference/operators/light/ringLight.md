---
layout: operator
title: ringLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/ringLight
redirect_from:
  - /reference/opType/raytk.operators.light.ringLight/
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
  name: ringLight
  opType: raytk.operators.light.ringLight
  parameters:
  - label: Intensity
    name: Intensity
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: The axis which the ring faces.
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Center position of the ring.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of the ring.
  - label: Attenuated
    name: Enableattenuation
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to limit the light range.
  - label: Attenuation Start
    name: Attenuationstart
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: The distance at which the light starts to dim.
  - label: Attenuation End
    name: Attenuationend
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: The distance at which the light is fully dimmed.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the light should produce shadows.
  summary: Light that emits from a torus or ring shape.

---


Light that emits from a torus or ring shape.