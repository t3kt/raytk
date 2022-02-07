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
    - ParticleContext
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
    summary: Optional field used to control rotation. The field is evaluated before
      each iteration, and the resulting value is added to the `Rotate` parameter.
      If the field uses 2D/3D coordinates, the current position is used. If the field
      uses 1D coordinates, it is passed `i / (n-1)`, where `i` is the loop iteration,
      and `n` is the total number of iterations.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
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
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Step Index
      name: index
    - label: Step Ratio
      name: ratio
    name: Iterationtype
  summary: Performs a transform multiple times, optionally reflecting across axes
    in between the steps.
  thumb: assets/images/reference/operators/filter/iteratedTransform_thumb.png
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---


Performs a transform multiple times, optionally reflecting across axes in between the steps.

This can be used to create KIFS fractals (kaleidoscopic iterated function systems).