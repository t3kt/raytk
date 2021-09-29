---
layout: operator
title: customRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/customRender
redirect_from:
  - /reference/opType/raytk.operators.output.customRender/
op:
  category: output
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: customRender
  opType: raytk.operators.output.customRender
  parameters:
  - label: Body Template
    name: Bodytemplate
  - label: Create Body Template
    name: Createbodytemplate
  - label: Output Buffer Table
    name: Outputbuffertable
  - label: Create Output Buffer Table
    name: Createoutputbuffertable
  - label: Library Names
    menuOptions:
    - label: hg_sdf
      name: hg_sdf
    - label: raytkCommon
      name: raytkCommon
    - label: raytkSdf
      name: raytkSdf
    - label: raytkMaterial
      name: raytkMaterial
    - label: Label 5
      name: ' raytkCore'
    name: Librarynames
  - label: Type Spec
    name: Typespec
  - label: Time Reference Operator
    name: Timerefop
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
  - label: Resolution
    name: Res
  - label: Input Smoothness
    menuOptions:
    - label: Nearest Pixel
      name: nearest
    - label: Interpolate Pixels
      name: linear
    - label: Mipmap Pixels
      name: mipmap
    name: Inputfiltertype
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  status: alpha

---
