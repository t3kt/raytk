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
  detail: 'Only connected inputs are considered, and they are renumbered to skip over
    any missing ones. So if

    only 2 and 4 are connected, they are treated as 1 and 2.


    Iteration values are rounded to the nearest integer (after the `Extend` mode is
    applied to handle values

    outside the expected range from 0 to the number of connected inputs minus 1.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which component of the iteration vector to use. In most cases this should
      be X.
  - label: Extend
    menuOptions:
    - description: Clamp iteration to 0..(N-1) range.
      label: Clamp
      name: clamp
    - description: Loop from 0 to N-1.
      label: Loop
      name: loop
    - description: Zig-zag back and forth between 0 and N-1.
      label: Zig-Zag
      name: zigzag
    name: Extend
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: 'How to handle iteration values outside the 0..(N-1) range. '
  summary: Switches between inputs based on the iteration value provided by a downstream
    operator.
  thumb: assets/images/reference/operators/combine/iterationSwitch_thumb.png

---


Switches between inputs based on the iteration value provided by a downstream operator.

Only connected inputs are considered, and they are renumbered to skip over any missing ones. So if
only 2 and 4 are connected, they are treated as 1 and 2.

Iteration values are rounded to the nearest integer (after the `Extend` mode is applied to handle values
outside the expected range from 0 to the number of connected inputs minus 1.