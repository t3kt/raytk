---
layout: operator
title: render2D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/render2D
redirect_from:
  - /reference/opType/raytk.operators.output.render2D/
op:
  name: render2D
  opType: raytk.operators.output.render2D
  category: output
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2]
      contextTypes: [Context]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Res
      label: Resolution
    - name: Format
      label: Pixel Format
      menuOptions:
        - name: useinput
          label: Use Input
        - name: rgba8fixed
          label: 8-bit fixed (RGBA)
        - name: srgba8fixed
          label: sRGB 8-bit fixed (RGBA)
        - name: rgba16float
          label: 16-bit float (RGBA)
        - name: rgba32float
          label: 32-bit float (RGBA)
        - name: _separator_
          label: _separator_
        - name: rgb10a2fixed
          label: 10-bit RGB, 2-bit Alpha, fixed (RGBA)
        - name: rgba16fixed
          label: 16-bit fixed (RGBA)
        - name: rgba11float
          label: 11-bit float (RGB), Positive Values Only
        - name: rgb16float
          label: 16-bit float (RGB)
        - name: rgb32float
          label: 32-bit float (RGB)
        - name: mono8fixed
          label: 8-bit fixed (Mono)
        - name: mono16fixed
          label: 16-bit fixed (Mono)
        - name: mono16float
          label: 16-bit float (Mono)
        - name: mono32float
          label: 32-bit float (Mono)
        - name: rg8fixed
          label: 8-bit fixed (RG)
        - name: rg16fixed
          label: 16-bit fixed (RG)
        - name: rg16float
          label: 16-bit float (RG)
        - name: rg32float
          label: 32-bit float (RG)
        - name: a8fixed
          label: 8-bit fixed (A)
        - name: a16fixed
          label: 16-bit fixed (A)
        - name: a16float
          label: 16-bit float (A)
        - name: a32float
          label: 32-bit float (A)
        - name: monoalpha8fixed
          label: 8-bit fixed (Mono+Alpha)
        - name: monoalpha16fixed
          label: 16-bit fixed (Mono+Alpha)
        - name: monoalpha16float
          label: 16-bit float (Mono+Alpha)
        - name: monoalpha32float
          label: 32-bit float (Mono+Alpha)
    - name: Enableedge
      label: Enable Edge
    - name: Edgethickness
      label: Edge Thickness
    - name: Edgeblending
      label: Edge Blending
    - name: Edgecolor
      label: Edge Color
    - name: Insideperiod
      label: Inside Period
    - name: Insidecolor1
      label: Inside Color 1
    - name: Insidecolor2
      label: Inside Color 2
    - name: Outsideperiod
      label: Outside Period
    - name: Outsidecolor1
      label: Outside Color 1
    - name: Outsidecolor2
      label: Outside Color 2
    - name: Timerefop
      label: Time Reference Operator
    - name: Shaderbuilderconfig
      label: Shader Builder Config
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# render2D

Category: output

