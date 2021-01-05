---
layout: operator
title: gridSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gridSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.gridSdf/
op:
  name: gridSdf
  summary: An infinite grid shape, along two axes.
  opType: raytk.operators.sdf.gridSdf
  category: sdf
  parameters:
    - name: Coordtype
      label: Coord Type
      summary: |
        allows the shape to be used in a 2D context.
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Crosssectionshape
      label: Cross Section Shape
      summary: |
        choose the shape of the bars of the grid. Not available in 2D mode.
      menuOptions:
        - name: circle
          label: Circle
        - name: diamond
          label: Diamond
    - name: Axis
      label: Axis
      summary: |
        choose which axis the grid should face.
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Spacing
      label: Spacing
      summary: |
        spacing between the bars of the grid. If this value is very small and the `Thickness` is high enough, the bars can merge into a solid surface. But if it is set to zero the grid will disappear due to a calculation error.
    - name: Axisoffset
      label: Axis Offset
      summary: |
        shifts the grid forwards or backwards along the `Axis` that it is facing. Not available in 2D mode.
    - name: Offset
      label: Offset
      summary: |
        shifts the grid along its plane.
    - name: Thickness
      label: Thickness
      summary: |
        the thickness of the bars.
    - name: Contexttype
      label: Context Type
      summary: |
        advanced parameter that should usually just be set to `Context`
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# gridSdf

Category: sdf



An infinite grid shape, along two axes.