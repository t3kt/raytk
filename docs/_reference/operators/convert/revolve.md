---
layout: operator
title: revolve
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/revolve
redirect_from:
  - /reference/opType/raytk.operators.convert.revolve/
op:
  category: convert
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Cross-Section SDF
    name: cross_section_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    summary: The 2D shape that is revolved around the axis.
  name: revolve
  opType: raytk.operators.convert.revolve
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Radial Offset
    name: Radialoffset
    summary: Moves the cross-section shape closer or further from the axis.
  - label: Axis Offset
    name: Axisoffset
    summary: Moves the resulting shape along the axis.
  summary: Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.

---


Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.