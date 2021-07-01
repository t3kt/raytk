---
layout: operator
title: uvTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/uvTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.uvTransform/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
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
  name: uvTransform
  opType: raytk.operators.filter.uvTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Transform Primary UVs
    name: Transformprimary
  - label: Transform Secondary UVs
    name: Transformsecondary
  - label: Enable Translate
    name: Enabletranslate
  - label: Enable Rotate
    name: Enablerotate
  - label: Enable Scale
    name: Enablescale
  - label: Enable Pivot
    name: Enablepivot
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
  status: beta

---
