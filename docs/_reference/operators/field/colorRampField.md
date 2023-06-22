---
layout: operator
title: colorRampField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorRampField
redirect_from:
  - /reference/opType/raytk.operators.field.colorRampField/
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
    coordTypes:
    - float
    label: Easing Function
    name: easingFunc
    returnTypes:
    - float
  keywords:
  - color
  - gradient
  - ramp
  name: colorRampField
  opType: raytk.operators.field.colorRampField
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
  - label: Coordinate Range
    name: Range
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
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
  - label: Color 1
    name: Color1
  - label: Alpha 1
    name: Alpha1
  - label: Color 2
    name: Color2
  - label: Alpha 2
    name: Alpha2
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
  summary: A vector field that maps an input field to values from a range of colors.
  thumb: assets/images/reference/operators/field/colorRampField_thumb.png

---


A vector field that maps an input field to values from a range of colors.