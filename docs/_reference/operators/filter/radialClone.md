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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    supportedVariables:
    - index
    - normindex
    - rotaccum
    - normrotaccum
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Radial Offset Field
    name: radialOffsetField
    required: true
    returnTypes:
    - float
    supportedVariables:
    - index
    - normindex
    - rotaccum
    - normrotaccum
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Angle Offset Field
    name: angleOffsetField
    required: true
    returnTypes:
    - float
    supportedVariables:
    - index
    - normindex
    - rotaccum
    - normrotaccum
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Blend Radius Field
    name: blendRadiusField
    required: true
    returnTypes:
    - float
    supportedVariables:
    - index
    - normindex
    - rotaccum
    - normrotaccum
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: The axis around which to rotate the copies.
  - label: Count
    name: Count
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of copies. The performance cost of the input is multiplied
      by this number.
  - label: Angle Range
    name: Anglerange
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The angle spread around the axis, where the copies are distributed.
  - label: Angle Offset
    name: Angleoffset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the angle of the first copy around the axis.
  - label: Radius Offset
    name: Radiusoffset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets the copies towards/away from the axis. At zero, all copies will
      be centered on the axis.
  - label: Merge Type
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
      name: simpleDiff
    - label: Smooth Union
      name: smoothUnion
    - label: Smooth Intersect
      name: smoothIntersect
    - label: Smooth Difference
      name: smoothDiff
    - label: Round Union
      name: roundUnion
    - label: Round Intersect
      name: roundIntersect
    - label: Round Difference
      name: roundDiff
    - label: Chamfer Union
      name: chamferUnion
    - label: Chamfer Intersect
      name: chamferIntersect
    - label: Chamfer Difference
      name: chamferDiff
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    - label: Simple XOR
      name: simpleXOR
    name: Mergetype
    readOnlyHandling: semibaked
    regularHandling: semibaked
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether and how to expose iteration values to upstream operators.
  - label: Rotate Mode
    menuOptions:
    - label: Position and Rotation
      name: both
    - label: Position Only
      name: pos
    name: Rotatemode
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether the copies should be rotated or just positioned in a ring in
      their original orientation.
  - label: Merge Number
    name: Mergenumber
  - label: Merge Offset
    name: Mergeoffset
  summary: Repeats an SDF radially around an axis, combining the resulting shapes.
  thumb: assets/images/reference/operators/filter/radialClone_thumb.png
  variables:
  - label: Index
    name: index
    summary: Index of the current clone (0..N)
  - label: Normalized Index (0..1)
    name: normindex
    summary: Index of the current clone, scaled to a 0..1 range.
  - label: Rotation (Accumulated) (0..360)
    name: rotaccum
    summary: Amount of rotation applied for the current clone (0..360).
  - label: Normalized Rotation (Accumulated) (0..1)
    name: normrotaccum
    summary: Amount of rotation applied for the current clone, scaled to 0..1 range.

---


Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.