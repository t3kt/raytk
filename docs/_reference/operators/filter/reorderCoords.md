---
layout: operator
title: reorderCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reorderCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.reorderCoords/
op:
  name: reorderCoords
  opType: raytk.operators.filter.reorderCoords
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
    - name: Axisx
      label: X Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Axisy
      label: Y Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Axisz
      label: Z Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# reorderCoords

Category: filter

