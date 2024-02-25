---
layout: operator
title: transform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/transform
redirect_from:
  - /reference/opType/raytk.operators.filter.transform/
op:
  category: filter
  detail: 'Various parts of the transform can be switched off to improve performance,
    and the sequence of transform steps can be reordered.

    It either uses the origin (0,0,0) as the pivot point, or can use another pivot
    point.'
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
    label: Rotate Field
    name: rotateField
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
    label: Translate Field
    name: translateField
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  keywords:
  - move
  - pivot
  - position
  - rotate
  - scale
  - transform
  - translate
  name: transform
  opType: raytk.operators.filter.transform
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Translate
    name: Enabletranslate
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Rotate
    name: Enablerotate
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Scale
    name: Enablescale
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Pivot
    name: Enablepivot
    readOnlyHandling: baked
    regularHandling: baked
  - label: Translate
    name: Translate
  - label: Rotate
    name: Rotate
  - label: Scale
    name: Scale
  - label: Uniform Scale
    name: Uniformscale
  - label: Pivot
    name: Pivot
  - label: Transform Order
    menuOptions:
    - label: Scale Rotate Translate
      name: srt
    - label: Scale Translate Rotate
      name: str
    - label: Rotate Scale Translate
      name: rst
    - label: Rotate Translate Scale
      name: rts
    - label: Translate Scale Rotate
      name: tsr
    - label: Translate Rotate Scale
      name: trs
    name: Transformorder
  - label: Rotate Order
    menuOptions:
    - label: Rx Ry Rz
      name: xyz
    - label: Rx Rz Ry
      name: xzy
    - label: Ry Rx Rz
      name: yxz
    - label: Ry Rz Rx
      name: yzx
    - label: Rz Rx Ry
      name: zxy
    - label: Rz Ry Rx
      name: zyx
    name: Rotateorder
  - label: Scale Type
    menuOptions:
    - label: Separate XYZ
      name: separate
    - label: Uniform
      name: uniform
    name: Scaletype
    readOnlyHandling: baked
    regularHandling: baked
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
  shortcuts:
  - tfm
  summary: Transform the coordinates of the input, with rotation, scaling, and translation.

---


Transform the coordinates of the input, with rotation, scaling, and translation.

Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.