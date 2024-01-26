---
layout: operator
title: extrudeLine
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/extrudeLine
redirect_from:
  - /reference/opType/raytk.operators.convert.extrudeLine/
op:
  category: convert
  detail: The extrude operator goes along a selected axis, with a height center on
    the origin. Instead of doing that, this operator extrudes so that one side is
    centered at Point1 and the other end at Point2.
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
    - vec2
    label: Cross-Section SDF
    name: crossSection
    required: true
    returnTypes:
    - Sdf
    summary: 2D SDF cross-section to extrude.
    supportedVariableInputs:
    - point1Field
    - point2Field
    supportedVariables:
    - axispos
    - normoffset
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
    - vec3
    label: Point 1 Field
    name: point1Field
    returnTypes:
    - vec4
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
    - vec3
    label: Point 2 Field
    name: point2Field
    returnTypes:
    - vec4
    supportedVariableInputs:
    - point1Field
  name: extrudeLine
  opType: raytk.operators.convert.extrudeLine
  parameters:
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  status: beta
  summary: Extrudes a 2D SDF cross-section into a 3D volume, like the extrude operator,
    but between two points.
  variables:
  - label: axispos
    name: axispos
  - label: normoffset
    name: normoffset

---


Extrudes a 2D SDF cross-section into a 3D volume, like the extrude operator, but between two points.

The extrude operator goes along a selected axis, with a height center on the origin. Instead of doing that, this operator extrudes so that one side is centered at Point1 and the other end at Point2.