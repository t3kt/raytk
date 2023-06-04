---
layout: operator
title: fieldRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/fieldRender
redirect_from:
  - /reference/opType/raytk.operators.output.fieldRender/
op:
  category: output
  name: fieldRender
  opType: raytk.operators.output.fieldRender
  parameters:
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Sample Coords
    name: Samplecoords
  - label: Grid Center
    name: Gridcenter
  - label: Grid Size
    name: Gridsize
  - label: Grid Resolution X
    name: Gridresolutionx
  - label: Grid Resolution Y
    name: Gridresolutiony
  - label: Grid Resolution Z
    name: Gridresolutionz
  - label: Unit Shape
    name: Unitshape
  - label: Use Scale
    name: Usescale
  - label: Scale Range
    name: Scalerange
  - label: Use Color
    name: Usecolor
  - label: Wireframe
    name: Wireframe
  - label: Shaded
    name: Shaded
  - label: Material
    name: Material
  - label: Pixel Format
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 8-bit fixed (RGBA)
      name: rgba8fixed
    - label: sRGB 8-bit fixed (RGBA)
      name: srgba8fixed
    - label: 16-bit float (RGBA)
      name: rgba16float
    - label: 32-bit float (RGBA)
      name: rgba32float
    - label: _separator_
      name: _separator_
    - label: 10-bit RGB, 2-bit Alpha, fixed (RGBA)
      name: rgb10a2fixed
    - label: 16-bit fixed (RGBA)
      name: rgba16fixed
    - label: 11-bit float (RGB), Positive Values Only
      name: rgba11float
    - label: 16-bit float (RGB)
      name: rgb16float
    - label: 32-bit float (RGB)
      name: rgb32float
    - label: 8-bit fixed (Mono)
      name: mono8fixed
    - label: 16-bit fixed (Mono)
      name: mono16fixed
    - label: 16-bit float (Mono)
      name: mono16float
    - label: 32-bit float (Mono)
      name: mono32float
    - label: 8-bit fixed (RG)
      name: rg8fixed
    - label: 16-bit fixed (RG)
      name: rg16fixed
    - label: 16-bit float (RG)
      name: rg16float
    - label: 32-bit float (RG)
      name: rg32float
    - label: 8-bit fixed (A)
      name: a8fixed
    - label: 16-bit fixed (A)
      name: a16fixed
    - label: 16-bit float (A)
      name: a16float
    - label: 32-bit float (A)
      name: a32float
    - label: 8-bit fixed (Mono+Alpha)
      name: monoalpha8fixed
    - label: 16-bit fixed (Mono+Alpha)
      name: monoalpha16fixed
    - label: 16-bit float (Mono+Alpha)
      name: monoalpha16float
    - label: 32-bit float (Mono+Alpha)
      name: monoalpha32float
    name: Format
  - label: Camera
    name: Camera
  - label: Resolution
    name: Resolution
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Customize Shader Config
    name: Customizeshaderconfig
  status: beta
  thumb: assets/images/reference/operators/output/fieldRender_thumb.png

---
