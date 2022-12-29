---
layout: operator
title: adjustColor
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/adjustColor
redirect_from:
  - /reference/opType/raytk.operators.filter.adjustColor/
op:
  category: filter
  detail: This is similar to Level TOP and HSV Adjust TOP.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Brightness Field
    name: brightnessField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Contrast Field
    name: contrastField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Hue Field
    name: hueField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Saturation Field
    name: saturationField
    returnTypes:
    - float
  keywords:
  - adjust
  - brightness
  - color
  - contrast
  - filter
  - hue
  - saturation
  name: adjustColor
  opType: raytk.operators.filter.adjustColor
  parameters:
  - label: Enable
    name: Enable
  - label: Brightness
    name: Brightness
  - label: Contrast
    name: Contrast
  - label: Saturation
    name: Saturation
  - label: Hue Offset
    name: Hueoffset
  - label: Gamma
    name: Gamma
  status: beta
  summary: Adjust properties of color values.
  thumb: assets/images/reference/operators/filter/adjustColor_thumb.png

---


Adjust properties of color values.

This is similar to Level TOP and HSV Adjust TOP.