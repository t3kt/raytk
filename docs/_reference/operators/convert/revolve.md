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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Rotate Field
    name: rotate_field_in
    returnTypes:
    - float
    summary: Optional field that controls rotation of the cross-section as it goes
      around the axis.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Scale Field
    name: scale_field_in
    returnTypes:
    - float
    summary: Optional field that controls scale of the cross-section as it goes around
      the axis.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Translate Field
    name: translate_field_in
    returnTypes:
    - vec4
    summary: Optional field that controls translate of the cross-section as it goes
      around the axis.
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
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Ratio
      name: ratio
    name: Iterationtype
  summary: Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.

---


Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.