---
layout: operator
title: curlNoiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/curlNoiseField
redirect_from:
  - /reference/opType/raytk.operators.field.curlNoiseField/
op:
  category: field
  detail: 'Note that this operator can be very resource intensive, especially when
    used in a 3D raymarching scene.

    Based on https://github.com/cabbibo/glsl-curl-noise'
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
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
  name: curlNoiseField
  opType: raytk.operators.field.curlNoiseField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - name: Contexttype
  - label: Translate
    name: Translate
    summary: Coordinate translation.
  - label: Scale
    name: Scale
    summary: Coordinate scale.
  - label: Amplitude
    name: Amplitude
    summary: Noise value amplitude.
  - label: Offset
    name: Offset
    summary: Noise value offset.
  summary: Curl noise field.
  thumb: assets/images/reference/operators/field/curlNoiseField_thumb.png

---


Curl noise field.

Note that this operator can be very resource intensive, especially when used in a 3D raymarching scene.
Based on https://github.com/cabbibo/glsl-curl-noise