---
layout: operator
title: vectorToFloat
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/vectorToFloat
redirect_from:
  - /reference/opType/raytk.operators.convert.vectorToFloat/
op:
  name: vectorToFloat
  opType: raytk.operators.convert.vectorToFloat
  category: convert
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [vec4]
  parameters:
    - name: Enable
      label: Enable
    - name: Usepart
      label: Use Part
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
        - name: w
          label: W
        - name: lengthxyz
          label: Length(XYZ)
        - name: lengthxyzw
          label: Length(XYZW)
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# vectorToFloat

Category: convert

