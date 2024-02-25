---
layout: operator
title: pointDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/pointDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.pointDistanceField/
op:
  category: field
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
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
    summary: If provided, this is used to produce positions instead of the actual
      coordinates.
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
    label: Center Field
    name: centerField
    returnTypes:
    - float
    - vec4
    summary: If provided, this is used to produce the center position instead of the
      Center parameter.
    supportedVariableInputs:
    - coordField
  name: pointDistanceField
  opType: raytk.operators.field.pointDistanceField
  parameters:
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The point from which distance is measured.
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
    summary: The type of coordinates to use.
  - label: Axes
    menuOptions:
    - label: XYZ
      name: xyz
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: XZ
      name: xz
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axes
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which axes to use when calculating distances.
  summary: A float field that provides the distance from a specific point in space
    from either the current position or from another point.
  thumb: assets/images/reference/operators/field/pointDistanceField_thumb.png

---


A float field that provides the distance from a specific point in space from either the current position or from another point.