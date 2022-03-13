---
layout: operator
title: waveletNoiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/waveletNoiseField
redirect_from:
  - /reference/opType/raytk.operators.field.waveletNoiseField/
op:
  category: field
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
    - vec3
    label: Phase Field
    name: phaseField
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
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
  name: waveletNoiseField
  opType: raytk.operators.field.waveletNoiseField
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
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  - label: Iterations
    name: Iterations
  - label: Translate
    name: Translate
  - label: Period
    name: Period
  - label: Scale Factor
    name: Scalefactor
  - label: Phase
    name: Phase
  - label: Enable Vorticity
    name: Enablevorticity
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  thumb: assets/images/reference/operators/field/waveletNoiseField_thumb.png

---
