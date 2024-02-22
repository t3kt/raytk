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
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Attenuated
    name: Enableattenuation
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Attenuation Start
    name: Attenuationstart
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Attenuation End
    name: Attenuationend
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
  status: beta

---
