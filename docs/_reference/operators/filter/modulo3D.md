---
layout: operator
title: modulo3D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo3D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo3D/
op:
  category: filter
  detail: 'This has the effect of making an infinite 3D grid of copies of (slices/cells
    of) the input, but without the cost of having

    to separately calculate each one.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Size Field
    name: sizeField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - sizeField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - sizeField
    - shiftField
    supportedVariables:
    - cellcoord
    - normcoord
    - shiftedcellcoord
  keywords:
  - grid
  - modulo
  - repeat
  name: modulo3D
  opType: raytk.operators.filter.modulo3D
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The spacing of the grid along each axis, which is also the size of the
      cell that is taken from the input.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts where the input cell is taken from without moving the position
      of the grid.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the whole grid (and its contents).
  - label: Limit Type
    menuOptions:
    - label: None
      name: none
    - label: Both
      name: both
    - label: Start Only
      name: start
    - label: Stop Only
      name: stop
    name: Limittype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Limit Start
    name: Limitstart
  - label: Limit Stop
    name: Limitstop
  - label: Limit Offset
    name: Limitoffset
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Coordinate
      name: cellcoord
    - label: Alternating Cell Coordinate (0,1,0,1)
      name: alternatingcoord
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  shortcuts:
  - m3
  summary: Repeats space along all 3 axes.
  thumb: assets/images/reference/operators/filter/modulo3D_thumb.png
  variables:
  - label: Cell Coord
    name: cellcoord
  - label: Normalized Cell Coord
    name: normcoord
  - label: Shifted Cell Coord
    name: shiftedcellcoord

---


Repeats space along all 3 axes.

This has the effect of making an infinite 3D grid of copies of (slices/cells of) the input, but without the cost of having
to separately calculate each one.