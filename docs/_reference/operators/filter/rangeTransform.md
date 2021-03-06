---
layout: operator
title: rangeTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rangeTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.rangeTransform/
op:
  category: filter
  detail: 'This operator defines two different sets of transform settings. It then
    uses some index value to decide

    where in that range it will use. A simple use case for this would be iteration
    with 3 items, where the

    first item moves to one position and the last item moves to another position,
    and the one in the middle

    moves to half way between those two.


    The index is based either on the first (x) part of the iteration value provided
    by a downstream op, or

    if the second input is connected, that float value field is used to determine
    the index.

    The index is then scaled from the specified range down to 0..1. The `Extend` parameter
    controls how

    values outside that range are handled.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
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
    coordTypes:
    - vec3
    label: Index Field
    name: index_field_definition_in
    returnTypes:
    - float
    summary: Optional float value field to use instead of the iteration value. It
      is passed the current coordinates.
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Easing
    name: easing_definition_in
    returnTypes:
    - float
  name: rangeTransform
  opType: raytk.operators.filter.rangeTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Index Range
    name: Indexrange
    summary: The range of index values that are expected. The first value will use
      `Translate1` and the second will use `Translate2`.
  - label: Extend Mode
    menuOptions:
    - description: Linearly scale values, which is like making a graph with a line
        between the two settings, and then just extending that line in the same direction
        as it goes past 1 (and before 0).
      label: Linear
      name: linear
    - description: Clamp the index values to the range.
      label: Clamp
      name: clamp
    - description: Loop the values over the range.
      label: Loop
      name: loop
    name: Extendmode
    summary: How to handle index values outside of `Indexrange`.
  - label: Enable Translate
    name: Enabletranslate
    summary: Wheteher to use translation.
  - label: Translate 1
    name: Translate1
    summary: Translate setting for the beginning of the range.
  - label: Translate 2
    name: Translate2
    summary: Translate setting for the end of the range.
  - label: Enable Rotate
    name: Enablerotate
    summary: Whether to use rotation.
  - label: Rotate 1
    name: Rotate1
    summary: Rotate setting for the beginning of the range.
  - label: Rotate 2
    name: Rotate2
    summary: Rotate setting for the end of the range.
  - label: Use Pivot
    name: Usepivot
  - label: Pivot 1
    name: Pivot1
  - label: Pivot 2
    name: Pivot2
  status: beta
  summary: Applies a transform based on a range of settings, mapped with either the
    iteration value or a field input.

---


Applies a transform based on a range of settings, mapped with either the iteration value or a field input.

This operator defines two different sets of transform settings. It then uses some index value to decide
where in that range it will use. A simple use case for this would be iteration with 3 items, where the
first item moves to one position and the last item moves to another position, and the one in the middle
moves to half way between those two.

The index is based either on the first (x) part of the iteration value provided by a downstream op, or
if the second input is connected, that float value field is used to determine the index.
The index is then scaled from the specified range down to 0..1. The `Extend` parameter controls how
values outside that range are handled.