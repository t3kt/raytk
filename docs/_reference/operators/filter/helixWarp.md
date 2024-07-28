---
layout: operator
title: helixWarp
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/helixWarp
redirect_from:
  - /reference/opType/raytkAbstractions.operators.filter.helixWarp/
op:
  category: filter
  detail: 'This operator pushes space along two axes by varying amounts along the
    third axis.

    When applied to a cylinder along that main axis, this would produce a helix shape.

    Note that it doesn''t actually do any rotation, just shifts it side to side (and
    front to back, if using the Y axis).'
  moduleName: raytkAbstractions
  name: helixWarp
  opType: raytkAbstractions.operators.filter.helixWarp
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Period
    name: Period
    summary: How spread out the wave should be.
  - label: Phase
    name: Phase
    summary: Shifts the wave along the axis.
  - label: Amplitude
    name: Amplitude
    summary: How far to offset space.
  status: beta
  summary: Warps space in a helix pattern around an axis.

---


Warps space in a helix pattern around an axis.

This operator pushes space along two axes by varying amounts along the third axis.
When applied to a cylinder along that main axis, this would produce a helix shape.
Note that it doesn't actually do any rotation, just shifts it side to side (and front to back, if using the Y axis).