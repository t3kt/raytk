---
layout: operator
title: pointLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/pointLight
redirect_from:
  - /reference/opType/raytk.operators.light.pointLight/
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
    summary: Field controls the color of the light based on the position of surface
      hits where it is being applied. The resulting color is multiplied by the `Color`
      parameter and `Intensity`.
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    summary: Field/function that controls the slope and coloration of the attenuation
      rolloff is shaped. It can be used to make the light shift from one color to
      another, or to control the sharpness of the rolloff.
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
  name: pointLight
  opType: raytk.operators.light.pointLight
  parameters:
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The point from which the light emits.
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
  shortcuts:
  - pl
  summary: Light that emits from a single point in space.
  variables:
  - label: Light Direction
    name: lightdir

---


Light that emits from a single point in space.