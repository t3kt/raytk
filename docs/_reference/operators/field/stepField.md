---
layout: operator
title: stepField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/stepField
redirect_from:
  - /reference/opType/raytk.operators.field.stepField/
op:
  category: field
  detail: 'This can be used to apply one color to the left of some point and another
    color on the right side of that point.

    It can also smooth out the transition between the two values.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: definition_in
    returnTypes:
    - float
    - vec4
    summary: Optional field whose value is used instead of coordinates when checking
      which side of the threshold a point is on.
  name: stepField
  opType: raytk.operators.field.stepField
  parameters:
  - label: Enable
    name: Enable
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
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
  - label: Edge
    name: Edge
  - label: Reverse
    name: Reverse
  - label: Enable Blend
    name: Enableblend
  - label: Blend
    name: Blend
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Value 1
    name: Value1
    summary: Value used when below `Edge`
  - label: Value 2
    name: Value2
    summary: Value used when above `Edge`
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  status: beta
  summary: A field that switches between two values at a threshold point.

---


A field that switches between two values at a threshold point.

This can be used to apply one color to the left of some point and another color on the right side of that point.
It can also smooth out the transition between the two values.