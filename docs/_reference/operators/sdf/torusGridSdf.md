---
layout: operator
title: torusGridSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/torusGridSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.torusGridSdf/
op:
  category: sdf
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
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariables:
    - angle
    - normangle
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    supportedVariables:
    - angle
    - normangle
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
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - radiusField
    - thicknessField
    supportedVariables:
    - angle
    - normangle
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
    - vec3
    label: Bar Thickness Field
    name: barRhicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - thicknessField
    - shiftField
    supportedVariables:
    - angle
    - normangle
    - col
    - normcol
    - row
    - normrow
  name: torusGridSdf
  opType: raytk.operators.sdf.torusGridSdf
  parameters:
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
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Parts
    menuOptions:
    - label: Both
      name: both
    - label: Rows Only
      name: rows
    - label: Columns Only
      name: cols
    name: Parts
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Rows
    name: Rows
  - label: Columns
    name: Cols
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bar Thickness
    name: Barthickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: the thickness of the bars.
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
    name: Combine
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Blend Radius
    name: Blendradius
  - label: Blend Number
    name: Blendnumber
  - label: Blend Offset
    name: Blendoffset
  status: beta
  thumb: assets/images/reference/operators/sdf/torusGridSdf_thumb.png
  variables:
  - label: angle
    name: angle
  - label: normangle
    name: normangle
  - label: col
    name: col
  - label: normcol
    name: normcol
  - label: row
    name: row
  - label: normrow
    name: normrow

---
