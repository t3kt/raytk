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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Cross-Section SDF
    name: cross_section_definition_in
    required: true
    returnTypes:
    - Sdf
    summary: The 2D shape that is extruded along the axis.
    supportedVariableInputs:
    - height_definition_in
    - offset_definition_in
    supportedVariables:
    - RTK_raytk_operators_convert_extrude_axispos
    - RTK_raytk_operators_convert_extrude_normoffset
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
    - vec2
    - vec3
    label: Height Field
    name: height_definition_in
    returnTypes:
    - float
    supportedVariables:
    - axispos
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
    - vec2
    - vec3
    label: Offset Field
    name: offset_definition_in
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    supportedVariables:
    - axispos
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Infinite Height
    name: Infiniteheight
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether the shape should be infinitely thick along the axis.
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Height of the extruded shape.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the extruded shape up and down along the axis.
  - label: UV Mode
    menuOptions:
    - label: Flat
      name: flat
    - label: Depth
      name: depth
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Ratio
      name: ratio
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Optimize
    name: Optimize
  shortcuts:
  - ext
  summary: Creates a 3D SDF by extruding a 2D SDF along along an axis.
  thumb: assets/images/reference/operators/convert/extrude_thumb.png
  variables:
  - label: RTK_raytk_operators_convert_extrude_axispos
    name: RTK_raytk_operators_convert_extrude_axispos
  - label: RTK_raytk_operators_convert_extrude_normoffset
    name: RTK_raytk_operators_convert_extrude_normoffset

---


Creates a 3D SDF by extruding a 2D SDF along along an axis.