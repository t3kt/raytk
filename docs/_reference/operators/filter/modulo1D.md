---
layout: operator
title: modulo1D
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modulo1D
redirect_from:
  - /reference/opType/raytk.operators.filter.modulo1D/
op:
  name: modulo1D
  opType: raytk.operators.filter.modulo1D
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [Context]
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
    - name: Size
      label: Size
    - name: Offset
      label: Offset
    - name: Shift
      label: Shift
    - name: Mirrortype
      label: Mirror Type
      menuOptions:
        - name: none
          label: None
        - name: mirror
          label: Mirror
    - name: Uselimit
      label: Use Limit
    - name: Limitstart
      label: Limit Start
    - name: Limitstop
      label: Limit Stop
    - name: Limitoffset
      label: Limit Offset
    - name: Iterateoncells
      label: Iterate On Cells
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# modulo1D

Category: filter

