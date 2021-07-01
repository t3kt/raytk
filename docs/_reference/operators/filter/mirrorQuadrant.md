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
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
    label: Rotate Axis Field
    name: rotate_axis_field_definition_in
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec3
    label: Offset Field
    name: offset_field_definition_in
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
  - label: Size
    name: Size
  - label: Offset
    name: Offset
  - label: Rotate Axis
    name: Rotateaxis
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Quadrant Index (0-3)
      name: index
    - label: Signed Axes (-1/1, -1/1)
      name: sign
    name: Iterationtype

---
