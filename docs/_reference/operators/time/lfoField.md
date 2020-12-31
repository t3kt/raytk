---
layout: operator
title: lfoField
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/lfoField
redirect_from:
  - /reference/opType/raytk.operators.time.lfoField/
op:
  name: lfoField
  opType: raytk.operators.time.lfoField
  category: time
  inputs:
    - name: wave_definition_in
      label: wave_definition_in
      required: false
      coordTypes: [float]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
  parameters:
    - name: Enable
      label: Enable
    - name: Period
      label: Period
    - name: Intervaltype
      label: Interval Type
      menuOptions:
        - name: seconds
          label: Seconds (Timeline)
        - name: frames
          label: Frames (Timeline)
        - name: absseconds
          label: Seconds (Absolute)
        - name: frames
          label: Frames (Absolute)
    - name: Timesource
      label: Time Source
      menuOptions:
        - name: global
          label: Global
        - name: context
          label: Context
    - name: Phase
      label: Phase (Fraction)
    - name: Amplitude
      label: Amplitude
    - name: Offset
      label: Offset
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: float
          label: 1D
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# lfoField

Category: time

