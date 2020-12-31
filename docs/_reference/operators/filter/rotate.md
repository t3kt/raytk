---
layout: operator
title: rotate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rotate
redirect_from:
  - /reference/opType/raytk.operators.filter.rotate/
op:
  name: rotate
  opType: raytk.operators.filter.rotate
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: definition_in_2
      label: definition_in_2
      required: false
      coordTypes: [vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [vec4,Sdf]
  parameters:
    - name: Enable
      label: Enable
    - name: Rotatemode
      label: Rotate Mode
      menuOptions:
        - name: axis
          label: Axis
        - name: euler
          label: Euler
        - name: 2d
          label: 2D
    - name: Axis
      label: Axis
    - name: Rotate
      label: Rotate
    - name: Rord
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
    - name: Rot
      label: Rotate XYZ
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# rotate

Category: filter

