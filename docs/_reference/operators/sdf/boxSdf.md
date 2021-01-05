---
layout: operator
title: boxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/boxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.boxSdf/
op:
  name: boxSdf
  summary: SDF for a box, optionally infinite one one axis.
  opType: raytk.operators.sdf.boxSdf
  category: sdf
  parameters:
    - name: Boxtype
      label: Box Type
      summary: |
        The type of box function.
      menuOptions:
        - name: boxcheap
          label: Box Cheap
          description: |
            A bit more efficient but slightly less accurate.
        - name: box
          label: Box
          description: |
            More accurate but slightly less efficient.
    - name: Infiniteaxis
      label: Infinite Axis
      summary: |
        Axis along which the box should stretch infinitely.
      menuOptions:
        - name: none
          label: None
          description: |
            Regular box.
        - name: x
          label: X
          description: |
            Box is infinite along the x axis.
        - name: y
          label: Y
          description: |
            Box is infinite along the y axis.
        - name: z
          label: Z
          description: |
            Box is infinite along the z axis.
    - name: Translate
      label: Translate
      summary: |
        Move the center of the box.
    - name: Scale
      label: Scale
      summary: |
        The size of the box in each dimension.
    - name: Uniformscale
      label: Uniform Scale
      summary: |
        Scaling applied to all dimensions of the `Scale`.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# boxSdf

Category: sdf



SDF for a box, optionally infinite one one axis.