---
layout: operator
title: mirrorOctant
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorOctant
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorOctant/
op:
  name: mirrorOctant
  summary: Mirror coordinates across two axes and the diagonals.
  opType: raytk.operators.filter.mirrorOctant
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: rotate_axis_field_definition_in
      label: Rotate Axis Field
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [Context]
      returnTypes: [float,Sdf]
      summary: |
        Value field used to vary the `Rotateaxis`. If the field is a 1D field, it is given the distance from the center. If it is a 2D field, it is given the position along the mirror axes. If it is a 3D field, it is given the raw position. The value is converted to radians and *added* to the `Rotateaxis` parameter.
  parameters:
    - name: Enable
      label: Enable
    - name: Axis
      label: Axis
      summary: |
        Axis that faces the plane where coordinates are mirrored.
      menuOptions:
        - name: x
          label: YZ
        - name: y
          label: ZX
        - name: z
          label: XY
    - name: Size
      label: Size
      summary: |
        Spacing of the reflection planes.
    - name: Offset
      label: Offset
      summary: |
        Shifts the input before applying reflection.
    - name: Rotateaxis
      label: Rotate Axis
      summary: |
        Rotates the input before applying reflection.
    - name: Iterateoncells
      label: Iterate On Cells
      summary: |
        Enables upstream operators to check which cell in the reflection grid a point is in.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# mirrorOctant

Category: filter



Mirror coordinates across two axes and the diagonals.