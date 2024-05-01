---
layout: operator
title: chamferBoxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chamferBoxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chamferBoxSdf/
op:
  category: sdf
  detail: Based on [ChamferBox Super Primitive](https://www.shadertoy.com/view/3lBGzt)
    by TLC123
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
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
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
    - vec3
    label: Chamfer Field
    name: chamferField
    returnTypes:
    - float
    supportedVariableInputs:
    - scaleField
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
    - vec3
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - scaleField
    - chamferField
  keywords:
  - box
  - chamfer
  - cube
  name: chamferBoxSdf
  opType: raytk.operators.sdf.chamferBoxSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Uniform Scale
    name: Uniformscale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Chamfer
    name: Chamfer
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width of cropping on edges/corners.
  - label: Round
    name: Round
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rounding that smooths out the edges of the crops.
  summary: A box with cropped corners at 45 degree angles.
  thumb: assets/images/reference/operators/sdf/chamferBoxSdf_thumb.png

---


A box with cropped corners at 45 degree angles.

Based on [ChamferBox Super Primitive](https://www.shadertoy.com/view/3lBGzt) by TLC123