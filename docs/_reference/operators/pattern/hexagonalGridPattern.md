---
layout: operator
title: hexagonalGridPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalGridPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalGridPattern/
op:
  category: pattern
  detail: This operator produces different types of values from the grid depending
    on the selected Pattern.
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
    - ParticleContext
    - VertexContext
    - PixelContext
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    summary: Field that controls the amount of blending between cells and edges.
    supportedVariableInputs:
    - coordField
    - thicknessField
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
    label: Poly Color 1 Field
    name: polyColor1Field
    returnTypes:
    - float
    - vec4
    summary: Field to provide cell color 1.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
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
    label: Poly Color 2 Field
    name: polyColor2Field
    returnTypes:
    - float
    - vec4
    summary: Field to provide cell color 2.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
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
    label: Poly Color 3 Field
    name: polyColor3Field
    returnTypes:
    - float
    - vec4
    summary: Field to provide cell color 3.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
  name: hexagonalGridPattern
  opType: raytk.operators.pattern.hexagonalGridPattern
  parameters:
  - label: Pattern
    menuOptions:
    - description: Produces float values, with 1 for the grid cells, and 0 for the
        edges between cells.
      label: Hex Grid
      name: hexgrid
    - description: Produces float values with the distance scaled so that edges are
        0 and cell centers are 1.
      label: Hex Distance
      name: hexdist
    - description: Produces float values which mark each cell with either 0, 0.5,
        or 1, such that no two adjacent cells are the same.
      label: Hex 3 Pattern
      name: hex3
    - description: Produces vectors with colors where 3 chosen colors are applied
        to cells, such that no two adjacent cells are the same.
      label: Hex 3 Color Pattern
      name: hex3color
    name: Pattern
    readOnlyHandling: baked
    regularHandling: baked
    summary: What type of values to produce from the grid.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the edges between the cells.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending between cells and edges.
  - label: Poly Color 1
    name: Polycolor1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color 1 to use for cells (when applicable).
  - label: Poly Color 2
    name: Polycolor2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color 2 to use for cells (when applicable).
  - label: Poly Color 3
    name: Polycolor3
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color 3 to use for cells (when applicable).
  summary: Hexagonal grid pattern.
  thumb: assets/images/reference/operators/pattern/hexagonalGridPattern_thumb.png

---


Hexagonal grid pattern.

This operator produces different types of values from the grid depending on the selected Pattern.