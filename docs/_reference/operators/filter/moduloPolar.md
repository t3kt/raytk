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
    - VertexContext
    - PixelContext
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
    - Volume
    - Ray
    - Light
    supportedVariables:
    - step
    - normstep
    - globalangle
    - normglobalangle
    - normlocalangle
    - centerdist
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Pre Rotate Field
    name: preRotateField
    returnTypes:
    - float
    supportedVariables:
    - step
    - normstep
    - centerdist
    - globalangle
    - normglobalangle
    - normlocalangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - preRotateField
    supportedVariables:
    - step
    - normstep
    - centerdist
    - globalangle
    - normglobalangle
    - normlocalangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
    supportedVariables:
    - centerdist
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: The axis around which space is sliced.
  - label: Repetitions
    name: Repetitions
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of angle repetitions. For example, a value of 6 would mean
      6 slices of space, each with a 60 degree width.
  - label: Round To Integer
    name: Roundtointeger
    summary: Whether to round the `Repetitions` (and `Limit Low` and `Limit High`)
      to whole integers.
  - label: Pre Rotate
    name: Prerotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation applied before slicing.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation applied after slicing.
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to flip every other slice. This is useful to avoid hard breaks
      at edges. It will result in the appearance of half as many slices, since half
      of them will be flipped.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Distance to shift the shape before slicing it.
  - label: Use Limit
    name: Uselimit
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to limit the range of repetitions. Space outside that range will
      be left as it is.
  - label: Limit Low
    name: Limitlow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Start or the repetition range, in terms of the number of repetitions.
  - label: Limit High
    name: Limithigh
    readOnlyHandling: baked
    regularHandling: runtime
    summary: End or the repetition range, in terms of the number of repetitions.
  - name: Iterateoncells
    summary: Whether to expose the slice number as an "iteration" value for upstream
      ops.
  - label: Enable
    name: Enable
  - label: Pivot
    name: Pivot
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Index
      name: index
    - label: Cell Ratio
      name: ratio
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  shortcuts:
  - mp
  summary: Repeats space radially, like a kaleidoscope.
  thumb: assets/images/reference/operators/filter/moduloPolar_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep
  - label: Global Angle (0..360)
    name: globalangle
  - label: Normalized Global Angle (0..1)
    name: normglobalangle
  - label: Normalized Local Angle (0..1)
    name: normlocalangle
  - label: Center Distance
    name: centerdist

---


Repeats space radially, like a kaleidoscope.