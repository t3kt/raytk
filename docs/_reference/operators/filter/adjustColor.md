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
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - vec4
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

---


Adjust properties of color values.

This is similar to Level TOP and HSV Adjust TOP.