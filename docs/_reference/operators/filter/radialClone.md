---
layout: operator
title: radialClone
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/radialClone
redirect_from:
  - /reference/opType/raytk.operators.filter.radialClone/
op:
  category: filter
  detail: Note that this runs its input multiple times, which can lead to performance
    issues.
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
    - Sdf
  name: radialClone
  opType: raytk.operators.filter.radialClone
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
  - label: Count
    name: Count
  - label: Angle Range
    name: Anglerange
  - label: Angle Offset
    name: Angleoffset
  - label: Radius Offset
    name: Radiusoffset
  - label: Merge Type
    menuOptions:
    - label: Union
      name: union
    - label: Smooth Union
      name: smoothunion
    name: Mergetype
  - label: Merge Radius
    name: Mergeradius
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Clone Index
      name: index
    - label: Scaled Clone Index
      name: scaled
    name: Iterationtype
  summary: Repeats an SDF radially around an axis, combining the resulting shapes.

---

# radialClone

Category: filter



Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.