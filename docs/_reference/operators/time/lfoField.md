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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    label: Wave Function
    name: waveFunction
    returnTypes:
    - float
    - vec4
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
    readOnlyHandling: baked
    regularHandling: runtime
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
    readOnlyHandling: baked
    regularHandling: baked
  - label: Time Source
    menuOptions:
    - label: Seconds (Timeline)
      name: seconds
    - label: Frames (Timeline)
      name: frames
    - label: Seconds (Absolute)
      name: absseconds
    - label: Frames (Absolute)
      name: absframes
    name: Timesource
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Reverse
    name: Reverse
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Phase (Fraction)
    name: Phase
  - label: Amplitude
    name: Amplitude
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
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
