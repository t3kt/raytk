---
layout: operator
title: linearClone
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/linearClone
redirect_from:
  - /reference/opType/raytk.operators.filter.linearClone/
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    supportedVariables:
    - RTK_raytk_operators_filter_linearClone_index
    - RTK_raytk_operators_filter_linearClone_normindex
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
    - RTK_raytk_operators_filter_linearClone_index
    - RTK_raytk_operators_filter_linearClone_normindex
  name: linearClone
  opType: raytk.operators.filter.linearClone
  parameters:
  - label: Enable
    name: Enable
  - label: Count
    name: Count
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of copies. The performance cost of the input is multiplied
      by this number.
  - label: Translate 1
    name: Translate1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 2
    name: Translate2
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
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Clone Index
      name: index
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether and how to expose iteration values to upstream operators.
  thumb: assets/images/reference/operators/filter/linearClone_thumb.png
  variables:
  - label: RTK_raytk_operators_filter_linearClone_index
    name: RTK_raytk_operators_filter_linearClone_index
  - label: RTK_raytk_operators_filter_linearClone_normindex
    name: RTK_raytk_operators_filter_linearClone_normindex

---
