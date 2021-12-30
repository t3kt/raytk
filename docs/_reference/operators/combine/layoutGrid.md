---
layout: operator
title: layoutGrid
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/layoutGrid
redirect_from:
  - /reference/opType/raytk.operators.combine.layoutGrid/
op:
  category: combine
  detail: 'This is useful to see several different variations of a shape.

    The input shapes are shifted to the center of their cell.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
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
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
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
    - vec2
    - vec3
    label: definition_in_3
    name: definition_in_3
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
    - vec2
    - vec3
    label: definition_in_4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: layoutGrid
  opType: raytk.operators.combine.layoutGrid
  parameters:
  - label: Enable
    name: Enable
  - label: Layout
    menuOptions:
    - description: Slice space into cells horizontally. The first cell extends off
        infinitely to the left and the last cell extends infinitely off to the right.
      label: Row
      name: row
    - description: Slice space into cells vertically.
      label: Column
      name: column
    - description: Slice space into 4 cells arranged in a grid.
      label: Grid Rows
      name: gridrow
    name: Layout
    summary: How to arrange the cells.
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    summary: The plane along which to arrange the cells.
  - label: Size
    name: Size
    summary: The size of the cells
  - label: Pre Scale
    name: Prescale
    summary: Scales the inputs within their cells.
  summary: Slices space into a grid, and places each input in a separate cell.
  thumb: assets/images/reference/operators/combine/layoutGrid_thumb.png

---


Slices space into a grid, and places each input in a separate cell.

This is useful to see several different variations of a shape.
The input shapes are shifted to the center of their cell.