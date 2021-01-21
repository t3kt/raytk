---
layout: operator
title: functionGraphRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/functionGraphRender
redirect_from:
  - /reference/opType/raytk.operators.output.functionGraphRender/
op:
  name: functionGraphRender
  summary: Visualizes the graph of a function operator.
  detail: |
    This is intended primarily for use in the Inspector, though there may be other uses.
    It can take in multiple function inputs, which it will visualize with different colors of lines in the same graph.
    
    It provides several outputs:
    * Color - The rendered graph line.
    * GUI - The graph line along with axes and range markers.
  opType: raytk.operators.output.functionGraphRender
  category: output
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: false
      coordTypes: [float]
      contextTypes: [Context]
      returnTypes: [float]
    - name: definition_in_2
      label: definition_in_2
      required: false
      coordTypes: [float]
      contextTypes: [Context]
      returnTypes: [float]
    - name: definition_in_3
      label: definition_in_3
      required: false
      coordTypes: [float]
      contextTypes: [Context]
      returnTypes: [float]
    - name: definition_in_4
      label: definition_in_4
      required: false
      coordTypes: [float]
      contextTypes: [Context]
      returnTypes: [float]
  parameters:
    - name: Resolution
      label: Resolution
      summary: |
        The rendering resolution.
    - name: Domainlow
      label: Domain Low
      summary: |
        The low bound of the domain (x axis).
    - name: Domainhigh
      label: Domain High
      summary: |
        The high bound of the domain (x axis).
    - name: Rangelow
      label: Range Low
      summary: |
        The low bound of the range (y axis).
    - name: Rangehigh
      label: Range High
      summary: |
        The high bound of the range (y axis).
    - name: Linethickness
      label: Line Thickness
      summary: |
        Thickness of the graph line.
    - name: Lineblending
      label: Line Blending
      summary: |
        Amount of blending applied to the edges of the graph line.
    - name: Showaxislabels
      label: Show Axis Labels
      summary: |
        Whether to show axis labels in the GUI output.
    - name: Timereferenceoperator
      label: Timereferenceoperator
    - name: Shaderbuilderconfig
      label: Shader Builder Config
    - name: Shaderinfo
      label: Shaderinfo
    - name: Shadercode
      label: Shadercode
    - name: Shadertop
      label: Shadertop
    - name: Outputtable
      label: Outputtable
    - name: Shaderbuilder
      label: Shaderbuilder
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
    - name: Timerefop
      label: Time Reference Operator
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# functionGraphRender

Category: output



Visualizes the graph of a function operator.

This is intended primarily for use in the Inspector, though there may be other uses.
It can take in multiple function inputs, which it will visualize with different colors of lines in the same graph.

It provides several outputs:
* Color - The rendered graph line.
* GUI - The graph line along with axes and range markers.