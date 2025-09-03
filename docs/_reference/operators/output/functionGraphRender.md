---
layout: operator
title: functionGraphRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/functionGraphRender
redirect_from:
  - /reference/opType/raytk.operators.output.functionGraphRender/
op:
  category: output
  detail: 'This is intended primarily for use in the Inspector, though there may be
    other uses.

    It can take in multiple function inputs, which it will visualize with different
    colors of lines in the same graph.


    It provides several outputs:

    * Color - The rendered graph line.

    * GUI - The graph line along with axes and range markers.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    label: Function 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    coordTypes:
    - float
    label: Function 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    coordTypes:
    - float
    label: Function 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    coordTypes:
    - float
    label: Function 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
  name: functionGraphRender
  opType: raytk.operators.output.functionGraphRender
  parameters:
  - name: Resolution
    summary: The rendering resolution.
  - label: Domain Low
    name: Domainlow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low bound of the domain (x axis).
  - label: Domain High
    name: Domainhigh
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The high bound of the domain (x axis).
  - label: Range Low
    name: Rangelow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The low bound of the range (y axis).
  - label: Range High
    name: Rangehigh
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The high bound of the range (y axis).
  - label: Line Thickness
    name: Linethickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the graph line.
  - label: Line Blending
    name: Lineblending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending applied to the edges of the graph line.
  - label: Show Axis Labels
    name: Showaxislabels
    summary: Whether to show axis labels in the GUI output.
  - name: Timereferenceoperator
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - name: Shaderinfo
  - name: Shadercode
  - name: Shadertop
  - name: Outputtable
  - name: Shaderbuilder
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
  - label: Show Axes
    name: Showaxes
  - label: Time Reference Operator
    name: Timerefop
  - label: Customize Shader Config
    name: Customizeshaderconfig
  - label: Compile Behavior
    menuOptions:
    - label: Stall Until Done
      name: stalluntildone
    - label: Threaded, Show Checkerboard Until Done
      name: threadedcheckerboard
    - label: Threaded, Show Black Until Done
      name: threadedblack
    - label: Threaded, Show Previous Shader Until Done
      name: threadedprevious
    name: Compilebehavior
  summary: Visualizes the graph of a function operator.
  thumb: assets/images/reference/operators/output/functionGraphRender_thumb.png

---


Visualizes the graph of a function operator.

This is intended primarily for use in the Inspector, though there may be other uses.
It can take in multiple function inputs, which it will visualize with different colors of lines in the same graph.

It provides several outputs:
* Color - The rendered graph line.
* GUI - The graph line along with axes and range markers.