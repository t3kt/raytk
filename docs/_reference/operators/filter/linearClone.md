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
  detail: 'Note that this multiplies the work of the input for each clone, meaning
    that 4 clones means 4x the work of whatever is connected to the input.


    The `modulo1D` can be a cheaper alternative to `linearClone` though it comes with
    limitations.'
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
    - index
    - normindex
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
    summary: Position of the start of the line of clones.
  - label: Translate 2
    name: Translate2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Position of the end of the line of clones.
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
  summary: Repeats an SDF along a line, combining the results.
  thumb: assets/images/reference/operators/filter/linearClone_thumb.png
  variables:
  - label: index
    name: index
  - label: normindex
    name: normindex

---


Repeats an SDF along a line, combining the results.

Note that this multiplies the work of the input for each clone, meaning that 4 clones means 4x the work of whatever is connected to the input.

The `modulo1D` can be a cheaper alternative to `linearClone` though it comes with limitations.