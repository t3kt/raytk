---
layout: operator
title: rectangleSdf
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/rectangleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.rectangleSdf/
op:
  category: sdf2d
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
    - vec2
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
    - vec2
    label: Translate Field
    name: translateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - scaleField
  name: rectangleSdf
  opType: raytk.operators.sdf2d.rectangleSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the rectangle.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the rectangle on the x and y axes.
  - label: UV Mode
    menuOptions:
    - label: XY Normalized
      name: normxy
    - label: XY Fit to Outside
      name: outerxy
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  summary: SDF for a 2D rectangle.
  thumb: assets/images/reference/operators/sdf2d/rectangleSdf_thumb.png

---


SDF for a 2D rectangle.