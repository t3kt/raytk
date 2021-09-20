---
layout: operator
title: combine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combine
redirect_from:
  - /reference/opType/raytk.operators.combine.combine/
op:
  category: combine
  detail: 'Depending on which `Combine` option is selected, different parameters will
    be enabled.

    This operator only supports two input SDFs (along with a value field to control
    blending).

    To combine more than two SDFs, use one of the specialized operators like [`simpleUnion`](/raytk/reference/operators/combine/).'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: input1
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: input2
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: radius_field_definition_in
    name: radiusField
    returnTypes:
    - float
    - Sdf
  keywords:
  - chamfer
  - columns
  - combine
  - diff
  - intersect
  - round
  - smooth
  - stairs
  - union
  name: combine
  opType: raytk.operators.combine.combine
  parameters:
  - label: Enable
    name: Enable
  - label: Combine
    menuOptions:
    - description: The combined areas of each of the inputs.
      label: Simple Union
      name: simpleUnion
    - description: The overlapping areas of each of the inputs.
      label: Simple Intersect
      name: simpleIntersect
    - description: The first input with the second input removed from it.
      label: Simple Difference
      name: simpleDiff
    - description: Like `simpleUnion` but with the intersecting edges rounded out.
      label: Smooth Union
      name: smoothUnion
    - description: Like `simpleIntersect` but with the intersecting edges rounded
        out.
      label: Smooth Intersect
      name: smoothIntersect
    - description: Like `simpleDiff` but with the intersecting edges rounded out.
      label: Smooth Difference
      name: smoothDiff
    - description: Uses a quarter circle blending area along the edges.
      label: Round Union
      name: roundUnion
    - label: Round Intersect
      name: roundIntersect
    - label: Round Difference
      name: roundDiff
    - description: Uses a 45 degree flat slope to blend along the edges.
      label: Chamfer Union
      name: chamferUnion
    - label: Chamfer Intersect
      name: chamferIntersect
    - label: Chamfer Difference
      name: chamferDiff
    - description: Uses vertical and horizontal stairs to blend along the edges.
      label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - description: Uses multiple circular tubes to blend along the edges.
      label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine
    summary: The type of combination operation to perform.
  - label: Swap Inputs
    name: Swapinputs
    summary: Swaps the order of the inputs. This is only relevant for "diff" modes.
  - label: Radius
    name: Radius
    summary: The size of the blending region.
  - label: Number
    name: Number
    summary: For stair and column modes, this controls how many steps are used in
      the blending regions.
  - label: Offset
    name: Offset
  summary: Combines SDFs in various ways.

---


Combines SDFs in various ways.

Depending on which `Combine` option is selected, different parameters will be enabled.
This operator only supports two input SDFs (along with a value field to control blending).
To combine more than two SDFs, use one of the specialized operators like [`simpleUnion`](/raytk/reference/operators/combine/).