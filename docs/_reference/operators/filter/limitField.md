---
layout: operator
title: limitField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitField
redirect_from:
  - /reference/opType/raytk.operators.filter.limitField/
op:
  category: filter
  detail: This is similar to the Limit CHOP.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input Field
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Low Value Field
    name: lowField
    required: true
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp1
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: High Value Field
    name: highField
    required: true
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp1
    - lowField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Blending Field
    name: blendingField
    required: true
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
    - lowField
    - highField
  keywords:
  - clamp
  - limit
  - loop
  - value
  - zigzag
  name: limitField
  opType: raytk.operators.filter.limitField
  parameters:
  - label: Enable
    name: Enable
  - label: Limit Type
    menuOptions:
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    - label: Zig-Zag
      name: zigzag
    - label: Clamp Low
      name: clamplow
    - label: Clamp High
      name: clamphigh
    - label: Smooth Clamp
      name: smoothclamp
    - label: Smooth Clamp Low
      name: smoothclamplow
    - label: Smooth Clamp High
      name: smoothclamphigh
    name: Limittype
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Low Bound
    name: Low
  - label: High Bound
    name: High
  - label: Blending
    name: Blending
  summary: Limits the values produced by a float or vector field.
  thumb: assets/images/reference/operators/filter/limitField_thumb.png

---


Limits the values produced by a float or vector field.

This is similar to the Limit CHOP.