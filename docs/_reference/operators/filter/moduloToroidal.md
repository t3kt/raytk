---
layout: operator
title: moduloToroidal
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloToroidal
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloToroidal/
op:
  category: filter
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
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - repetitionsField
    - radiusField
    - thicknessField
    - shiftField
    supportedVariables:
    - cell
    - normcell
    - angle
    - normangle
    - innerangle
    - norminnerangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Repetitions Field
    name: repetitionsField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - repetitionsField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - repetitionsField
    - radiusField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
    - repetitionsField
    - radiusField
    - thicknessField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
  keywords:
  - torus
  name: moduloToroidal
  opType: raytk.operators.filter.moduloToroidal
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
    summary: Axis that the torus is around.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Primary radius of the torus around the main axis.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the torus.
  - label: Repetitions
    name: Repetitions
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of rows and columns across the torus.
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the repetitions across the rows and columns of the torus.
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Rows
      name: rows
    - label: Columns
      name: cols
    - label: Grid
      name: grid
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Flips alternating repetitions so they mirror each other.
  status: beta
  summary: Repeats space as rows and columns of a torus-shaped grid.
  thumb: assets/images/reference/operators/filter/moduloToroidal_thumb.png
  variables:
  - label: Cell (Row, Col)
    name: cell
    summary: Index of the row and column as integers (0..N).
  - label: Normalized Cell (Row, Col) (0..1)
    name: normcell
    summary: Index of the row and column scaled to a 0..1 range based on the number
      of Repetitions.
  - label: Angle (0-360)
    name: angle
    summary: Angle around the main axis as degrees (0..360).
  - label: Normalized Angle (0-1)
    name: normangle
    summary: Angle around the main axis, scaled to a 0..1 range.
  - label: Inner Angle (0-360)
    name: innerangle
    summary: Angle around the inner body of the torus as degrees (0..360).
  - label: Normalized Inner Angle (0..1)
    name: norminnerangle
    summary: Angle around the inner body of the torus, scaled to a 0..1 range.

---


Repeats space as rows and columns of a torus-shaped grid.