---
layout: operator
title: rampField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/rampField
redirect_from:
  - /reference/opType/raytk.operators.field.rampField/
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
    required: true
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Point 1 Field
    name: point1Field
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Point 2 Field
    name: point2Field
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    label: Easing Function
    name: easingFunc
    returnTypes:
    - float
  name: rampField
  opType: raytk.operators.field.rampField
  parameters:
  - label: Enable
    name: Enable
  - label: Coordinate Mode
    menuOptions:
    - label: Axis
      name: axis
    - label: Endpoints
      name: points
    name: Coordmode
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
    readOnlyHandling: constant
    regularHandling: constant
  - label: Coordinate Range
    name: Range
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 1
    name: Point1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: macro
    regularHandling: runtime
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
    readOnlyHandling: constant
    regularHandling: constant
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Value 1
    name: Value1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Value 2
    name: Value2
    readOnlyHandling: macro
    regularHandling: runtime
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
  status: beta
  thumb: assets/images/reference/operators/field/rampField_thumb.png

---
