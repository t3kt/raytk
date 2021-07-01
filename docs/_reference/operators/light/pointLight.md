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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Color Field
    name: color_field_definition_in
    returnTypes:
    - float
    - vec4
    summary: Optional field that can control the color of the light based on the position
      of surface hits where it is being applied. The resulting color is multiplied
      by the `Color` parameter and `Intensity`.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Attenuation Field
    name: attenutation_field_definition_in
    returnTypes:
    - float
    - vec4
    summary: Optional field/function that controls the slope and coloration of the
      attentuation rolloff is shaped. It can be used to make the light shift from
      one color to another, or to control the sharpness of the rolloff.
  name: pointLight
  opType: raytk.operators.light.pointLight
  parameters:
  - label: Position
    name: Position
    summary: The point from which the light eminates.
  - label: Intensity
    name: Intensity
    summary: Brightness of the light.
  - label: Color
    name: Color
    summary: Color of the light.
  - label: Attenuated
    name: Enableattenuation
    summary: Whether to limit the light range.
  - label: Attenuation Start
    name: Attenuationstart
    summary: The distance at which the light starts to dim.
  - label: Attenuation End
    name: Attenuationend
    summary: The distance at which the light is fully dimmed.
  summary: Light eminating from a single point in space, with optional distance attentuation.

---


Light eminating from a single point in space, with optional distance attentuation.