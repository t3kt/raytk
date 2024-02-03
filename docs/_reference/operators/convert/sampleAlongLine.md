---
layout: operator
title: sampleAlongLine
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/sampleAlongLine
redirect_from:
  - /reference/opType/raytk.operators.convert.sampleAlongLine/
op:
  category: convert
  detail: It's similar to crossSection but with a single line instead of a 2D plane.
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
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: sampleAlongLine
  opType: raytk.operators.convert.sampleAlongLine
  parameters:
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Position in 2D/3D space where the center of the line sits. When a position
      of 0 is passed to this operator, it will check its input at the Center location.
  - label: Direction
    name: Direction
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Vector indicating which direction the line goes from the center.
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Rotation for the sampling line.
  status: beta
  summary: Samples a 2D/3D input along a single line, producing a 1D function.

---


Samples a 2D/3D input along a single line, producing a 1D function.

It's similar to crossSection but with a single line instead of a 2D plane.