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
  inputs:
  - contextTypes:
    - Context
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
  - label: Iterate On Cells
    name: Iterateoncells
    summary: Whether to expose the slice number as an "iteration" value for upstream
      ops.
  - label: Enable
    name: Enable
  summary: Repeats space radially, like a kaleidoscope.

---


Repeats space radially, like a kaleidoscope.