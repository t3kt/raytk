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
    summary: If attached, the wave will use this to determine the numbers that it
      passes to the wave function (instead of using the position along the chosen
      `Axis`).
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
    label: Period Field
    name: periodField
    returnTypes:
    - float
    summary: If attached, the wave will use this field to multiply the `Period` parameter,
      which can be used for frequency modulation.
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
    - float
    label: Wave Function
    name: waveFunc
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
    label: Amplitude Field
    name: amplitudeField
    returnTypes:
    - float
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
    - label: Reverse Ramp
      name: rramp
    - label: Square
      name: square
    - label: Additive Square (2)
      name: addsquare2
    - label: Additive Square (4)
      name: addsquare4
    - label: Additive Square (8)
      name: addsquare8
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
    readOnlyHandling: constant
    regularHandling: constant
    summary: Axis used for the wave function phase. If there is a coordinate field,
      this controls which part of the returned value is used. Otherwise it controls
      which part of the position in used.
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
  - label: Period
    name: Period
    summary: The length of a single cycle of the wave.
  - label: Phase
    name: Phase
    summary: Offset of the wave along the axis / coordinates.
  - label: Amplitude
    name: Amplitude
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The height of the wave, which scales the range of output values. If this
      is set to 3 (and `Offset` is 0), a ramp wave will produce values from 0 to 3.
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Adds to the values produced by the wave. If this is set to 0.5 (and `Amplitude`
      is set to 1), a ramp wave will produce values from 0.5 to 1.5.
  - name: Contexttype
  summary: A field that uses a periodic wave.
  thumb: assets/images/reference/operators/field/waveField_thumb.png

---


A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.