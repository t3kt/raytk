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
  name: curlNoiseField
  opType: raytk.operators.field.curlNoiseField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
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

---


Curl noise field.

Note that this operator can be very resource intensive, especially when used in a 3D raymarching scene.
Based on https://github.com/cabbibo/glsl-curl-noise