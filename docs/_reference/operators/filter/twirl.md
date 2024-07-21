---
layout: operator
title: twirl
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/twirl
redirect_from:
  - /reference/opType/raytk.operators.filter.twirl/
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
    - Volume
    - Ray
    - Light
    - Particle
    supportedVariables:
    - axispos
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
    label: Center Field
    name: centerField
    required: true
    returnTypes:
    - vec4
    supportedVariables:
    - axispos
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
    label: Size Field
    name: sizeField
    required: true
    returnTypes:
    - float
    supportedVariableInputs:
    - centerField
    supportedVariables:
    - axispos
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
    label: Amount Field
    name: amountField
    required: true
    returnTypes:
    - float
    supportedVariableInputs:
    - centerField
    - sizeField
    supportedVariables:
    - axispos
  name: twirl
  opType: raytk.operators.filter.twirl
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Amount
    name: Amount
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/twirl_thumb.png
  variables:
  - label: Position Along Axis
    name: axispos

---
