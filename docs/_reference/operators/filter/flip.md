---
layout: operator
title: flip
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/flip
redirect_from:
  - /reference/opType/raytk.operators.filter.flip/
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
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - offsetField
    - shiftField
    supportedVariables:
    - sign
    - index
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - shiftField
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
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
  name: flip
  opType: raytk.operators.filter.flip
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
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the reflection plane along the axis.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the input towards / away from the reflection plane.
  - label: Merge Type
    menuOptions:
    - label: None
      name: none
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
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to just flip the input or flip it and merge that with the original.
  - label: Merge Radius
    name: Mergeradius
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - description: The original is assigned 0, flipped 1.
      label: Index (0/1)
      name: index
    - description: Original is assigned 1, flipped -1.
      label: Signed (-1/1)
      name: sign
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: What kind of iteration values should be provided for upstream ops.
  - label: Merge Number
    name: Mergenumber
  - label: Merge Offset
    name: Mergeoffset
  summary: Flips the input across an axis, either on its own or merged with the original.
  thumb: assets/images/reference/operators/filter/flip_thumb.png
  variables:
  - label: sign
    name: sign
  - label: index
    name: index

---


Flips the input across an axis, either on its own or merged with the original.