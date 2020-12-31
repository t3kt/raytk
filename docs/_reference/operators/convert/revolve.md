---
layout: operator
title: revolve
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/revolve
redirect_from:
  - /reference/opType/raytk.operators.convert.revolve/
op:
  name: revolve
  opType: raytk.operators.convert.revolve
  category: convert
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
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
    - name: Radialoffset
      label: Radial Offset
    - name: Axisoffset
      label: Axis Offset
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# revolve

Category: convert

