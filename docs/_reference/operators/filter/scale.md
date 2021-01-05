---
layout: operator
title: scale
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/scale
redirect_from:
  - /reference/opType/raytk.operators.filter.scale/
op:
  name: scale
  summary: Scales space.
  detail: |
    Scaling works for either 3D or 2D inputs.
  opType: raytk.operators.filter.scale
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: scale_field_definition_in
      label: Scale Field
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
      summary: |
        If provided, this field is used to modify the scaling at different points in space. If the field returns float values, the value of all the `Scale` parameters are multiplied by that value. If it returns vec4 values, each part of the `Scale` parameter is multiplied by the corresponding value in the vec4.
  parameters:
    - name: Enable
      label: Enable
    - name: Scale
      label: Scale
      summary: |
        Scale to apply to each axis. If input is 2D only X and Y are used.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# scale

Category: filter



Scales space.

Scaling works for either 3D or 2D inputs.