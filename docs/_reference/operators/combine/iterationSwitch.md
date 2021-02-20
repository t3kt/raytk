---
layout: operator
title: iterationSwitch
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/iterationSwitch
redirect_from:
  - /reference/opType/raytk.operators.combine.iterationSwitch/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    summary: The input that should be used when the iteration is 0 (or more accurately
      < 0.5).
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    summary: The input that should be used when the iteration is 1 (or more accurately
      >= 0.5).
  name: iterationSwitch
  opType: raytk.operators.combine.iterationSwitch
  parameters:
  - label: Enable
    name: Enable
  - label: Iteration Part
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: W
      name: w
    name: Iterationpart
    summary: Which component of the iteration vector to use. In most cases this should
      be X.
  - label: Extend
    menuOptions:
    - description: Clamp iteration to 0..1 range.
      label: Clamp
      name: clamp
    - description: Alternate between 0 for even numbers and 1 for odd numbers.
      label: Loop
      name: loop
    name: Extend
    summary: 'How to handle iteration values outside the 0..1 range. '
  summary: Switches between inputs based on the iteration value provided by a downstream
    operator.

---


Switches between inputs based on the iteration value provided by a downstream operator.