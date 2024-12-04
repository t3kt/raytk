---
layout: operator
title: texture3dRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/texture3dRender
redirect_from:
  - /reference/opType/raytkVolumes.operators.output.texture3dRender/
op:
  category: output
  detail: 'When rendering a field (either float or vector), it just produces the field
    value as the main output.


    When rendering an SDF, it produces the SDF''s assigned density in the main output.
    If the SDF doesn''t have a density, it will fill the interior with a density of
    1 and the exterior with a density of 0. The color output uses a material if one
    is assigned to the SDF, or the SDF''s color if it has one, or white on the interior
    if it doesn''t.


    When rendering a volume, it produces the density value as the main output. The
    color output uses the volume''s color attribute if it has one, with the density
    value as the alpha. If the volume doesn''t have a color attribute, it will produce
    0.


    The renderer defines a box-shaped area to sample and fills the 3D texture with
    the results of the sampling.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: primary_definition_in
    name: primary
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera (For Materials Only)
    name: camera
    returnTypes:
    - Ray
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    returnTypes:
    - Light
  keywords:
  - volume
  moduleName: raytkVolumes
  name: texture3dRender
  opType: raytkVolumes.operators.output.texture3dRender
  parameters:
  - label: Volume Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Center of the sampling box.
  - label: Volume Size
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Size of the sampling box.
  - label: Output Resolution
    menuOptions:
    - label: Use Input
      name: useinput
    - label: Custom
      name: custom
    name: Outputresolution
  - label: Resolution
    name: Resolution
    readOnlyHandling: baked
    regularHandling: runtime
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
  - label: Input Smoothness
    menuOptions:
    - label: Nearest Pixel
      name: nearest
    - label: Interpolate Pixels
      name: linear
    - label: Mipmap Pixels
      name: mipmap
    name: Inputfiltertype
  - label: Enable Normal Output
    name: Enablenormaloutput
    summary: Enable producing normal vectors. For each point, this will produce a
      vector pointing in the direction that the nearest surface point is facing. These
      values can be accessed using a `renderSelect` operator.
  - label: Enable World Pos Output
    name: Enableworldposoutput
    summary: Enables the world xyz position output buffer.
  - label: Enable Object Id Output
    name: Enableobjectidoutput
    summary: Enable object ID output, which produces a TOP with values assigned with
      the `injectObjectId` operator for whichever shape each point is inside.
  - label: Enable Debug Output
    name: Enabledebugoutput
  - label: Enable Custom Output 1
    name: Enablecustomoutput1
  - label: Enable Custom Output 2
    name: Enablecustomoutput2
  - label: Enable Normal Smoothing
    name: Enablenormalsmoothing
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to smooth out surface normals by sampling at larger distances.
  - label: Normal Smoothing
    name: Normalsmoothing
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How far apart to sample to calculate surface normals.
  - label: Material Mode
    menuOptions:
    - label: Only Inside SDF
      name: inside
    - label: Only SDF Surface
      name: surface
    - label: Fill Everwhere
      name: everywhere
    name: Materialmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Enable Blending
    name: Enableblending
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Customize Shader Config
    name: Customizeshaderconfig
  status: beta
  summary: Renderer that produces 3D textures that sample SDFs, Volumes, or fields.

---


Renderer that produces 3D textures that sample SDFs, Volumes, or fields.

When rendering a field (either float or vector), it just produces the field value as the main output.

When rendering an SDF, it produces the SDF's assigned density in the main output. If the SDF doesn't have a density, it will fill the interior with a density of 1 and the exterior with a density of 0. The color output uses a material if one is assigned to the SDF, or the SDF's color if it has one, or white on the interior if it doesn't.

When rendering a volume, it produces the density value as the main output. The color output uses the volume's color attribute if it has one, with the density value as the alpha. If the volume doesn't have a color attribute, it will produce 0.

The renderer defines a box-shaped area to sample and fills the 3D texture with the results of the sampling.