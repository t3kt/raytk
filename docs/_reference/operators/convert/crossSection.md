---
layout: operator
title: crossSection
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/crossSection
redirect_from:
  - /reference/opType/raytk.operators.convert.crossSection/
op:
  category: convert
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
    - vec2
    - vec3
    - vec4
    label: Input
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - offsetField
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
    - vec2
    - vec3
    - vec4
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
  name: crossSection
  opType: raytk.operators.convert.crossSection
  parameters:
  - label: Enable
    name: Enable
  - label: Axes
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YX
      name: yx
    - label: YZ
      name: yz
    - label: ZY
      name: zy
    - label: XZ
      name: xz
    - label: ZX
      name: zx
    name: Axes
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets the plane or axis where the input is sampled.
  summary: Takes a 3D (or 2D) operator and take a cross section of it across a plane
    or a single axis.

---


Takes a 3D (or 2D) operator and take a cross section of it across a plane or a single axis.