---
layout: operator
title: gridSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gridSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.gridSdf/
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
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    - vec4
  keywords:
  - bars
  - grid
  name: gridSdf
  opType: raytk.operators.sdf.gridSdf
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
    summary: allows the shape to be used in a 2D context.
  - label: Cross Section Shape
    menuOptions:
    - label: Circle
      name: circle
    - label: Diamond
      name: diamond
    name: Crosssectionshape
    summary: choose the shape of the bars of the grid. Not available in 2D mode.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: choose which axis the grid should face.
  - label: Spacing
    name: Spacing
    summary: spacing between the bars of the grid. If this value is very small and
      the `Thickness` is high enough, the bars can merge into a solid surface. But
      if it is set to zero the grid will disappear due to a calculation error.
  - label: Axis Offset
    name: Axisoffset
    summary: shifts the grid forwards or backwards along the `Axis` that it is facing.
      Not available in 2D mode.
  - label: Offset
    name: Offset
    summary: shifts the grid along its plane.
  - label: Thickness
    name: Thickness
    summary: the thickness of the bars.
  - menuOptions:
    - name: none
    - name: Context
    - name: MaterialContext
    - name: CameraContext
    - name: LightContext
    name: Contexttype
    summary: advanced parameter that should usually just be set to `Context`
  - label: Pattern
    menuOptions:
    - label: Grid (2D)
      name: grid
    - label: Axis 1 Bars
      name: hbars
    - label: Axis 2 Bars
      name: vbars
    name: Pattern
  summary: An infinite grid shape, along two axes.
  thumb: assets/images/reference/operators/sdf/gridSdf_thumb.png

---


An infinite grid shape, along two axes.