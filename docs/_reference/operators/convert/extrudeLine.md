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
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Cross-Section SDF
    name: crossSection
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
    coordTypes:
    - vec3
    label: Point 2 Field
    name: point2Field
    returnTypes:
    - vec4
  name: extrudeLine
  opType: raytk.operators.convert.extrudeLine
  parameters:
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  status: beta
  variables:
  - label: axispos
    name: axispos
  - label: normoffset
    name: normoffset

---
