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
    - vec4
    label: Color Input
    name: definition_in
    required: true
    returnTypes:
    - vec4
    - Sdf
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
    - vec4
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
    - vec4
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
    - vec4
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
    - vec4
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
  summary: Adjust properties of color values, either directly on a field, or on the
    assigned surface color of an Sdf result.
  thumb: assets/images/reference/operators/filter/adjustColor_thumb.png

---


Adjust properties of color values, either directly on a field, or on the assigned surface color of an Sdf result.

This is similar to Level TOP and HSV Adjust TOP.