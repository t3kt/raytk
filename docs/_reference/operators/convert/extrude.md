---
layout: operator
title: extrude
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/extrude
redirect_from:
  - /reference/opType/raytk.operators.convert.extrude/
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
    - Sdf
    summary: The 2D shape that is extruded along the axis.
  name: extrude
  opType: raytk.operators.convert.extrude
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
  - label: Infinite Height
    name: Infiniteheight
    summary: Whether the shape should be infinitely thick along the axis.
  - label: Height
    name: Height
    summary: Height of the extruded shape.
  - label: Offset
    name: Offset
    summary: Moves the extruded shape up and down along the axis.
  - label: UV Mode
    menuOptions:
    - label: Flat
      name: flat
    - label: Depth
      name: depth
    name: Uvmode
  summary: Creates a 3D SDF by extruding a 2D SDF along along an axis.

---


Creates a 3D SDF by extruding a 2D SDF along along an axis.