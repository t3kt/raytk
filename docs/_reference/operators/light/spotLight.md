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
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Color Field
    name: color_field_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Attenuation Field
    name: attenutation_field_definition_in
    returnTypes:
    - float
    - vec4
  name: spotLight
  opType: raytk.operators.light.spotLight
  parameters:
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Position
    name: Position
  - label: Direction
    name: Direction
  - label: Cone Angle
    name: Coneangle
  - label: Cone Delta
    name: Conedelta
  - label: Attenuated
    name: Enableattenuation
  - label: Attenuation Start
    name: Attenuationstart
  - label: Attenuation End
    name: Attenuationend
  status: beta

---
