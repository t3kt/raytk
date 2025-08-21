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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    label: Cross-Section SDF
    name: crossSection
    required: true
    returnTypes:
    - Sdf
    summary: The 2D shape that is revolved around the axis.
    supportedVariableInputs:
    - cross_section_definition_in
    - rotate_field_in
    - scale_field_in
    - translate_field_in
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
    summary: Optional field that controls rotation of the cross-section as it goes
      around the axis.
    supportedVariableInputs:
    - radialOffsetField
    - axisOffsetField
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    summary: Optional field that controls scale of the cross-section as it goes around
      the axis.
    supportedVariableInputs:
    - rotateField
    - radialOffsetField
    - axisOffsetField
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec3
    label: Translate Field
    name: translateField
    returnTypes:
    - vec4
    summary: Optional field that controls translate of the cross-section as it goes
      around the axis.
    supportedVariableInputs:
    - scaleField
    - rotateField
    - radialOffsetField
    - axisOffsetField
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Radial Offset Field
    name: radialOffsetField
    returnTypes:
    - float
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Axis Offset Field
    name: axisOffsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - radialOffsetField
    supportedVariables:
    - angle
    - normangle
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Radial Offset
    name: Radialoffset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the cross-section shape closer or further from the axis.
  - label: Axis Offset
    name: Axisoffset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the resulting shape along the axis.
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Ratio
      name: ratio
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  summary: Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.
  thumb: assets/images/reference/operators/convert/revolve_thumb.png
  variables:
  - label: Angle
    name: angle
  - label: Normalized Angle
    name: normangle

---


Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.