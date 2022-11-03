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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Repetitions Field
    name: repetitionsField
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
    coordTypes:
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
  - label: Shift
    name: Shift
  - label: Offset
    name: Offset
  - label: Pivot
    name: Pivot
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
  variables:
  - label: cell
    name: cell
  - label: normcell
    name: normcell

---
