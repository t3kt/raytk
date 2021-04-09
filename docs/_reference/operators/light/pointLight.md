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
    - none
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
    - none
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
  name: pointLight
  opType: raytk.operators.light.pointLight
  parameters:
  - label: Position
    name: Position
  - label: Intensity
    name: Intensity
  - label: Color
    name: Color
  - label: Attenuated
    name: Enableattenuation
  - label: Attenuation Start
    name: Attenuationstart
  - label: Attenuation End
    name: Attenuationend
  summary: Light eminating from a single point in space, with optional distance attentuation.

---


Light eminating from a single point in space, with optional distance attentuation.