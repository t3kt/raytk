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
    label: Position Field
    name: positionField
    returnTypes:
    - vec4
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - positionField
    supportedVariables:
    - lightdir
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    label: Attenuation Field
    name: attenuationField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - positionField
    - colorField
    supportedVariables:
    - lightdir
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
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Intensity
    name: Intensity
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Attenuated
    name: Enableattenuation
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Attenuation Start
    name: Attenuationstart
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Attenuation End
    name: Attenuationend
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: Light that emits from along an axis, similar to an infinitely long tube
    light.
  variables:
  - label: RTK_raytk_operators_light_axisLight_lightdir
    name: RTK_raytk_operators_light_axisLight_lightdir

---


Light that emits from along an axis, similar to an infinitely long tube light.