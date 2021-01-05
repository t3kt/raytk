---
layout: operator
title: bend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/bend
redirect_from:
  - /reference/opType/raytk.operators.filter.bend/
op:
  name: bend
  summary: Bends space, along a main axis, towards a second axis.
  detail: |
    For example, bends sideways (towards X) depending on the vertical position (along Y).
  opType: raytk.operators.filter.bend
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: definition_in_2
      label: Bend Field
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,Sdf]
      summary: |
        Value field that determines how much to bend. If this accepts 1D coords, it is passed the position along the bend axis. For 2D coords, both the bend axis and the bend direction are passed. For 3D coords, the relative XYZ position is passed.
  parameters:
    - name: Enable
      label: Enable
    - name: Direction
      label: Direction
      summary: |
        Chooses the axis to bend along and the axis to bend towards.
      menuOptions:
        - name: xyz
          label: Along X Toward Y
        - name: xzy
          label: Along X Toward Z
        - name: yxz
          label: Along Y Toward X
        - name: yzx
          label: Along Y Toward Z
        - name: zxy
          label: Along Z Toward X
        - name: zyx
          label: Along Z Toward Y
    - name: Amount
      label: Amount
      summary: |
        Amount of bending.
    - name: Shift
      label: Shift
      summary: |
        Shifts the axis to bend along and the axis to bend towards.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# bend

Category: filter



Bends space, along a main axis, towards a second axis.

For example, bends sideways (towards X) depending on the vertical position (along Y).