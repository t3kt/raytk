---
layout: operator
title: iteratedTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/iteratedTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.iteratedTransform/
op:
  name: iteratedTransform
  summary: Performs a transform multiple times, optionally reflecting across axes in between the steps.
  detail: |
    This can be used to create KIFS fractals (kaleidoscopic iterated function systems).
  opType: raytk.operators.filter.iteratedTransform
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Iterations
      label: Iterations
    - name: Reflectmode
      label: Reflect Mode
      menuOptions:
        - name: none
          label: None
        - name: xyz
          label: XYZ
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
        - name: xy
          label: XY
        - name: yz
          label: YZ
        - name: zx
          label: ZX
    - name: Enabletranslate
      label: Enable Translate
    - name: Enablerotate
      label: Enable Rotate
    - name: Enablescale
      label: Enable Scale
    - name: Enablepivot
      label: Enable Pivot
    - name: Translate
      label: Translate
    - name: Rotate
      label: Rotate XYZ
    - name: Scale
      label: Scale
    - name: Pivot
      label: Pivot
    - name: Transformorder
      label: Transform Order
      menuOptions:
        - name: srt
          label: Scale Rotate Translate
        - name: str
          label: Scale Translate Rotate
        - name: rst
          label: Rotate Scale Translate
        - name: rts
          label: Rotate Translate Scale
        - name: tsr
          label: Translate Scale Rotate
        - name: trs
          label: Translate Rotate Scale
    - name: Rotateorder
      label: Rotate Order
      menuOptions:
        - name: xyz
          label: Rx Ry Rz
        - name: xzy
          label: Rx Rz Ry
        - name: yxz
          label: Ry Rx Rz
        - name: yzx
          label: Ry Rz Rx
        - name: zxy
          label: Rz Rx Ry
        - name: zyx
          label: Rz Ry Rx
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help
    - name: Customcode
      label: Custom Code
    - name: Floatparam1
      label: Float Param 1
    - name: Floatparam2
      label: Float Param 2
    - name: Floatparam3
      label: Float Param 3
    - name: Floatparam4
      label: Float Param 4
    - name: Vecparam1
      label: Vec Param 1
    - name: Vecparam2
      label: Vec Param 2
    - name: Vecparam3
      label: Vec Param 3
    - name: Vecparam4
      label: Vec Param 4

---

# iteratedTransform

Category: filter



Performs a transform multiple times, optionally reflecting across axes in between the steps.

This can be used to create KIFS fractals (kaleidoscopic iterated function systems).