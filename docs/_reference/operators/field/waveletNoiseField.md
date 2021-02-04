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

# waveletNoiseField

Category: field

