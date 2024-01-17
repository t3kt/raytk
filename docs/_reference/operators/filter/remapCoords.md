---
layout: operator
title: remapCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/remapCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.remapCoords/
op:
  category: filter
  detail: When the shader uses the operator, it will first pass the coordinates to
    the "Coord Field". It then uses the resulting remapped coordinates when running
    the first input operator.
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
    - vec4
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    required: true
    returnTypes:
    - float
    - vec4
  name: remapCoords
  opType: raytk.operators.filter.remapCoords
  parameters:
  - label: Enable
    name: Enable
  - label: Remap Mode
    menuOptions:
    - description: Totally replace the original coordinates with the new ones that
        came from the "Coord Field".
      label: Replace
      name: replace
    - description: Add the new coordinates to the original ones.
      label: Add
      name: add
    - description: Multiply the new coordinates with the original ones.
      label: Multiply
      name: multiply
    name: Remapmode
    summary: How the remapped coordinates are applied to the original coordinates.
  - label: Mix
    name: Mix
    summary: Cross-fades between the original coordinates and the remapped ones.
  status: beta
  summary: Modifies space using a vector field.

---


Modifies space using a vector field.

When the shader uses the operator, it will first pass the coordinates to the "Coord Field". It then uses the resulting remapped coordinates when running the first input operator.