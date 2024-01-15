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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Float Field
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