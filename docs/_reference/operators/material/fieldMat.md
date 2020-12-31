---
layout: operator
title: fieldMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/fieldMat
redirect_from:
  - /reference/opType/raytk.operators.material.fieldMat/
op:
  name: fieldMat
  summary: A material that uses a vector field input to determine the color. Essentially this is a conversion from a field to a material, with no other features.
  opType: raytk.operators.material.fieldMat
  category: material
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec3]
      contextTypes: [none,Context]
      returnTypes: [Sdf]
    - name: color_definition_in
      label: color_definition_in
      required: true
      coordTypes: [vec3]
      contextTypes: [MaterialContext]
      returnTypes: [vec4]
  parameters:
    - name: Enable
      label: Enable
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# fieldMat

Category: material



A material that uses a vector field input to determine
the color. Essentially this is a conversion from a
field to a material, with no other features.