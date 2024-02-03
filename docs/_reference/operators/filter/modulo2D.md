---
layout: operator
title: modulo2D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo2D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo2D/
op:
  category: filter
  detail: 'This has the effect of making an infinite grid of copies of (slices/cells
    of) the input, but without the cost of having

    to separately calculate each copy.'
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
    - tiledquad
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
    - vec2
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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
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
    - tiledquad
    - normcoord
    - shiftedcellcoord
  keywords:
  - grid
  - modulo
  - repeat
  name: modulo2D
  opType: raytk.operators.filter.modulo2D
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - description: Repeat space on the Y and Z axes.
      label: YZ
      name: x
    - description: Repeat space on the X and Z axes.
      label: ZX
      name: y
    - description: Repeat space on the X and Y axes.
      label: XY
      name: z
    name: Axis
    readOnlyHandling: constant
    regularHandling: runtime
    summary: The axis facing the plane along which space is repeated.
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The spacing of the grid along the two axes. This sets the size of the
      cell taken from the input.
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts where the input cell is taken from without moving the position
      of the grid.
  - label: Shift
    name: Shift
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts the whole grid (and its contents).
  - label: Mirror Type
    menuOptions:
    - description: All cells are treated the same.
      label: None
      name: none
    - description: Every other cell is flipped.
      label: Mirror
      name: mirror
    - description: Flip every other cell along the diagonal axis as well. This means
        that for an input with something in one corner, there will be groups of 4
        cells with all those corners facing each other.
      label: Grid
      name: grid
    name: Mirrortype
    readOnlyHandling: constant
    regularHandling: constant
    summary: How the cells are varied.
  - label: Iteration Type
    menuOptions:
    - description: Pass along whatever is provided by the next op after this one.
      label: None
      name: none
    - description: For each cluster of 4 cells, output 0 for the top left, 1 for top
        right, 2 for bottom left,  and 3 for bottom right, and put that value in the
        x component, and set yzw to 0.
      label: Quadrant Index (0-3) In Tiles
      name: tiledquadrant
    - description: Use the cell coordinates as the x and y components of the iteration,
        with zw set to 0. Note that it always uses xy, even if the grid is along another
        plane.
      label: Cell Coordinates
      name: cellcoord
    - description: Cell coordinates that alternate between 0 and 1 along both axes
        in xy, with zw set to 0.
      label: Alternating Cell Coordinates On Axes (0-1, 0-1)
      name: alternatingcoord
    name: Iterationtype
    readOnlyHandling: constant
    regularHandling: constant
    summary: Whether and how to expose iteration values to upstream operators.
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
  - label: Limit Start
    name: Limitstart
  - label: Limit Stop
    name: Limitstop
  - label: Limit Offset
    name: Limitoffset
  shortcuts:
  - m2
  summary: Repeats space along 2 axes.
  thumb: assets/images/reference/operators/filter/modulo2D_thumb.png
  variables:
  - label: cellcoord
    name: cellcoord
  - label: tiledquad
    name: tiledquad
  - label: normcoord
    name: normcoord
  - label: shiftedcellcoord
    name: shiftedcellcoord

---


Repeats space along 2 axes.

This has the effect of making an infinite grid of copies of (slices/cells of) the input, but without the cost of having
to separately calculate each copy.