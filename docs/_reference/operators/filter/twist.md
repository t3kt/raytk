---
layout: operator
title: twist
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/twist
redirect_from:
  - /reference/opType/raytk.operators.filter.twist/
op:
  name: twist
  summary: Twists space around an axis.
  opType: raytk.operators.filter.twist
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
  parameters:
    - name: Enable
      label: Enable
    - name: Axis
      label: Axis
      summary: |
        The axis around which to twist.
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Amount
      label: Amount
      summary: |
        The amount of twisting to apply.
    - name: Shift
      label: Shift
      summary: |
        Offsets the twisting along the axis, effectively rotating everything equally around it.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# twist

Category: filter



Twists space around an axis.