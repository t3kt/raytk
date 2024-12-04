---
layout: operator
title: arrange
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/arrange
redirect_from:
  - /reference/opType/raytk.operators.combine.arrange/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 1
    name: definition_in_1
    returnTypes:
    - Sdf
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 2
    name: definition_in_2
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp1
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 3
    name: definition_in_3
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-2]
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 4
    name: definition_in_4
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-3]
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 5
    name: definition_in_5
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-4]
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 6
    name: definition_in_6
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-5]
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 7
    name: definition_in_7
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-6]
    supportedVariables:
    - index
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 8
    name: definition_in_8
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp[1-7]
    supportedVariables:
    - index
  name: arrange
  opType: raytk.operators.combine.arrange
  parameters:
  - label: Combine
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
    - label: Smooth Avoid
      name: smoothAvoid
    name: Combine
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How the SDFs are combined.
  - label: Swap Inputs
    name: Swapinputs
  - label: Radius
    name: Radius
  - label: Number
    name: Number
  - label: Offset
    name: Offset
  - label: Translate 1
    name: Translate1
    summary: Moves the input SDF 1.
  - label: Translate 2
    name: Translate2
    summary: Moves the input SDF 2.
  - label: Translate 3
    name: Translate3
    summary: Moves the input SDF 3.
  - label: Translate 4
    name: Translate4
    summary: Moves the input SDF 4.
  - label: Translate 5
    name: Translate5
    summary: Moves the input SDF 5.
  - label: Translate 6
    name: Translate6
    summary: Moves the input SDF 6.
  - label: Translate 7
    name: Translate7
    summary: Moves the input SDF 7.
  - label: Translate 8
    name: Translate8
    summary: Moves the input SDF 8.
  - label: Optimize
    name: Optimize
    summary: Improves performance by assuming that settings don't change. This will
      make things much slower when settings do change though.
  - label: Enable 1
    name: Enable1
  - label: Enable 2
    name: Enable2
  - label: Enable 3
    name: Enable3
  - label: Enable 4
    name: Enable4
  - label: Enable 5
    name: Enable5
  - label: Enable 6
    name: Enable6
  - label: Enable 7
    name: Enable7
  - label: Enable 8
    name: Enable8
  - label: Enable Translate
    name: Enabletranslate
    summary: Whether to use positioning features. Keep this off if you don't need
      it, to improve performance.
  - label: Gutter
    name: Gutter
  summary: Combines multiple SDFs, with a different position for each.
  thumb: assets/images/reference/operators/combine/arrange_thumb.png
  variables:
  - label: Index
    name: index

---


Combines multiple SDFs, with a different position for each.