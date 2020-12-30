---
layout: operator
title: moduloPolar
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloPolar
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloPolar/
op:
  name: moduloPolar
  summary: |
    Repeats space radially, like a kaleidoscope.
  opType: raytk.operators.filter.moduloPolar
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Axis
      label: Axis
      summary: |
        The axis around which space is sliced.
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Repetitions
      label: Repetitions
      summary: |
        The number of angle repetitions. For example, a value of 6 would mean 6 slices of space, each with a 60 degree width.
    - name: Roundtointeger
      label: Round To Integer
      summary: |
        Whether to round the `Repetitions` (and `Limit Low` and `Limit High`) to whole integers.
    - name: Prerotate
      label: Pre Rotate
      summary: |
        Rotation applied before slicing.
    - name: Rotate
      label: Rotate
      summary: |
        Rotation applied after slicing.
    - name: Mirrortype
      label: Mirror Type
      summary: |
        Whether to flip every other slice. This is useful to avoid hard breaks at edges. It will result in the appearance of half as many slices, since half of them will be flipped.
      menuOptions:
        - name: none
          label: None
        - name: mirror
          label: Mirror
    - name: Offset
      label: Offset
      summary: |
        Distance to shift the shape before slicing it.
    - name: Uselimit
      label: Use Limit
      summary: |
        Whether to limit the range of repetitions. Space outside that range will be left as it is.
    - name: Limitlow
      label: Limit Low
      summary: |
        Start or the repetition range, in terms of the number of repetitions.
    - name: Limithigh
      label: Limit High
      summary: |
        End or the repetition range, in terms of the number of repetitions.
    - name: Iterateoncells
      label: Iterate On Cells
      summary: |
        Whether to expose the slice number as an "iteration" value for upstream ops.
    - name: Enable
      label: Enable
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# moduloPolar

Category: filter



Repeats space radially, like a kaleidoscope.