---
layout: operator
title: gridPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/gridPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.gridPattern/
op:
  category: pattern
  detail: This operator produces different types of values from the grid depending
    on the selected Format.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    - vec4
    summary: Field that controls the sizing of the grid cells.
    supportedVariableInputs:
    - coordField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    summary: Field that controls the thickness of the edges between cells.
    supportedVariableInputs:
    - coordField
    - spacingField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    summary: Field that controls the amount of blending between cells and edges.
    supportedVariableInputs:
    - coordField
    - spacingField
    - thicknessField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Fill Color Field
    name: fillColorField
    returnTypes:
    - float
    - vec4
    summary: Field that provides colors for the cells.
    supportedVariableInputs:
    - coordField
    - spacingField
    - thicknessField
    - blendingField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Edge Color Field
    name: edgeColorField
    returnTypes:
    - float
    - vec4
    summary: Field that provides colors for the edges.
    supportedVariableInputs:
    - coordField
    - spacingField
    - thicknessField
    - blendingField
    - fillColorField
  name: gridPattern
  opType: raytk.operators.pattern.gridPattern
  parameters:
  - label: Format
    menuOptions:
    - description: Produces float values, with 0 for the grid cells and 1 for the
        edges between cells.
      label: Grid Edges
      name: edge
    - description: Produces float values with the raw distance from the edge, like
        an SDF.
      label: Grid Distance
      name: dist
    - description: Produces float values with the distance scaled so that edges are
        0 and cell centers are 1.
      label: Grid Normalized Distance
      name: normdist
    - description: Produces vectors with the chosen color for the cells and the edges.
      label: Grid Color
      name: color
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
    summary: What type of values to produce from the pattern.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - name: Size
    summary: Scales the pattern.
  - label: Thickness
    name: Thickness
    summary: Thickness of the edges between the cells.
  - label: Blending
    name: Blending
    summary: Amount of blending between cells and edges.
  - label: Fill Color
    name: Fillcolor
    summary: Color to use for the cells (when applicable).
  - label: Edge Color
    name: Edgecolor
    summary: Color to use for the edges (when applicable).
  - label: Spacing
    name: Spacing
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Rectangular grid pattern.
  thumb: assets/images/reference/operators/pattern/gridPattern_thumb.png

---


Rectangular grid pattern.

This operator produces different types of values from the grid depending on the selected Format.