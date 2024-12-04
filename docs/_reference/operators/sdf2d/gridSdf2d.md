---
layout: operator
title: gridSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/gridSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.gridSdf2d/
op:
  category: sdf2d
  detail: Based on [GridX6 by Del](https://www.shadertoy.com/view/7dX3Dj).
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
    - vec2
    label: Size Field
    name: sizeField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
  name: gridSdf2d
  opType: raytk.operators.sdf2d.gridSdf2d
  parameters:
  - label: Shape
    menuOptions:
    - label: Square
      name: square
    - label: Hexagon
      name: hexagon
    - label: Triangle
      name: triangle
    - label: Diamond
      name: diamond
    - label: Brick
      name: brick
    - label: Octagon
      name: octagon
    name: Shape
  - label: Format
    menuOptions:
    - label: Cell Interiors
      name: interior
    - label: Cell Edges
      name: edge
    - label: Cell Centers
      name: center
    name: Format
    summary: Which part of the grid to treat as the interior.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scaling for the grid.
  - label: Spacing
    name: Spacing
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Spacing between grid cells.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of circles at grid centers.
  status: beta
  summary: Various types of grid SDFs.
  thumb: assets/images/reference/operators/sdf2d/gridSdf2d_thumb.png

---


Various types of grid SDFs.

Based on [GridX6 by Del](https://www.shadertoy.com/view/7dX3Dj).