---
layout: operator
title: layoutGrid
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/layoutGrid
redirect_from:
  - /reference/opType/raytk.operators.combine.layoutGrid/
op:
  name: layoutGrid
  summary: Slices space into a grid, and places each input in a separate cell.
  detail: |
    This is useful to see several different variations of a shape.
    The input shapes are shifted to the center of their cell.
  opType: raytk.operators.combine.layoutGrid
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,Sdf]
    - name: definition_in_2
      label: definition_in_2
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,Sdf]
    - name: definition_in_3
      label: definition_in_3
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,Sdf]
    - name: definition_in_4
      label: definition_in_4
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,Sdf]
  parameters:
    - name: Enable
      label: Enable
    - name: Layout
      label: Layout
      summary: |
        How to arrange the cells.
      menuOptions:
        - name: row
          label: Row
          description: |
            Slice space into cells horizontally. The first cell extends off infinitely to the left and the last cell extends infinitely off to the right.
        - name: column
          label: Column
          description: |
            Slice space into cells vertically.
        - name: gridrow
          label: Grid Rows
          description: |
            Slice space into 4 cells arranged in a grid.
    - name: Axis
      label: Plane
      summary: |
        The plane along which to arrange the cells.
      menuOptions:
        - name: x
          label: YZ
        - name: y
          label: ZX
        - name: z
          label: XY
    - name: Size
      label: Size
      summary: |
        The size of the cells
    - name: Prescale
      label: Pre Scale
      summary: |
        Scales the inputs within their cells.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# layoutGrid

Category: combine



Slices space into a grid, and places each input in a separate cell.

This is useful to see several different variations of a shape.
The input shapes are shifted to the center of their cell.