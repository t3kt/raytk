---
layout: operator
title: iteratedTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/iteratedTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.iteratedTransform/
op:
  category: filter
  detail: This can be used to create KIFS fractals (kaleidoscopic iterated function
    systems).
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
  name: iteratedTransform
  opType: raytk.operators.filter.iteratedTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Iterations
    name: Iterations
  - label: Reflect Mode
    menuOptions:
    - label: None
      name: none
    - label: XYZ
      name: xyz
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    name: Reflectmode
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
  - label: Rotate XYZ
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
  - label: Custom Code
    name: Customcode
  - label: Float Param 1
    name: Floatparam1
  - label: Float Param 2
    name: Floatparam2
  - label: Float Param 3
    name: Floatparam3
  - label: Float Param 4
    name: Floatparam4
  - label: Vec Param 1
    name: Vecparam1
  - label: Vec Param 2
    name: Vecparam2
  - label: Vec Param 3
    name: Vecparam3
  - label: Vec Param 4
    name: Vecparam4
  summary: Performs a transform multiple times, optionally reflecting across axes
    in between the steps.

---


Performs a transform multiple times, optionally reflecting across axes in between the steps.

This can be used to create KIFS fractals (kaleidoscopic iterated function systems).