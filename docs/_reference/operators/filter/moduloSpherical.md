---
layout: operator
title: moduloSpherical
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloSpherical
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloSpherical/
op:
  category: filter
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
    - Particle
    supportedVariableInputs:
    - repetitionsField
    - offsetField
    - shiftField
    supportedVariables:
    - cell
    - normcell
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
    - vec3
    label: Repetitions Field
    name: repetitionsField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - shiftField
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
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - shiftField
    - repetitionsField
    supportedVariables:
    - cell
    - normcell
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
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    - vec4
  name: moduloSpherical
  opType: raytk.operators.filter.moduloSpherical
  parameters:
  - label: Enable
    name: Enable
  - label: Repetitions
    name: Repetitions
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How many rows and columns to have.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the repetitions across the rows and columns.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the contents of each repetition, away from the sphere center or
      side to side along the columns.
  - label: Pivot
    name: Pivot
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Center point of the sphere
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Rows
      name: rows
    - label: Columns
      name: cols
    - label: Grid
      name: grid
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Flips alternating repetitions so they mirror each other.
  summary: Repeats space in a spherical mesh layout with rows and columns.
  thumb: assets/images/reference/operators/filter/moduloSpherical_thumb.png
  variables:
  - label: cell
    name: cell
    summary: Index of the row and column as integers (0..N).
  - label: normcell
    name: normcell
    summary: Index of the row and column scaled to a 0..1 range based on the number
      of Repetitions.

---


Repeats space in a spherical mesh layout with rows and columns.