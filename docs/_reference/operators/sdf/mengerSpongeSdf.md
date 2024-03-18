---
layout: operator
title: mengerSpongeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mengerSpongeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mengerSpongeSdf/
op:
  category: sdf
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
    label: Box Scale Field
    name: boxScaleField
    returnTypes:
    - float
    supportedVariables:
    - RTK_raytk_operators_sdf_mengerSpongeSdf_step
    - RTK_raytk_operators_sdf_mengerSpongeSdf_normstep
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
    label: Cross Scale Field
    name: crossScaleField
    returnTypes:
    - float
    supportedVariableInputs:
    - boxScaleField
    supportedVariables:
    - RTK_raytk_operators_sdf_mengerSpongeSdf_step
    - RTK_raytk_operators_sdf_mengerSpongeSdf_normstep
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
    label: Step Offset Field
    name: stepOffsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - boxScaleField
    - crossScaleField
    supportedVariables:
    - RTK_raytk_operators_sdf_mengerSpongeSdf_step
    - RTK_raytk_operators_sdf_mengerSpongeSdf_normstep
  name: mengerSpongeSdf
  opType: raytk.operators.sdf.mengerSpongeSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Steps
    name: Steps
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of levels of detail.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Box Scale
    name: Boxscale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The scale of the boxes used at each step.
  - label: Cross Scale
    name: Crossscale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the holes cut through the boxes at each step.
  - label: Step Offset
    name: Stepoffset
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  thumb: assets/images/reference/operators/sdf/mengerSpongeSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_mengerSpongeSdf_step
    name: RTK_raytk_operators_sdf_mengerSpongeSdf_step
  - label: RTK_raytk_operators_sdf_mengerSpongeSdf_normstep
    name: RTK_raytk_operators_sdf_mengerSpongeSdf_normstep

---


Menger sponge fractal, made of boxes with holes cut through each axis.