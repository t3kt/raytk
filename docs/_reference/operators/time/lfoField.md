---
layout: operator
title: lfoField
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/lfoField
redirect_from:
  - /reference/opType/raytk.operators.time.lfoField/
op:
  category: time
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
    label: Wave Function
    name: waveFunction
    returnTypes:
    - float
  name: lfoField
  opType: raytk.operators.time.lfoField
  parameters:
  - label: Enable
    name: Enable
  - label: Wave Type
    menuOptions:
    - label: Sine
      name: sin
    - label: Cosine
      name: cos
    - label: Triangle
      name: tri
    - label: Ramp
      name: ramp
    - label: Square
      name: square
    name: Wavetype
  - label: Period
    name: Period
  - label: Interval Type
    menuOptions:
    - label: Seconds (Timeline)
      name: seconds
    - label: Frames (Timeline)
      name: frames
    - label: Seconds (Absolute)
      name: absseconds
    - label: Frames (Absolute)
      name: frames
    name: Intervaltype
  - label: Time Source
    menuOptions:
    - label: Global
      name: global
    - label: Context
      name: context
    name: Timesource
  - label: Reverse
    name: Reverse
  - label: Phase (Fraction)
    name: Phase
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
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
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    - label: Ray Context
      name: RayContext
    - label: Particle Context
      name: ParticleContext
    name: Contexttype

---
