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
    coordTypes:
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
    summary: The spacing of the grid along each axis, which is also the size of the
      cell that is taken from the input.
  - label: Offset
    name: Offset
    summary: Shifts where the input cell is taken from without moving the position
      of the grid.
  - label: Shift
    name: Shift
    summary: Shifts the whole grid (and its contents).
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Coordinate
      name: cellcoord
    - label: Alternating Cell Coordinate (0,1,0,1)
      name: alternatingcoord
    name: Iterationtype
  summary: Repeats space along all 3 axes.

---


Repeats space along all 3 axes.

This has the effect of making an infinite 3D grid of copies of (slices/cells of) the input, but without the cost of having
to separately calculate each one.