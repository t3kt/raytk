---
layout: operator
title: spotLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/spotLight
redirect_from:
  - /reference/opType/raytk.operators.light.spotLight/
op:
  category: light
  detail: This is similar to the Light COMP in spotlight mode.
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
    summary: Optional field that controls the color of the light.
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    label: Attenuation Field
    name: attenuationField
    returnTypes:
    - float
    - vec4
    summary: Field controls the color of the light based on the position of surface
      hits where it is being applied. The resulting color is multiplied by the `Color`
      parameter and `Intensity`.
    supportedVariableInputs:
    - colorField
  - label: attenuationField
    name: attenuationField
    summary: Field/function that controls the slope and coloration of the attenuation
      rolloff is shaped. It can be used to make the light shift from one color to
      another, or to control the sharpness of the rolloff.
  name: spotLight
  opType: raytk.operators.light.spotLight
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
  - label: Position
    name: Position
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The position of the tip of the light cone.
  - label: Direction
    name: Direction
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The direction which the cone faces, as a vector.
  - label: Cone Angle
    name: Coneangle
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The width of the cone.
  - label: Cone Delta
    name: Conedelta
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of blending between the inside and the outside of the cone.
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
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation for the direction that the light faces.
  - label: Enable Look At
    name: Enablelookat
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the light should face a specific position.
  - label: Look At Position
    name: Lookatpos
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Coordinates that the light should face.
  - label: Up Vector
    name: Upvec
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Up vector used to orient the light.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the light should produce shadows.
  summary: Cone-shaped spotlight.

---


Cone-shaped spotlight.

This is similar to the Light COMP in spotlight mode.