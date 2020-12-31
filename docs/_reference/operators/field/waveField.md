---
layout: operator
title: waveField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/waveField
redirect_from:
  - /reference/opType/raytk.operators.field.waveField/
op:
  name: waveField
  summary: A field that uses a periodic wave.
  detail: |
    If there is an input, that rop is used to get the coordinate that is fed into the wave function.
    Without an input, the Axis is used to run the wave function on the position along the selected axis.
  opType: raytk.operators.field.waveField
  category: field
  inputs:
    - name: definition_in
      label: Wave Coordinate Source
      required: false
      summary: |
        If attached, the wave will use this to determine the numbers that it passes to the wave function (instead of using the position along the chosen `Axis`).
  parameters:
    - name: Enable
      label: Enable
    - name: Function
      label: Wave
      summary: |
        The type of wave.
      menuOptions:
        - name: sin
          label: Sine
        - name: cos
          label: Cosine
        - name: tri
          label: Triangle
        - name: ramp
          label: Ramp
        - name: square
          label: Square
    - name: Axis
      label: Axis
      summary: |
        If there is no input, the coordinate along this axis is used for the wave function phase.
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
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
        - name: useinput
          label: Use Input
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Period
      label: Period
      summary: |
        The length of a single cycle of the wave.
    - name: Phase
      label: Phase
      summary: |
        Offset of the wave along the axis / coordinates.
    - name: Amplitude
      label: Amplitude
      summary: |
        The height of the wave, which scales the range of output values. If this is set to 3 (and `Offset` is 0), a ramp wave will produce values from 0 to 3.
    - name: Offset
      label: Offset
      summary: |
        Adds to the values produced by the wave. If this is set to 0.5 (and `Amplitude` is set to 1), a ramp wave will produce values from 0.5 to 1.5.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# waveField

Category: field



A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.