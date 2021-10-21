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
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  keywords:
  - clone
  - copy
  - radial
  - repeat
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
    summary: The axis around which to rotate the copies.
  - label: Count
    name: Count
    summary: The number of copies. The performance cost of the input is multiplied
      by this number.
  - label: Angle Range
    name: Anglerange
    summary: The angle spread around the axis, where the copies are distributed.
  - label: Angle Offset
    name: Angleoffset
    summary: Shifts the angle of the first copy around the axis.
  - label: Radius Offset
    name: Radiusoffset
    summary: Offsets the copies towards/away from the axis. At zero, all copies will
      be centered on the axis.
  - label: Merge Type
    menuOptions:
    - description: Show all the shapes, without any special treatment for overlap
        between them.
      label: Union
      name: union
    - description: Smooths overlaps between the copies.
      label: Smooth Union
      name: smoothunion
    name: Mergetype
    summary: How to merge the copies.
  - label: Merge Radius
    name: Mergeradius
    summary: The amount of smoothing to apply when merging copies.
  - label: Iteration Type
    menuOptions:
    - description: Pass along whatever is provided by the next op after this one.
      label: None
      name: none
    - description: Use the copy index (from 0 to `Count`-1) as the x iteration value.
      label: Clone Index
      name: index
    name: Iterationtype
    summary: Whether and how to expose iteration values to upstream operators.
  summary: Repeats an SDF radially around an axis, combining the resulting shapes.

---


Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.