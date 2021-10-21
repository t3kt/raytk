---
layout: operator
title: mirrorQuadrant
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorQuadrant
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorQuadrant/
op:
  category: filter
  detail: This is similar to `mirrorOctant` but without mirroring on the diagonals.
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
    - float
    - vec2
    - vec3
    label: Rotate Axis Field
    name: rotateField
    returnTypes:
    - float
    - Sdf
    summary: 'Value field used to vary the `Rotateaxis`. If the field is a 1D field,
      it is given the distance from the center. If it is a 2D field, it is given the
      position along the mirror axes. If it is a 3D field, it is given the raw position.
      The value is converted to radians and *added* to the `Rotateaxis` parameter.*
      `offset_field_definition_in`:'
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
  name: mirrorQuadrant
  opType: raytk.operators.filter.mirrorQuadrant
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
    summary: Axis that faces the plane where coordinates are mirrored.
  - label: Size
    name: Size
    summary: Spacing of the reflection planes.
  - label: Offset
    name: Offset
    summary: Shifts the input before applying reflection.
  - label: Rotate Axis
    name: Rotateaxis
    summary: Rotates the input before applying reflection.
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - description: Numbers the quadrants from 0 to 3.
      label: Quadrant Index (0-3)
      name: index
    - description: Populates the x and y parts of the iteration value with 1 or -1
        for different sides of the dividing planes.
      label: Signed Axes (-1/1, -1/1)
      name: sign
    name: Iterationtype
    summary: Exposes information to upstream operators about which quadrant a point
      is in.
  summary: Mirror coordinates across two axes.

---


Mirror coordinates across two axes.

This is similar to `mirrorOctant` but without mirroring on the diagonals.