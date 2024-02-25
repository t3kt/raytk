---
layout: operator
title: texture1dField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/texture1dField
redirect_from:
  - /reference/opType/raytk.operators.field.texture1dField/
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
  name: texture1dField
  opType: raytk.operators.field.texture1dField
  parameters:
  - label: Texture
    name: Texture
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
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Which axis to use to determine the position in the TOP to use.
  - label: Coord Mode
    menuOptions:
    - label: Position
      name: position
    - label: Scaled Index
      name: scaledindex
    name: Coordmode
  - label: Translate
    name: Translate
    summary: Offsets the coordinate value. This is applied before the "Extend Mode".
  - label: Scale
    name: Scale
    summary: Scales the coordinate value. This is applied before the "Extend Mode".
  - label: Index Range
    name: Indexrange
  - label: Extend Mode
    menuOptions:
    - label: Hold
      name: hold
    - label: Zero
      name: zero
    - label: Repeat
      name: repeat
    - label: Mirror
      name: mirror
    name: Extendmode
    readOnlyHandling: baked
    regularHandling: baked
    summary: How to handle coordinates outside the 0..1 range.
  status: beta

---
