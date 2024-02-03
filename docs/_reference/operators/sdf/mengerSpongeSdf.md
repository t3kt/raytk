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
  name: mengerSpongeSdf
  opType: raytk.operators.sdf.mengerSpongeSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Steps
    name: Steps
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Number of levels of detail.
  - label: Scale
    name: Scale
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Box Scale
    name: Boxscale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The scale of the boxes used at each step.
  - label: Cross Scale
    name: Crossscale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The size of the holes cut through the boxes at each step.
  - label: Step Offset
    name: Stepoffset
    readOnlyHandling: macro
    regularHandling: runtime
  summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  thumb: assets/images/reference/operators/sdf/mengerSpongeSdf_thumb.png
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---


Menger sponge fractal, made of boxes with holes cut through each axis.