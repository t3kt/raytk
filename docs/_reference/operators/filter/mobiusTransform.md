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
    - VertexContext
    - PixelContext
    - PopContext
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
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
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
    - VertexContext
    - PixelContext
    - PopContext
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
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: The plane whose axes will be transformed.
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point
    name: Point
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/filter/mobiusTransform_thumb.png

---
