---
layout: operator
title: floatToSdf
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/floatToSdf
redirect_from:
  - /reference/opType/raytk.operators.convert.floatToSdf/
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
    - float
  name: floatToSdf
  opType: raytk.operators.convert.floatToSdf
  parameters:
  - label: Enable
    name: Enable
  summary: Converts a float value field into an SDF.

---


Converts a float value field into an SDF.