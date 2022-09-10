---
layout: operator
title: lfoGenerator
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/lfoGenerator
redirect_from:
  - /reference/opType/raytk.operators.utility.lfoGenerator/
op:
  category: utility
  name: lfoGenerator
  opType: raytk.operators.utility.lfoGenerator
  parameters:
  - label: Play
    name: Play
  - label: Sync
    name: Sync
  - label: Sync Period
    menuOptions:
    - label: 1/16
      name: sixteenth
    - label: 1/8
      name: eighth
    - label: 1/4
      name: fourth
    - label: 1/2
      name: half
    - label: '1'
      name: one
    - label: '2'
      name: two
    - label: '4'
      name: four
    - label: '8'
      name: eight
    - label: '16'
      name: sixteen
    - label: '32'
      name: thirtytwo
    - label: '64'
      name: sixtyfour
    - label: '128'
      name: onetwentyeight
    name: Syncperiod
  - label: Free Period
    name: Freeperiod
  - label: Wave Type
    menuOptions:
    - label: Constant
      name: const
    - label: Ramp
      name: ramp
    - label: Sine
      name: sin
    - label: Triangle
      name: tri
    - label: Square
      name: square
    - label: Pulse
      name: pulse
    - label: Gaussian
      name: gaussian
    name: Wavetype
  - label: Reverse
    name: Reverse
  - label: Phase
    name: Phase
  - label: Bias
    name: Bias
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  - label: Amplitude Multipliers
    name: Partamp
  - label: Name
    name: Name
  - label: Reset Pulse
    name: Resetpulse
  - label: Reset
    name: Reset
  - label: Reset on Start
    name: Resetonstart
  - label: Reset Value
    name: Resetvalue
  status: beta

---
