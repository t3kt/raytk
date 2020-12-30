---
layout: operator
title: moduloDistance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloDistance
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloDistance/
op:
  name: moduloDistance
  opType: raytk.operators.filter.moduloDistance
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Distancemode
      label: Distance Mode
      menuOptions:
        - name: xaxis
          label: X Axis
        - name: yaxis
          label: Y Axis
        - name: zaxis
          label: Z Axis
        - name: spherical
          label: Spherical
    - name: Mirrortype
      label: Mirror Type
      menuOptions:
        - name: none
          label: None
        - name: mirror
          label: Mirror
    - name: Length
      label: Length
    - name: Center
      label: Center
    - name: Iterateonrings
      label: Iterate On Rings
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# moduloDistance

Category: filter

