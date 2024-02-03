---
layout: operator
title: mobiusTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mobiusTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.mobiusTransform/
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
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - pointField
    - centerField
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
    label: Point Field
    name: pointField
    returnTypes:
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
    - vec3
    label: Center Field
    name: centerField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - pointField
  name: mobiusTransform
  opType: raytk.operators.filter.mobiusTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: XZ
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: constant
    regularHandling: constant
    summary: The plane whose axes will be transformed.
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point
    name: Point
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/filter/mobiusTransform_thumb.png

---
