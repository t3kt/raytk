---
layout: operator
title: extend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/extend
redirect_from:
  - /reference/opType/raytk.operators.filter.extend/
op:
  name: extend
  opType: raytk.operators.filter.extend
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
  parameters:
    - name: Enable
      label: Enable
    - name: Center
      label: Center
    - name: Size
      label: Size
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# extend

Category: filter

