---
layout: operator
title: limitArea
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitArea
redirect_from:
  - /reference/opType/raytk.operators.filter.limitArea/
op:
  category: filter
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
    label: Inside
    name: inside
    required: true
    returnTypes:
    - float
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
    - float
    - vec2
    - vec3
    - vec4
    label: Outside
    name: outside
    returnTypes:
    - float
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
    - float
    - vec2
    - vec3
    - vec4
    label: Bound Volume
    name: boundVolume
    required: true
    returnTypes:
    - float
    - Sdf
  name: limitArea
  opType: raytk.operators.filter.limitArea
  parameters:
  - label: Enable
    name: Enable
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Outside Value
    name: Outsidevalue
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta

---
