---
layout: operator
title: sdfToFloat
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/sdfToFloat
redirect_from:
  - /reference/opType/raytk.operators.convert.sdfToFloat/
op:
  category: convert
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: sdfToFloat
  opType: raytk.operators.convert.sdfToFloat
  parameters:
  - label: Enable
    name: Enable
  summary: Converts an SDF into a float value field, based on the SDF surface distance.

---


Converts an SDF into a float value field, based on the SDF surface distance.