---
layout: operator
title: waveField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/waveField
redirect_from:
  - /reference/opType/raytk.operators.field.waveField/
op:
  category: field
  detail: 'If there is an input, that rop is used to get the coordinate that is fed
    into the wave function.

    Without an input, the Axis is used to run the wave function on the position along
    the selected axis.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: coordinate_field_in
    returnTypes:
    - float
    - vec4
    summary: If attached, the wave will use this to determine the numbers that it
      passes to the wave function (instead of using the position along the chosen
      `Axis`).
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Period Field
    name: period_field_definition_in
    returnTypes:
    - float
    summary: If attached, the wave will use this field to multiply the `Period` parameter,
      which can be used for frequency modulation.
  name: waveField
  opType: raytk.operators.field.waveField
  parameters:
  - label: Enable
    name: Enable
  - label: Wave
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
    name: Function
    summary: The type of wave.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - description: Uses distance from the origin instead of an axis.
      label: Distance From Origin
      name: dist
    name: Axis
    summary: If there is no input, the coordinate along this axis is used for the
      wave function phase.
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Period
    name: Period
    summary: The length of a single cycle of the wave.
  - label: Phase
    name: Phase
    summary: Offset of the wave along the axis / coordinates.
  - label: Amplitude
    name: Amplitude
    summary: The height of the wave, which scales the range of output values. If this
      is set to 3 (and `Offset` is 0), a ramp wave will produce values from 0 to 3.
  - label: Offset
    name: Offset
    summary: Adds to the values produced by the wave. If this is set to 0.5 (and `Amplitude`
      is set to 1), a ramp wave will produce values from 0.5 to 1.5.
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
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
  summary: A field that uses a periodic wave.

---


A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.