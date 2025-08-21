---
layout: operator
title: bend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/bend
redirect_from:
  - /reference/opType/raytk.operators.filter.bend/
op:
  category: filter
  detail: For example, bends sideways (towards X) depending on the vertical position
    (along Y).
  images:
  - assets/images/reference/operators/filter/bend_2d_along_x_to_y.png
  - assets/images/reference/operators/filter/bend_2d_along_y_to_x.png
  - assets/images/reference/operators/filter/bend_along_x_to_y.png
  - assets/images/reference/operators/filter/bend_along_x_to_z.png
  - assets/images/reference/operators/filter/bend_along_y_to_x.png
  - assets/images/reference/operators/filter/bend_along_y_to_z.png
  - assets/images/reference/operators/filter/bend_along_z_to_x.png
  - assets/images/reference/operators/filter/bend_along_z_to_y.png
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
    - vec3
    label: Input
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - definition_in_2
    supportedVariables:
    - axispos
    - bendpos
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
    - vec2
    - vec3
    label: Bend Field
    name: bendField
    returnTypes:
    - float
    - Sdf
    summary: Value field that determines how much to bend. If this accepts 1D coords,
      it is passed the position along the bend axis. For 2D coords, both the bend
      axis and the bend direction are passed. For 3D coords, the relative XYZ position
      is passed.
    supportedVariables:
    - axispos
    - bendpos
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
    - vec2
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - bendField
    supportedVariables:
    - axispos
    - bendpos
  name: bend
  opType: raytk.operators.filter.bend
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - label: Along X Toward Y
      name: xyz
    - label: Along X Toward Z
      name: xzy
    - label: Along Y Toward X
      name: yxz
    - label: Along Y Toward Z
      name: yzx
    - label: Along Z Toward X
      name: zxy
    - label: Along Z Toward Y
      name: zyx
    name: Direction
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Chooses the axis to bend along and the axis to bend towards.
  - label: Amount
    name: Amount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of bending.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the axis to bend along and the axis to bend towards.
  - label: Side
    menuOptions:
    - label: Both
      name: both
    - label: Negative
      name: neg
    - label: Positive
      name: pos
    name: Side
    readOnlyHandling: semibaked
    regularHandling: semibaked
  summary: Bends space, along a main axis, towards a second axis.
  thumb: assets/images/reference/operators/filter/bend_thumb.png
  variables:
  - label: Position Along Axis
    name: axispos
  - label: Position On Bend Axis
    name: bendpos

---


Bends space, along a main axis, towards a second axis.

For example, bends sideways (towards X) depending on the vertical position (along Y).