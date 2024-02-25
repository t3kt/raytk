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
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Pivot
    name: Pivot
    readOnlyHandling: baked
    regularHandling: runtime
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
  variables:
  - label: cell
    name: cell
  - label: normcell
    name: normcell

---
