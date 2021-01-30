---
layout: operator
title: timeField
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/timeField
redirect_from:
  - /reference/opType/raytk.operators.time.timeField/
op:
  category: time
  name: timeField
  opType: raytk.operators.time.timeField
  parameters:
  - label: Part
    menuOptions:
    - label: Seconds
      name: seconds
    - label: Frame
      name: frame
    - label: Start Frame
      name: start
    - label: End Frame
      name: end
    - label: Fraction
      name: fraction
    - label: Frame Rate
      name: rate
    - label: BPM
      name: bpm
    - label: Absolute Frame
      name: absFrame
    - label: Absolute Seconds
      name: absSeconds
    - label: Absolute Step Frames
      name: absStepFrames
    - label: Absolute Step Seconds
      name: absStepSeconds
    name: Part
  - label: Time Source
    menuOptions:
    - label: Global
      name: global
    - label: Context
      name: context
    name: Timesource
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype

---

# timeField

Category: time

