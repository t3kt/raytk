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
      this controls which part of the returned value is used. Otherwise it controls
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
  - label: High Width
    name: Highwidth
  - label: Value Mode
    menuOptions:
    - label: Float Range
      name: floatrange
    - label: Float Offset & Amplitude
      name: floatamp
    - label: Vector Range
      name: vectorrange
    - label: Vector Offset & Amplitude
      name: vectoramp
    - label: Color Range
      name: colorrange
    name: Valuemode
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
  - label: Play
    name: Animplay
  - label: Reverse
    name: Animreverse
  - label: Speed
    name: Animspeed
  - label: Speed Multiplier
    name: Animspeedmult
  status: beta

---
