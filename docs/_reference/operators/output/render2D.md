---
layout: operator
title: render2D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/render2D
redirect_from:
  - /reference/opType/raytk.operators.output.render2D/
op:
  category: output
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
  name: render2D
  opType: raytk.operators.output.render2D
  parameters:
  - label: Resolution
    name: Res
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
  - label: Max Distance
    name: Maxdist
  - label: Enable Edge
    name: Enableedge
  - label: Edge Thickness
    name: Edgethickness
  - label: Edge Blending
    name: Edgeblending
  - label: Edge Color
    name: Edgecolor
  - label: Inside Period
    name: Insideperiod
  - label: Inside Color 1
    name: Insidecolor1
  - label: Inside Color 2
    name: Insidecolor2
  - label: Outside Period
    name: Outsideperiod
  - label: Outside Color 1
    name: Outsidecolor1
  - label: Outside Color 2
    name: Outsidecolor2
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig

---

# render2D

Category: output

