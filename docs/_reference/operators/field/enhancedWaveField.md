---
layout: operator
title: enhancedWaveField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/enhancedWaveField
redirect_from:
  - /reference/opType/raytkAbstractions.operators.field.enhancedWaveField/
op:
  category: field
  detail: 'This is an enhanced version of the `waveField` operator with added convenience
    features, including:


    * More wave functions including the `pausingWaveFn`, which is sort of like a square
    wave with ramped edges.

    * More control over the output value, including the ability to output vectors
    and colors.

    * Animation controls for the wave phase.'
  moduleName: raytkAbstractions
  name: enhancedWaveField
  opType: raytkAbstractions.operators.field.enhancedWaveField
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin XY
      name: distxy
    - label: Distance From Origin YZ
      name: distyz
    - label: Distance From Origin XZ
      name: distxz
    - label: Distance From Origin XYZ
      name: dist
    name: Axis
    summary: Axis used for the wave function phase. If there is a coordinate field,
      this controls which part of the returned value is used. Otherwise, it controls
      which part of the position in used.
  - label: Center
    name: Center
    summary: The point from which distance is measured.
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
    - label: Smooth Square (.1)
      name: smsquare1
    - label: Smooth Square (.3)
      name: smsquare3
    - label: Pausing Wave
      name: pausing
    name: Function
    summary: The type of wave.
  - label: Period
    name: Period
    summary: The length of a single cycle of the wave.
  - label: Phase
    name: Phase
    summary: Offset of the wave along the axis / coordinates.
  - label: Low Width
    name: Lowwidth
    summary: For the pausing wave, this is the width of the low part of the wave.
      The ramp area is between this and `Highwidth`.
  - label: High Width
    name: Highwidth
    summary: For the pausing wave, this is the width of the high part of the wave.
  - label: Value Mode
    menuOptions:
    - description: Produce a single float value by defining a low and high range.
        Waves that typically produce negative values (like sine) are scaled to match
        the range, just like waves that typically produce 0..1 (like ramp).
      label: Float Range
      name: floatrange
    - description: Produce a single float value by defining an amplitude and offset.
        The wave is scaled to match the amplitude, and then the offset is added.
      label: Float Offset & Amplitude
      name: floatamp
    - description: Produce a vector value by defining a low and high range for each
        component.
      label: Vector Range
      name: vectorrange
    - description: Produce a vector value by defining an amplitude and offset for
        each component.
      label: Vector Offset & Amplitude
      name: vectoramp
    - description: Produce a vector value by defining a range of values as colors.
      label: Color Range
      name: colorrange
    name: Valuemode
    summary: How the wave should produce values.
  - label: Range Low (Float)
    name: Floatrangelow
  - label: Range High (Float)
    name: Floatrangehigh
  - label: Amplitude (Float)
    name: Floatamplitude
  - label: Offset (Float)
    name: Floatoffset
  - label: Range Low (Vector)
    name: Vectorrangelow
  - label: Range High (Vector)
    name: Vectorrangehigh
  - label: Amplitude (Vector)
    name: Vectoramplitude
  - label: Offset (Vector)
    name: Vectoroffset
  - label: Range Low (Color)
    name: Colorrangelow
  - label: Range High (Color)
    name: Colorrangehigh
  - label: Enable Phase Animation
    name: Enableanim
    summary: Whether animation should be enabled for the wave phase. When off, the
      phase will stay constant.
  - label: Play
    name: Animplay
    summary: Whether the animation should be playing or paused at whatever offset
      it was at when it was paused.
  - label: Reverse
    name: Animreverse
  - label: Speed
    name: Animspeed
    summary: How fast the phase should increase.
  - label: Speed Multiplier
    name: Animspeedmult
    summary: Multiplies the speed of the animation, making it easier to have speed
      mapped to something like audio levels while also having a separate slider to
      scale that speed.
  status: beta
  summary: Field that produces different types of values based on wave functions.

---


Field that produces different types of values based on wave functions.

This is an enhanced version of the `waveField` operator with added convenience features, including:

* More wave functions including the `pausingWaveFn`, which is sort of like a square wave with ramped edges.
* More control over the output value, including the ability to output vectors and colors.
* Animation controls for the wave phase.