---
layout: operator
title: quadTreeRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quadTreeRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.quadTreeRepeat/
op:
  category: filter
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
    - vec2
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
    summary: Main input which appears within each cell.
    supportedVariableInputs:
    - offsetField
    - shiftField
    supportedVariables:
    - cell
    - layer
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
    - vec2
    - vec3
    label: Shift Field
    name: shiftField
    required: true
    returnTypes:
    - vec4
    summary: Field that controls the shifting of the overall grid layout.
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
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    required: true
    returnTypes:
    - vec4
    summary: Field that controls the offsetting of the contents within each cell.
    supportedVariableInputs:
    - shiftField
    supportedVariables:
    - cell
    - layer
  name: quadTreeRepeat
  opType: raytk.operators.filter.quadTreeRepeat
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Axis that the grid plane faces.
  - label: Division
    name: Division
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of steps of subdividing.
  - label: Level 1 Chance
    name: Chance1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Likelyhood of a cell getting one level of subdivision.
  - label: Level 2 Chance
    name: Chance2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Likelyhood of a sub-divided cell getting another level of subdivision.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the contents within each repeated cell.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Move the entire arrangement of cells.
  - label: Enable Rescale
    name: Enablerescale
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to apply uniform scaling within each cell so that the contents
      fit the size of the cell.
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Id (xy) & Layer (z)
      name: cell
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How to expose the cell information as iteration values for upstream operators
      to use.
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Seed number used as the basis of the randomization.
  status: beta
  summary: Repeats space in a 2d grid where some cells are subdivided into smaller
    cells recursively.
  thumb: assets/images/reference/operators/filter/quadTreeRepeat_thumb.png
  variables:
  - label: Cell ID Hash (XY)
    name: cell
    summary: Randomization values different for each cell, but without a predictable
      layout.
  - label: Layer Index
    name: layer
    summary: Which layer of subdivision the current cell has.

---


Repeats space in a 2d grid where some cells are subdivided into smaller cells recursively.