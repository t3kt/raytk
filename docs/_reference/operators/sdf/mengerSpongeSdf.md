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
    summary: Moves the center of the shape.
  - label: Steps
    name: Steps
    summary: Number of levels of detail.
  - label: Scale
    name: Scale
  - label: Box Scale
    name: Boxscale
    summary: The scale of the boxes used at each step.
  - label: Cross Scale
    name: Crossscale
    summary: The size of the holes cut through the boxes at each step.
  - label: Step Offset
    name: Stepoffset
  summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  thumb: assets/images/reference/operators/sdf/mengerSpongeSdf_thumb.png
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---


Menger sponge fractal, made of boxes with holes cut through each axis.