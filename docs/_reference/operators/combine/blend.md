---
layout: operator
title: blend
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/blend
redirect_from:
  - /reference/opType/raytk.operators.combine.blend/
op:
  name: blend
  summary: Smoothly blends/morphs between up to 4 SDFs.
  detail: |
    The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.
  opType: raytk.operators.combine.blend
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in_2
      label: definition_in_2
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in_3
      label: definition_in_3
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in_4
      label: definition_in_4
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Enable
      label: Enable
    - name: Blend
      label: Blend
      summary: |
        Which input or combination of inputs to use. If this value is 0, the first connected input is used. 0.5 is half way between the first and second connected inputs, etc.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# blend

Category: combine



Smoothly blends/morphs between up to 4 SDFs.

The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.