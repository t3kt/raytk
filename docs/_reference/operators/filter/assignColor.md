---
layout: operator
title: assignColor
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignColor
redirect_from:
  - /reference/opType/raytk.operators.filter.assignColor/
op:
  category: filter
  detail: Various types of materials and fields can access and use the surface color
    attributes.
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    summary: SDF definition to which the color is applied.
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
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    summary: Optional field used to calculate the color instead of the `Color` parameter.
  keywords:
  - color
  - material
  - modularmat
  - surface
  name: assignColor
  opType: raytk.operators.filter.assignColor
  parameters:
  - label: Enable
    name: Enable
  - label: Color
    name: Color
  summary: Assigns a surface color attribute to an SDF surface.

---


Assigns a surface color attribute to an SDF surface.

Various types of materials and fields can access and use the surface color attributes.