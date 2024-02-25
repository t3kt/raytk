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
    - VertexContext
    - PixelContext
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
    - VertexContext
    - PixelContext
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
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Iterations
    name: Iterations
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Period
    name: Period
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale Factor
    name: Scalefactor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Phase
    name: Phase
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Vorticity
    name: Enablevorticity
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Amplitude
    name: Amplitude
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/field/waveletNoiseField_thumb.png

---
