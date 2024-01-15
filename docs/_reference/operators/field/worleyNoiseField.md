---
layout: operator
title: worleyNoiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/worleyNoiseField
redirect_from:
  - /reference/opType/raytk.operators.field.worleyNoiseField/
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
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
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
    label: Jitter Field
    name: jitterField
    returnTypes:
    - float
  name: worleyNoiseField
  opType: raytk.operators.field.worleyNoiseField
  parameters:
  - label: Noise Type
    menuOptions:
    - label: Worley 2D (Original)
      name: worley2d
    - label: Worley 2D (Fast)
      name: worley2x2
    - label: Worley 3D (Original)
      name: worley3d
    - label: Worley 3D (Fast)
      name: worley2x2x2
    name: Noisetype
    summary: The type of noise function.
  - label: Distance Type
    menuOptions:
    - label: Euclidean
      name: euclidean
    - label: Manhattan
      name: manhattan
    name: Distancetype
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
    summary: The type of coordinates that the op supports.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: When the `Noisetype` uses 2D coordinates but `Coordtype` is 3D, this
      is used to choose which plane of the coordinates are used.
  - label: Translate
    name: Translate
    summary: Offsets the coordinates used to calculate noise.
  - label: Scale
    name: Scale
    summary: Scales the coordinates used to calculate noise.
  - label: Jitter
    name: Jitter
  - label: Amplitude
    name: Amplitude
    summary: Multiplies the amount produced by the noise.
  - label: Offset
    name: Offset
    summary: Offsets (adds to) the amount produced by the noise.
  status: beta
  thumb: assets/images/reference/operators/field/worleyNoiseField_thumb.png

---
