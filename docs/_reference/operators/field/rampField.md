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
    summary: Whether to specify the ends of the ramp using an axis or arbitrary points.
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which axis of the position (or coord input) the ramp should use.
  - label: Coordinate Range
    name: Range
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The start and end of the ramp along the chosen axis.
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The start point when using arbitrary points.
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The ened point when using arbitrary points.
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How to handle points outside the specified range.
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
    summary: What type of values to produce (single number floats or vectors).
  - label: Value 1
    name: Value1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The value at the start of the ramp. If in float mode only the first part
      is used.
  - label: Value 2
    name: Value2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The value at the end of the ramp. If in float mode only the first part
      is used.
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
  summary: Field that produces values that fade from one value to another along an
    axis or line.
  thumb: assets/images/reference/operators/field/rampField_thumb.png

---


Field that produces values that fade from one value to another along an axis or line.