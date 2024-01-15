---
layout: operator
title: pausingWaveFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/pausingWaveFn
redirect_from:
  - /reference/opType/raytk.operators.function.pausingWaveFn/
op:
  category: function
  inputs:
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
    label: Low Width Field
    name: lowWidthField
    returnTypes:
    - float
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
    label: High Width Field
    name: highWidthField
    returnTypes:
    - float
  keywords:
  - toggle
  - wave
  name: pausingWaveFn
  opType: raytk.operators.function.pausingWaveFn
  parameters:
  - label: Low Width
    name: Lowwidth
  - label: High Width
    name: Highwidth
  thumb: assets/images/reference/operators/function/pausingWaveFn_thumb.png

---
