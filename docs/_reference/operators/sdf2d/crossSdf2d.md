---
layout: operator
title: crossSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/crossSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.crossSdf2d/
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
    label: Outer Size Field
    name: outerSizeField
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
    - vec2
    label: Inner Size Field
    name: innerSizeField
    returnTypes:
    - float
    supportedVariableInputs:
    - outerSizeField
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
    label: Roundness Field
    name: roundnessField
    returnTypes:
    - float
    supportedVariableInputs:
    - outerSizeField
    - innerSizeField
  name: crossSdf2d
  opType: raytk.operators.sdf2d.crossSdf2d
  parameters:
  - label: Outer Size
    name: Outersize
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The length of the arms.
  - label: Inner Size
    name: Innersize
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Thickness of the arms.
  - label: Roundness
    name: Roundness
    readOnlyHandling: macro
    regularHandling: runtime
    summary: How much to round out the intersection corners.
  summary: 2D cross shape SDF, with 4 arms and option rounding of the intersections.
  thumb: assets/images/reference/operators/sdf2d/crossSdf2d_thumb.png

---


2D cross shape SDF, with 4 arms and option rounding of the intersections.