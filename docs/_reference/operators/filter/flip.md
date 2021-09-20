---
layout: operator
title: flip
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/flip
redirect_from:
  - /reference/opType/raytk.operators.filter.flip/
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
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: flip
  opType: raytk.operators.filter.flip
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
  - label: Offset
    name: Offset
    summary: Moves the reflection plane along the axis.
  - label: Shift
    name: Shift
    summary: Moves the input towards / away from the reflection plane.
  - label: Merge Type
    menuOptions:
    - label: None
      name: none
    - label: Union
      name: union
    - label: Smooth Union
      name: smoothUnion
    name: Mergetype
    summary: Whether to just flip the input or flip it and merge that with the original.
  - label: Merge Radius
    name: Mergeradius
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - description: The original is assigned 0, flipped 1.
      label: Index (0/1)
      name: index
    - description: Original is assigned 1, flipped -1.
      label: Signed (-1/1)
      name: sign
    name: Iterationtype
    summary: What kind of iteration values should be provided for upstream ops.
  summary: Flips the input across an axis, either on its own or merged with the original.

---


Flips the input across an axis, either on its own or merged with the original.