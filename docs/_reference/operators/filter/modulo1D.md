---
layout: operator
title: modulo1D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo1D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo1D/
op:
  category: filter
  detail: 'This has the effect of making infinite copies of (slices of) the input,
    but without the cost

    of having to separately calculate each copy.'
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - sizeField
    - shiftField
    - offsetField
    supportedVariables:
    - cellcoord
    - normcoord
    - shiftedcellcoord
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
    label: Size Field
    name: sizeField
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
    - vec2
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
    - shiftField
    supportedVariables:
    - cellcoord
    - normcoord
    - shiftedcellcoord
  keywords:
  - modulo
  - repeat
  name: modulo1D
  opType: raytk.operators.filter.modulo1D
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: The axis to repeat space along.
  - label: Size
    name: Size
    summary: The spacing of the repetition. This sets the with of the slice taken
      from the input.
  - label: Offset
    name: Offset
    summary: Shifts where the input slice is taken from without moving the position
      of the repetitions.
  - label: Shift
    name: Shift
    summary: Shifts the whole repeated space.
  - label: Mirror Type
    menuOptions:
    - description: No mirroring.
      label: None
      name: none
    - description: Flip every other slice.
      label: Mirror
      name: mirror
    name: Mirrortype
    summary: How to the slices are varied.
  - label: Use Limit
    name: Uselimit
    summary: Whether to have a limited number of slices instead of an infinite series.
  - label: Limit Start
    name: Limitstart
    summary: The index of the first slice to show. This can also be a fractional value
      to cut off part of the first slice (though this can cause rendering issues).
  - label: Limit Stop
    name: Limitstop
    summary: THe index of the last slice to show. This can also be a fractional value
      to cut off part of the last slice (though this can cause rendering issues).
  - label: Limit Offset
    name: Limitoffset
    summary: Offsets the `Limitstart` and `Limitstop` indices.
  - label: Iteration Type
    menuOptions:
    - description: Pass along whatever is provided by the next op after this one.
      label: None
      name: none
    - description: Use the slice index as the x component of the iteration, with yzw
        set to 0.
      label: Cell Coordinate
      name: cellcoord
    - description: Alternates back and forth between 0 and 1 in the x component, with
        yzw set to 0.
      label: Alternating Cell Coordinate (0,1,0,1)
      name: alternatingcoord
    name: Iterationtype
    summary: Whether and how to expose iteration values to upstream operators.
  - label: Limit Type
    menuOptions:
    - label: Both
      name: both
    - label: Start Only
      name: start
    - label: Stop Only
      name: stop
    name: Limittype
  shortcuts:
  - m1
  summary: Repeats space along one axis.
  thumb: assets/images/reference/operators/filter/modulo1D_thumb.png
  variables:
  - label: cellcoord
    name: cellcoord
  - label: normcoord
    name: normcoord
  - label: shiftedcellcoord
    name: shiftedcellcoord

---


Repeats space along one axis.

This has the effect of making infinite copies of (slices of) the input, but without the cost
of having to separately calculate each copy.