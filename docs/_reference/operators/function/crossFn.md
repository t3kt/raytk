---
layout: operator
title: crossFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/crossFn
redirect_from:
  - /reference/opType/raytk.operators.function.crossFn/
op:
  name: crossFn
  opType: raytk.operators.function.crossFn
  category: function
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4]
    - name: definition_in_2
      label: definition_in_2
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4]
    - name: mix_definition_in
      label: mix definition in
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4]
  parameters:
    - name: Enable
      label: Enable
    - name: Mix
      label: Mix
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# crossFn

Category: function

