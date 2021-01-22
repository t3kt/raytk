---
layout: operator
title: helixSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/helixSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.helixSdf/
op:
  name: helixSdf
  opType: raytk.operators.sdf.helixSdf
  category: sdf
  inputs:
    - name: thickness_field_definition_in
      label: Thickness Field
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
      summary: |
        Field used to multiply the `Radius` parameter. If it uses 1D coordinates, it is provided the position along the axis. If it uses 3D coordinates, it uses the absolute position.
    - name: radius_field_definition_in
      label: Radius Field
      required: false
      coordTypes: [float,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
      summary: |
        Field used to multiply the `Thickness` parameter. If it uses 1D coordinates, it is provided the position along the axis. If it uses 3D coordinates, it uses the absolute position.
  parameters:
    - name: Enable
      label: Enable
    - name: Axis
      label: Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Translate
      label: Translate
    - name: Radius
      label: Radius
    - name: Thickness
      label: Thickness
    - name: Spread
      label: Spread
    - name: Dualspread
      label: Dual Spread
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# helixSdf

Category: sdf

