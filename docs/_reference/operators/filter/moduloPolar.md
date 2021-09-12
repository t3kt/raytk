---
layout: operator
title: moduloPolar
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloPolar
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloPolar/
op:
  category: filter
  images:
  - assets/images/reference/operators/filter/moduloPolar_2d.png
  - assets/images/reference/operators/filter/moduloPolar_3d_iteration_index.png
  - assets/images/reference/operators/filter/moduloPolar_3d_iteration_ratio.png
  - assets/images/reference/operators/filter/moduloPolar_3d_limit.png
  - assets/images/reference/operators/filter/moduloPolar_3d_mirror.png
  - assets/images/reference/operators/filter/moduloPolar_3d_no_mirror.png
  - assets/images/reference/operators/filter/moduloPolar_3d_offset.png
  - assets/images/reference/operators/filter/moduloPolar_3d_offset_field.png
  - assets/images/reference/operators/filter/moduloPolar_3d_pre_rotate_field.png
  - assets/images/reference/operators/filter/moduloPolar_3d_rotate_field.png
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
    - vec2
    - vec3
    label: Pre Rotate Field
    name: pre_rotate_field_definition_in
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offset_field_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotate_field_definition_in1
    returnTypes:
    - float
  keywords:
  - kaleidoscope
  - modulo
  - polar
  - repeat
  name: moduloPolar
  opType: raytk.operators.filter.moduloPolar
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
    summary: The axis around which space is sliced.
  - label: Repetitions
    name: Repetitions
    summary: The number of angle repetitions. For example, a value of 6 would mean
      6 slices of space, each with a 60 degree width.
  - label: Round To Integer
    name: Roundtointeger
    summary: Whether to round the `Repetitions` (and `Limit Low` and `Limit High`)
      to whole integers.
  - label: Pre Rotate
    name: Prerotate
    summary: Rotation applied before slicing.
  - label: Rotate
    name: Rotate
    summary: Rotation applied after slicing.
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    summary: Whether to flip every other slice. This is useful to avoid hard breaks
      at edges. It will result in the appearance of half as many slices, since half
      of them will be flipped.
  - label: Offset
    name: Offset
    summary: Distance to shift the shape before slicing it.
  - label: Use Limit
    name: Uselimit
    summary: Whether to limit the range of repetitions. Space outside that range will
      be left as it is.
  - label: Limit Low
    name: Limitlow
    summary: Start or the repetition range, in terms of the number of repetitions.
  - label: Limit High
    name: Limithigh
    summary: End or the repetition range, in terms of the number of repetitions.
  - name: Iterateoncells
    summary: Whether to expose the slice number as an "iteration" value for upstream
      ops.
  - label: Enable
    name: Enable
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Index
      name: index
    - label: Cell Ratio
      name: ratio
    name: Iterationtype
  summary: Repeats space radially, like a kaleidoscope.

---


Repeats space radially, like a kaleidoscope.