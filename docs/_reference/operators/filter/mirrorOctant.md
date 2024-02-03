---
layout: operator
title: mirrorOctant
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorOctant
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorOctant/
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
    - vec2
    - vec3
    label: definition_in
    name: definition_in
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
    label: Rotate Axis Field
    name: rotateField
    returnTypes:
    - float
    - Sdf
    summary: Value field used to vary the `Rotateaxis`. If the field is a 1D field,
      it is given the distance from the center. If it is a 2D field, it is given the
      position along the mirror axes. If it is a 3D field, it is given the raw position.
      The value is converted to radians and *added* to the `Rotateaxis` parameter.
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
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
  name: mirrorOctant
  opType: raytk.operators.filter.mirrorOctant
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
    readOnlyHandling: constant
    regularHandling: constant
    summary: Axis that faces the plane where coordinates are mirrored.
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Spacing of the reflection planes.
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts the input before applying reflection.
  - label: Rotate Axis
    name: Rotateaxis
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Rotates the input before applying reflection.
  - name: Iterateoncells
    summary: Enables upstream operators to check which cell in the reflection grid
      a point is in.
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Quadrant Index (0-3)
      name: index
    - label: Signed Axes (-1/1, -1/1)
      name: sign
    name: Iterationtype
    readOnlyHandling: constant
    regularHandling: constant
  summary: Mirror coordinates across two axes and the diagonals.
  thumb: assets/images/reference/operators/filter/mirrorOctant_thumb.png
  variables:
  - label: index
    name: index
  - label: sign
    name: sign

---


Mirror coordinates across two axes and the diagonals.