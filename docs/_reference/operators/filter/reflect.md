---
layout: operator
title: reflect
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reflect
redirect_from:
  - /reference/opType/raytk.operators.filter.reflect/
op:
  name: reflect
  summary: Reflects space across a plane.
  opType: raytk.operators.filter.reflect
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext]
      returnTypes: [float,vec4,Sdf]
    - name: blend_func_definition_in
      label: Blend Function
      required: false
      coordTypes: [float]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
      summary: |
        Function used to control blending across the reflection plane.
  parameters:
    - name: Enable
      label: Enable
    - name: Direction
      label: Direction
      menuOptions:
        - name: custom
          label: Custom
        - name: xpos
          label: X+
        - name: xneg
          label: X-
        - name: ypos
          label: Y+
        - name: yneg
          label: Y-
        - name: zpos
          label: Z+
        - name: zneg
          label: Z-
    - name: Planenormal
      label: Plane Normal
      summary: |
        Vector that the cut plane faces. Note that this is only a direction and not a position in space.
    - name: Offset
      label: Offset
      summary: |
        Moves the reflection plane along the normal that it faces.
    - name: Shift
      label: Shift
      summary: |
        Moves the whole resulting shape along the normal.
    - name: Exposeiteration
      label: Expose Iteration
      summary: |
        Whether to expose which side of the plane a point is on as an iteration value for upstream ops.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# reflect

Category: filter



Reflects space across a plane.