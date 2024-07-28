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
    coordTypes:
    - vec2
    label: Input 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input 8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    - Particle
  name: customRender
  opType: raytk.operators.output.customRender
  parameters:
  - label: Main Code
    name: Maincode
  - label: Output Buffer Table
    name: Outputbuffertable
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
  - label: Output Type
    menuOptions:
    - label: 2D Texture
      name: texture2d
    - label: 2D Texture Array
      name: texture2darray
    - label: 3D Texture
      name: texture3d
    name: Type
  - label: Input Smoothness
    menuOptions:
    - label: Nearest Pixel
      name: nearest
    - label: Interpolate Pixels
      name: linear
    - label: Mipmap Pixels
      name: mipmap
    name: Inputfiltertype
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Custom Render Config
    name: Customrenderconfig
  - label: Create Main Code
    name: Createmaincode
  - label: Create Output Buffer Table
    name: Createoutputbuffertable
  status: beta

---
