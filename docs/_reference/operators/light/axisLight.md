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
    summary: Field offsets the position of the light. The coordinates that this field
      gets are the spot on the surface that the light is being calculated for.
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
    summary: Field/function that controls the slope and coloration of the attenuation
      rolloff is shaped. It can be used to make the light shift from one color to
      another, or to control the sharpness of the rolloff.
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
    summary: Axis that the limit emits from.
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Position of the light. One axis of this won't be used since the light
      is infinite along one axis.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotates the light source.
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
  - label: Attenuated
    name: Enableattenuation
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to limit the light range.
  - label: Attenuation Start
    name: Attenuationstart
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The distance at which the light starts to dim.
  - label: Attenuation End
    name: Attenuationend
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The distance at which the light is fully dimmed.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the light should produce shadows.
  summary: Light that emits from along an axis, similar to an infinitely long tube
    light.
  thumb: assets/images/reference/operators/light/axisLight_thumb.png
  variables:
  - label: lightdir
    name: lightdir
    summary: Direction that the light is from the current position on a surface that's
      being shaded. This will be the closet point along the chosen axis.

---


Light that emits from along an axis, similar to an infinitely long tube light.