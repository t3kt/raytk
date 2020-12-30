---
layout: operator
title: transform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/transform
redirect_from:
  - /reference/opType/raytk.operators.filter.transform/
op:
  name: transform
  summary: |
    Transform the coordinates of the input, with rotation, scaling, and translation.
  detail: |
    Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
    It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.
  opType: raytk.operators.filter.transform
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
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
      label: Rotate
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

---

# transform

Category: filter



Transform the coordinates of the input, with rotation, scaling, and translation.

Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.