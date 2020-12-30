---
layout: operator
title: timeField
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/timeField
redirect_from:
  - /reference/opType/raytk.operators.time.timeField/
op:
  name: timeField
  opType: raytk.operators.time.timeField
  category: time
  parameters:
    - name: Part
      label: Part
      menuOptions:
        - name: seconds
          label: Seconds
        - name: frame
          label: Frame
        - name: start
          label: Start Frame
        - name: end
          label: End Frame
        - name: fraction
          label: Fraction
        - name: rate
          label: Frame Rate
        - name: bpm
          label: BPM
        - name: absFrame
          label: Absolute Frame
        - name: absSeconds
          label: Absolute Seconds
    - name: Timesource
      label: Time Source
      menuOptions:
        - name: global
          label: Global
        - name: context
          label: Context
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

# timeField

Category: time

