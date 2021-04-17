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
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Phase Field
    name: phase_field_definition_in
    returnTypes:
    - float
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

---
