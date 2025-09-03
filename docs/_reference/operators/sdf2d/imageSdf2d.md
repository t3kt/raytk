---
layout: operator
title: imageSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/imageSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.imageSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: UV Map Field
    name: uvField
    returnTypes:
    - vec4
  name: imageSdf2d
  opType: raytk.operators.sdf2d.imageSdf2d
  parameters:
  - label: Texture
    name: Texture
    summary: TOP used for the texture.
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: baked
    regularHandling: runtime
    summary: When using 3D coordinates, the axis that faces the plane used for UV.
      This is not used when a UV field input is attached.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets the UV coordinates.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the UV coordinates.
  - label: Multiply Add (MAD)
    name: Multiplyadd
  - label: Resolution
    menuOptions:
    - label: 32x32
      name: r32
    - label: 64x64
      name: r64
    - label: 128x128
      name: r128
    - label: 256x256
      name: r256
    - label: 512x512
      name: r512
    - label: 1024x1024
      name: r1024
    - label: 2048x2048
      name: r2048
    - label: 4096x4096
      name: r4096
    name: Resolution
  - label: Fit
    menuOptions:
    - label: Fill
      name: fill
    - label: Fit Horizontal
      name: fithorz
    - label: Fit Vertical
      name: fitvert
    - label: Fit Best
      name: fitbest
    - label: Fit Outside
      name: fitoutside
    - label: Native Resolution
      name: nativeres
    name: Fit
  status: beta
  thumb: assets/images/reference/operators/sdf2d/imageSdf2d_thumb.png

---
