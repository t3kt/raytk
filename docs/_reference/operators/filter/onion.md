---
layout: operator
title: onion
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/onion
redirect_from:
  - /reference/opType/raytk.operators.filter.onion/
op:
  name: onion
  opType: raytk.operators.filter.onion
  category: filter
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
    - name: Thickness
      label: Thickness
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# onion

Category: filter

