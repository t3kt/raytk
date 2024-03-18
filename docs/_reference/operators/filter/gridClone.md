---
layout: operator
title: gridClone
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/gridClone
redirect_from:
  - /reference/opType/raytk.operators.filter.gridClone/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    supportedVariables:
    - RTK_raytk_operators_filter_gridClone_coord
    - RTK_raytk_operators_filter_gridClone_normcoord
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
    - RTK_raytk_operators_filter_gridClone_coord
    - RTK_raytk_operators_filter_gridClone_normcoord
  name: gridClone
  opType: raytk.operators.filter.gridClone
  parameters:
  - label: Enable
    name: Enable
  - label: Count
    name: Count
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: The number of copies. The performance cost of the input is multiplied
      by this number.
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
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
    name: Mergetype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How to merge the copies.
  - label: Merge Radius
    name: Mergeradius
    summary: The amount of smoothing to apply when merging copies.
  - label: Merge Number
    name: Mergenumber
  - label: Merge Offset
    name: Mergeoffset
  thumb: assets/images/reference/operators/filter/gridClone_thumb.png
  variables:
  - label: RTK_raytk_operators_filter_gridClone_coord
    name: RTK_raytk_operators_filter_gridClone_coord
  - label: RTK_raytk_operators_filter_gridClone_normcoord
    name: RTK_raytk_operators_filter_gridClone_normcoord

---
