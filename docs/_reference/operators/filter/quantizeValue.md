---
layout: operator
title: quantizeValue
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quantizeValue
redirect_from:
  - /reference/opType/raytk.operators.filter.quantizeValue/
op:
  name: quantizeValue
  opType: raytk.operators.filter.quantizeValue
  category: filter
  status: beta
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Enable
      label: Enable
    - name: Size
      label: Size
    - name: Sizemult
      label: Size Multiplier
    - name: Offset
      label: Offset
    - name: Smoothing
      label: Smoothing
    - name: Smoothingmult
      label: Smoothing Multiplier
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# quantizeValue

Category: filter

