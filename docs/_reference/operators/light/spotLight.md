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
    summary: Optional function that controls the color/intensity of the light based
      on the attenuation distance.
  name: spotLight
  opType: raytk.operators.light.spotLight
  parameters:
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Position
    name: Position
    summary: The position of the tip of the light cone.
  - label: Direction
    name: Direction
    summary: The direction which the cone faces, as a vector.
  - label: Cone Angle
    name: Coneangle
    summary: The width of the cone.
  - label: Cone Delta
    name: Conedelta
    summary: The amount of blending between the inside and outside of the cone.
  - label: Attenuated
    name: Enableattenuation
    summary: Whether to adjust the amount of light depending on distance.
  - label: Attenuation Start
    name: Attenuationstart
    summary: The start of the blending range, inside which the light will be at full
      intensity.
  - label: Attenuation End
    name: Attenuationend
    summary: The end of the blending range, outside which the light will be at zero
      intensity.
  - label: Rotate
    name: Rotate
  - label: Enable Shadow
    name: Enableshadow
  summary: Cone-shaped spotlight.

---


Cone-shaped spotlight.

This is similar to the Light COMP in spotlight mode.