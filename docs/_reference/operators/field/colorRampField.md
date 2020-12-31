---
layout: operator
title: colorRampField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorRampField
redirect_from:
  - /reference/opType/raytk.operators.field.colorRampField/
op:
  name: colorRampField
  summary: A vector field that maps an input field to values from a range of colors.
  opType: raytk.operators.field.colorRampField
  category: field
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
  parameters:
    - name: Enable
      label: Enable
    - name: Color1
      label: Color 1
    - name: Color2
      label: Color 2
    - name: Alpha1
      label: Alpha 1
    - name: Alpha2
      label: Alpha 2
    - name: Clamprange
      label: Clamp Range
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# colorRampField

Category: field



A vector field that maps an input field to values from a range of colors.