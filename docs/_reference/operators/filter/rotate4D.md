---
layout: operator
title: rotate4D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rotate4D
redirect_from:
  - /reference/opType/raytk.operators.filter.rotate4D/
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
    - float
    - vec2
    - vec3
    - vec4
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
    label: Rotate Field
    name: rotateField
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
    - vec2
    - vec3
    - vec4
    label: Pivot Field
    name: pivotField
    returnTypes:
    - vec4
  name: rotate4D
  opType: raytk.operators.filter.rotate4D
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: XW
      name: xw
    - label: YW
      name: yw
    - label: ZW
      name: zw
    name: Plane
  - label: Rotate
    name: Rotate
  - label: Pivot
    name: Pivot
  - label: Pivot 4D
    name: Pivotw
  summary: Projects 3D space into 4D space, applies rotation along two axes and then
    projects back into 3D space.
  thumb: assets/images/reference/operators/filter/rotate4D_thumb.png
  variables:
  - label: pos4d
    name: pos4d

---


Projects 3D space into 4D space, applies rotation along two axes and then projects back into 3D space.