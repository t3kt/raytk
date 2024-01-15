---
layout: operator
title: reflect
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reflect
redirect_from:
  - /reference/opType/raytk.operators.filter.reflect/
op:
  category: filter
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
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Offset Field
    name: offsetField
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
    - vec3
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
  keywords:
  - flip
  - mirror
  - reflect
  name: reflect
  opType: raytk.operators.filter.reflect
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - label: Custom
      name: custom
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Direction
  - label: Plane Normal
    name: Planenormal
    summary: Vector that the cut plane faces. Note that this is only a direction and
      not a position in space.
  - label: Offset
    name: Offset
    summary: Moves the reflection plane along the normal that it faces.
  - label: Shift
    name: Shift
    summary: Moves the whole resulting shape along the normal.
  - name: Exposeiteration
    summary: Whether to expose which side of the plane a point is on as an iteration
      value for upstream ops.
  - label: Enable Blend
    name: Enableblend
  - label: Blending
    name: Blend
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Index (0/1)
      name: index
    - label: Signed (-1/1)
      name: sign
    name: Iterationtype
  shortcuts:
  - ref
  summary: Reflects space across a plane.
  thumb: assets/images/reference/operators/filter/reflect_thumb.png
  variables:
  - label: sign
    name: sign
  - label: index
    name: index

---


Reflects space across a plane.