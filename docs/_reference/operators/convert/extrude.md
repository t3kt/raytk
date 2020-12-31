---
layout: operator
title: extrude
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/extrude
redirect_from:
  - /reference/opType/raytk.operators.convert.extrude/
op:
  name: extrude
  opType: raytk.operators.convert.extrude
  category: convert
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [Sdf]
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
    - name: Height
      label: Height
    - name: Offset
      label: Offset
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# extrude

Category: convert

