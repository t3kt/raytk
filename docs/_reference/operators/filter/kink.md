---
layout: operator
title: kink
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/kink
redirect_from:
  - /reference/opType/raytk.operators.filter.kink/
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
    label: Amount Field
    name: amountField
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
    - float
    - vec2
    - vec3
    - vec4
    label: Spread Field
    name: spreadField
    returnTypes:
    - float
  name: kink
  opType: raytk.operators.filter.kink
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - label: Along X Toward Y
      name: xy
    - label: Along X Toward Z
      name: xz
    - label: Along Y Toward X
      name: yx
    - label: Along Y Toward Z
      name: yz
    - label: Along Z Toward X
      name: zx
    - label: Along Z Toward Y
      name: zy
    name: Direction
    readOnlyHandling: constant
    regularHandling: constant
  - label: Side
    menuOptions:
    - label: Negative
      name: neg
    - label: Positive
      name: pos
    name: Side
    readOnlyHandling: constant
    regularHandling: constant
  - label: Amount
    name: Amount
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Spread
    name: Spread
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/filter/kink_thumb.png

---
